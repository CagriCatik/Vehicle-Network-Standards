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
