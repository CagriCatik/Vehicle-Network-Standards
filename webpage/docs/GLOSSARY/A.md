
# A

- **API (Application Programming Interface)**: A set of rules and specifications that software programs can follow to communicate with each other.

- **ACK** steht für "Acknowledgement" und wird verwendet, um den Empfang von Daten in einer Kommunikationsverbindung zu bestätigen. Es ist ein Signal, das von einem Empfänger an einen Sender gesendet wird, um anzuzeigen, dass die empfangenen Daten korrekt übertragen wurden.

- **Activation Line**: Die Aktivierungslinie bei der Diagnose über das Internetprotokoll (DoIP) bezeichnet den spezifischen Kommunikationskanal, der zwischen einem Diagnosegerät und einem Fahrzeug eingerichtet wird, um die Übertragung von Diagnosedaten sowie die Aktivierung von Diagnosefunktionen zu ermöglichen, wobei sie eine virtuelle Verbindung darstellt, die es dem Diagnosegerät ermöglicht, Befehle an das Fahrzeug zu senden und relevante Daten für Diagnosezwecke zu empfangen.
 

**ACK** steht für "Acknowledgement" und wird verwendet, um den Empfang von Daten in einer Kommunikationsverbindung zu bestätigen. Es ist ein Signal, das von einem Empfänger an einen Sender gesendet wird, um anzuzeigen, dass die empfangenen Daten korrekt übertragen wurden.


- **Authentifizierung** Authentifizierung ist ein Dienst, der sich auf die Identifikation bezieht. Diese Funktion gilt sowohl für Entitäten als auch für die Informationen selbst. Zwei Parteien, die in eine Kommunikation eintreten, sollten sich gegenseitig identifizieren. Informationen, die über einen Kanal übermittelt werden, sollten hinsichtlich Herkunft, Datum der Herkunft, Dateninhalt, Zeitpunkt der Übermittlung usw. authentifiziert werden. Aus diesen Gründen wird dieser Aspekt der Kryptographie in der Regel in zwei Hauptklassen unterteilt: Entitätsauthentifizierung und Datenherkunftsauthentifizierung. Die Datenherkunftsauthentifizierung bietet implizit Datenintegrität (denn wenn eine Nachricht geändert wird, hat sich die Quelle geändert). 

- **Service ID**: A unique identifier for each diagnostic service within the UDS protocol.
- **Sub-function**: An optional parameter that modifies the behavior of a diagnostic service.
- **NRC (Negative Response Code)**: Codes indicating errors or issues in processing diagnostic service requests.



- **Service ID**: A unique identifier for each diagnostic service within the UDS protocol.
- **Sub-function**: An optional parameter that modifies the behavior of a diagnostic service.
- **NRC (Negative Response Code)**: Codes indicating errors or issues in processing diagnostic service requests.
- **CAN (Controller Area Network)**: A robust vehicle bus standard designed to allow microcontrollers and devices to communicate without a host computer.
- **LIN (Local Interconnect Network)**: A serial network protocol used for communication between components in vehicles.
- **Ethernet**: A family of networking technologies commonly used in local area networks (LAN), including automotive Ethernet for high-speed communication within vehicles.
- **Security Access (0x27)**: A UDS service that provides authentication mechanisms to access secured diagnostic services.
- **Diagnostic Session Control (0x10)**: A UDS service that initiates or terminates diagnostic sessions, determining the access level and available services.


### CAN

**CAN** steht für "Controller Area Network" und ist ein serielles Bussystem, das in der Regel in Fahrzeugen und industriellen Anwendungen zur Kommunikation zwischen verschiedenen Steuergeräten verwendet wird. CAN ermöglicht eine robuste und zuverlässige Datenübertragung über kurze bis mittlere Entfernungen.

### CAN-FD

**CAN-FD** steht für "Controller Area Network - Flexible Data-Rate" und ist eine Erweiterung des klassischen CAN-Protokolls. CAN-FD bietet höhere Datenübertragungsraten und größere Nutzlasten im Vergleich zum herkömmlichen CAN.

