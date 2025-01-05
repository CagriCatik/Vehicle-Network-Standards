# Einführung

Die Authentifizierung und Integritätssicherung sensibler Daten ist notwendig, um die korrekte und sichere Funktionalität der Fahrzeugsysteme zu schützen - dies gewährleistet, dass die empfangenen Daten von der richtigen Steuergeräteeinheit (ECU) stammen und den richtigen Wert haben. 

Das in der AUTOSAR-Spezifikation beschriebene SecOC-Modul bietet die erforderliche Funktionalität zur Überprüfung der Authentizität und Frische der auf PDU basierenden Kommunikation zwischen ECUs innerhalb der Fahrzeugarchitektur. 

Der Ansatz erfordert, dass sowohl das sendende ECU als auch das empfangende ECU ein SecOC-Modul implementieren. Um die Nachrichtenfrische zu gewährleisten, erhält das SecOC-Modul auf der Sender- und Empfängerseite Frische von einem externen **Freshness-Manager** für jede eindeutig identifizierbare gesicherte I-PDU, d. h. für jede gesicherte Kommunikationsverbindung. 

Auf der Senderseite erstellt das SecOC-Modul eine gesicherte I-PDU, indem es Authentifizierungsinformationen zum ausgehenden authentischen I-PDU hinzufügt. Die Authentifizierungsinformationen bestehen aus einem Authenticator (z. B. einer Nachrichtenauthentifizierungscode) und optional einem Frische-Wert. Unabhängig davon, ob der Frische-Wert in der Payload der gesicherten I-PDU enthalten ist oder nicht, wird der Frische-Wert bei der Generierung des Authenticators berücksichtigt. 

Wenn anstelle eines Zeitstempels ein Frischezähler verwendet wird, sollte der Frischezähler vom Frische-Manager vor der Bereitstellung der Authentifizierungsinformationen an die Empfängerseite inkrementiert werden. Auf der Empfängerseite überprüft das SecOC-Modul die Frische und Authentizität des authentischen I-PDU, indem es die Authentifizierungsinformationen überprüft, die vom SecOC-Modul der Senderseite angehängt wurden. 

Um die Authentizität und Frische eines authentischen I-PDU zu überprüfen, sollte die gesicherte I-PDU, die an das SecOC der Empfängerseite bereitgestellt wird, dieselbe gesicherte I-PDU sein, die vom SecOC der Senderseite bereitgestellt wurde, und das SecOC der Empfängerseite sollte Kenntnis vom Frische-Wert haben, der vom SecOC der Senderseite während der Erstellung des Authenticators verwendet wurde.


# Einführung und funktionale Übersicht

Diese Spezifikation definiert die Softwareanforderungen des AUTOSAR Secure Onboard Communication (SecOC)-Moduls. Sie basiert auf den Richtlinien von AUTOSAR SecOC [5] und legt fest, wie die Anforderungen des AUTOSAR SecOC-SRS implementiert werden sollen. Sie beschreibt die grundlegenden Sicherheitsfunktionen, die Funktionalität und die API des AUTOSAR SecOC-Moduls. Ziel des SecOC-Moduls ist es, ressourceneffiziente und praktikable Authentifizierungsmechanismen für kritische Daten auf der PDU-Ebene bereitzustellen und nahtlos in bestehende AUTOSAR-Kommunikationssysteme zu integrieren. Dabei soll der Ressourcenverbrauch so gering wie möglich gehalten werden, um auch Legacy-Systeme mit einem zusätzlichen Schutz ausstatten zu können.

Die Spezifikation geht davon aus, dass hauptsächlich symmetrische Authentifizierungsansätze mit Message Authentication Codes (MACs) verwendet werden. Diese bieten ein vergleichbares Sicherheitsniveau bei deutlich kleineren Schlüsseln im Vergleich zu asymmetrischen Ansätzen und können daher platzsparend und effizient sowohl in Software als auch in Hardware implementiert werden. Dennoch bietet die Spezifikation die nötige Flexibilität, um sowohl symmetrische als auch asymmetrische Authentifizierungsansätze zu unterstützen.

