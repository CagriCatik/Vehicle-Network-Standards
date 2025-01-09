# ARP, NDP, ICMP, IGMP, DHCP

Hilfsprotokolle
Für Hilfs- und Unterstützungsaufgaben existiert eine Reihe weiterer Protokolle die mehr oder weniger im Hintergrund ablaufen. In der Automobilbranche kommen heute beispielsweise folgende Ergänzungen zum Einsatz:

DHCP
Das Dynamic Host Configuration Protocol ist in der Lage, einem oder mehreren Knoten IP-Adressen automatisch zuzuweisen. Dadurch ist das Einbinden eines neuen IP-Knotens in ein bestehendes Netzwerk, ohne dessen manuelle Konfiguration, möglich.

ICMP
Das Internet Control Message Protocol gehört zu jeder IP-Implementierung und wird dort für Steuerungsaufgaben verwendet. Typisches Anwendungsbeispiel ist der ICMP Echo Request (PING). Mit Hilfe dieses Kommandos kann die IP-Kommunikation zwischen zwei Rechnern überprüft werden. Dies erfolgt durch Aussenden eines ICMP Echo Request an einen gewünschten Knoten. Antwortet dieser daraufhin mit einem ICMP Echo Reply (PONG), so weiß der anfragende Knoten, dass der gewünschte Teilnehmer verfügbar ist.

ARP
Das Address Resolution Protocol dient zur Zuordnung von IP- und MAC-Adressen. Möchte ein IP-Knoten ein bestimmtes Ziel adressieren, kennt aber dessen MAC-Adresse nicht, so kann diese mit Hilfe von ARP angefragt werden. Dies erfolgt mit Hilfe eines ARP-Request der vom Sendeknoten per Broadcast ins Netzwerk ausgesendet wird. Nach Empfangen der Antwort (ARP-Response) kann die enthaltene MAC-Adresse dann im ARP-Cache gespeichert und weiterverwendet werden.

NDP
Das Neighbor Discovery Protocol ersetzt das ARP-Protokoll bei Verwendung von IPv6 und basiert auf ICMPv6. Das Protokoll wird für folgende Einsatzzwecke verwendet:

Router Discovery: Identifizieren der vorhandenen Router im Netz
Prefix Discovery: Festlegen des Adress-Präfixes (Netzwerk-Bits der IPv6-Adresse) für lokale und entfernte Knoten
Unterstützung bei der automatischen Konfiguration von IPv6-Adressen eines Netzknotens (Link-Local Address Generation) ohne Verwendung von DHCP
Parameter Discovery: Einstellen verschiedener Parameter wie Hop Limit

IGMP
Das Internet Group Management Protocol wird von IPv4-Systemen verwendet, um ihre Multicast-Gruppenzugehörigkeit an Multicast-Router weiterzugeben. Alle Hosts, die IP-Multicast empfangen wollen, müssen dieses Protokoll implementiert haben.
