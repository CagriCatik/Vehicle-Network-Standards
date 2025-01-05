# Layout von Signalen, PDUs und Frames

## Layout von Signalen, PDUs und Frames

In der automobilen Kommunikation, besonders im Rahmen von AUTOSAR (AUTomotive Open System ARchitecture), sind Signale, Protokolldateneinheiten (PDUs) und Frames die zentralen Bausteine für den Datenaustausch zwischen elektronischen Steuergeräten (ECUs). Diese Elemente sind hierarchisch organisiert und bilden die Grundlage für die strukturierte und effiziente Datenübertragung innerhalb eines Fahrzeugs. Dieser Abschnitt bietet eine umfassende Analyse der Struktur und des Layouts dieser Komponenten, ergänzt durch reale Beispiele, detaillierte Diagramme und Best Practices.

###  Hierarchische Struktur: Signale, PDUs und Frames

Die Kommunikation in einem AUTOSAR-basierten Fahrzeugnetzwerk folgt einer streng hierarchischen Struktur:

- Signale: Die kleinste Daten- und Informationseinheit, die spezifische Fahrzeugzustände oder -informationen darstellt, wie z. B. die Geschwindigkeit oder Motortemperatur.
- Protokolldateneinheiten (PDUs): Container für Signale. Eine PDU enthält mehrere Signale und zusätzliche Steuerinformationen, die für den Transport und die Interpretation der Signale notwendig sind.
- Frames: Eine oder mehrere PDUs werden in einem Frame zusammengefasst, der über das Netzwerkprotokoll (z. B. CAN, LIN, FlexRay) übertragen wird. Der Frame stellt sicher, dass die PDUs korrekt adressiert und priorisiert werden.

Diagramm zur Veranschaulichung der Hierarchie:

```markdown
+------------------------------------------------------------+
|                         Frame                              |
| +--------------------------------------------------------+ |
| |                    PDU (Protokolldateneinheit)          | |
| | +------------------------------------+ +--------------+ | |
| | |          Signal 1                  | | Signal 2     | | |
| | +------------------------------------+ +--------------+ | |
| | +--------------+ +-----------------------------+       | |
| | |   Signal 3   | |   Signal 4                  |       | |
| | +--------------+ +-----------------------------+       | |
| +--------------------------------------------------------+ |
+------------------------------------------------------------+
```

### 2.2.2 Struktur von Signalen

Definition:
Ein Signal ist die kleinste Informationseinheit im Netzwerk eines Fahrzeugs. Es repräsentiert eine spezifische Dateninformation, die von einem Sensor, Aktuator oder einer ECU stammt und typischerweise in Echtzeit verarbeitet wird.

Typische Eigenschaften eines Signals:

- Name: Eindeutige Bezeichnung des Signals, wie „VehicleSpeed“ oder „EngineTemperature“.
- Startbit: Die genaue Bit-Position innerhalb der PDU, an der das Signal beginnt.
- Länge: Die Anzahl der Bits, die das Signal belegt (z. B. 8 Bit für ein 1-Byte-Signal).
- Endianness: Die Anordnung der Bytes im Signal (Big-Endian oder Little-Endian).
- Skalierungsfaktor: Definiert das Verhältnis zwischen dem digitalen Wert und dem physikalischen Wert des Signals.
- Offset: Ein konstanter Wert, der zum digitalen Wert des Signals hinzugefügt wird, um den tatsächlichen physikalischen Wert zu berechnen.
- Signaltyp: Typ der Daten (z. B. Integer, Float, Boolean).
- Wertebereich: Der zulässige Bereich der Werte, den das Signal annehmen kann.

Beispiel:
Das Signal „MotorTemperatur“ könnte folgendermaßen definiert sein:

- Länge: 8 Bit (1 Byte)
- Skalierungsfaktor: 0,5
- Offset: -40
- Wertebereich: -40 bis 215 °C

Diagramm: Struktur eines Signals innerhalb einer PDU:

```markdown
+--------------------+--------------------+--------------------+
| Signalname:        | MotorTemperatur    |                    |
+--------------------+--------------------+--------------------+
| Länge:             | 8 Bit (1 Byte)     |                    |
+--------------------+--------------------+--------------------+
| Startbit:          | Bit 0              |                    |
+--------------------+--------------------+--------------------+
| Skalierungsfaktor: | 0,5                |                    |
+--------------------+--------------------+--------------------+
| Offset:            | -40                |                    |
+--------------------+--------------------+--------------------+
| Endianness:        | Little-Endian      |                    |
+--------------------+--------------------+--------------------+
```

