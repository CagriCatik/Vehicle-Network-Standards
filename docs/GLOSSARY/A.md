
# A

- **API (Application Programming Interface)**: A set of rules and specifications that software programs can follow to communicate with each other.
 
- **UDS (Unified Diagnostic Services)**: A protocol used for diagnostics and communication between diagnostic testers and vehicle ECUs.
- **Service ID**: A unique identifier for each diagnostic service within the UDS protocol.
- **Sub-function**: An optional parameter that modifies the behavior of a diagnostic service.
- **NRC (Negative Response Code)**: Codes indicating errors or issues in processing diagnostic service requests.

- **ECU (Electronic Control Unit)**: Embedded systems in automotive electronics that control one or more electrical systems or subsystems.
- **UDS (Unified Diagnostic Services)**: A protocol used for diagnostics and communication between diagnostic testers and vehicle ECUs.
- **Service ID**: A unique identifier for each diagnostic service within the UDS protocol.
- **Sub-function**: An optional parameter that modifies the behavior of a diagnostic service.
- **NRC (Negative Response Code)**: Codes indicating errors or issues in processing diagnostic service requests.
- **CAN (Controller Area Network)**: A robust vehicle bus standard designed to allow microcontrollers and devices to communicate without a host computer.
- **LIN (Local Interconnect Network)**: A serial network protocol used for communication between components in vehicles.
- **Ethernet**: A family of networking technologies commonly used in local area networks (LAN), including automotive Ethernet for high-speed communication within vehicles.
- **Security Access (0x27)**: A UDS service that provides authentication mechanisms to access secured diagnostic services.
- **Diagnostic Session Control (0x10)**: A UDS service that initiates or terminates diagnostic sessions, determining the access level and available services.

- **Activation Line**: Die Aktivierungslinie bei der Diagnose über das Internetprotokoll (DoIP) bezeichnet den spezifischen Kommunikationskanal, der zwischen einem Diagnosegerät und einem Fahrzeug eingerichtet wird, um die Übertragung von Diagnosedaten sowie die Aktivierung von Diagnosefunktionen zu ermöglichen, wobei sie eine virtuelle Verbindung darstellt, die es dem Diagnosegerät ermöglicht, Befehle an das Fahrzeug zu senden und relevante Daten für Diagnosezwecke zu empfangen.

# Glossar

## A

### ACK

**ACK** steht für "Acknowledgement" und wird verwendet, um den Empfang von Daten in einer Kommunikationsverbindung zu bestätigen. Es ist ein Signal, das von einem Empfänger an einen Sender gesendet wird, um anzuzeigen, dass die empfangenen Daten korrekt übertragen wurden.

## B

### Bitstuffing

**Bitstuffing** ist eine Methode zur Fehlererkennung und -korrektur in der Datenübertragung. Dabei werden spezielle Bits in die Daten eingefügt, um sicherzustellen, dass das empfangene Signal korrekt interpretiert wird. Dies geschieht durch das Einfügen zusätzlicher Bits, wenn eine bestimmte Bitfolge im Datenstrom auftritt, um zu verhindern, dass diese Bitfolge fälschlicherweise als Steuerzeichen interpretiert wird.

### Botschaftszähler

Ein Botschaftszähler (engl. Message Counter) ist ein wichtiges Konzept bei der Buskommunikation, wie beispielsweise beim CAN-Bus (Controller Area Network). Der Botschaftszähler dient dazu, doppelte oder verlorene Nachrichten zu erkennen und somit die Datenkonsistenz zu gewährleisten. Jede Nachricht, die über den Bus gesendet wird, erhält eine fortlaufende Nummer (den Botschaftszähler). Der Empfänger kann anhand dieser Nummer erkennen, ob eine Nachricht doppelt empfangen wurde (gleiche Nummer wie zuvor) oder ob eine Nachricht verloren ging (es fehlt eine Nummer in der Reihenfolge). Durch den Botschaftszähler können Fehler erkannt und behoben werden, indem z.B. verlorene Nachrichten erneut angefordert werden. Dies erhöht die Integrität und Zuverlässigkeit der Datenkommunikation über den Bus erheblich. Der Botschaftszähler ist besonders wichtig in sicherheitskritischen Systemen, wo eine korrekte Datenübertragung zwischen den verschiedenen Steuergeräten essentiell ist.

