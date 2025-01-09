# Eigenschaften von TCP & UDP

In der modernen Automobilindustrie sind zuverlässige und effiziente Kommunikationsnetzwerke essenziell für die Funktionalität und Sicherheit moderner Fahrzeuge. Ethernet hat sich als dominierende Technologie im Automotive Umfeld etabliert, unterstützt durch Transportprotokolle wie das Transmission Control Protocol (TCP) und das User Datagram Protocol (UDP). Diese Protokolle ermöglichen eine flexible Datenübertragung, die den unterschiedlichen Anforderungen von Fahrzeuganwendungen gerecht wird. Diese Dokumentation bietet einen detaillierten Überblick über TCP und UDP, ihre Eigenschaften und deren technische Umsetzung in Fahrzeugnetzwerken.

## Grundlagen von TCP und UDP

In der Transportschicht (Schicht 4) des OSI-Schichtenmodells existieren zwei wesentliche Transportprotokolle: TCP und UDP. Beide Protokolle teilen die zu übertragenden Daten in kleinere Einheiten auf. Bei TCP werden diese aufgeteilten Daten **Segmente** genannt, während bei UDP von **Paketen** gesprochen wird.

### Transmission Control Protocol (TCP)

TCP ist ein verbindungsorientiertes Transportprotokoll, das eine zuverlässige Übertragung von Datenpaketen über Netzwerke gewährleistet. Es stellt Mechanismen bereit, die eine garantierte Zustellung, Reihenfolge und Integrität der übertragenen Daten sicherstellen. Dies macht TCP zu einer geeigneten Wahl für Anwendungen, bei denen Zuverlässigkeit und Datenintegrität von entscheidender Bedeutung sind.

### User Datagram Protocol (UDP)

UDP hingegen ist ein verbindungsloses Transportprotokoll, das eine einfache und schnelle Übertragung von Datenpaketen ermöglicht. Im Gegensatz zu TCP bietet UDP keine Garantien für die Zustellung, Reihenfolge oder Integrität der Daten. Dies macht UDP ideal für Anwendungen, bei denen Geschwindigkeit und geringe Latenz wichtiger sind als die Zuverlässigkeit der Datenübertragung.

## Adressierung

Um den gewünschten Zielknoten zu erreichen, erfolgt die Übertragung von Daten über das Internet Protocol (IP) auf der darunter liegenden Schicht 3. Die Anbindung an die höheren Schichten erfolgt mit Hilfe von **Ports**, die das Adressieren von Funktionen und Anwendungen ermöglichen. Jeder Port entspricht einer spezifischen Anwendung oder Funktion auf dem Zielgerät. Wird ein Port geöffnet, können Daten mit der zugehörigen Funktion oder Anwendung ausgetauscht werden. Dies ermöglicht eine gezielte Kommunikation zwischen verschiedenen Anwendungen innerhalb eines Fahrzeugs.

## Vorteile von TCP und UDP

### Vorteile von TCP

1. **Verbindungsorientiert**  
   TCP erfordert den Aufbau einer stabilen Verbindung zwischen Sender und Empfänger, was die zuverlässige Datenübertragung gewährleistet.

2. **Zuverlässigkeit**  
   Durch Mechanismen wie Sequenznummern, Acknowledgements und Retransmissionen stellt TCP sicher, dass Datenpakete korrekt und vollständig ankommen.

3. **Datenintegrität**  
   Die integrierte Prüfsumme (CRC) stellt sicher, dass die Daten während der Übertragung nicht verfälscht werden.

4. **Flusskontrolle**  
   Das Window-Feld ermöglicht die Steuerung der Datenflussrate zwischen Sender und Empfänger, um eine Überlastung zu verhindern.

5. **Reihenfolgegarantie**  
   TCP stellt sicher, dass die Datenpakete in der richtigen Reihenfolge beim Empfänger ankommen, selbst wenn sie in einer anderen Reihenfolge übertragen werden.

### Vorteile von UDP

1. **Verbindungslos**  
   UDP benötigt keine vorherige Verbindung zwischen Sender und Empfänger, was die Einrichtung von Kommunikationssitzungen beschleunigt und den Overhead reduziert.

