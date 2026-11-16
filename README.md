# PFADT Property Care Mallorca: Website-Entwurf

Gestaltungsentwurf für eine neue Website in drei Sprachen (Deutsch, Spanisch, Englisch).
Dies ist eine Vorschau und noch nicht die offizielle Website. Alle Seiten tragen `noindex`.

## Aufbau

- `de/`, `es/`, `en/`: die fertigen Seiten je Sprache (12 Seiten pro Sprache)
- `assets/`: Gestaltung, Schriften (lokal eingebunden), Bilder
- `src/`: Texte je Sprache (`content_*.py`) und der Seitengenerator (`build.py`)

Texte ändern: Datei in `src/` anpassen, dann `python3 src/build.py` ausführen.

Menü: Leistungen (Hausbetreuung und Kontrollgänge, Reinigung, Ankunfts- und Abreiseservice,
Immobilienservice), So arbeite ich, Über Leoni, Region, Fragen, Kontakt.

## Bitte vor Veröffentlichung bestätigen

Diese Punkte gehen über die bisherige Website hinaus und sind Vorschläge:

1. Rückmeldung mit Fotos nach jedem Besuch
2. Schlüsselverwahrung mit Code statt Name oder Adresse
3. Handwerkerkoordination, Angebote einholen, Lieferungen annehmen
4. Abstimmung mit Gärtner und Poolservice, Ansprechpartnerin im Notfall
5. Wäscheservice, Kühlschrank füllen, Außenmöbel verstauen
6. Besuchsrhythmus (wöchentlich, zweiwöchentlich, monatlich) und Zusatzbesuch nach Unwetter
7. Antwort innerhalb eines Werktags
8. Ortsliste des Einsatzgebiets
9. Sprachen, in denen betreut wird

## Platzhalter

- **Kundenstimmen:** ausgedacht und auf der Seite sichtbar als Beispiel gekennzeichnet.
- **Porträt:** Platzhalter. Foto als `assets/img/leoni.jpg` ablegen und `python3 src/build.py` ausführen.
- **Impressum und Datenschutz:** Platzhalter, vollständige Rechtstexte folgen.
- **Kontaktformular:** öffnet WhatsApp oder das E-Mail-Programm, es wird nichts gespeichert.

## Bilder und Schriften

Fotos von Unsplash (Unsplash-Lizenz), Foto-IDs: 1681038246005-b300835f0282, 1691357262296-18b01b9ce9fd,
1631724604275-af3bbb5c904d, 1721906495109-959e8b8a2927, 1609770231080-e321deccc34c,
1589284112965-62a5a0ffda77, 1631724953362-965648cc302c, 1694011426216-02a594332606.
Sie sind Stellvertreter und sollten durch eigene Fotos der betreuten Häuser ersetzt werden.

Schriften: Cormorant Garamond und Manrope (SIL Open Font License), lokal eingebunden.
Keine Cookies, kein Tracking, keine externen Skripte.
