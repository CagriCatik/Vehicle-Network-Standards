# IEEE 1000BASE-T

Physikalische Anbindung
Das IEEE 1000BASE-T benötigt für die physikalische Anbindung vier Kanäle, die jeweils über zwei verdrillte Leiter verfügen. Die Leiterpaare dienen der Übertragung von symmetrischen Differenzspannungen, die zuvor kodierte Symbole repräsentieren.

![1712318298889](/img/eth/1712317661687.png)


## Kodierung und Dekodierung

Ein Sender kodiert die Symbole entsprechend dem gewünschten Bitstrom. Ein Empfänger dekodiert den Symbolstrom und gewinnt so die gesendeten Bits zurück. Im Gegensatz zu IEEE 100BASE-T1 oder IEEE 100BASE-TX verwendet das IEEE 1000BASE-T für die Kodierung und Dekodierung sowie für die Erzeugung der Differenzspannungen eine Kombination aus 8B1Q4-, Trellis-, Viterbi- und PAM5-Verfahren. Diese Verfahren sind im IEEE 1000BASE-T PHY implementiert, der als eigener Baustein im Steuergerät (ECU) eingebaut wird. Der PHY stellt die Verbindung zwischen physikalischem Medium und Ethernet Controller her.

![1712318298889](/img/eth/1712317681688.png)


## Leitungen und Stecker

Für IEEE 1000BASE-T kommen typischerweise normierte Cat5e-Leitungen zum Einsatz. Alle acht Leiter werden für die Anbindung der vier Kanäle benötigt. Die Belegung der Leiterpaare ist in den beiden Standards EIA/TIA-568A sowie EIA/TIA-568B festgelegt. Diese Standards beinhalten auch die Pin-Belegung für die üblicherweise verwendeten RJ45-Stecker und -Buchsen.

## Topologie

An einer Leitung sind immer nur zwei Knoten angeschlossen. Als Topologie steht somit nur die Punkt-zu-Punkt-Verbindung zur Verfügung. Mehr als zwei Knoten können mit Hilfe eines Koppelelements verbunden werden. Hier kommt üblicherweise ein Switch zum Einsatz, der als Layer-2-Koppelelement die Anbindung an mehrere physikalische Verbindungen erlaubt und selbständig Botschaften von Zweig zu Zweig weiterleiten kann.

## Full Duplex

Auf Grund des PAM5-Verfahrens können zwei miteinander verbundene Knoten auf vier Kanälen gleichzeitig senden und empfangen (Full Duplex). Als Sender addiert ein Knoten seine eigenen Differenzspannungen auf die Leiter, während er als Empfänger seine eigenen Spannungen von den anliegenden Gesamtspannungen subtrahiert. Das Ergebnis der Subtraktionen entspricht den Spannungen, die von der Gegenseite gesendet wurden. Dieser Mechanismus ist Bestandteil des Echo-Cancellation-Verfahrens, das auch bei anderen Ethernet-Techniken zum Einsatz kommt.

## Synchronisation

Damit Differenzspannungen addiert bzw. subtrahiert werden können, müssen die beiden Knoten wissen, wann ein neues Symbol beginnt. Das bedeutet, dass beide Knoten auf den Symbolstrom synchronisiert sein müssen. Dies erfolgt mit Hilfe eines Master- und eines Slave-Knotens. Der Master erzeugt einen kontinuierlichen Symbolstrom, auf den sich der Slave synchronisiert. Im Gegensatz zu IEEE 100BASE-T1 werden die Rollen nicht fest konfiguriert, sondern mit Hilfe eines Autonegotiation-Mechanismus ausgehandelt.
