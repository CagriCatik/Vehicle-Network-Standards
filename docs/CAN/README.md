# Controller Area Network (CAN) 🚗

<div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/CAN_Logo.jpg" alt="CAN Logo" style="width:20%; max-width:600px;">
</div>

Dieses Repository enthält Informationen und Erklärungen zum Controller Area Network und dessen Erweiterung, dem CAN FD. Es bietet Einblicke in die Funktionsweise, die Protokolle und die Technologien hinter diesen Netzwerken. CAN steht für "Controller Area Network". Es handelt sich um ein serielles Bussystem, das vor allem in der Automobilindustrie für die Kommunikation zwischen verschiedenen Steuergeräten in Fahrzeugen verwendet wird. CAN wurde in den 1980er Jahren von Bosch entwickelt und hat sich seitdem als Standard für die Fahrzeugkommunikation etabliert. Es ermöglicht eine zuverlässige und robuste Datenübertragung auch unter extremen Bedingungen, wie sie in Fahrzeugen auftreten können.

## 📚 Inhaltsverzeichnis

### 1. [Einführung 🚀](./01_Einführung/README.md)

- 1.1. Motivation für CAN
- 1.2. Standardisierung

### 2. [CAN-Kommunikation 💬](./02_CAN-Kommunikation/README.md)

- 2.1. CAN-Netzwerk
- 2.2. CAN-Knoten
- 2.3. CAN-Controller
- 2.4. CAN-Transceiver
- 2.5. CAN-Bus
- 2.6. CAN-Buspegel
- 2.7. CAN-Buslogik
- 2.8. Kommunikationsprinzip

### 3. [CAN-Framing 🔄](./03_CAN-Framing/README.md)

- 3.1. Frametypen
- 3.2. Data Frame
- 3.3. Remote Frame
- 3.4. Adressierung
- 3.5. CRC und Acknowledgement
- 3.6. Bitstuffing

### 4. [CAN-Buszugriff 📡](./04_CAN-Buszugriff/README.md)

- 4.1. Prinzip des Buszugriffs
- 4.2. Bitweise Arbitrierung
- 4.3. Priorisierung

### 5. [CAN-Datensicherung 🔒](./05_CAN-Datensicherung/README.md)

- 5.1. Prinzip der Datensicherung
- 5.2. NRZ-Codierung
- 5.3. Twisted Pair
- 5.4. Terminierung
- 5.5. Logische Fehlererkennung
- 5.6. Logische Fehlerbehandlung
- 5.7. Fehlerverfolgung

### 6. [CAN FD 🚀](./06_CAN-FD/README.md)

- 6.1. Motivation für CAN FD
- 6.2. Vorteile und Konsequenzen
- 6.3. Neue Botschaftsformate
- 6.4. Details der CAN FD Botschaft
- 6.5. CAN oder CAN FD, die Unterscheidung
- 6.6. Kompatibilität von CAN und CAN FD Controllern
- 6.7. Beschleunigte Übertragung
- 6.8. Selbstanzeige bei zu häufigen Fehlern
- 6.9. Länge des Datenfelds
- 6.10. Mehr Daten bei gleichbleibender Sicherheit
- 6.11. Geändertes Bitstuffing

## Quellen

- [CAN: Lernmodul Einführung in CAN | Vector E-Learning](https://elearning.vector.com/mod/page/view.php?id=111)
- [Bussysteme in der Fahrzeugtechnik: Protokolle, Standards und Softwarearchitektur | SpringerLink](https://link.springer.com/book/10.1007/978-3-658-02419-2)
- [Elektrik/Elektronik-Architekturen im Kraftfahrzeug: Modellierung und Bewertung von Echtzeitsystemen | SpringerLink](https://link.springer.com/book/10.1007/978-3-642-25478-9)