### 2.2.3 Struktur von Protokolldateneinheiten (PDUs)

Definition:
Eine PDU ist ein Datencontainer, der mehrere Signale enthält. Sie bildet die direkte Einheit, die auf einem Kommunikationsbus übertragen wird. PDUs enthalten neben den Signaldaten auch Steuerinformationen, die notwendig sind, um die Daten korrekt zu adressieren, zu interpretieren und weiterzuleiten.

Aufbau einer PDU:

- PDU-ID: Eine eindeutige Kennung, die die PDU identifiziert.
- Länge: Die Gesamtlänge der PDU in Bytes.
- Signaldaten: Die eigentlichen Daten, bestehend aus den Signalen, die in der PDU enthalten sind.
- Header: Enthält Kontrollinformationen, wie z. B. den Zielknoten, die Priorität der Nachricht, den Protokolltyp und eine Prüfsumme zur Fehlererkennung.

Beispiel einer PDU:
Angenommen, eine PDU enthält die Signale für „Fahrzeuggeschwindigkeit“ (16 Bit) und „Motortemperatur“ (8 Bit). Die PDU hätte eine Länge von 3 Bytes und könnte folgendermaßen strukturiert sein:

Diagramm: Aufbau einer PDU mit mehreren Signalen:

```markdown
+-----------------+----------------+----------------+----------------+
| PDU-ID (8 Bit)  | Länge (8 Bit)   | Signal 1:      | Signal 2:       |
|                 |                 | VehicleSpeed   | MotorTemperature|
|                 |                 | (16 Bit)       | (8 Bit)         |
+-----------------+----------------+----------------+----------------+
```

### 2.2.4 Struktur von Frames

Definition:
Ein Frame ist die größte Einheit in der Kommunikationshierarchie und enthält eine oder mehrere PDUs. Frames werden über das Netzwerkprotokoll, z. B. CAN, FlexRay oder LIN, übertragen. Der Frame ist verantwortlich dafür, dass die PDUs korrekt adressiert und im Netzwerk übertragen werden.

Aufbau eines Frames:

- Frame-Header: Enthält Informationen zur Adressierung, zur Steuerung der Übertragung und zur Priorität des Frames.
- Payload (Nutzdaten): Der eigentliche Inhalt des Frames, bestehend aus einer oder mehreren PDUs.
- Frame-Trailer: Optional, enthält Informationen wie Prüfsummen zur Fehlererkennung und -korrektur.

Beispiel eines Frames:
Ein CAN-Frame könnte wie folgt strukturiert sein:

- Frame-Header: Enthält den 11-Bit-Identifier, der den Frame eindeutig identifiziert, sowie Steuerinformationen.
- Payload: Besteht aus einer PDU mit Fahrzeugdaten.
- Frame-Trailer: Enthält eine Prüfsumme zur Sicherstellung der Datenintegrität.

Diagramm: Aufbau eines CAN-Frames:

```markdown
+-------------------+-------------------+----------------------+
| 11-Bit Identifier | Steuerinformationen| PDU (Signale)        |
+-------------------+-------------------+----------------------+
| Frame-Trailer     |                                      |
+-------------------+--------------------------------------+
```

### 2.2.5 Signal-Mapping: Von Signalen zu PDUs zu Frames

1. Signal-Mapping auf PDUs:

- Die Signale werden in einer bestimmten Reihenfolge und an spezifischen Bit-Positionen innerhalb der PDU platziert. Das Mapping der Signale auf die PDU wird durch die Kommunikationsmatrix (Signal-zu-PDU-Mapping) definiert, die die Position jedes Signals innerhalb der PDU festlegt.
- Beispiel: Das Signal „VehicleSpeed“ beginnt bei Bit 0 der PDU und belegt 16 Bits, während „MotorTemperatur“ bei Bit 16 beginnt und 8 Bits belegt.

2. PDU-Mapping auf Frames:

