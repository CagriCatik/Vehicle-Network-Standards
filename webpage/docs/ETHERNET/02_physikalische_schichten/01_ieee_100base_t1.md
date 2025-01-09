# IEEE 100BASE-T1 (ehem. OABR)

IEEE 100BASE-T1 ist ein Ethernet-Standard, der speziell für Anwendungen in der Automobilindustrie entwickelt wurde. Dieser Standard ermöglicht die Übertragung von Daten über eine einzelne verdrillte Zweidrahtleitung mit hohen Datenraten und bietet gleichzeitig eine robuste Kommunikationslösung, die den Anforderungen moderner vernetzter Fahrzeuge gerecht wird. Der Standard wurde ursprünglich von der Firma Broadcom als Open Alliance BroadR-Reach (OABR) entwickelt und später von der IEEE standardisiert.

## Physikalische Anbindung

Für die physikalische Übertragung wird eine symmetrische, verdrillte Zweidrahtleitung verwendet. Die Informationsübertragung erfolgt über Differenzspannungen, die von einem Sender erzeugt werden. Diese Spannungen repräsentieren Symbole, welche entsprechend dem übertragenen Bitstrom kodiert werden. Der Empfänger dekodiert den Symbolstrom, um die enthaltenen Bits zurückzugewinnen. Diese Methode minimiert Störeinflüsse und erlaubt eine zuverlässige Signalübertragung in elektromagnetisch anspruchsvollen Umgebungen.

## Kodierung und Dekodierung

Die Kodierung und Dekodierung in 100BASE-T1 werden durch eine Kombination mehrerer Kodierungsschemata erreicht:

1. **4B3B (Vier Binär Drei Ternär) Kodierung** : Wandelt 4-Bit-Binärdaten in einen 3-Symbol-Ternärcode um, wodurch die benötigte Bandbreite für die Übertragung reduziert wird.
2. **3B2T (Drei Binär Zwei Ternär) Kodierung** : Komprimiert die Daten weiter in ein formatgerechtes Übertragungsformat.
3. **PAM3 (Pulsamplitudenmodulation mit 3 Pegeln)** : Verwendet drei Spannungspegel zur Darstellung der Datensymbole.

Diese Kodierungsschemata sind im 100BASE-T1 PHY (Physical Layer Transceiver) implementiert, einem integralen Bestandteil der elektronischen Steuergeräte (ECU). Der PHY dient als Brücke zwischen dem physikalischen Medium und dem Ethernet-Controller und sorgt für eine effiziente Datenübertragung.

![1712318298889](/img/eth/1712317526881.png)

## Topologie

IEEE 100BASE-T1 unterstützt eine Punkt-zu-Punkt-Verbindung, wobei üblicherweise zwei Knoten an einer Leitung angeschlossen sind. Für Netzwerke mit mehr als zwei Knoten wird ein Switch eingesetzt, der auf Layer-2-Ebene die Verbindung zu mehreren Knoten herstellt. Diese flexible Topologie erlaubt den Einsatz in komplexen Netzwerken, wie sie in modernen Fahrzeugen zu finden sind.

![1712318298889](/img/eth/1712317547537.png)

## Full Duplex

Ein besonderes Merkmal von IEEE 100BASE-T1 ist die Full-Duplex-Kommunikation, die es erlaubt, Daten bidirektional mit einer Geschwindigkeit von 100 Mbit/s über eine einzelne Leitung zu übertragen. Hierbei sendet jeder Knoten seine Differenzspannungen auf der Leitung, während gleichzeitig empfangene Spannungen subtrahiert werden. Dieser Mechanismus basiert auf Echo-Cancellation, einer Technik, die auch in anderen Ethernet-Standards verwendet wird. Full-Duplex bietet erhebliche Vorteile hinsichtlich Datenrate und Effizienz.

![1712318298889](/img/eth/1712317571251.png)

## Synchronisation

Die Synchronisation zwischen Sender und Empfänger ist essenziell, um sicherzustellen, dass die übertragenen Symbole korrekt interpretiert werden. Dies wird durch die Konfiguration eines Masters und eines Slaves erreicht. Der Master generiert kontinuierlich ein Symbolstrom, mit dem der Slave synchronisiert wird. Die Master- oder Slave-Konfiguration des PHYs erfolgt über die Basissoftware des Mikrocontrollers. Diese Synchronisation sorgt dafür, dass die Kommunikation stabil und verlustfrei bleibt.

**Vorteile von IEEE 100BASE-T1**

- Kosteneffizienz: Geringe Kabelkosten durch Nutzung von Zweidrahtleitungen.
- Robustheit: Hohe Widerstandsfähigkeit gegen elektromagnetische Störungen.
- Datenrate: Bis zu 100 Mbit/s über eine Leitung.
- Flexibilität: Einsatz in Punkt-zu-Punkt-Topologien und komplexen Netzwerken.
- Full-Duplex-Unterstützung: Gleichzeitiges Senden und Empfangen von Daten.

Zusammenfassend lässt sich sagen, dass IEEE 100BASE-T1 ein robuster und effizienter Standard für Automotive Ethernet ist, der Hochgeschwindigkeits-Vollduplex-Kommunikation über ein einfaches verdrilltes Paar ermöglicht und somit bestens für die anspruchsvollen Umgebungen moderner Fahrzeugnetzwerke geeignet ist