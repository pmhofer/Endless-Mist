#!/usr/bin/env python3
"""Stufe 1 (kostenlos): rendert Hörbuch-Skripte mit Edge-TTS zu MP3 pro Abschnitt.

Aufruf: render-edge-tts.py <skript.txt> [--lang de|en] [--voice NAME] [--out DIR] [--rate -6%] [--abschnitt N]
Vorbereitung: python3 -m venv .venv && .venv/bin/pip install edge-tts; ffmpeg muss installiert sein.
Cloud-Umgebung: Host speech.platform.bing.com muss in der Netzwerkfreigabe stehen (sonst 403).
- Marker-Zeilen [TEIL …] werden nicht gesprochen; jeder [ABSCHNITT n: Titel] ergibt eine MP3.
- Absatzweise gesprochen (Zeilen ohne Leerzeile = ein Absatz); [pause] -> 0,9 s Stille; Absatzende 0,45 s; '* * *' und '---' -> 1,6 s; andere Tags (Stufe-2-Tags) werden ignoriert.
- *kursiv* -> Sterne entfernt. Benötigt: pip install edge-tts, ffmpeg. Netz: speech.platform.bing.com.
"""
import argparse, asyncio, os, re, subprocess, sys, tempfile
import edge_tts

def parse(path):
    text = open(path, encoding="utf-8").read()
    parts = re.split(r"^\[TEIL [IVX]+ \| KAPITEL: [^|\]]*\| ABSCHNITT (\d+): ([^\]]+)\]\s*$", text, flags=re.M)
    # parts: [kopf, n1, titel1, body1, n2, titel2, body2, ...]
    return [(int(parts[i]), parts[i + 1].strip(), parts[i + 2]) for i in range(1, len(parts) - 2, 3)]

def segments(body):
    """Absatzweise: Zeilen ohne Leerzeile gehören zu einem Absatz und werden in einem Zug gesprochen
    (lange Absätze an Satzenden in Stücke von höchstens ca. 900 Zeichen). Pausen nur an Markern und zwischen Absätzen."""
    body = body.replace("\u201e", "").replace("\u201c", "").replace("\u201d", "").replace("\"", "")
    out, buf = [], []
    def flush(gap=0.45):
        t = " ".join(buf).strip()
        buf.clear()
        if not t: return
        parts, cur = [], ""
        for sent in re.split(r"(?<=[.!?\u2026])\s+", t):
            if cur and len(cur) + len(sent) > 900:
                parts.append(cur); cur = sent
            else:
                cur = (cur + " " + sent).strip()
        if cur: parts.append(cur)
        for k, part in enumerate(parts):
            out.append(("say", part))
        out.append(("gap", gap))
    for line in body.splitlines():
        s = line.strip()
        if not s: flush(); continue
        if s == "---" or re.fullmatch(r"(\*\s*){3,}", s): flush(0.0); out.append(("gap", 1.6)); continue
        if re.fullmatch(r"\[pause\]", s): flush(0.0); out.append(("gap", 0.9)); continue
        if re.fullmatch(r"\[[a-z ]+\]", s): continue
        s = re.sub(r"\[[a-z ]+\]\s*", "", s).replace("*", "")
        buf.append(s)
    flush()
    return out

async def say(text, voice, rate, proxy, path):
    for attempt in range(4):
        try:
            await edge_tts.Communicate(text, voice, rate=rate, proxy=proxy).save(path)
            if os.path.getsize(path) > 0: return
        except Exception as e:
            err = e
            await asyncio.sleep(2 * (attempt + 1))
    raise SystemExit(f"Edge-TTS fehlgeschlagen: {err}")

def silence(sec, path):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                    "-t", str(sec), "-c:a", "libmp3lame", "-b:a", "48k", path], check=True)

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script"); ap.add_argument("--lang", default="de", choices=["de", "en"]); ap.add_argument("--voice")
    ap.add_argument("--out", default="audio"); ap.add_argument("--rate", default="-6%")
    ap.add_argument("--abschnitt", type=int)
    a = ap.parse_args()
    a.voice = a.voice or {"de": "de-DE-KillianNeural", "en": "en-US-EricNeural"}[a.lang]
    proxy = os.environ.get("HTTPS_PROXY")
    os.makedirs(a.out, exist_ok=True)
    base = os.path.splitext(os.path.basename(a.script))[0]
    for n, titel, body in parse(a.script):
        if a.abschnitt and n != a.abschnitt: continue
        with tempfile.TemporaryDirectory() as td:
            files = []
            for i, (kind, val) in enumerate(segments(body)):
                p = os.path.join(td, f"{i:04d}.mp3")
                if kind == "say": await say(val, a.voice, a.rate, proxy, p)
                else: silence(val, p)
                files.append(p)
            lst = os.path.join(td, "list.txt")
            open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
            safe = re.sub(r"[^A-Za-z0-9ÄÖÜäöüß]+", "-", titel).strip("-")
            outp = os.path.join(a.out, f"{base}-abschnitt-{n:02d}-{safe}.mp3")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                            "-c:a", "libmp3lame", "-b:a", "48k", outp], check=True)
            dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", outp],
                                 capture_output=True, text=True).stdout.strip()
            print(f"{outp}  {float(dur)/60:.1f} min  {os.path.getsize(outp)//1024} KB")

asyncio.run(main())
