# IEEE Ethernet MAC und VLAN




## Ethernet Frame

Basic und Tagged Frame
In den IEEE-Spezifikationen sind unterschiedliche Formate für Ethernet Frames definiert. Die Automobilbranche verwendet typischerweise den Ethernet II Frame, der als Erweiterung auch Informationen für VLAN beinhalten kann. Aus diesem Grund wird zwischen Basic MAC Frame (ohne VLAN) und Tagged MAC Frame (inklusive VLAN) unterschieden.

![1712318298889](/img/eth/1712317878278.png)


### MAC-Adressen

Generell beginnt ein Ethernet II Frame mit einer Empfänger- bzw. Zieladresse. Diese legt fest, welche Netzwerkteilnehmer eine Botschaft erhalten sollen. Im Gegensatz zur darauf folgenden Sender- bzw. Quelladresse, können hier neben Unicast- auch Multicast- oder Broadcast-Adressen verwendet werden. Für einen Ethernet Frame kann es somit immer nur einen Sender aber mehrere Empfänger geben.

### Ether Type

Eine Unterscheidung zwischen Basic und Tagged MAC Frame erfolgt mit dem Typfeld (Ether Type). Dieses kennzeichnet generell das enthaltene Paket im Nutzdatenbereich und gibt damit Auskunft über verwendete Protokolle in den höheren Schichten (z.B. IPv4). Sollte hier eine VLAN-Kennung (z.B. 0x8100) enthalten sein, so wird das Typfeld um vier Byte nach hinten verschoben und an dessen ursprünglicher Position ein VLAN Tag eingefügt.

![1712318298889](/img/eth/1712317917699.png)

### VLAN Tag

Ein VLAN Tag besteht aus einem Protocol Identifier (TPID) und einer Control Information (TCI). Während die TPID den Wert der VLAN-Kennung aus dem ursprünglichen Typfeld beinhaltet, besteht die TCI aus einer Priorität (PCP), einem Drop Eligible oder Canonical Form Indicator (DEI oder CFI) sowie einem Identifier (VID). In der Automobilbranche werden hauptsächlich Identifier und Priorität verwendet. Der Identifier kennzeichnet das jeweilige virtuelle Netzwerk für die unterschiedlichen Anwendungsbereiche. Die Priorität erlaubt die Optimierung von Laufzeiten durch Switches, sodass wichtige Informationen bevorzugt weitergeleitet werden.

### Payload

Der Ethernet II Frame beinhaltet im Anschluss an das Typfeld einen Nutzdatenbereich der als Payload bezeichnet wird. Die Payload hat eine Mindestlänge von 46 Byte ohne bzw. 42 Byte mit VLAN Tag. Maximal können in der Automobilbranche bis zu 1500 Byte enthalten sein.

### CRC-Prüfsumme

Am Ende des Ethernet II Frames wird eine CRC-Prüfsumme übertragen. Der enthaltene Wert wird mit Hilfe eines standardisierten Algorithmus berechnet, der in Sender und Empfänger gleich implementiert ist. Die Berechnung erfolgt mit allen Feldern des Ethernet II Frames und sichert daher die gesamte Botschaft ab.

### Ethernet Packet

Für die Übertragung des Ethernet II Frames fügt ein Ethernet Controller zu Beginn eine Präambel sowie einen Start Frame Delimiter (SFD) hinzu. Diese dienen historisch zur Signalisierung des Übertragungsbeginns. Die Kombination aus Präambel, Start Frame Delimiter und Ethernet II Frame wird als Ethernet Packet bezeichnet.

![1712318298889](/img/eth/1712317935542.png)

