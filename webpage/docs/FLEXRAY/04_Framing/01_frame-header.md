# Struktur einer FlexRay-Botschaft

FlexRay ist ein leistungsstarkes Kommunikationsprotokoll, das speziell für den Einsatz in modernen Fahrzeugen entwickelt wurde. Es ermöglicht die zuverlässige und deterministische Übertragung von Daten zwischen verschiedenen elektronischen Steuergeräten (ECUs) im Fahrzeug. Dieses Tutorial bietet eine detaillierte Erklärung der FlexRay-Datenübertragung, insbesondere des Botschaftsrahmens.

Eine FlexRay-Botschaft besteht aus drei Hauptkomponenten:

1. **Header**
2. **Payload**
3. **Trailer**

##  Header

Der Header einer FlexRay-Botschaft ist 40 Bits lang und besteht aus mehreren wichtigen Feldern:

- **Identifier (ID)**

  - Länge: 11 Bits
  - Funktion: Der Identifier kennzeichnet eine spezifische Botschaft und korrespondiert mit einem Slot im FlexRay-Cluster. Eine Ausnahme bildet die ID=0x00, die ungültige Botschaften kennzeichnet.
- **Indikatorbits**

  - Anzahl: 4 Bits
  - Funktion: Diese Bits spezifizieren näher die Art der Botschaft. Zu den Indikatorbits gehören:
    - **Payload Preamble Indicator**: Zeigt an, ob im Payload einer statischen Botschaft ein Network Management Vector oder in einer dynamischen Botschaft ein Message Identifier übertragen wird.
    - **Null Frame Indicator**: Kennzeichnet, ob der Payload ausschließlich aus Nullen besteht (ungültiger Payload).
    - **Sync Frame Indicator**: Gibt an, ob die Botschaft als Synchronisationsrahmen verwendet wird.
    - **Startup Frame Indicator**: Gibt an, ob die Botschaft als Startrahmen verwendet wird.
- **Reserviertes Bit**

  - Anzahl: 1 Bit
  - Funktion: Dieses Bit ist für zukünftige Erweiterungen reserviert und hat aktuell keine definierte Funktion.
- **Payload Length**

  - Länge: 7 Bits
  - Funktion: Zeigt die Größe des Payloads in Words (1 Word = 2 Bytes) an. Damit können maximal 254 Bytes Nutzdaten übertragen werden.
- **Header CRC Sequence**

  - Länge: 11 Bits
  - Funktion: Eine Prüfsumme, die zur Fehlererkennung dient. Sie wird basierend auf dem Identifier, der Payload Length, den Indikatorbits und einem spezifizierten Generatorpolynom berechnet.
- **Cycle Counter**

  - Länge: 6 Bits
  - Funktion: Repräsentiert die Nummer des Zyklus, in dem die Botschaft gesendet wird. Der Cycle Counter zählt von 0 bis 63 und wiederholt sich dann.

##  Payload

Der Payload-Bereich einer FlexRay-Botschaft enthält die eigentlichen Nutzdaten. Die maximale Länge des Payloads beträgt 254 Bytes, wie durch die Payload Length im Header spezifiziert. Die Datenstruktur im Payload kann je nach Anwendung variieren, aber sie ist in der Regel in statische und dynamische Segmente unterteilt:

- **Statische Segmente**: Diese sind fest zugewiesene Zeitfenster, die deterministische Kommunikationsmuster gewährleisten.
- **Dynamische Segmente**: Diese Segmente erlauben eine flexiblere Datenübertragung und können für unterschiedliche Prioritäten und Nutzlasten verwendet werden.

##  Trailer

Der Trailer einer FlexRay-Botschaft enthält abschließende Informationen, die zur Sicherstellung der Integrität und Vollständigkeit der Botschaft beitragen. Dazu gehört in der Regel eine CRC-Prüfsumme, die über den gesamten Botschaftsinhalt berechnet wird.

## Fehlerkorrektur und Synchronisation

Die FlexRay-Kommunikation ist so konzipiert, dass sie extrem robust gegenüber Fehlern und Synchronisationsproblemen ist. Die Header CRC Sequence und die CRC-Prüfsumme im Trailer stellen sicher, dass Fehler bei der Übertragung erkannt werden. Zusätzlich sorgen der Sync Frame Indicator und der Startup Frame Indicator dafür, dass die Botschaften korrekt synchronisiert und initialisiert werden.
