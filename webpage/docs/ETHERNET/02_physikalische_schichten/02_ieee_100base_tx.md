# IEEE 100BASE-TX

Physikalische Anbindung
Für die physikalische Anbindung benötigt IEEE 100BASE-TX typischerweise zwei Kanäle, die jeweils über zwei verdrillte Leiter verfügen. Es ist zwar möglich, diese Ethernet-Variante auch mit einem Kanal zu betreiben, in der Praxis ist das allerdings nur selten der Fall, da diese Netzwerke nur Simplex oder Half Duplex unterstützen.

![1712318298889](/img/eth/1712317609488.png)


## Kodierung und Dekodierung

Die Leiterpaare dienen der Übertragung von symmetrischen Differenzspannungen, die zuvor kodierte Symbole repräsentieren. Ähnlich wie bei IEEE 100BASE-T1 kodiert ein Sender die Symbole basierend auf dem gewünschten Bitstrom. Ein Empfänger dekodiert den Symbolstrom und gewinnt so die gesendeten Bits zurück.

Im Gegensatz zu IEEE 100BASE-T1 verwendet IEEE 100BASE-TX für die Kodierung und Dekodierung sowie für die Erzeugung der Differenzspannungen eine Kombination aus NRZI-, 4B5B- und MLT-3-Verfahren. Diese Verfahren sind im IEEE 100BASE-TX PHY implementiert, der als eigener Baustein im Steuergerät (ECU) eingebaut wird. Der PHY stellt die Verbindung zwischen physikalischem Medium und Ethernet Controller her.

![1712318298889](/img/eth/1712317628782.png)


## Leitungen und Stecker

Für IEEE 100BASE-TX kommen typischerweise normierte Cat5- oder Cat5e-Leitungen zum Einsatz. Von den acht verfügbaren Leitern werden vier für die Anbindung der beiden Kanäle benötigt. Die Belegung der Leiterpaare ist in den beiden Standards EIA/TIA-568A sowie EIA/TIA-568B festgelegt. Diese Standards beinhalten auch die Pin-Belegung für die üblicherweise verwendeten RJ45-Stecker und -Buchsen.

## Topologie

An einer Leitung sind immer nur zwei Knoten angeschlossen. Als Topologie steht somit nur die Punkt-zu-Punkt-Verbindung zur Verfügung. Mehr als zwei Knoten können mit Hilfe eines Koppelelements verbunden werden. Hier kommt üblicherweise ein Switch zum Einsatz, der als Layer-2-Koppelelement die Anbindung an mehrere physikalische Verbindungen erlaubt und selbständig Botschaften von Zweig zu Zweig weiterleiten kann.

## Dual Simplex

Wird IEEE 100BASE-TX mit zwei Kanälen betrieben, können Informationen bidirektional mit 100 Mbit/s übertragen werden. Hierzu verwendet ein Knoten einen Kanal zum Senden und den zweiten Kanal zum Empfangen. Unterstützt ein PHY nur festgelegte Kanalzuweisungen, muss für eine Verbindung zwischen zwei Knoten ein Crossover-Kabel verwendet werden. Allerdings verfügen moderne PHYs heute mehrheitlich über einen Autonegotiation-Mechanismus, mit dessen Hilfe ein Knoten die Kanalverwendung automatisch erkennt. Mit Autonegotiation ist der Einsatz von Crossover-Kabeln nicht mehr erforderlich.