## C

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


# Glossar

## A

### Authentische I-PDU

Eine authentische I-PDU ist eine willkürliche AUTOSAR-I-PDU, deren Inhalt während der Netzwerkübertragung durch die Secured I-PDU gesichert ist. Der gesicherte Inhalt umfasst die vollständige I-PDU oder einen Teil der I-PDU.

### Authentifizierung

Authentifizierung ist ein Dienst, der sich auf die Identifikation bezieht. Diese Funktion gilt sowohl für Entitäten als auch für die Informationen selbst. Zwei Parteien, die in eine Kommunikation eintreten, sollten sich gegenseitig identifizieren. Informationen, die über einen Kanal übermittelt werden, sollten hinsichtlich Herkunft, Datum der Herkunft, Dateninhalt, Zeitpunkt der Übermittlung usw. authentifiziert werden. Aus diesen Gründen wird dieser Aspekt der Kryptographie in der Regel in zwei Hauptklassen unterteilt: Entitätsauthentifizierung und Datenherkunftsauthentifizierung. Die Datenherkunftsauthentifizierung bietet implizit Datenintegrität (denn wenn eine Nachricht geändert wird, hat sich die Quelle geändert).

### Authentifizierungsinformationen

Die Authentifizierungsinformationen bestehen aus einem Frische-Wert (oder einem Teil davon) und einem Authentifikator (oder einem Teil davon). Authentifizierungsinformationen sind die zusätzlichen Informationen, die von SecOC hinzugefügt werden, um die Secured I-PDU zu realisieren.

### Authentifikator

Ein Authentifikator ist Daten, die zur Bereitstellung der Nachrichtenauthentifizierung verwendet werden. Im Allgemeinen wird der Begriff "Message Authentication Code" (MAC) für symmetrische Ansätze verwendet, während der Begriff "Signatur" oder "Digitale Signatur" für asymmetrische Ansätze verwendet wird, die unterschiedliche Eigenschaften und Einschränkungen haben.

## D

### Datenintegrität

Datenintegrität ist die Eigenschaft, dass Daten seit dem Zeitpunkt ihrer Erstellung, Übertragung oder Speicherung durch eine autorisierte Quelle nicht unbefugt verändert wurden. Um die Datenintegrität zu gewährleisten, sollte man die Fähigkeit haben, Manipulationen von Daten durch unbefugte Parteien zu erkennen. Datenmanipulation umfasst das Einfügen, Löschen und Ersetzen von Daten.

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

### ECU-Extract

Das "ECU Extract" ist eine Konfiguration der einzelnen Steuergeräte, die aus der formalen Beschreibung der Softwarefunktionen und Hardwarevoraussetzungen generiert wird und als Basis für die Erstellung der Steuergeräte-Konfigurationen dient, bevor Generatoren lauffähigen Code erzeugen.

## F

### Fault Tolerant Midpoint (FTM)

Der Fault Tolerant Midpoint (FTM) ist ein Algorithmus, der in FlexRay-Netzwerken verwendet wird, um die Synchronisation der lokalen Uhren der einzelnen Knoten innerhalb des Clusters sicherzustellen. Der Zweck des FTM-Algorithmus besteht darin, den Offsetkorrekturwert für die Uhren jedes Knotens zu berechnen, um sicherzustellen, dass alle Knoten den Kommunikationszyklus zum gleichen Zeitpunkt beginnen.

Hier ist eine kurze Erläuterung, wie der FTM-Algorithmus funktioniert:

