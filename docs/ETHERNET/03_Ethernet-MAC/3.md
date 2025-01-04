# 3. IEEE Ethernet MAC und VLAN

## Eigenschaften - MAC & VLAN

### Grundfunktionen

Die zweite Schicht der Ethernet-Kommunikation stellt wichtige Grundfunktionen für eine geregelte Datenübertragung zur Verfügung. Hierzu gehören neben dem einheitlichen Botschaftsaufbau auch die Adressierung der Teilnehmer sowie das Buszugriffsverfahren. Alle Grundfunktionen sind im Ethernet Controller implementiert, der heute üblicherweise Bestandteil eines Mikrocontrollers ist.

### Datenübertragung

Während auf der physikalischen Schicht von Symbolen und Symbolraten gesprochen wird, kommen auf der zweiten Schicht Bits zum Einsatz, die zu Ethernet Frames zusammengefasst werden. Die Übertragung des Bitstroms zwischen Ethernet PHY und Ethernet Controller erfolgt typischerweise mit dem Media Independent Interface (MII). Hierbei handelt es sich um eine Schnittstellenfamilie, die von der IEEE standardisiert ist und mehrere Varianten für diverse Übertragungsgeschwindigkeiten anbietet.

<img src="image/README/1712317719827.png" alt="ethernet11" style="max-width:40%;" />

### Buszugriffsverfahren

Der Ethernet Controller lauscht zunächst auf dem physikalischen Medium, bevor eine Botschaft gesendet wird (Carrier Sense). Dies vermeidet das Überschreiben einer Nachricht, falls ein anderer Teilnehmer im Netzwerk bereits sendet. Ist das Medium frei, kann der Ethernet Controller seinen eigenen Sendevorgang beginnen.

Da bei Ethernet mehrere Knoten gleichzeitig auf den Bus zugreifen dürfen (Multiple Access), kann es bei klassischen Busvernetzungen zu Kollisionen kommen, wenn zwei Knoten zum gleichen Zeitpunkt mit dem Senden beginnen. Für diese Situationen verfügt jeder Ethernet Controller über eine Kollisionserkennung (Collision Detection), mit deren Hilfe ein Sendevorgang abgebrochen wird. Um eine erneute Kollision zu vermeiden, leitet ein Knoten das Neusenden anschließend erst nach Ablauf einer Zufallszeit ein (Backoff-Prozess). Die Zeitdauer muss jeder Sender selbst berechnen.

### Kollisionserkennung

Das vollständige Buszugriffsverfahren wird als Carrier Sense Multiple Access/Collision Detection (CSMA/CD) bezeichnet. Der zugehörige Algorithmus ist in jedem Ethernet Controller implementiert. Für die physikalischen Schichten in der Automobilbranche hat die Kollisionserkennung eine eher untergeordnete Rolle. Sowohl IEEE 100BASE-T1 aber auch IEEE 100BASE-TX und IEEE 1000BASE-T erlauben eine Datenübertragung mit Full Duplex oder Dual Simplex. Daher treten auf diesen physikalischen Medien normalerweise keine Kollisionen auf.

### Adressierung

Teilnehmeradressierung
Im Ethernet-Netzwerk kommt die Teilnehmeradressierung für die gezielte Zustellung von Botschaften zum Einsatz. Hierzu verfügt jeder Knoten über mindestens eine MAC-Adresse, die zur eindeutigen Kennung im lokalen Netzwerk (LAN) dient. Eine gesendete Botschaft beinhaltet immer eine Sender- und eine Empfängeradresse, sodass ein Rückschluss auf die Kommunikationsteilnehmer möglich ist.

<img src="image/README/1712317769475.png" alt="ethernet11" style="max-width:40%;" />

<img src="image/README/1712317744832.png" alt="ethernet11" style="max-width:40%;" />

### Unicast

Die eindeutige Adressierung der Teilnehmer erfolgt mit Hilfe von Unicast-Adressen. Diese Adressen gibt der Fahrzeughersteller entweder vor oder Zulieferer dürfen aus einem eigenen Adressbereich wählen. Adressbereiche können bei der IEEE Registry Authority beantragt sowie registriert werden und sind einem Unternehmen weltweit eindeutig zugewiesen.

### Multi- und Broadcast

Damit Botschaften mehreren Teilnehmern zustellbar sind, können neben Unicast- auch Multicast-Adressen verwendet werden. Mit deren Hilfe sind Knotengruppen definierbar, deren Mitglieder eine Nachricht über eine gemeinsame MAC-Adresse erhalten. Im Gegensatz zur Broadcast-Adresse, die das Versenden einer Botschaft an alle Teilnehmer erlaubt, müssen Multicast-Adressen im jeweiligen Knoten konfiguriert werden.

### VLAN