2. **Geringe Latenz**  
   Da keine Bestätigungen oder Verbindungsaufbauprozesse erforderlich sind, eignet sich UDP hervorragend für zeitkritische Anwendungen.

3. **Multicast und Broadcast**  
   UDP unterstützt die Übertragung von Daten an mehrere Empfänger gleichzeitig, was die Netzwerkauslastung reduziert, wenn dieselben Informationen an mehrere Knoten gesendet werden müssen.

4. **Effizienz**  
   Der geringe Protokoll-Overhead ermöglicht eine effizientere Nutzung der Bandbreite, insbesondere bei Anwendungen, die große Mengen an kleinen Datenpaketen übertragen.

## Verbindungsaufbau und Datenübertragung

### Verbindungsaufbau mit TCP: Three-Way Handshake

Der Verbindungsaufbau in TCP erfolgt durch einen dreistufigen Prozess, bekannt als **Three-Way Handshake**:

1. **SYN**  
   Der Initiator der Verbindung sendet ein TCP-Segment mit gesetztem SYN-Flag (Synchronize) an den Empfänger. Dieses Segment enthält eine **Initial Sequence Number (ISN)**, die den Startpunkt der Datenübertragung markiert.

2. **SYN-ACK**  
   Der Empfänger antwortet mit einem TCP-Segment, das sowohl das SYN- als auch das ACK-Flag (Acknowledgement) gesetzt hat. Dieses Segment enthält ebenfalls eine ISN des Empfängers und bestätigt den Empfang der ISN des Senders.

3. **ACK**  
   Der Initiator sendet ein letztes TCP-Segment mit gesetztem ACK-Flag, das den Empfang der ISN des Empfängers bestätigt. Nach diesem Schritt ist die Verbindung etabliert, und der Datenaustausch kann beginnen.


### Datenübertragung mit TCP

Nach dem erfolgreichen Aufbau der Verbindung beginnt die Datenübertragung. TCP stellt hierbei sicher, dass die Daten zuverlässig und in der richtigen Reihenfolge beim Empfänger ankommen. Wichtige Mechanismen umfassen:

- **Sequenznummern**  
  Jedes Byte der übertragenen Daten wird nummeriert. Dies ermöglicht dem Empfänger, die Reihenfolge der Daten korrekt zu rekonstruieren.

- **Acknowledgements (ACKs)**  
  Der Empfänger sendet Bestätigungen (ACKs) für empfangene Daten. Diese Bestätigungen enthalten die nächste erwartete Sequenznummer.

- **Retransmissionen**  
  Wenn der Sender innerhalb eines bestimmten Zeitfensters keine Bestätigung für ein gesendetes Segment erhält, wird das Segment erneut übertragen.

- **Flusskontrolle**  
  Das Window-Feld im TCP-Header gibt an, wie viel Pufferraum der Empfänger zur Verfügung hat. Dies verhindert, dass der Sender mehr Daten sendet, als der Empfänger verarbeiten kann.

- **Staukontrolle**  
  TCP passt die Datenübertragungsrate dynamisch an die Netzwerkbedingungen an, um Überlastungen zu vermeiden.

### Datenübertragung mit UDP

UDP ermöglicht eine einfache und schnelle Datenübertragung ohne die Mechanismen zur Gewährleistung der Zuverlässigkeit, die TCP bietet. Die Datenübertragung mit UDP erfolgt wie folgt:

- **Pakete**  
  UDP-Daten werden in Einheiten namens **Pakete** übertragen. Jedes UDP-Paket besteht aus einem Header und den Nutzdaten.

- **Keine Verbindung**  
  Es wird keine Verbindung zwischen Sender und Empfänger aufgebaut, was die Übertragung beschleunigt.

- **Keine Garantie für Zustellung und Reihenfolge**  
  UDP bietet keine Garantien für die Zustellung oder Reihenfolge der Pakete, wodurch Pakete verloren gehen oder in falscher Reihenfolge ankommen können.

- **Multicast und Broadcast**  
  UDP unterstützt die Übertragung an mehrere Empfänger gleichzeitig, was besonders in Fahrzeugnetzwerken nützlich ist, um Informationen effizient zu verteilen.


## Verbindungsabbau

### Verbindungsabbau mit TCP

Der Verbindungsabbau in TCP erfolgt ebenfalls in mehreren Schritten, um eine ordnungsgemäße Beendigung der Verbindung zu gewährleisten:

