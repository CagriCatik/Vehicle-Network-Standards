# CAN

---

## 1. **Einführung**
Dieses Kapitel gibt einen Überblick über die Grundlagen und die Bedeutung von CAN in der Fahrzeugkommunikation.

- **Wichtige Inhalte:**
  - Motivation: Entwicklung von CAN für zuverlässige Kommunikation in Fahrzeugen
  - Standardisierung: Überblick über ISO 11898 und internationale Normen

---

## 2. **CAN-Kommunikation**
In diesem Abschnitt wird die grundlegende Architektur und Funktionsweise des CAN-Busses beschrieben.

- **Wichtige Inhalte:**
  - Netzwerk: Aufbau und Topologien
  - Knoten und Controller: Beschreibung der Teilnehmer und ihrer Funktionen
  - Transceiver: Signalumsetzung und physikalische Übertragung
  - Buslogik und Pegel: Funktionsweise der Logik und des Signalniveaus des CAN-Busses
  - Kommunikationsprinzip: Nachrichtenbasierte Kommunikation ohne Master-Slave-Architektur

---

## 3. **CAN-Framing**
Dieser Abschnitt behandelt die Struktur und den Aufbau von Nachrichten im CAN-Protokoll.

- **Wichtige Inhalte:**
  - Rahmentypen: Unterschiede zwischen Daten-, Remote-, Fehler- und Overload-Frames
  - Daten- und Remote-Frame: Aufbau und Verwendung
  - Bit-Stuffing: Regel zur Fehlervermeidung bei Signalübertragung
  - CRC und ACK: Sicherung und Bestätigung von Daten

---

## 4. **CAN-Buszugriff**
Hier wird erklärt, wie der Zugriff auf den Bus geregelt wird, um Kollisionen zu vermeiden.

- **Wichtige Inhalte:**
  - Prinzip: Zugriff auf den Bus durch Priorisierung
  - Arbitrierung: Konfliktlösung bei gleichzeitigen Nachrichten
  - Priorisierung: Höchste Priorität gewinnt den Buszugriff

---

## 5. **CAN-Datensicherung**
In diesem Kapitel werden die Mechanismen zur Sicherstellung der Datenübertragung und der Fehlerbehandlung erläutert.

- **Wichtige Inhalte:**
  - Codierung: NRZ-Codierung für effiziente Signalübertragung
  - Kabelarten: Einsatz von Twisted-Pair zur Störungsminimierung
  - Fehlererkennung und -behandlung: Mechanismen zur Sicherstellung der Zuverlässigkeit

---

## 6. **CAN-FD**
CAN Flexible Data Rate (CAN-FD) ist eine Weiterentwicklung des klassischen CAN-Protokolls und ermöglicht größere Datenmengen und höhere Übertragungsraten.

- **Wichtige Inhalte:**
  - Motivation: Erweiterung für größere Datenmengen und schnellere Übertragungen
  - Bot- und Datenformate: Unterschiede zu klassischem CAN
  - Kompatibilität: Rückwärtskompatibilität zu Standard-CAN
  - Optimierungen: Beschleunigte Übertragung und erhöhte Sicherheit

--- 

Diese Struktur bietet eine klare Übersicht über die Funktionsweise und technischen Aspekte des CAN-Protokolls.

## ToDo

- [ ] Einführung
- [ ] Kommunikation
- [ ] Framing
- [ ] Buszugriff
- [ ] Datensicherung
- [ ] FD