### CRC

**CRC** steht für "Cyclic Redundancy Check" und ist ein Verfahren zur Fehlererkennung in Datenübertragungen.

### DLC

**DLC** steht für "Data Length Code" und bezieht sich auf das Feld in einem CAN-Nachrichtenframe, das die Anzahl der Datenbytes in der Nachricht angibt.

## E

### EOF

**EOF** steht für "End of Frame" und markiert das Ende einer Nachricht in einem seriellem Datenübertragungsprotokoll wie CAN.

## I

### IDE

**IDE** steht für "Identifier Extension" und bezieht sich auf ein Bit im CAN-Nachrichtenrahmen, das angibt, ob der CAN-Identifier aus 11 oder 29 Bit besteht.

### ITM

**ITM** steht für

## M

### Multi-Master

Das Multi-Master-Prinzip in der Buskommunikation ermöglicht es mehreren Geräten, gleichzeitig die Rolle des Masters zu übernehmen, wodurch eine gleichzeitige Datenübertragung und eine flexible Kommunikation ermöglicht werden.

### Master-Slave

Das Master-Slave-Prinzip in der Buskommunikation bezeichnet eine Architektur, in der ein Hauptgerät (Master) die Kontrolle über den Kommunikationsbus hat und Daten an andere Geräte (Slaves) sendet. Die Slaves können nur auf Anforderung des Masters antworten.

## R

### RTR

**RTR** steht für "Remote Transmission Request" und wird in CAN verwendet, um anzuzeigen, dass der Sender eine Remote-Anforderung für Datenübertragung an den Empfänger sendet.

## S

### SOF

**SOF** steht für "Start of Frame" und markiert den Beginn einer Nachricht in einem seriellem Datenübertragungsprotokoll wie CAN.

### Authentische I-PDU

Eine authentische I-PDU ist eine willkürliche AUTOSAR-I-PDU, deren Inhalt während der Netzwerkübertragung durch die Secured I-PDU gesichert ist. Der gesicherte Inhalt umfasst die vollständige I-PDU oder einen Teil der I-PDU.

### Authentifizierungsinformationen

Die Authentifizierungsinformationen bestehen aus einem Frische-Wert (oder einem Teil davon) und einem Authentifikator (oder einem Teil davon). Authentifizierungsinformationen sind die zusätzlichen Informationen, die von SecOC hinzugefügt werden, um die Secured I-PDU zu realisieren.

### Authentifikator

Ein Authentifikator ist Daten, die zur Bereitstellung der Nachrichtenauthentifizierung verwendet werden. Im Allgemeinen wird der Begriff "Message Authentication Code" (MAC) für symmetrische Ansätze verwendet, während der Begriff "Signatur" oder "Digitale Signatur" für asymmetrische Ansätze verwendet wird, die unterschiedliche Eigenschaften und Einschränkungen haben.


### 

### Datenherkunftsauthentifizierung

Die Datenherkunftsauthentifizierung ist eine Art der Authentifizierung, bei der eine Partei als (ursprüngliche) Quelle bestimmter Daten bestätigt wird, die zu einem (typischerweise unbestimmten) Zeitpunkt in der Vergangenheit erstellt wurden. Datenherkunftsauthentifizierung umfasst per Definition Datenintegrität.

### Unterscheidung unilaterale / bilaterale Authentifizierung

Bei unilateraler Authentifizierung weist eine Seite die Identität nach. Die anfordernde Seite wird nicht einmal in dem Maße authentifiziert, dass nachgewiesen wird, dass sie berechtigt ist, eine Authentifizierung anzufordern. Bei bilateraler Authentifizierung wird der Anforderer ebenfalls mindestens (siehe unten) authentifiziert, um das Privileg des Anforderns nachzuweisen. Es gibt einen effizienteren und sichereren Weg, um beide Endpunkte zu authentifizieren, basierend auf der oben beschriebenen bilateralen Authentifizierung. Zusammen mit der Authentifizierung (in der zweiten Nachricht), die ursprünglich vom Empfänger angefordert wird (in der ersten Nachricht), fordert der Sender auch eine Authentifizierung an. Der Empfänger sendet eine dritte Nachricht, die die vom Sender angeforderte Authentifizierung bereitstellt. Dies sind nur drei Nachrichten (im Gegensatz zu vier mit zwei unilateralen Nachrichten).