1. **Sammeln von Zeitdifferenzen**: Jeder FlexRay-Knoten vergleicht die erwarteten Zeitpunkte für den Empfang der Sync-Botschaften mit den tatsächlichen Zeitpunkten, zu denen die Sync-Botschaften eintreffen. Anhand dieser Vergleiche berechnet jeder Knoten eine Liste von Zeitdifferenzen.
2. **Entfernen von Extremwerten**: Der FTM-Algorithmus eliminiert die Extremwerte aus der Liste der Zeitdifferenzen, um zu verhindern, dass stark abweichende lokale Uhren die Berechnung des Offsetkorrekturwerts beeinflussen.
3. **Berechnung des Mittelwerts**: Nachdem die Extremwerte entfernt wurden, werden die verbleibenden Zeitdifferenzen addiert und gemittelt, um den Offsetkorrekturwert zu erhalten.
4. **Anpassung der lokalen Uhr**: Basierend auf dem berechneten Offsetkorrekturwert passen die FlexRay-Knoten ihre lokalen Uhren entsprechend an, um sicherzustellen, dass alle Uhren synchronisiert sind und jeder Knoten den Kommunikationszyklus zum gleichen Zeitpunkt beginnt.

Der FTM-Algorithmus ist ein zentraler Bestandteil der Synchronisationsstrategie in FlexRay-Netzwerken und trägt dazu bei, eine präzise und zuverlässige Datenkommunikation zwischen den Knoten zu gewährleisten.

## I

## M

## R

## S


# Glossar

## A

### ACK

**ACK** steht für "Acknowledgement" und wird verwendet, um den Empfang von Daten in einer Kommunikationsverbindung zu bestätigen. Es ist ein Signal, das von einem Empfänger an einen Sender gesendet wird, um anzuzeigen, dass die empfangenen Daten korrekt übertragen wurden.

## B

### Bitstuffing

**Bitstuffing** ist eine Methode zur Fehlererkennung und -korrektur in der Datenübertragung. Dabei werden spezielle Bits in die Daten eingefügt, um sicherzustellen, dass das empfangene Signal korrekt interpretiert wird. Dies geschieht durch das Einfügen zusätzlicher Bits, wenn eine bestimmte Bitfolge im Datenstrom auftritt, um zu verhindern, dass diese Bitfolge fälschlicherweise als Steuerzeichen interpretiert wird.

### BRS

Bit Rate Switch

### Botschaftszähler

Ein Botschaftszähler (engl. Message Counter) ist ein wichtiges Konzept bei der Buskommunikation, wie beispielsweise beim CAN-Bus (Controller Area Network). Der Botschaftszähler dient dazu, doppelte oder verlorene Nachrichten zu erkennen und somit die Datenkonsistenz zu gewährleisten. Jede Nachricht, die über den Bus gesendet wird, erhält eine fortlaufende Nummer (den Botschaftszähler). Der Empfänger kann anhand dieser Nummer erkennen, ob eine Nachricht doppelt empfangen wurde (gleiche Nummer wie zuvor) oder ob eine Nachricht verloren ging (es fehlt eine Nummer in der Reihenfolge). Durch den Botschaftszähler können Fehler erkannt und behoben werden, indem z.B. verlorene Nachrichten erneut angefordert werden. Dies erhöht die Integrität und Zuverlässigkeit der Datenkommunikation über den Bus erheblich. Der Botschaftszähler ist besonders wichtig in sicherheitskritischen Systemen, wo eine korrekte Datenübertragung zwischen den verschiedenen Steuergeräten essentiell ist.

## C

### CAN

**CAN** steht für "Controller Area Network" und ist ein serielles Bussystem, das in der Regel in Fahrzeugen und industriellen Anwendungen zur Kommunikation zwischen verschiedenen Steuergeräten verwendet wird. CAN ermöglicht eine robuste und zuverlässige Datenübertragung über kurze bis mittlere Entfernungen.

### CAN-FD

**CAN-FD** steht für "Controller Area Network - Flexible Data-Rate" und ist eine Erweiterung des klassischen CAN-Protokolls. CAN-FD bietet höhere Datenübertragungsraten und größere Nutzlasten im Vergleich zum herkömmlichen CAN.





### EOF

**EOF** steht für "End of Frame" und markiert das Ende einer Nachricht in einem seriellem Datenübertragungsprotokoll wie CAN.

## I

### IDE

**IDE** steht für "Identifier Extension" und bezieht sich auf ein Bit im CAN-Nachrichtenrahmen, das angibt, ob der CAN-Identifier aus 11 oder 29 Bit besteht.

### ITM

**ITM** steht für















