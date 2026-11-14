# Essensbestellung – rekonstruierter Lernstand

Dies ist **keine 1:1-Kopie der Originaldateien**. Das Projekt wurde aus den
wieder auffindbaren Schritten einer früheren ChatGPT-Unterhaltung neu aufgebaut.
Nicht rekonstruierbare Details (z. B. einzelne HTML-/CSS-Werte) sind sinnvolle
Ergänzungen und können von deinen ursprünglichen Dateien abweichen.

## Aktueller Umfang

- Flask-Anwendung mit GET-Route `/`
- Dynamische Jinja2-Tabelle für die historischen Beispieltage **09.–13.11.2026**
- Zwei Menüoptionen pro Tag (historische Beispieldaten)
- Radio-Auswahl pro Tag: `menu_1`, `menu_2`, `none`
- CSS einschließlich Tabellen-Hover mit `background-color: #dcebe5`
- Das Absenden ist bewusst deaktiviert: **keine POST-Verarbeitung, keine Datenbank**

## Start in PyCharm (Windows oder Linux)

1. Diesen Ordner als Projekt öffnen.
2. Als Python-Interpreter eine virtuelle Umgebung `.venv` wählen (venv oder uv).
3. Projektabhängigkeiten installieren (bei uv z. B. `uv sync`, ansonsten `python -m pip install 'Flask>=3.1,<4'`).
4. `app.py` ausführen oder im Terminal `python app.py` starten.
5. `http://127.0.0.1:5000` im Browser öffnen.

Nur für lokale Entwicklung: `debug=True` ist **nicht** für den Produktivbetrieb gedacht.

## Nächste Entwicklungsschritte (noch NICHT implementiert)

1. POST-Route und Formularverarbeitung mit Validierung hinzufügen.
2. SQLite-Datenmodell für Nutzer, Menüs, Bestellungen und Abwesenheiten entwerfen.
3. Auswahlen speichern und bestehende Bestellungen wieder anzeigen.
4. Übersicht über alle Bestellungen und Export bauen.
5. Admin-Funktion zum Abschließen von Bestellungen einführen.
6. Sitzbereich/Etage und Abwesenheiten (`Urlaub`, `Abwesend`) ergänzen.
7. Tests, Rechtekonzept und Konfiguration ergänzen.

## Quelle und Genauigkeit

Nachvollziehbar aus dem Gespräch: Flask/Python-Projekt, Wochenliste, fünf Tage,
Menünamen, Jinja2-Ausgabe (`menus | length`), Datumsfeld `date_iso`, geplante
POST-Form mit gruppierten Radios, CSS-Hover und noch fehlende SQLite-Speicherung.

Rekonstruiert und nicht als Original zu verstehen: konkreter Wortlaut der
Templates, CSS-Layoutwerte, exakte ursprüngliche Dateiverteilung und Projekteinstellungen.
Für eine originalgetreue Wiederherstellung sind deine lokalen Dateien maßgeblich.

Der frühere Gesprächsverlauf diskutierte außerdem eine **Zielstruktur** mit
`templates/base.html`, `templates/orders.html`, `templates/admin.html`,
`static/js/main.js` und `instance/essen.db`; diese Dateien werden hier nicht
fälschlich als bereits implementiert ausgegeben.