- Mehrere PDUs können in einem Frame organisiert werden, abhängig von der Netzwerktopologie und den Übertragungsanforderungen. Das PDU-zu-Frame-Mapping definiert, welche PDUs in einem Frame kombiniert und in welcher Reihenfolge sie angeordnet werden.
- Beispiel: Eine PDU, die Geschwindigkeit und Motortemperatur enthält, könnte in einem CAN-Frame zusammen mit einer weiteren PDU übertragen werden, die den Kraftstoffstand enthält.

Diagramm: Mapping von Signalen zu PDUs und PDUs zu Frames:

```markdown
Signal 1: VehicleSpeed (16 Bit)  -->  +--------------------------+
                                      | PDU 1                    |
Signal 2: MotorTemperatur (8 Bit) --> | PDU 1 (24 Bit)           | 
                                      +--------------------------+
Signal 3: FuelLevel (8 Bit)       --> | PDU 2 (8 Bit)            |
                                      +--------------------------+
------------------------------------------------------------------
                                      | CAN-Frame (32 Bit)        |
                                      +--------------------------+
```

### 2.2.6 Beispiele für typische Layouts in automobilen Systemen

Beispiel 1: CAN-Bus Kommunikation

- Signale: Fahrzeuggeschwindigkeit (16 Bit), Motortemperatur (8 Bit).

- PDU: Diese Signale werden in einer PDU mit einer Länge von 24 Bit organisiert.
- Frame: Die PDU wird in einem CAN-Frame übertragen, der einen 11-Bit-Identifier, Steuerinformationen und die PDU als Nutzdaten enthält.

Beispiel 2: FlexRay Kommunikation

- Signale: Informationen zu Radpositionen, Bremsdruck (jeweils 32 Bit).
- PDU: Jedes Signal wird in einer 32-Bit-PDU organisiert.
- Frame: Ein FlexRay-Frame könnte mehrere dieser PDUs enthalten, die in unterschiedlichen Zeit-Slots übertragen werden, um deterministische Kommunikation zu gewährleisten.

Diagramm: Typischer FlexRay-Frame Layout

```markdown
+-------------------+----------------------+---------------------+
| Header:           | PDU 1 (32 Bit)        | PDU 2 (32 Bit)      |
| Sync, Slot Info   | Signal: Radposition   | Signal: Bremsdruck  |
+-------------------+----------------------+---------------------+
| Frame-Trailer     |                       |                    |
+-------------------+-----------------------+--------------------+
```

### 2.2.7 Best Practices

1. Optimierung des Signal-Mappings:

- Platzieren Sie die Signale innerhalb der PDU so, dass der verfügbare Platz effizient genutzt wird, und vermeiden Sie unnötige Lücken. Dies spart Speicherplatz und reduziert die Übertragungszeit.

2. Priorisierung von Signalen und Frames:

- Kritische Signale sollten in PDUs und Frames mit höherer Priorität und besserer Fehlererkennung platziert werden, um sicherzustellen, dass sie ohne Verzögerung und mit hoher Zuverlässigkeit übertragen werden.

3. Vermeidung von Fragmentierung:

- Um die Fragmentierung von Daten zu vermeiden, sollten PDUs so organisiert werden, dass sie innerhalb eines Frames vollständig übertragen werden können. Dies reduziert die Komplexität bei der Wiederzusammensetzung der Daten am Empfangsgerät.

4. Nutzung von Endianness-Kontrollen:

- Achten Sie auf die Byte-Reihenfolge (Endianness) beim Mapping von Signalen in PDUs, um sicherzustellen, dass die Daten unabhängig von der ECU-Architektur korrekt interpretiert werden.

5. Verwendung von Prüfsummen und Fehlerkorrektur:

- Integrieren Sie robuste Prüfsummen und Fehlerkorrekturmechanismen sowohl auf der PDU- als auch auf der Frame-Ebene, um die Integrität der übertragenen Daten sicherzustellen und Fehler während der Übertragung frühzeitig zu erkennen und zu korrigieren.

6. Dokumentation und Rückverfolgbarkeit:

- Stellen Sie sicher, dass jede Phase des Signal-, PDU- und Frame-Layouts umfassend dokumentiert ist. Eine gut dokumentierte Kommunikationsmatrix erleichtert spätere Wartungsarbeiten und erlaubt eine einfache Fehlerdiagnose.
