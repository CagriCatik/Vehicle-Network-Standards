
# Standardisierung

Die Controller Area Network (CAN)-Technologie ist seit 1994 standardisiert und spielt eine zentrale Rolle in der Fahrzeug-Elektronik. Die CAN-Standards werden hauptsächlich durch drei ISO-Dokumente beschrieben, die spezifische Aspekte des CAN-Protokolls und seiner Implementierung abdecken. In dieser detaillierten Einführung werden wir die verschiedenen Schichten des ISO/OSI-Referenzmodells, die relevanten CAN-Standards und die Implementierung von CAN in Fahrzeugen betrachten.


## CAN-Protokoll

Das CAN-Protokoll ist durch die ISO 11898-1 standardisiert. Im Vergleich zum ISO/OSI-Referenzmodell der Datenkommunikation deckt das CAN-Protokoll die Schichten Data Link Layer und Physical Layer ab.

## Data Link Layer

Im Data Link Layer wird das CAN-Protokoll in zwei Hauptkomponenten unterteilt:

- **LLC (Logical Link Control)**: Diese Komponente sorgt für die logische Steuerung des Datenflusses.
- **MAC (Medium Access Control)**: Diese Komponente regelt den Zugang zum Übertragungsmedium und steuert die Datenübertragung zwischen den Netzwerkteilnehmern.

## Physical Layer

Der Physical Layer des CAN-Protokolls wird durch die PLS (Physical Layer Signalling) beschrieben, welche die physikalische Signalisierung der Daten definiert.

## CAN-Controller

Das CAN-Protokoll wird in Hardware durch sogenannte CAN-Controller implementiert. Es gibt verschiedene Arten von CAN-Controllern, die sich im Umgang mit CAN-Botschaften unterscheiden. Man unterscheidet hauptsächlich zwischen:

- **Full-CAN-Controller**: Diese Controller speichern CAN-Botschaften in einem internen Speicher.
- **Basic-CAN-Controller**: Diese Controller besitzen keinen internen Objektespeicher und bearbeiten Botschaften direkt.

## CAN-High-Speed und CAN-Low-Speed

Die physikalische Schicht des CAN-Protokolls wird durch zwei Hauptstandards definiert:

- **ISO 11898-2 (CAN-High-Speed)**: Dieser Standard erlaubt Datenraten bis zu 1 MBit/s und findet Anwendung in sicherheitskritischen Bereichen wie Antrieb und Fahrwerk.
- **ISO 11898-3 (CAN-Low-Speed)**: Dieser Standard erlaubt Datenraten bis zu 125 KBit/s und wird vorwiegend in weniger kritischen Bereichen wie Komfortsystemen verwendet.

## Datenraten

Die Datenübertragungsraten im CAN-Netzwerk variieren je nach Anwendungsbereich:

- **ISO 11898-2**: Unterstützt Datenraten bis zu 1 MBit/s und wird in Bereichen eingesetzt, die hohe Datenübertragungsraten erfordern.
- **ISO 11898-3**: Unterstützt Datenraten bis zu 125 KBit/s und wird in Anwendungen verwendet, die geringere Übertragungsraten benötigen.

## Medium Dependent Interface (MDI)

Für die Unterschicht MDI des Physical Layers existiert kein spezifischer Standard. Die CiA DS-102 (CAN in Automation) gibt jedoch Empfehlungen für die Verwendung bestimmter Stecker, wie zum Beispiel SUB-D9-Stecker, und deren Belegung.

## Ereignisgesteuerte Kommunikation

Die Kommunikation im CAN-Netzwerk ist ereignisgesteuert, wie in der ISO 11898-1 definiert. Bei hoher Buslast kann es zur Verzögerung niederpriorisierter CAN-Botschaften kommen. Um eine deterministische Kommunikation zu gewährleisten, kann die ISO 11898-4 herangezogen werden, welche eine zeitgesteuerte Kommunikationsoption für CAN-basierte Netzwerke bietet.

## ISO/OSI-Referenzmodell und CAN

Die folgende Grafik zeigt die Beziehung zwischen dem ISO/OSI-Referenzmodell der Datenkommunikation, dem CAN-Standard und der Implementierung:

<img src="./image/1712017003646.png" alt="CAN-Netzwerk" style="max-width:50%; display: block; margin: 0 auto;" />

## Schichtenmodell

- **ISO/OSI-Modell**: Das klassische 7-Schichten-Modell der Datenkommunikation.
- **CAN im ISO/OSI-Modell**: Darstellung der Schichten, die durch das CAN-Protokoll abgedeckt werden.
- **Standards und Implementierung**: Überblick über die relevanten ISO-Standards und deren Implementierung in Hardware und Netzwerken.

Durch die Standardisierung und die detaillierte Spezifikation ermöglicht CAN eine zuverlässige und effiziente Kommunikation in Fahrzeugnetzwerken, die sowohl sicherheitskritische als auch komfortbezogene Anwendungen abdeckt.