Als Erweiterung zur klassischen Adressierung kommen in der Automobilbranche häufig VLAN-Adressen zum Einsatz. Diese adressieren virtuelle Netzwerke, die innerhalb eines Gesamtnetzwerks vorhanden sind und eine Abgrenzung der Kommunikation erlauben. Auf diese Weise können Domänen für unterschiedliche Anwendungsbereiche festgelegt werden, deren Mitglieder auf die dort vorhandene Kommunikation zugreifen dürfen. Da ein Steuergerät üblicherweise in mehreren Anwendungsbereichen tätig ist, darf es auch Mitglied in mehreren Domänen und somit mehreren VLAN-Netzwerken sein.

<img src="image/README/1712317815931.png" alt="ethernet11" style="max-width:40%;" />

### Prioritäten

VLAN bietet für eine Verbesserung des Echtzeitverhaltens außerdem die Festlegung von Prioritäten für Botschaften an. So kann wichtiger Datenverkehr bevorzugt durch Switches geleitet werden, was eine Reduzierung von Latenzzeiten zur Folge hat.

## Ethernet Frame

Basic und Tagged Frame
In den IEEE-Spezifikationen sind unterschiedliche Formate für Ethernet Frames definiert. Die Automobilbranche verwendet typischerweise den Ethernet II Frame, der als Erweiterung auch Informationen für VLAN beinhalten kann. Aus diesem Grund wird zwischen Basic MAC Frame (ohne VLAN) und Tagged MAC Frame (inklusive VLAN) unterschieden.

<img src="image/README/1712317878278.png" alt="ethernet11" style="max-width:40%;" />

### MAC-Adressen

Generell beginnt ein Ethernet II Frame mit einer Empfänger- bzw. Zieladresse. Diese legt fest, welche Netzwerkteilnehmer eine Botschaft erhalten sollen. Im Gegensatz zur darauf folgenden Sender- bzw. Quelladresse, können hier neben Unicast- auch Multicast- oder Broadcast-Adressen verwendet werden. Für einen Ethernet Frame kann es somit immer nur einen Sender aber mehrere Empfänger geben.

### Ether Type

Eine Unterscheidung zwischen Basic und Tagged MAC Frame erfolgt mit dem Typfeld (Ether Type). Dieses kennzeichnet generell das enthaltene Paket im Nutzdatenbereich und gibt damit Auskunft über verwendete Protokolle in den höheren Schichten (z.B. IPv4). Sollte hier eine VLAN-Kennung (z.B. 0x8100) enthalten sein, so wird das Typfeld um vier Byte nach hinten verschoben und an dessen ursprünglicher Position ein VLAN Tag eingefügt.

<img src="image/README/1712317917699.png" alt="ethernet11" style="max-width:40%;" />

### VLAN Tag

Ein VLAN Tag besteht aus einem Protocol Identifier (TPID) und einer Control Information (TCI). Während die TPID den Wert der VLAN-Kennung aus dem ursprünglichen Typfeld beinhaltet, besteht die TCI aus einer Priorität (PCP), einem Drop Eligible oder Canonical Form Indicator (DEI oder CFI) sowie einem Identifier (VID). In der Automobilbranche werden hauptsächlich Identifier und Priorität verwendet. Der Identifier kennzeichnet das jeweilige virtuelle Netzwerk für die unterschiedlichen Anwendungsbereiche. Die Priorität erlaubt die Optimierung von Laufzeiten durch Switches, sodass wichtige Informationen bevorzugt weitergeleitet werden.

### Payload

Der Ethernet II Frame beinhaltet im Anschluss an das Typfeld einen Nutzdatenbereich der als Payload bezeichnet wird. Die Payload hat eine Mindestlänge von 46 Byte ohne bzw. 42 Byte mit VLAN Tag. Maximal können in der Automobilbranche bis zu 1500 Byte enthalten sein.

### CRC-Prüfsumme

Am Ende des Ethernet II Frames wird eine CRC-Prüfsumme übertragen. Der enthaltene Wert wird mit Hilfe eines standardisierten Algorithmus berechnet, der in Sender und Empfänger gleich implementiert ist. Die Berechnung erfolgt mit allen Feldern des Ethernet II Frames und sichert daher die gesamte Botschaft ab.

### Ethernet Packet

Für die Übertragung des Ethernet II Frames fügt ein Ethernet Controller zu Beginn eine Präambel sowie einen Start Frame Delimiter (SFD) hinzu. Diese dienen historisch zur Signalisierung des Übertragungsbeginns. Die Kombination aus Präambel, Start Frame Delimiter und Ethernet II Frame wird als Ethernet Packet bezeichnet.

<img src="image/README/1712317935542.png" alt="ethernet11" style="max-width:40%;" />
