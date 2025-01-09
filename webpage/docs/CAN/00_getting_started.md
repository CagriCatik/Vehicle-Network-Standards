---
sidebar_position: 1
---

# Controller Area Network
---
## 1. Einführung
- **Motivation:** Warum wurde CAN entwickelt? Zuverlässige Kommunikation in Fahrzeugen und industriellen Anwendungen.
- **Standardisierung:** Überblick über ISO 11898 und internationale Normen.
---
## 2. CAN-Kommunikation
- **Netzwerk:** Aufbau und Topologien.
- **Knoten und Controller:** Beschreibung der Teilnehmer und ihrer Funktionen.
- **Transceiver:** Signalumsetzung und physikalische Übertragung.
- **Buslogik und Pegel:** Wie funktioniert die Logik und das Signalniveau des CAN-Busses?
- **Kommunikationsprinzip:** Nachrichtenbasierte Kommunikation **ohne** Master-Slave-Architektur.
---
## 3. CAN-Framing
- **Rahmentypen:** Unterschiede zwischen Daten-, Remote-, Fehler- und Overload-Frames.
- **Daten- und Remote-Frame:** Aufbau und Verwendung.
- **Bit-Stuffing:** Regel zur Fehlervermeidung bei Signalübertragung.
- **CRC und ACK:** Sicherung und Bestätigung von Daten.
---
## 4. CAN-Buszugriff
- **Prinzip:** Zugriff auf den Bus durch Priorisierung.
- **Arbitrierung:** Konfliktlösung bei gleichzeitigen Nachrichten.
- **Priorisierung:** Höchste Priorität gewinnt den Buszugriff.
---
## 5. CAN-Datensicherung
- **Codierung:** NRZ-Codierung für effiziente Signalübertragung.
- **Kabelarten:** Einsatz von Twisted-Pair zur Störungsminimierung.
- **Fehlererkennung und -behandlung:** Mechanismen zur Sicherstellung der Zuverlässigkeit.
---
## 6. CAN-FD
- **Motivation:** Erweiterung für größere Datenmengen und schnellere Übertragungen.
- **Bot- und Datenformate:** Unterschiede zu klassischem CAN.
- **Kompatibilität:** Rückwärtskompatibilität zu Standard-CAN.
- **Optimierungen:** Beschleunigte Übertragung und Sicherheit.


## ToDo

- [ ] Einführung
- [ ] Kommunikation
- [ ] Framing
- [ ] Buszugriff
- [ ] Datensicherung
- [ ] FD