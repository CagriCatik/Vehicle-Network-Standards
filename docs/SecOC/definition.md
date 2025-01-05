# Secure Onboard Communication

## Definition von SecOC

SecOC sichert und authentifiziert die Kommunikation zwischen Steuergeräten auf Basis von Message Authentication Codes (MACs). Nur auf Basis von gültigen MACs können Simulations- und Testwerkzeuge mit den Steuergeräten kommunizieren. Für die Vector Werkzeuge übernimmt der Security Manager zusammen mit den OEM Security Add-Ons* das Erzeugen und Validieren der MACs. Die notwendigen Eingangswerte wie z.B. geheime Schlüssel (Secret key) und Freshness Values werden im Security Manager gespeichert.

## Notwendigkeit von SecOC

Security ist ein wichtiger Wegbereiter für die sichere Vernetzung von Fahrzeugen. Zunehmend etablieren sich beispielsweise signierte Software-Updates, sichere OnBoard-Kommunikation und Secure Boot. Aktuell rücken ­Intrusion-Detection-Systeme (IDS) als ein weiterer Security-Mechanismus in den Fokus der Aufmerksamkeit. Obwohl IDS ein lang bekannter Security-Mechanismus klassischer IT-Systeme ist, sind sie im Automobil noch nicht fest etabliert. 

Ein Grund dafür ist deren mangelnde technische Standardisierung. Es gibt keinerlei Standards für die Spezifikation von Security-Events (SEvs), deren Verarbeitung und Reporting im Fahrzeug, ihre effiziente Speicherung und auch keine definierte Onboard-Infrastruktur für das Realisieren von IDS. Außerdem lassen sich die Entwicklungsprozesse von IDS-Anbietern häufig nur schwer in existierende Systementwicklungsprozesse bei Fahrzeugherstellern und -zulieferern integrieren. Es sind zum Teil Eingriffe in die Steuergerätesoftware notwendig, die bereits abgeschlossene Safety-Prozesse torpedieren oder nicht zu der heutigen Aufgabenteilung zwischen Fahrzeughersteller und -zulieferer passen. Einige IDS-Ansätze verlangen den Einsatz proprietärer Hardwarekomponenten, die die Kosten für IDS explodieren lassen.

Gleichzeitig entsteht aktuell der Standard ISO 21434 (Road vehicles – Cybersecurity Engineering). Dieser fordert unter anderem einen definierten Incident-Response-Prozess (Bild 1). Darin ist festgelegt, dass ein Fahrzeughersteller auf Security-Schwachstellen (Vulnerabilities) reagieren muss, die in seinen Fahrzeugen aufgetreten sind. Das kann er aber nur, wenn er diese Schwachstellen auch kennt. Dazu können Automotive-IDS beitragen. Diese bestehen aus einem Onboard-IDS in den Fahrzeugen und einem Backend.




Title: Comprehensive Tutorial on AUTOSAR SecOC Module - Part 1: Introduction to Secure On-board Communication

**Introduction:**
In this tutorial, we'll delve into the intricacies of the AUTOSAR SecOC (Secure On-board Communication) module, specifically focusing on its importance in automotive embedded systems. SecOC plays a crucial role in securing in-vehicle communication, ensuring data integrity and authenticity in an environment where automotive ECUs (Electronic Control Units) exchange information. This tutorial will provide a detailed understanding of SecOC, its architecture, implementation, and working principles.

**1. Understanding AUTOSAR Architecture:**
Before diving into SecOC, it's essential to grasp the fundamentals of AUTOSAR (AUTomotive Open System ARchitecture). AUTOSAR is a standardized automotive software architecture developed collaboratively by automotive manufacturers, suppliers, and software industries. It aims to establish a common platform for automotive software development, promoting interoperability and scalability across the industry.