## E

### Entitätsauthentifizierung

Entitätsauthentifizierung ist der Prozess, bei dem eine Partei durch den Erwerb von überzeugenden Beweisen von der Identität einer zweiten Partei, die an einem Protokoll beteiligt ist, versichert wird, und dass die zweite tatsächlich teilgenommen hat (d. h. aktiv ist oder unmittelbar vor der Zeit, zu der die Beweise erworben werden).

Hinweis: Die Entitätsauthentifizierung bedeutet, die Präsenz und operative Bereitschaft eines Kommunikationsendpunkts nachzuweisen. Dies geschieht zum Beispiel oft durch den Nachweis des Zugriffs auf einen kryptografischen Schlüssel und das Wissen über ein Geheimnis. Es ist notwendig, dies zu tun, ohne entweder Schlüssel oder Geheimnis preiszugeben. Die Entitätsauthentifizierung kann verwendet werden, um Aufzeichnungs- und Wiederholungsangriffe zu verhindern. Die Frische von Nachrichten kompliziert sie nur durch die Notwendigkeit, eine Lebensdauer aufzuzeichnen und entweder Sender oder Empfänger (Echtzeit-) Uhr zu korrigieren. Die Entitätsauthentifizierung wird vom Empfänger ausgelöst, d.h. demjenigen, der überzeugt werden soll, während der Sender reagieren muss, indem er überzeugt. Aufzeichnungs- und Wiederholungsangriffe auf Entitätsauthentifizierung werden normalerweise verhindert, indem dem Empfänger eine gewisse Kontrolle über den Authentifizierungsprozess ermöglicht wird. Um zu verhindern, dass der Empfänger diese Kontrolle dazu verwendet, den Sender zu böswilligen Zwecken zu lenken oder einen Schlüssel oder ein Geheimnis zu bestimmen ("Oracle-Angriff"), kann der Sender mehr Zufälligkeit hinzufügen. Wenn nicht nur der Zugriff auf einen Schlüssel (was die Mitgliedschaft in einer privilegierten Gruppe impliziert), sondern auch Individualität nachgewiesen werden soll, fügt der Sender zusätzlich seine eindeutige Identifizierung hinzu und authentifiziert sie.

## M

### Message Authentification

Nachrichtenauthentifizierung (Message Authentification) ist ein Begriff, der analog zur Datenherkunftsauthentifizierung verwendet wird. Sie bietet Datenherkunftsauthentifizierung hinsichtlich der ursprünglichen Nachrichtenquelle (und Datenintegrität, aber keine Garantien für Einzigartigkeit und Aktualität).

### SecuredI-P

Eine gesicherte I-PDU ist eine AUTOSAR-I-PDU, die Payload einer authentischen I-PDU enthält, ergänzt durch zusätzliche Authentifizierungsinformationen.

## T

### Transaktionsauthentifizierung

Transaktionsauthentifizierung bezeichnet die Nachrichtenauthentifizierung, die ergänzt wird, um zusätzlich Einzigartigkeits- und Aktualitätsgarantien für Daten bereitzustellen (um somit nicht erkennbare Nachrichtenwiederholungen zu verhindern).


# Glossar

## A

## B

### Bus Guardian

Bus Guardian ist eine Funktion im FlexRay-Kommunikationssystem, die aktiv die Integrität und Zuverlässigkeit der Datenkommunikation auf dem FlexRay-Bus überwacht, um potenzielle Fehler oder Anomalien zu erkennen und durch entsprechende Maßnahmen wie Blockieren fehlerhafter Nachrichten oder Auslösen von Warnungen die Sicherheit und Funktionsfähigkeit sicherzustellen.

## C

## D

## E

### 