Das SecOC-Modul wird auf der Ebene des AUTOSAR PduR integriert. Abbildung 1 zeigt die Einbindung des SecOC-Moduls als Teil des Autosar-Kommunikationsstapels. In dieser Konfiguration ist der PduR für die Weiterleitung eingehender und ausgehender sicherheitsrelevanter I-PDUs an das SecOC-Modul zuständig. Das SecOC-Modul verarbeitet dann die sicherheitsrelevanten Informationen und gibt die Ergebnisse in Form einer I-PDU zurück an den PduR, der sie weiterleitet. Darüber hinaus nutzt das SecOC-Modul kryptografische Dienste der CSM und interagiert mit dem Rte, um die Verwaltung von Schlüsseln und Zählern zu ermöglichen.

Das SecOC-Modul ist darauf ausgelegt, alle von PduR unterstützten Kommunikationsparadigmen und -prinzipien zu unterstützen, einschließlich Multicast-Kommunikationen, Transportprotokollen und dem PduR-Gateway. Die folgenden Abschnitte bieten eine detaillierte Spezifikation der SecOC-Schnittstellen, Funktionalität und Konfiguration.

# Sichere On-Board Kommunikation

Authentic I-PDU

Eine authentische I-PDU enthält Daten, die durch SOK geschützt werden sollten.
Eine authentische I-PDU ist die zwischen dem AUTOSAR COM-Stack und dem SecOC-Modul kommunizierte Nachricht. Die authentische I-PDU wird vom AUTOSAR COM-Stack aus ihren konstituierenden Signalen konstruiert und darauf reduziert. Da dieses Detail für dieses Dokument nicht relevant ist, werden "authentische I-PDU" und "zu schützende Daten" synonym verwendet, und die authentische I-PDU wird als direkt von einer Anwendung stammend betrachtet, ohne die Vermittlung des COM-Stacks.

Freshness Value

Der Freshness Value dient dazu, Replay-Angriffe zu verhindern. Er wird in die Berechnung des Authentifikators einbezogen.

Der Datenquelle muss bei der Erstellung des Authentifikators derselbe Freshness Value verwendet werden, der auch vom Datenziel für die Überprüfung verwendet wird. Der Freshness Value und der Nachrichtenzähler dürfen niemals für zwei gesicherte I-PDUs mit derselben PDU-ID identisch sein.

Aus diesem Grund muss eine Methode vorhanden sein, um die Freshness Valuee, die von der Datenquelle und dem Datenziel verwendet werden, authentisch zu synchronisieren. Die Strategie zur Erreichung dieser Synchronisation ist Teil des SOK-Protokolls.

Ein Freshness Value wird in SecOC durch eine eindeutige Freshness Value-ID referenziert.

Ein verkürzter Teil des Freshness Values kann vom SecOC als "Trunkierter Freshness Value" in der gesicherten I-PDU übertragen werden. Im Kontext von SOK hat der trunkierte Freshness Value immer eine Länge von null, das heißt, kein Teil des Freshness Values wird als Teil der gesicherten I-PDU übertragen.


[HoliSec Holistic Approach to Improve Data Security (autosec.se)](https://autosec.se/wp-content/uploads/2019/03/4.-Bashar-Dawood.pdf)


[Bachelorarbeit_Bumberger.pdf](file:///C:/Users/mccat/AppData/Local/Temp/MicrosoftEdgeDownloads/40d303c1-8364-413e-b542-8795db82c29e/Bachelorarbeit_Bumberger.pdf)

• Why is secure on-board communication necessary?
• What is AUTOSAR SecOC?
• SecOC Basics
• SecOC opportunities for standardization
• Key management methodologies for symmetric key authentication
• Key management methodologies for asymmetric key authentication
