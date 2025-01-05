# Details der CAN-FD Botschaft

## Aufbau eines CAN FD Rahmens

Ein CAN FD Rahmen besteht aus mehreren Feldern, die die Struktur und den Inhalt der Nachricht definieren. Die grundlegenden Änderungen von CAN zu CAN FD betreffen vor allem den Bereich zwischen dem Identifier Extension Bit (IDE) und dem Acknowledge Bit (ACK).

### Vergleich der Rahmenspezifikationen

**Klassischer CAN-Rahmen:**

- **Start of Frame (SOF)**
- **Arbitration Field**: Enthält den Identifier und das RTR-Bit (Remote Transmission Request).
- **Control Field**: Enthält das IDE-Bit und weitere Steuerbits.
- **Data Field**: Enthält die eigentlichen Nutzdaten.
- **CRC Field**: Prüfsumme zur Fehlererkennung.
- **ACK Field**: Bestätigung der korrekten Nachrichtenerfassung.
- **End of Frame (EOF)**

**CAN FD-Rahmen:**

- **Start of Frame (SOF)**
- **Arbitration Field**: Enthält den Identifier und das RRS-Bit (Remote Request Substitution).
- **Control Field**: Enthält das IDE-Bit, das FDF-Bit (Flexible Data-Rate Format), das BRS-Bit (Bit Rate Switch), und das ESI-Bit (Error State Indicator).
- **Data Field**: Kann bis zu 64 Byte Nutzdaten enthalten (im Vergleich zu 8 Byte bei klassischem CAN).
- **CRC Field**: Verlängert, um die erhöhte Datenmenge abzudecken.
- **ACK Field**
- **End of Frame (EOF)**

## Detaillierte Betrachtung der CAN FD Felder

**1. Start of Frame (SOF):**
   Das SOF-Bit bleibt unverändert und signalisiert den Beginn eines Rahmens.

**2. Arbitration Field:**

- **Identifier**: Unverändert vom klassischen CAN.
- **RRS-Bit (Remote Request Substitution)**: Ersetzt das RTR-Bit des klassischen CAN. Da CAN FD keine Remote Frames unterstützt, wird das RTR-Bit durch ein dominantes RRS-Bit ersetzt.

**3. Control Field:**

- **IDE-Bit (Identifier Extension)**: Bestimmt weiterhin, ob der Identifier 11 oder 29 Bit lang ist.
- **FDF-Bit (Flexible Data-Rate Format)**: Zeigt an, dass der Rahmen im CAN FD Format ist.
- **BRS-Bit (Bit Rate Switch)**: Erlaubt die Umschaltung auf eine höhere Bitrate nach dem Arbitration Field, um die Übertragungsrate zu erhöhen.
- **ESI-Bit (Error State Indicator)**: Gibt den Fehlerstatus des sendenden Knotens an.

**4. Data Field:**
   Das Datenfeld kann nun bis zu 64 Byte umfassen, was eine signifikante Erhöhung im Vergleich zu den 8 Byte des klassischen CAN darstellt. Diese Erweiterung ermöglicht eine effizientere Übertragung großer Datenmengen.

**5. CRC Field:**
   Die CRC-Prüfsumme wurde erweitert, um die Integrität der größeren Datenmengen zu gewährleisten. Es enthält nun eine 17- oder 21-Bit CRC, abhängig von der Datenfeldlänge.

**6. Acknowledge Field (ACK):**
   Bleibt unverändert und ermöglicht dem Empfänger, dem Sender die erfolgreiche Nachrichtenerfassung zu bestätigen.

**7. End of Frame (EOF):**
   Beinhaltet wie beim klassischen CAN das Ende des Rahmens.

**8. Intermission Field (ITM):**
   Beinhaltet eine Ruhepause zwischen den Nachrichten, um die Synchronisation der Nodes zu gewährleisten.

## Verbesserungen und Vorteile von CAN FD

1. **Höhere Datenrate:** Durch das BRS-Bit kann die Datenrate nach dem Arbitration Field erhöht werden, was zu schnelleren Übertragungen führt.
2. **Größeres Datenfeld:** Die Möglichkeit, bis zu 64 Byte an Daten zu übertragen, ermöglicht effizientere und weniger häufige Nachrichtenübertragungen.
3. **Erweiterte Fehlererkennung:** Die erweiterte CRC ermöglicht eine verbesserte Fehlererkennung bei größeren Datenmengen.
4. **Flexibilität:** CAN FD bietet durch die flexible Datenrate und die größere Datenfeldlänge eine bessere Anpassung an unterschiedliche Anwendungen und Anforderungen.

## Schlussfolgerung

CAN FD stellt eine bedeutende Weiterentwicklung des klassischen CAN-Protokolls dar, um den gestiegenen Anforderungen moderner Fahrzeugsysteme gerecht zu werden. Die wesentlichen Änderungen im Bereich zwischen dem IDE- und dem ACK-Bit bieten erweiterte Funktionalitäten und höhere Effizienz, was CAN FD zu einem unverzichtbaren Standard in der Automobilindustrie macht. Die genaue Implementierung und Nutzung von CAN FD erfordert ein tiefes Verständnis der Protokollspezifikationen und der entsprechenden Hardwareunterstützung, um die Vorteile vollständig ausschöpfen zu können.
