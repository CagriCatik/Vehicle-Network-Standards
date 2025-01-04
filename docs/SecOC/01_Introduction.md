# Einführung

Die Authentifizierung und Integritätssicherung sensibler Daten ist notwendig, um die korrekte und sichere Funktionalität der Fahrzeugsysteme zu schützen - dies gewährleistet, dass die empfangenen Daten von der richtigen Steuergeräteeinheit (ECU) stammen und den richtigen Wert haben. 

Das in der AUTOSAR-Spezifikation beschriebene SecOC-Modul bietet die erforderliche Funktionalität zur Überprüfung der Authentizität und Frische der auf PDU basierenden Kommunikation zwischen ECUs innerhalb der Fahrzeugarchitektur. 

Der Ansatz erfordert, dass sowohl das sendende ECU als auch das empfangende ECU ein SecOC-Modul implementieren. Um die Nachrichtenfrische zu gewährleisten, erhält das SecOC-Modul auf der Sender- und Empfängerseite Frische von einem externen **Freshness-Manager** für jede eindeutig identifizierbare gesicherte I-PDU, d. h. für jede gesicherte Kommunikationsverbindung. 

Auf der Senderseite erstellt das SecOC-Modul eine gesicherte I-PDU, indem es Authentifizierungsinformationen zum ausgehenden authentischen I-PDU hinzufügt. Die Authentifizierungsinformationen bestehen aus einem Authenticator (z. B. einer Nachrichtenauthentifizierungscode) und optional einem Frische-Wert. Unabhängig davon, ob der Frische-Wert in der Payload der gesicherten I-PDU enthalten ist oder nicht, wird der Frische-Wert bei der Generierung des Authenticators berücksichtigt. 

Wenn anstelle eines Zeitstempels ein Frischezähler verwendet wird, sollte der Frischezähler vom Frische-Manager vor der Bereitstellung der Authentifizierungsinformationen an die Empfängerseite inkrementiert werden. Auf der Empfängerseite überprüft das SecOC-Modul die Frische und Authentizität des authentischen I-PDU, indem es die Authentifizierungsinformationen überprüft, die vom SecOC-Modul der Senderseite angehängt wurden. 

Um die Authentizität und Frische eines authentischen I-PDU zu überprüfen, sollte die gesicherte I-PDU, die an das SecOC der Empfängerseite bereitgestellt wird, dieselbe gesicherte I-PDU sein, die vom SecOC der Senderseite bereitgestellt wurde, und das SecOC der Empfängerseite sollte Kenntnis vom Frische-Wert haben, der vom SecOC der Senderseite während der Erstellung des Authenticators verwendet wurde.
