
# A

## API 

(Application Programming Interface) A set of rules and specifications that software programs can follow to communicate with each other.


## ACK
ACK steht für "Acknowledgement" und wird verwendet, um den Empfang von Daten in einer Kommunikationsverbindung zu bestätigen. Es ist ein Signal, das von einem Empfänger an einen Sender gesendet wird, um anzuzeigen, dass die empfangenen Daten korrekt übertragen wurden.

## Authentifikator

Ein Authentifikator ist Daten, die zur Bereitstellung der Nachrichtenauthentifizierung verwendet werden. Im Allgemeinen wird der Begriff "Message Authentication Code" (MAC) für symmetrische Ansätze verwendet, während der Begriff "Signatur" oder "Digitale Signatur" für asymmetrische Ansätze verwendet wird, die unterschiedliche Eigenschaften und Einschränkungen haben.

## Activation Line

Die Aktivierungslinie bei der Diagnose über das Internetprotokoll (DoIP) bezeichnet den spezifischen Kommunikationskanal, der zwischen einem Diagnosegerät und einem Fahrzeug eingerichtet wird, um die Übertragung von Diagnosedaten sowie die Aktivierung von Diagnosefunktionen zu ermöglichen, wobei sie eine virtuelle Verbindung darstellt, die es dem Diagnosegerät ermöglicht, Befehle an das Fahrzeug zu senden und relevante Daten für Diagnosezwecke zu empfangen.
 
## Authentifizierung 

Authentifizierung ist ein Dienst, der sich auf die Identifikation bezieht. Diese Funktion gilt sowohl für Entitäten als auch für die Informationen selbst. Zwei Parteien, die in eine Kommunikation eintreten, sollten sich gegenseitig identifizieren. Informationen, die über einen Kanal übermittelt werden, sollten hinsichtlich Herkunft, Datum der Herkunft, Dateninhalt, Zeitpunkt der Übermittlung usw. authentifiziert werden. Aus diesen Gründen wird dieser Aspekt der Kryptographie in der Regel in zwei Hauptklassen unterteilt: Entitätsauthentifizierung und Datenherkunftsauthentifizierung. Die Datenherkunftsauthentifizierung bietet implizit Datenintegrität (denn wenn eine Nachricht geändert wird, hat sich die Quelle geändert). 

## Authentische I-PDU

Eine authentische I-PDU ist eine willkürliche AUTOSAR-I-PDU, deren Inhalt während der Netzwerkübertragung durch die Secured I-PDU gesichert ist. Der gesicherte Inhalt umfasst die vollständige I-PDU oder einen Teil der I-PDU.

## Authentifizierungsinformationen

Die Authentifizierungsinformationen bestehen aus einem Frische-Wert (oder einem Teil davon) und einem Authentifikator (oder einem Teil davon). Authentifizierungsinformationen sind die zusätzlichen Informationen, die von SecOC hinzugefügt werden, um die Secured I-PDU zu realisieren.

## Authentifizierung unilaterale / bilaterale 

Bei unilateraler Authentifizierung weist eine Seite die Identität nach. Die anfordernde Seite wird nicht einmal in dem Maße authentifiziert, dass nachgewiesen wird, dass sie berechtigt ist, eine Authentifizierung anzufordern. Bei bilateraler Authentifizierung wird der Anforderer ebenfalls mindestens (siehe unten) authentifiziert, um das Privileg des Anforderns nachzuweisen. Es gibt einen effizienteren und sichereren Weg, um beide Endpunkte zu authentifizieren, basierend auf der oben beschriebenen bilateralen Authentifizierung. Zusammen mit der Authentifizierung (in der zweiten Nachricht), die ursprünglich vom Empfänger angefordert wird (in der ersten Nachricht), fordert der Sender auch eine Authentifizierung an. Der Empfänger sendet eine dritte Nachricht, die die vom Sender angeforderte Authentifizierung bereitstellt. Dies sind nur drei Nachrichten (im Gegensatz zu vier mit zwei unilateralen Nachrichten).