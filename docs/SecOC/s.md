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
