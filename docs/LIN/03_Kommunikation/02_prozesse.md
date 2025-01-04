### LIN-Kommunikation im Fahrzeug

#### Master-Task und Slave-Task

In der Local Interconnect Network (LIN) Kommunikation gibt es keinen dedizierten Kommunikationscontroller. Stattdessen wird das Protokoll als Softwarekomponente auf dem Mikrocontroller implementiert. Jeder Knoten in einem LIN-Netzwerk besitzt daher entweder eine Master- oder eine Slave-Task, um die notwendige Kommunikation abzuwickeln. Grundsätzlich verfügt jeder Knoten über eine Slave-Task, die zum Empfangen und Senden von Informationen dient. Der Master-Knoten hat zusätzlich eine Master-Task, die das Senderecht verteilt und den Buszugriff regelt.

#### Master-Verhalten

Wenn ein LIN-Netzwerk in Betrieb genommen wird, wird die Master-Task im Master-Knoten gestartet. Diese beginnt mit der zyklischen Abarbeitung des sogenannten Schedules, das das gewünschte Sendeschema abbildet. In diesem Schedule sind Slots für die einzelnen Botschaften definiert. Diese Slots müssen groß genug sein, um sowohl den Frame Header als auch die Frame Response zu übertragen. In jedem Slot wird immer ein kompletter Frame übertragen.

#### Slave-Verhalten

Für die Slave-Tasks wird ein spezifisches Antwortverhalten definiert. Dieses Verhalten legt fest, wie eine Slave-Task auf einen empfangenen Header reagieren soll. Mögliche Reaktionen umfassen das Senden einer Response, das Empfangen einer Response oder das Ignorieren des Headers. Eine gesendete Response kann generell von jeder Slave-Task empfangen werden. Das gewünschte Antwortverhalten der einzelnen Knoten ist in der LIN Description File (LDF) beschrieben.

#### Technische Details und Protokollstruktur

##### Frame-Struktur

Ein LIN-Frame besteht aus mehreren Komponenten:

- **Break-Feld**: Signalisiert den Beginn eines Frames.
- **Sync-Feld**: Synchronisationsfeld, das die Baudrate festlegt.
- **Identifier-Feld**: Beinhaltet die Kennung der Nachricht.
- **Data-Feld**: Enthält die eigentlichen Nutzdaten.
- **Checksum-Feld**: Dient der Fehlererkennung.

Der Master-Knoten sendet den Break, das Sync-Feld und das Identifier-Feld. Die Slaves reagieren basierend auf ihrer Konfiguration im LDF.

##### Kommunikationsplan (Schedule Table)

Der Schedule Table ist ein wesentlicher Bestandteil der LIN-Kommunikation. Er definiert, wann welcher Frame gesendet wird und stellt sicher, dass die Kommunikation deterministisch abläuft. Jeder Eintrag im Schedule Table enthält:

- **Slotzeit**: Dauer des Slots.
- **Frame-Informationen**: Welcher Frame in diesem Slot übertragen wird.

#### Implementierung und Konfiguration

Die Implementierung eines LIN-Netzwerks erfordert eine sorgfältige Planung und Konfiguration:

- **Master-Task**: Muss den Schedule Table korrekt abarbeiten und die Frames gemäß den Zeitvorgaben senden.
- **Slave-Task**: Muss auf die empfangenen Header korrekt reagieren und die vorgesehenen Daten senden oder empfangen.

Die Konfiguration erfolgt hauptsächlich durch die LIN Description File (LDF), die alle relevanten Informationen wie die Frames, ihre IDs und das Verhalten der Slaves enthält.

#### Fehlererkennung und Diagnostik

LIN bietet grundlegende Mechanismen zur Fehlererkennung, darunter die Checksum im Frame. Bei der Implementierung müssen zudem Diagnostik-Frames berücksichtigt werden, die dem Master und den Slaves ermöglichen, ihren Status mitzuteilen und Fehler zu melden.

Durch die genaue Beachtung dieser technischen Details und Protokollstrukturen kann ein robustes und effizientes LIN-Kommunikationsnetzwerk im Fahrzeug aufgebaut werden.
