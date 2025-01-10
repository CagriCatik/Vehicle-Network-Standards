# Motivation

## Elektronifizierung

Die fortschreitende Elektronifizierung hat in den letzten Jahrzehnten einen tiefgreifenden Wandel in der Automobilindustrie bewirkt. Fahrzeuge sind heute mit einer Vielzahl von elektronischen Funktionen ausgestattet, die nicht nur den Fahrkomfort und die Sicherheit erhöhen, sondern auch zur Verbesserung der Umweltverträglichkeit beitragen. Diese Funktionen werden durch eine Vielzahl von elektronischen Komponenten realisiert, darunter Steuergeräte, Sensoren und Aktoren, die in einem komplexen Netzwerk miteinander kommunizieren müssen. Der zunehmende Einsatz dieser elektronischen Komponenten erfordert einen effizienten und zuverlässigen Informationsaustausch, um die steigenden Anforderungen an Leistung und Funktionalität zu erfüllen.

## Herausforderungen der konventionellen Vernetzung

Traditionell wurden Sensoren und Aktoren in Fahrzeugen über einzelne Leitungen mit den jeweiligen Steuergeräten verbunden. Dieses einfache Verkabelungssystem führte jedoch schnell zu einer Vielzahl von Problemen. Die Anzahl der benötigten Leitungen nahm stetig zu, was zu immer dickeren und schwereren Kabelbäumen führte. Diese Kabelbäume beanspruchten nicht nur mehr Platz, sondern erhöhten auch das Gesamtgewicht des Fahrzeugs, was sich negativ auf den Kraftstoffverbrauch und die Fahrzeugdynamik auswirken kann.

Darüber hinaus erschwerte die zunehmende Komplexität der Verkabelung die Herstellung und Wartung der Fahrzeuge erheblich. Unterschiedliche Fahrzeugvarianten erforderten oft individuelle Anpassungen der Kabelbäume, was die Produktionskosten erhöhte und die Flexibilität in der Fertigung einschränkte. Die Vielzahl an Leitungen erhöhte zudem die Fehleranfälligkeit des Systems, da mehr Verbindungen potenzielle Fehlerquellen darstellten. Diese Herausforderungen führten letztlich zu steigenden Kosten für die Fahrzeugvernetzung und zwangen die Industrie dazu, nach effizienteren Lösungen zu suchen.

## CAN als Vorreiter

Ein bedeutender Schritt zur Bewältigung dieser Herausforderungen war die Entwicklung des Controller Area Network (CAN) durch die Robert Bosch GmbH im Jahr 1983. Der CAN-Bus wurde 1986 auf dem Kongress der Society of Automotive Engineers (SAE) als neues serielles Bussystem vorgestellt und etablierte sich schnell als Vorreiter in der Fahrzeugkommunikation. Der CAN-Bus ermöglichte die bitserielle Übertragung mehrerer Signale über ein einziges Leiterpaar, wodurch die benötigte Anzahl an Leitungen im Vergleich zur herkömmlichen Punkt-zu-Punkt-Verkabelung erheblich reduziert werden konnte.

Durch die Einführung von CAN konnte nicht nur die Verkabelung vereinfacht werden, sondern auch die Zuverlässigkeit und Flexibilität der Fahrzeugkommunikation verbessert werden. Der CAN-Bus ermöglichte eine effizientere Nutzung der verfügbaren Leitungen und erleichterte die Integration neuer elektronischer Funktionen. Dennoch stellte sich heraus, dass der CAN-Bus für bestimmte Anwendungen, insbesondere für kostengünstige Sensoren und Aktoren im Komfortbereich, zu teuer war.

## Kostenreduktion

Mitte der 1990er Jahre erkannten einige Fahrzeughersteller und Zulieferer die Notwendigkeit, kostengünstigere Kommunikationslösungen für einfache und nicht sicherheitskritische Anwendungen zu entwickeln. Die bestehenden herstellerspezifischen Bussysteme erwiesen sich jedoch als wenig geeignet, da sie aufgrund ihrer geringen Stückzahlen keine umfassende Kostenreduktion ermöglichten. In diesem Kontext entstand die Idee, ein einheitliches und standardisiertes Kommunikationssystem zu entwickeln, das die Vorteile der bestehenden Lösungen mit einer höheren Kosteneffizienz kombinierte.

Diese Überlegungen führten zur Gründung des LIN Consortium, einer Vereinigung mehrerer Automobilhersteller und Zulieferer, die sich gemeinsam der Entwicklung eines kostengünstigen Kommunikationssystems widmeten. Das Ziel war es, ein System zu schaffen, das einfach zu implementieren ist, geringe Hardwareanforderungen stellt und gleichzeitig eine ausreichende Leistung für die Anforderungen der Automobilindustrie bietet. Aus dieser Kooperation entstand das Local Interconnect Network (LIN), ein Bussystem, das speziell für die Integration einfacher, nicht sicherheitskritischer Funktionen in Fahrzeugen konzipiert wurde.

