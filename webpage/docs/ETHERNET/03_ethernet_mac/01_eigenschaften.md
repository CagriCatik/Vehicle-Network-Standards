# Eigenschaften - MAC & VLAN

## Grundfunktionen

Die zweite Schicht der Ethernet-Kommunikation stellt wichtige Grundfunktionen für eine geregelte Datenübertragung zur Verfügung. Hierzu gehören neben dem einheitlichen Botschaftsaufbau auch die Adressierung der Teilnehmer sowie das Buszugriffsverfahren. Alle Grundfunktionen sind im Ethernet Controller implementiert, der heute üblicherweise Bestandteil eines Mikrocontrollers ist.

## Datenübertragung

Während auf der physikalischen Schicht von Symbolen und Symbolraten gesprochen wird, kommen auf der zweiten Schicht Bits zum Einsatz, die zu Ethernet Frames zusammengefasst werden. Die Übertragung des Bitstroms zwischen Ethernet PHY und Ethernet Controller erfolgt typischerweise mit dem Media Independent Interface (MII). Hierbei handelt es sich um eine Schnittstellenfamilie, die von der IEEE standardisiert ist und mehrere Varianten für diverse Übertragungsgeschwindigkeiten anbietet.

![1712318298889](/img/eth/1712317719827.png)

## Buszugriffsverfahren

Der Ethernet Controller lauscht zunächst auf dem physikalischen Medium, bevor eine Botschaft gesendet wird (Carrier Sense). Dies vermeidet das Überschreiben einer Nachricht, falls ein anderer Teilnehmer im Netzwerk bereits sendet. Ist das Medium frei, kann der Ethernet Controller seinen eigenen Sendevorgang beginnen.

Da bei Ethernet mehrere Knoten gleichzeitig auf den Bus zugreifen dürfen (Multiple Access), kann es bei klassischen Busvernetzungen zu Kollisionen kommen, wenn zwei Knoten zum gleichen Zeitpunkt mit dem Senden beginnen. Für diese Situationen verfügt jeder Ethernet Controller über eine Kollisionserkennung (Collision Detection), mit deren Hilfe ein Sendevorgang abgebrochen wird. Um eine erneute Kollision zu vermeiden, leitet ein Knoten das Neusenden anschließend erst nach Ablauf einer Zufallszeit ein (Backoff-Prozess). Die Zeitdauer muss jeder Sender selbst berechnen.

## Kollisionserkennung

Das vollständige Buszugriffsverfahren wird als Carrier Sense Multiple Access/Collision Detection (CSMA/CD) bezeichnet. Der zugehörige Algorithmus ist in jedem Ethernet Controller implementiert. Für die physikalischen Schichten in der Automobilbranche hat die Kollisionserkennung eine eher untergeordnete Rolle. Sowohl IEEE 100BASE-T1 aber auch IEEE 100BASE-TX und IEEE 1000BASE-T erlauben eine Datenübertragung mit Full Duplex oder Dual Simplex. Daher treten auf diesen physikalischen Medien normalerweise keine Kollisionen auf.
