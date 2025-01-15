
# Dynamisches Segment

FlexRay ist ein hochentwickeltes Bussystem, das in der modernen Fahrzeugelektronik weit verbreitet ist. Es ermöglicht sowohl deterministische als auch nicht-deterministische Datenübertragungen und wird häufig in sicherheitskritischen Anwendungen eingesetzt. Entwickelt speziell für die Automobilindustrie, besticht FlexRay durch seine hohe Zuverlässigkeit, schnelle Datenübertragung und Fehlertoleranz. Das System unterstützt sowohl synchrone als auch asynchrone Kommunikation und besteht aus zwei Hauptsegmenten: dem statischen und dem dynamischen Segment. In diesem Teil widmen wir uns ausführlich dem dynamischen Segment des FlexRay-Protokolls, um dessen Funktionalitäten und Einsatzmöglichkeiten detailliert zu erläutern.

Das dynamische Segment von FlexRay ist optional und wird verwendet, um bedarfsorientierte Botschaften zu übertragen, was asynchrone Vorgänge unterstützt. Im Gegensatz zum statischen Segment, das deterministische Übertragung garantiert, bietet das dynamische Segment eine flexible Kommunikationsmöglichkeit, um den aktuellen Bedarf zu decken.

## Struktur und Funktionsweise

Das dynamische Segment folgt immer auf das statische Segment und weist immer die gleiche Länge auf, um die deterministische Datenübertragung im statischen Segment nicht zu beeinflussen. Die Kommunikationsstrategie im dynamischen Segment basiert auf dem Flexible Time Division Multiple Access (FTDMA)-Verfahren. Dieses Verfahren ermöglicht trotz des Grundprinzips des Time Division Multiple Access (TDMA) einen flexiblen Kommunikationsablauf.

### Ablauf im dynamischen Segment

1. **Zählerinkrementierung**: Zu Beginn des dynamischen Segments inkrementieren alle FlexRay-Knoten ihre lokalen Zähler. Der aktuelle Zählerwert ist dabei einem Knoten und einer dynamischen Botschaft zugeordnet.
2. **Minislot-Prinzip**: Wenn keine Sendeanforderung für die dynamische Botschaft vorliegt, die dem aktuellen Zählerwert entspricht, inkrementieren die Knoten ihre Zähler um die Länge eines Minislots. Ein Minislot repräsentiert die minimale Zeiteinheit im dynamischen Segment.
3. **Sendeanforderung und dynamische Slots**: Liegt eine Sendeanforderung vor, überträgt der entsprechende Knoten die Botschaft. Nach der Übertragung folgt wieder ein Minislot, und die Zähler werden erneut inkrementiert. Dieses Verfahren wiederholt sich, bis das dynamische Segment für weitere Übertragungen zu kurz ist.
4. **Restzeit und Zyklen**: Wenn das dynamische Segment für eine weitere Übertragung zu kurz ist, findet bis zum Ende des Segments keine Datenübertragung mehr statt. Nicht übertragene Botschaften können im nächsten Zyklus übertragen werden.

## Prioritäten im dynamischen Segment

Die Zuordnung von Zählerwerten zu dynamischen Botschaften ist entscheidend für die Übertragungswahrscheinlichkeit. Botschaften mit niedrigeren Zählerwerten haben eine höhere Priorität und somit eine größere Wahrscheinlichkeit, übertragen zu werden. Der Systemdesigner muss sicherstellen, dass auch Botschaften mit niedriger Priorität übertragen werden können, insbesondere wenn keine höher priorisierten Sendeanforderungen vorliegen.

### Herausforderungen und Designüberlegungen

1. **Prioritätenmanagement**: Der Systemdesigner muss ein ausgewogenes Prioritätensystem implementieren, um sicherzustellen, dass alle Botschaften unabhängig von ihrer Priorität in akzeptabler Zeit übertragen werden.
2. **Längste Botschaft**: Es muss gewährleistet sein, dass die längste dynamische Botschaft innerhalb des dynamischen Segments vollständig übertragen werden kann.
3. **Bedarfsorientierte Übertragung**: Die dynamischen Botschaften werden nur bei Bedarf übertragen, was eine effiziente Nutzung der verfügbaren Bandbreite ermöglicht.
