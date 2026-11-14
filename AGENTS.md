# Codex-Projektanweisungen

## Zweck
Lernprojekt: Flask-Anwendung für die wöchentliche Essensbestellung im Team.
Zwei Menüs pro Tag, Bestellübersicht für alle, Export, Admin-Abschluss,
Sitzbereich/Etage und Abwesenheit (Urlaub/Abwesend) sind Zielanforderungen.

## Verifizierter Stand
- `app.py`: GET-Route `/` mit historischen Beispieldaten (09.–13.11.2026).
- `templates/index.html`: Jinja2-Wochenübersicht mit Radio-Auswahl je Tag.
- `static/css/style.css`: Basis- und Tabellengestaltung.
- Noch KEINE funktionierende POST-Speicherung, SQLite, Nutzerverwaltung, Export,
  Admin-Oberfläche oder Abwesenheitsverwaltung.
- Der Stand ist aus einem Chat **rekonstruiert**, nicht aus dem Originalprojekt exportiert.

## Zusammenarbeit
- Der Nutzer beherrscht Python, möchte Flask und Webentwicklung aber verstehen.
- Vor größeren Änderungen einen kurzen Plan und die wichtigsten Abwägungen erklären.
- Veränderungen in überschaubaren Schritten vornehmen und begründen.
- Bestehende Dateien prüfen, bevor neue Strukturen angenommen werden.
- Keine produktiven oder personenbezogenen Daten erfinden.
- Bei Datenbankmigrationen und destruktiven Aktionen zuerst explizit nachfragen.
- Tests ergänzen, wenn entsprechende Funktionalität hinzugefügt wird.
- Niemals `.env`, Zugangsdaten oder lokale Datenbanken committen.

## Erste Aufgabe für Codex
Projekt durchsehen, Ist-Zustand gegen die Anforderungen abgleichen und die
nächsten sinnvollen Implementierungsschritte vorstellen. Zunächst keine Dateien ändern.