1. **FIN**  
   Ein Teilnehmer, der die Verbindung beenden möchte, sendet ein TCP-Segment mit gesetztem FIN-Flag (Finish) an den anderen Teilnehmer.

2. **ACK**  
   Der Empfänger dieses FIN-Segments bestätigt den Empfang durch Senden eines TCP-Segments mit gesetztem ACK-Flag.

3. **FIN**  
   Der Empfänger kann dann ebenfalls die Verbindung beenden, indem er ein eigenes TCP-Segment mit gesetztem FIN-Flag sendet.

4. **ACK**  
   Der ursprüngliche Sender bestätigt den Empfang dieses FIN-Segments mit einem letzten TCP-Segment mit gesetztem ACK-Flag.

Nach Abschluss dieses Prozesses ist die Verbindung vollständig geschlossen, und es können keine weiteren Daten mehr übertragen werden.

### Verbindungsabbau mit UDP

Da UDP ein verbindungsloses Protokoll ist, gibt es keinen formalen Verbindungsabbauprozess. Die Kommunikation kann jederzeit ohne vorherige Ankündigung beendet werden.

## Technische Implementierung von TCP und UDP über Ethernet

### TCP über Ethernet

TCP wird in Fahrzeugnetzwerken häufig über Ethernet implementiert, um die zuverlässige Übertragung großer Datenmengen sicherzustellen. Die Implementierung umfasst folgende Aspekte:

- **Kapselung**  
  TCP-Segmente werden innerhalb von IP-Paketen gekapselt und über das physische Ethernet-Netzwerk übertragen. Das Ethernet-Frame enthält die notwendigen Adressinformationen zur Zustellung der Daten an den richtigen Knoten.

- **Fehlerkorrektur**  
  TCP verwendet Sequenznummern und Acknowledgements, um sicherzustellen, dass alle Daten korrekt und vollständig übertragen werden. Bei Verlusten werden fehlende Segmente automatisch erneut gesendet.

- **Fluss- und Staukontrolle**  
  Durch das Window-Feld und adaptive Algorithmen passt TCP die Datenübertragungsrate dynamisch an die aktuellen Netzwerkbedingungen an, um Überlastungen zu vermeiden und eine effiziente Nutzung der Bandbreite zu gewährleisten.

### UDP über Ethernet

UDP wird über Ethernet eingesetzt, um eine schnelle und effiziente Übertragung von Datenpaketen zu ermöglichen, bei denen eine gewisse Fehlertoleranz akzeptabel ist. Die Implementierung umfasst folgende Aspekte:

- **Kapselung**  
  UDP-Pakete werden ebenfalls innerhalb von IP-Paketen gekapselt und über das Ethernet-Netzwerk übertragen. Das Ethernet-Frame sorgt für die korrekte Zustellung der Daten an den Zielknoten.

- **Effizienz**  
  Da UDP keine Verbindungsaufbau- oder Fehlerkorrekturmechanismen implementiert, ist der Overhead minimal. Dies ermöglicht eine höhere Übertragungsgeschwindigkeit und geringere Latenzzeiten.

- **Multicast- und Broadcast-Fähigkeiten**  
  UDP unterstützt die gleichzeitige Übertragung von Daten an mehrere Empfänger, was die Effizienz in Netzwerken mit hoher Anzahl an Empfängern erhöht.

## Zusammenfassung

TCP und UDP sind fundamentale Transportprotokolle in Fahrzeugnetzwerken, die jeweils spezifische Vorteile bieten. TCP gewährleistet eine zuverlässige und geordnete Datenübertragung durch verbindungsorientierte Mechanismen, während UDP eine schnelle und effiziente Übertragung ohne Garantie für Zustellung oder Reihenfolge ermöglicht. Die Wahl des geeigneten Protokolls hängt von den spezifischen Anforderungen der Anwendung ab. Ethernet als zugrunde liegende Netzwerktechnologie bietet die notwendige Bandbreite und Flexibilität, um beide Protokolle effektiv zu unterstützen. Durch die gezielte Implementierung von TCP und UDP können Fahrzeugnetzwerke den unterschiedlichen Anforderungen moderner Fahrzeuganwendungen gerecht werden.