## LIN (Local Interconnect Network)

LIN, oder Local Interconnect Network, ist ein Kommunikationssystem, das speziell entwickelt wurde, um die Anforderungen der Automobilindustrie an eine kostengünstige, zuverlässige und einfache Vernetzung von Sensoren und Aktoren zu erfüllen. Es wurde als Ergänzung zum CAN-Bus entwickelt und ermöglicht eine kosteneffiziente Integration einfacher, nicht sicherheitskritischer Funktionen.

### Eigenschaften des LIN-Busses

1. **Kosteneffizienz**:  LIN ist deutlich kostengünstiger als CAN, da es mit einfacheren Hardwarekomponenten auskommt und weniger komplexe Software erfordert. Dies ermöglicht eine Senkung der Gesamtkosten für die Fahrzeugvernetzung, insbesondere bei der Integration großer Mengen preiswerter Sensoren und Aktoren.
2. **Topologie**: LIN verwendet eine einfache Bus-Topologie, die die Verkabelung vereinfacht und die Installationskosten reduziert. Diese einfache Struktur erleichtert die Integration in bestehende Fahrzeugarchitekturen und ermöglicht eine flexible Erweiterung des Netzwerks.
3. **Datenrate**: Mit einer Datenrate von typischerweise bis zu 20 kbit/s ist LIN für viele Komfort- und Bedienelemente ausreichend. Obwohl dies deutlich niedriger ist als die Datenraten moderner CAN-Busse, reicht sie für die Anforderungen der meisten nicht sicherheitskritischen Anwendungen aus.
4. **Master-Slave-Architektur**: Ein LIN-Bus besteht aus einem Master-Steuergerät und mehreren Slave-Komponenten. Der Master initiiert die Kommunikation, was die Implementierung vereinfacht und die Kontrolle über den Datenfluss im Netzwerk erleichtert. Diese Architektur sorgt für eine geordnete Kommunikation und minimiert die Möglichkeit von Datenkollisionen.
5. **Fehlererkennung**: LIN bietet grundlegende Mechanismen zur Fehlererkennung und -behebung, die für nicht sicherheitskritische Anwendungen ausreichend sind. Diese Mechanismen tragen zur Zuverlässigkeit des Netzwerks bei und gewährleisten eine stabile Kommunikation zwischen den Komponenten.

### Anwendungen des LIN-Busses

Dank seiner kosteneffizienten und einfachen Implementierung findet LIN breite Anwendung in verschiedenen Bereichen des Fahrzeugs, insbesondere dort, wo niedrige Kosten und einfache Integration entscheidend sind. Typische Anwendungen umfassen:

- Fensterhebersteuerung: Die Steuerung der elektrischen Fensterheber in Fahrzeugen profitiert von der einfachen und kostengünstigen Vernetzung, die LIN bietet. Die Kommunikation zwischen dem Steuergerät und den Fensterhebern kann effizient über den LIN-Bus abgewickelt werden.

- Sitzverstellung: Elektrische Sitzverstellungen, die in modernen Fahrzeugen immer häufiger vorkommen, nutzen LIN zur Steuerung und Kommunikation der verschiedenen Mechanismen, die für die Anpassung der Sitzposition verantwortlich sind.

- Klimaanlagensteuerung: Die Steuerung der Klimaanlage, einschließlich Temperaturregelung und Lüftersteuerung, wird oft über den LIN-Bus realisiert, da diese Funktionen keine hohen Datenraten erfordern und von der Kosteneffizienz von LIN profitieren.

- Beleuchtungssysteme: Die Steuerung der Fahrzeugbeleuchtung, einschließlich Innenbeleuchtung und Außenbeleuchtung, nutzt LIN zur Kommunikation zwischen den Steuergeräten und den Leuchtelementen, was eine flexible und kostengünstige Steuerung ermöglicht.

- Türmodule: Elektronische Türmodule, die Funktionen wie die zentrale Verriegelung, das Einparken und die Innenraumbeleuchtung steuern, verwenden LIN für die Kommunikation zwischen den Steuergeräten und den entsprechenden Aktoren.

<img src="./image/1716459892814.png" alt="drawing" width="400"/>

Durch die Integration von LIN in diese und weitere Anwendungen können Fahrzeughersteller die Gesamtkosten der Fahrzeugvernetzung senken, die Komplexität der Verkabelung reduzieren und gleichzeitig eine zuverlässige und effiziente Kommunikation zwischen den elektronischen Komponenten sicherstellen. LIN hat sich somit als unverzichtbares Kommunikationssystem für eine Vielzahl von Komfort- und Bedienelementen in modernen Fahrzeugen etabliert und trägt maßgeblich zur weiteren Elektronifizierung und Vernetzung von Fahrzeugen bei.