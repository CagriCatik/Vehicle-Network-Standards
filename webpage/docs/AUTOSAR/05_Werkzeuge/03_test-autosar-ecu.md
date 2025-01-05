## Test von AUTOSAR Steuergeräten

Blackbox- Tests
Beim Testen eines AUTOSAR Steuergerätes lassen sich grundsätzlich die gleichen Verfahren anwenden wie beim Test von Steuergeräten mit einer anderen internen Software-Architektur. Betrachtet man das Steuergerät als Blackbox, gibt es lediglich folgende Dinge zu beachten

Netzwerk Management:
AUTOSAR hat ein eigenes Netzwerk Management (NM) Protokoll definiert, das sich von den bisher eingesetzten Protokollen wie z.B. OSEK NM unterscheidet. Die Testumgebung muss dieses NM-Protokoll berücksichtigen und die entsprechenden Botschaften auf den Netzwerk-Kanälen korrekt bereitstellen bzw. verarbeiten.
Dateiformate für die Beschreibung der Netzwerk Kommunikation:
Die Beschreibung der Netzwerk Kommunikation in AUTOSAR ist Bestandteil der System Description. Je nach Vorgabe des OEMs werden die bisherigen Formate wie .dbc, FIBEX oder .ldf durch das neue Format ersetzt. Die Testumgebung muss in der Lage sein, dieses Format zu verarbeiten.
nutzbare Zustandsgrößen
AUTOSAR bietet allerdings auch einen Zusatznutzen beim Testen und Debuggen des Steuergerätes: durch die standardisierte interne Software-Architektur existieren in jedem AUTOSAR Steuergerät bestimmte Zustandsgrößen, die in der Testumgebung berücksichtigt werden können. Beispiele hierfür sind der Steuergerätezustand, der im EcuM-Modul vorliegt, oder Kommunikationszustände der einzelnen Netzwerkkanäle, die im ComM-Modul hinterlegt sind. Bei geeigneter Implementierung der BSW-Module kann ein Zugriff auf diese Zustandsgrößen über einen XCP-Zugang zum Steuergerät stattfinden, z.B. über eines der Netzwerke oder eine Debugging-Schnittstelle wie JTAG oder Nexus. Eine passende Beschreibungsdatei (A2L) für diese Zustandsgrößen kann von den BSW-Generatoren bereitgestellt werden. Alternativ lässt sich für den Zugriff auch das speziell für diesen Zweck von AUTOSAR definierte Monitoring- und Debugging-Protokoll verwenden.

Zugriff auf SWC- Kommunikation
Auch beim Zugriff auf die Applikationsebene bietet AUTOSAR Vorteile. So kann die RTE derart generiert werden, dass ein Zugriff auf die zwischen den SWCs ausgetauschten Daten möglich ist. Auch hierfür kann wieder eine passende A2L-Datei vom RTE-Generator erzeugt werden.
