## Prozesse in der LIN-Kommunikation

### Einführung in die Aufgabenverteilung

Die Kommunikation im Local Interconnect Network (LIN) basiert auf der Implementierung des Protokolls als Softwarekomponente im Mikrocontroller der Knoten. Im Gegensatz zu anderen Bussystemen wird kein dedizierter Kommunikationscontroller verwendet. Stattdessen wird die LIN-Kommunikation durch softwarebasierte Prozesse abgewickelt, die als **Master-Task** und **Slave-Task** bezeichnet werden. Jeder Knoten im Netzwerk besitzt mindestens eine Slave-Task, während der Master-Knoten zusätzlich eine Master-Task ausführt, die das Senderecht verteilt und den Buszugriff koordiniert.

### Master-Task: Steuerung und Zeitmanagement

Die Master-Task im Master-Knoten ist für die zentrale Steuerung des LIN-Netzwerks verantwortlich. Sobald das Netzwerk in Betrieb genommen wird, beginnt die Master-Task mit der zyklischen Abarbeitung des **Schedule Tables**, der das festgelegte Sendeschema abbildet. 

#### Ablauf der Master-Task:
1. **Start des Schedules:** Der Master initiiert die Kommunikation, indem er die Einträge im Schedule Table nacheinander abarbeitet. Jeder Eintrag definiert einen **Slot**, in dem ein vollständiger Frame übertragen wird.
2. **Frame Header:** Für jeden Slot sendet der Master-Knoten den Frame Header, bestehend aus:
   - **Break-Feld**: Signalisiert den Beginn des Frames und dient als Synchronisationspunkt.
   - **Sync-Feld**: Legt die Baudrate fest, damit die Slaves sich auf die Übertragung einstellen können.
   - **Identifier-Feld**: Enthält die Kennung der Nachricht und gibt an, welcher Slave darauf reagieren soll.
3. **Koordination der Slaves:** Nach dem Senden des Frame Headers überlässt der Master den Bus an den zuständigen Slave, der entsprechend antwortet.

Durch die strikte Einhaltung des Schedules stellt die Master-Task sicher, dass die Kommunikation deterministisch bleibt und alle Knoten ihre vorgesehenen Aufgaben innerhalb der vorgegebenen Zeitfenster ausführen können.

### Slave-Task: Reaktive Kommunikation

Jeder Knoten im LIN-Netzwerk führt eine Slave-Task aus, die auf empfangene Anfragen des Masters reagiert. Die Reaktion einer Slave-Task hängt vom Inhalt des empfangenen **Frame Headers** ab. Das Verhalten wird durch die Konfiguration in der **LIN Description File (LDF)** festgelegt.

#### Mögliche Reaktionen der Slave-Task:
1. **Senden einer Response:** Der Slave-Knoten liefert eine Antwort, die im Data-Feld des Frames enthalten ist.
2. **Empfangen einer Response:** Der Slave nimmt die vom Master oder einem anderen Slave gesendete Antwort entgegen.
3. **Ignorieren des Headers:** Der Slave reagiert nicht, wenn der Frame Header für ihn irrelevant ist.

Dieses reaktive Verhalten ermöglicht eine effiziente Nutzung des Busses, da nur die Knoten aktiv werden, die für die aktuelle Kommunikation relevant sind. Die Konfiguration der Slave-Tasks durch die LDF gewährleistet, dass jeder Knoten genau weiß, wann und wie er auf bestimmte Header reagieren soll.

### Technische Details und Protokollstruktur

#### LIN-Frame-Struktur
Ein vollständiger LIN-Frame besteht aus mehreren standardisierten Komponenten, die eine zuverlässige Kommunikation ermöglichen:
1. **Break-Feld:** Signalisiert den Beginn des Frames und sorgt für eine klare Trennung zwischen den Übertragungen.
2. **Sync-Feld:** Dient zur Synchronisation der Baudrate zwischen Master und Slaves.
3. **Identifier-Feld:** Beinhaltet die Kennung des Frames, die die Empfänger darüber informiert, welche Daten folgen und wie sie darauf reagieren sollen.
4. **Data-Feld:** Enthält die eigentlichen Nutzdaten, die zwischen den Knoten übertragen werden.
5. **Checksum-Feld:** Ermöglicht die Fehlererkennung und erhöht die Zuverlässigkeit der Datenübertragung.

Diese klare Struktur stellt sicher, dass alle Knoten die Frames korrekt interpretieren und die Kommunikation robust bleibt.

#### Schedule Table
Der **Schedule Table** ist ein zentrales Element der LIN-Kommunikation, da er den zeitlichen Ablauf der Frames steuert. Jeder Eintrag im Schedule Table definiert:
- **Slotzeit:** Die Dauer des Slots, die ausreichend lang sein muss, um den vollständigen Frame zu übertragen.
- **Frame-Informationen:** Angaben darüber, welcher Frame in diesem Slot gesendet werden soll.

Die deterministische Natur des Schedule Tables ermöglicht eine präzise Planung und Synchronisation der Kommunikation im gesamten Netzwerk.

### Implementierung und Konfiguration

Die erfolgreiche Implementierung eines LIN-Netzwerks erfordert eine sorgfältige Planung und Konfiguration, die durch die LIN Description File (LDF) unterstützt wird. Diese Datei enthält alle relevanten Informationen über das Netzwerk, einschließlich:
- Frame-Strukturen und deren Identifier.
- Zeitliche Vorgaben für die Slots im Schedule Table.
- Verhalten der Slave-Tasks bei verschiedenen Frame Headers.

#### Aufgaben der Master-Task:
- Exakte Abarbeitung des Schedule Tables.
- Generierung und Übertragung der Frame Headers.
- Überwachung der korrekten Ausführung durch die Slaves.

#### Aufgaben der Slave-Task:
- Reaktion auf empfangene Frame Headers gemäß der LDF.
- Senden und Empfangen von Daten entsprechend der vorgesehenen Konfiguration.

Die LDF spielt eine zentrale Rolle bei der Definition der Kommunikationsprozesse und ermöglicht eine effiziente Implementierung und Fehlerdiagnose.

### Fehlererkennung und Diagnostik

LIN bietet grundlegende Mechanismen zur Fehlererkennung, die in die Protokollstruktur integriert sind:
- **Checksum-Feld:** Jedes Frame enthält eine Prüfsumme, die es den Empfängern ermöglicht, Übertragungsfehler zu erkennen.
- **Diagnostik-Frames:** Diese speziellen Frames ermöglichen es, den Status der Knoten zu überwachen und Fehler an den Master zu melden.

Diese Mechanismen tragen wesentlich zur Zuverlässigkeit und Stabilität des Netzwerks bei, insbesondere in Umgebungen mit hoher elektromagnetischer Störanfälligkeit.