**2. Introduction to SecOC Module:**
SecOC, short for Secure On-board Communication, addresses the security challenges associated with in-vehicle communication. Traditionally, automotive companies transmitted data between ECUs via protocols like CAN bus without adequate security measures. This left the communication vulnerable to unauthorized access and tampering. SecOC module, integrated into the AUTOSAR architecture, enhances the security of in-vehicle communication by adding encryption, authentication, and integrity-checking mechanisms.

**3. Architecture of SecOC Module:**
The architecture of the SecOC module follows a layered approach within the AUTOSAR framework. At its core, SecOC interacts with other AUTOSAR modules such as PDU Router (PDR), Crypto Service Manager (CSM), and Crypto Modules. These modules collaborate to ensure secure communication between ECUs. SecOC can be integrated into various automotive communication networks, including CAN and Ethernet.

**4. Working Principles of SecOC:**
a. **Message Transmission:** When an ECU sends a message, it passes through the communication stack, including the PDR. The PDR routes the plain message (Authentic IPDU) to the SecOC module.
b. **Security Processing:** SecOC performs security operations such as Message Authentication Code (MAC) generation using cryptographic algorithms and keys obtained from the CSM.
c. **Secure Transmission:** SecOC appends security information (e.g., MAC, freshness value) to the message, creating a Secured IPDU. This secured message is then routed back to the PDR.
d. **Message Reception:** At the receiving ECU, the SecOC module verifies the received message's authenticity by recalculating the MAC and comparing it with the received MAC. If the MACs match, the message is considered authentic and forwarded to upper layers.

**5. Handling Data Limitations and Secure PDU Collection:**
In protocols like CAN, which have limited data frame sizes, appending security information may reduce available data space. SecOC addresses this issue through Secure PDU Collection, allowing data and security content to be sent separately. However, both messages are required for verification at the receiver's end. In contrast, protocols like Ethernet offer more flexibility in data length, enabling the transmission of all information in a single message.

**6. Implementation Details and Considerations:**
SecOC implementation involves configuring cryptographic algorithms, keys, and security parameters based on system requirements. It's crucial to select appropriate encryption algorithms and key management strategies to ensure robust security without compromising performance.

**Conclusion:**
In conclusion, the AUTOSAR SecOC module plays a vital role in securing in-vehicle communication in automotive embedded systems. By implementing encryption, authentication, and integrity checks, SecOC mitigates the risks associated with unauthorized access and tampering of data. Understanding the architecture and working principles of SecOC is essential for developing robust and secure automotive software solutions.

This tutorial provides a comprehensive overview of the AUTOSAR SecOC module, laying the foundation for further exploration and implementation in automotive embedded systems.


## Sequenzdiagramm

In diesem Tutorial werden wir das Secure On-board Communication (SecOC) Modul der AUTOSAR-Architektur genauer betrachten. Dieses Modul spielt eine entscheidende Rolle bei der Sicherheit, Integrität und Authentizität der zwischen den elektronischen Steuergeräten (ECUs) in Automobilsystemen ausgetauschten Daten. Wir werden die Grundlagen der AUTOSAR-Architektur, die Notwendigkeit von SecOC, seine Arbeitsprinzipien und praktische Implementierungsbeispiele behandeln.

1. Verständnis der AUTOSAR-Architektur:
   AUTOSAR (AUTomotive Open System ARchitecture) ist eine standardisierte Softwarearchitektur, die gemeinsam von Automobilherstellern, Zulieferern und Softwareindustrien entwickelt wurde. Ihr Hauptziel ist es, eine gemeinsame Plattform für die Entwicklung von Automobilsoftware zu schaffen, um die Interoperabilität, Skalierbarkeit und Wiederverwendbarkeit in der Branche zu verbessern.
2. Einführung in das SecOC-Modul:
   SecOC, kurz für Secure On-board Communication, ist eine wichtige Komponente innerhalb der AUTOSAR-Architektur. Traditionell kommunizieren Automobil-ECUs über Protokolle wie den CAN-Bus ohne ausreichende Sicherheitsmaßnahmen, was sie anfällig für Datenmanipulation und unbefugten Zugriff macht. SecOC behebt diese Schwachstelle, indem es Sicherheitsfunktionen für die Fahrzeugkommunikation hinzufügt.
