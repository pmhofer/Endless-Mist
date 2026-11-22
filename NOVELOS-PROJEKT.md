# NOVELOS-PROJEKT — Endless Mist

*Projektverfassung für die NovelOS-Skills. Kurz halten, Details stehen in den verlinkten Dateien.*

## 1. Grunddaten
| Feld | Wert |
|---|---|
| Titel | Endless Mist (deutscher Arbeitstitel: *Nebelgänger*) |
| Sprache | Deutsch |
| Genre | Dark Fantasy, soulslike: wild, sphärisch, ohne Zahlen (E3). `genre-styles.yaml`: `dark_fantasy_horror`, Unterton `grimdark/psychological_grimdark` |
| **Aktiver Ansatz / Richtung** | A: Der Mistwalker-Loop (E1) |
| Aktuelle Phase | 2A (Konzept) |
| Zielwortzahl pro Kapitel | ca. 3.500 (vorläufig, offen) |
| Zielwortzahl Buch | ca. 85.000 (vorläufig, offen) |

## 2. Kanon
| Rolle | Datei |
|---|---|
| **Kanon-Master** (gewinnt bei Widersprüchen) | `ENTSCHEIDUNGEN.md` |
| Konzept, Figuren, Welt | `02_Konzept/Endless-Mist-Konzept.md` |
| Begriffe/Glossar | Abschnitt „Begriffe“ im Konzept |
| Story/Struktur | `03_Outline/` (noch leer) |
| **Rohinput (nie verändern)** | `01_Rohmaterial/` |

## 3. Stil
| Datei | Wofür |
|---|---|
| `02_Konzept/STIL.md` | **Erzählstimme und Handwerk (verbindlich)**, S1–S3 |
| `07_System/CLAUDE.md` | Ton und Stilregeln für KI-Agenten |
| `novelos/AGENTS.md` §5 | Anti-KI-Prosa-Gesetze |

**Erzählperspektive:** Ich-Perspektive der Seele (E4)
**Zeitform:** Präsens (E6)

## 4. Harte Regeln (per Textsuche prüfbar)
| # | Regel | Prüfung |
|---|---|---|
| R1 | Die Seele hat keinen Namen. Nur andere nennen sie „Mistwalker“. | `grep -n "Mistwalker" 05_Kapitel/` nur in wörtlicher Rede |
| R2 | Jeder Tod kostet eine Erinnerung und hinterlässt eine Narbe (einen dauerhaften Vorteil). Kein Tod ohne Preis. | Beat-Sheets: jeder Tod nennt Verlust + Narbe |
| R3 | Niemand kehrt aus dem Nebel zurück, der die markierten Routen verlässt oder verstoßen wird (E10). Ausnahmen nur per Entscheidung in `ENTSCHEIDUNGEN.md`. | Kanon-Check |
| R4 | Keine Zahlen, keine Systemmeldungen, keine Spielbegriffe (kein „Level“, „Perk“, „Run“, „XP“, „Loot“). Fortschritt zeigt sich nur am Körper, an Narben und an gefundener Rüstung (E3, E4). | `grep -niE "level|perk|xp|loot|skill" 05_Kapitel/` |
| R5 | Kälte ist immer da. Keine Szene ohne körperliche Winterkälte (Atem, Finger, Frost, Feuchte). | Lektorat: Hemingway-Wetter-Check |
| R7 | *Vorschlag (Lektorat Kap. 2):* Ab Kap. 2 kennt das Ich das Wort „Turm“ nicht mehr („das Hohe mit dem Licht“), bis die Erinnerung zurückkommt. | `grep -n "Turm" 05_Kapitel/` nur in fremder Rede ab Kap. 2 |
| R6 | Iron-Lung-Prinzip: Die Seele sieht nie mehr als ein paar Meter. Was im Nebel ist, wird über Geräusch, Druck und Kälte erfahren, selten über das Auge. | Lektorat: Sensorik-Check |

## 5. Dateien & Versionen
| Was | Pfad / Schema |
|---|---|
| Aktuelle Manuskriptversion | `05_Kapitel/MANUSKRIPT.md` (noch nicht angelegt) |
| Beat-Sheets | `04_Beats/Kapitel_XX_Beats.md` |
| Lektoratsberichte | `06_Analyse/lektorat-<datum>.md` |
| Session-Log | `07_System/session-log.md` |

**Regel (RULE 0):** Nichts löschen, nichts überschreiben. Neue Versionen anlegen, Veraltetes nach `99_Archiv/` verschieben (mit Notiz, warum).
**Regel (RULE 00-B):** Vor jedem Schreib-, Lektorats- oder Analyseschritt eine kurze 2-Zeilen-Ansage, was geladen wird und was das Ziel ist.
