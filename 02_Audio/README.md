# 02_Audio — Review-Audios (Englisch)

*Stufe 1 laut `AGENTS.md`: kostenloses Edge-TTS, Stimme `en-US-EricNeural`, Tempo −6 %. ElevenLabs erst nach Freigabe des Masters.*

| Version | Kapitel | Skript | Audio |
|---|---|---|---|
| v1.0 | 1 · Turned Away | `versions/v1.0/scripts/kapitel-01-en.txt` | `versions/v1.0/audio/kapitel-01-en-abschnitt-0*.mp3` |
| v1.0 | 2 · Something Missing | `versions/v1.0/scripts/kapitel-02-en.txt` | `versions/v1.0/audio/kapitel-02-en-abschnitt-0*.mp3` |

Die Skripte sind englische Fassungen des deutschen Manuskripts (`05_Kapitel/MANUSKRIPT.md`), fürs Vorlesen angepasst. Kanon ist das deutsche Manuskript.

**Rendern:** `python3 <meta>/02_Audio/tools/render_edge.py <skript> --lang en --out versions/v1.0/audio` (braucht `edge-tts` und `ffmpeg`. In der Cloud muss das Proxy-Zertifikat im certifi-Bundle der venv stehen.)