3. Hauptmerkmale von SecOC:

   - Integration in verschiedene Automobilkommunikationsnetzwerke wie CAN und Ethernet.
   - Gewährleistung der Integrität und Authentizität ausgehender Nachrichten.
   - Schutz vor Datenmanipulation und unbefugtem Zugriff.
   - Verwendung kryptografischer Algorithmen und Schlüssel zur Sicherung der Kommunikation.
4. SecOC-Architektur:
   Das SecOC-Modul arbeitet innerhalb der AUTOSAR-Architektur, typischerweise in die Kommunikationsstapel der ECUs integriert. Es empfängt Klarnachrichten vom Kommunikationsmodul (COM), verarbeitet sie, um Sicherheitsinformationen hinzuzufügen, und liefert gesicherte Nachrichten an die unteren Ebenen zur Übertragung.
5. Arbeitsprinzipien von SecOC:

   - Eingehende Nachrichten aus der Anwendungsschicht fließen über das Kommunikationsmodul (COM) zum Protocol Data Router (PDR).
   - PDR leitet Klarnachrichten (Authentic IPDU) an das SecOC-Modul weiter.
   - SecOC führt erforderliche kryptografische Operationen mit Unterstützung des Crypto Service Managers (CSM) und der Crypto-Module durch.
   - Gesicherte IPDUs, die Klartext, Frische und Authentifikator enthalten, werden generiert und an den PDR weitergeleitet.
   - PDR leitet die gesicherten IPDUs an untere Ebenen zur Übertragung über das Kommunikationsprotokoll (z. B. CAN oder Ethernet) weiter.
6. Sichere Datenübertragung:

   - Die sendende ECU (ECU1) generiert einen Message Authentication Code (MAC) mithilfe eines MAC-Generators und Eingaben wie Daten, Schlüssel und Frische.
   - Der MAC wird der ausgehenden gesicherten IPDU hinzugefügt und an die empfangende ECU (ECU2) übertragen.
   - Die empfangende ECU überprüft die empfangene Nachricht, indem sie den MAC erneut generiert und mit dem empfangenen MAC vergleicht.
   - Wenn die MACs übereinstimmen, gilt die Daten als nicht manipuliert und werden an obere Ebenen zur weiteren Verarbeitung weitergeleitet.
7. Umgang mit Datenrahmenbeschränkungen:

   - Das CAN-Protokoll hat eine begrenzte Datenrahmengröße (acht Bytes), was Herausforderungen für das Hinzufügen von Sicherheitsinformationen darstellt.
   - SecOC bietet eine Funktion namens Secured PDU Collection, um Daten und Sicherheitsinhalte getrennt zu senden.
   - Für die Ethernet-Kommunikation, die keine Datenlängenbeschränkungen hat, können alle Informationen in einer einzigen Nachricht gesendet werden.

Abschluss:
In diesem Tutorial haben wir die Grundlagen des AUTOSAR SecOC-Moduls, seine Bedeutung für die Sicherheit der Fahrzeugkommunikation und seine Arbeitsprinzipien untersucht. Das Verständnis von SecOC ist entscheidend für die Entwicklung robuster und sicherer Automobilsysteme. Bleiben Sie dran für weitere Tutorials zu eingebetteten Automobilsystemen.

[AUTOSAR SecOC Part-1 | Secure On-board Communication | AUTOSAR | AUTOMOTIVE Embedded - YouTube](https://www.youtube.com/watch?v=muz9yoSncqM)

[AUTOSAR SecOC Part-2 || Sequence Diagram || #automotive #embeddedsystems #autosar (youtube.com)](https://www.youtube.com/watch?v=LqW8zGnXtp0)

[4.-Bashar-Dawood.pdf (autosec.se)](https://autosec.se/wp-content/uploads/2019/03/4.-Bashar-Dawood.pdf)

[Wie ein standardisiertes Schlüsselmanagement Steuergeräte schützt (all-electronics.de)](https://www.all-electronics.de/automotive-transportation/wie-ein-standardisiertes-schluesselmanagement-steuergeraete-schuetzt.html)

[Authentische CAN-Kommunikation - Automotive - Elektroniknet](https://www.elektroniknet.de/automotive/authentische-can-kommunikation.151544.html)




**Title: Comprehensive Tutorial on AUTOSAR SecOC Part-2: Understanding Sequence Diagrams**

In this tutorial, we'll delve into the intricate world of AUTOSAR SecOC (Security-Oriented Communication) Part-2, focusing specifically on understanding sequence diagrams. Whether you're a seasoned automotive engineer or just starting out in the field of embedded systems, this tutorial aims to simplify the complexities of SecOC sequence diagrams.

**Introduction to AUTOSAR SecOC:**
Before we dive into sequence diagrams, let's briefly recap what AUTOSAR SecOC is all about. AUTOSAR (AUTomotive Open System ARchitecture) is a standardized automotive software architecture, and SecOC is a crucial aspect of it. SecOC ensures secure communication between various components within a vehicle's electronic systems, safeguarding against unauthorized access and tampering.

**Understanding the Transcript:**
The transcript provided gives us insights into the flow of data within an AUTOSAR SecOC system, particularly focusing on the transmit flow. Here's a breakdown of the key steps mentioned:

1. **Application Layer to RTE Layer:**

   - When a Real-Time (RT) write function is called from a software component, it reaches the RTE (Run-Time Environment) layer.
   - The RTE then calls the Comms and Signal function.
2. **Comms Layer:**

   - At the Comms layer, there are two types of communication for PDU (Protocol Data Unit) processing: default processing and immediate processing.
   - In default processing, raw data received at Comms is copied to a buffer and processed at the next Comms main function call.
   - In immediate processing, data is processed immediately with priority, bypassing the waiting for the next main function call.
3. **PDR Layer:**

   - After Comms, the PDR (Protocol Data Router) layer comes into play.
   - PDRCom transmit function is called, routing the PDU to SecOC.
4. **SecOC Layer:**

   - At the SecOC layer, similar to Comms, there are deferred and immediate processing cases.
   - In the transcript, the deferred processing case is discussed, where the PDU received is stored in a buffer and processed at the next SecOC main function call.
   - The process involves fetching the freshness value and authenticating the data using cryptographic functions.
5. **Cryptographic Module:**

   - The cryptographic module fetches the necessary keys and generates a Message Authentication Code (MAC) for authentication.
6. **Conclusion:**

   - After the authentication process, the control goes back to the PDR layer, and the usual transmit procedures ensue.

**Creating the Sequence Diagram:**
Based on the transcript, let's create a sequence diagram to visually represent the flow of messages within the AUTOSAR SecOC system.

1. **Application Layer:**

   - Start with the Application Layer, where the RT write function is called.
2. **RTE and Comms Layer:**

   - Show the flow of data from the RTE to the Comms layer, depicting both default and immediate processing cases.
3. **PDR and SecOC Layer:**

   - Illustrate the routing of the PDU from the PDR to the SecOC layer, focusing on the deferred processing case.
4. **Cryptographic Module:**

   - Represent the interaction between the SecOC layer and the cryptographic module, highlighting key fetching and MAC generation.
5. **Conclusion:**

   - Conclude the sequence diagram with the control returning to the PDR layer for further processing.

**Conclusion:**
Understanding sequence diagrams is crucial for comprehending the intricate flow of data within AUTOSAR SecOC systems. By breaking down the transcript and visualizing the sequence of message flows, we gain valuable insights into the inner workings of secure communication protocols in automotive embedded systems.

Remember, mastering AUTOSAR SecOC requires continuous learning and practice. Feel free to experiment with different scenarios and dive deeper into the intricacies of automotive security. Stay curious, and happy coding!
