## 4. Internet Protocol - IPv4/IPv6

### Eigenschaften - Internet Protocol

Aufgabe
Das Internet Protocol (IP) ermöglicht eine Kommunikation über die Grenzen eines lokalen Netzes (LAN). Die unteren Schichten, die den tatsächlichen Transport von Daten durchführen, werden hierzu abstrahiert. So ist ein Zielknoten, ohne Anpassung des übertragenen Pakets, im gleichen Netzwerk oder über mehrere Netze hinweg (z.B. UMTS, WLAN, etc.) erreichbar.

IP-Paket
Die vereinheitlichte Kommunikation wird mit Hilfe des IP-Pakets realisiert. Dieses verfügt über einen festgelegten Header mit einer Ziel- und einer Absender-Adresse. Eine Zieladresse kann auch außerhalb eines lokalen Netzwerkes (LAN) sein. Dies ermöglicht, dass prinzipiell jeder Knoten weltweit adressierbar ist.

Router
Um verschiedene Netze miteinander zu verbinden wird ein Router als Koppelelement verwendet. Ein Router ist ein Knoten der zu mehr als einem Netz gehört und somit auch mehr als eine IP-Adresse besitzt.

Damit IP-Pakete im Fehlerfall nicht für längere Zeit im Internet kreisen, zählt ein Router beim Weiterleiten eines IP-Pakets von Netz zu Netz einen Parameter im IP-Header herunter (Time To Live bei IPv4, Hop Limit bei IPv6). Sobald der Wert Null erreicht ist, wird das Paket vom nächsten Router verworfen.

### IPv4 - Version 4

Adressen und Klassen
Die 32 Bit großen IPv4-Adressen werden Byte für Byte als Dezimalzahl mit einem Punkt als Trennzeichen dargestellt (z.B. 192.168.10.1). Für IPv4 wurden vor vielen Jahren Adressklassen definiert, welche die Adressstruktur für den öffentlichen Bereich des Internets regeln. Diese Klassen haben heute zwar keine große praktische Bedeutung mehr, sie erlauben allerdings eine grobe Trennung in Netzwerk- und Hostadresse, so dass ein Rückschluss auf die Knotenanzahl möglich ist.

Lokale Adressen
Öffentliche IPv4-Adressen sind schon seit Jahren vergeben. Allerdings gibt es lokale bzw. private Adressbereiche, die beispielsweise in Firmen oder Privathaushalten frei genutzt werden dürfen. Da diese Adressen niemals im öffentlichen Netzwerk vorkommen, leitet ein Router lokale Adressen nicht ohne Änderungen in das Internet weiter.

Subnetzmasken
Die verwendeten Ziel- und Absenderknotenadressen setzen sich aus der linksbündigen Netzwerkadresse und der rechtsbündigen Hostadresse zusammen. Die Festlegung der Position an der die IP-Adresse aufgeteilt wird, erfolgt typischerweise mit Hilfe von Subnetzmasken. Diese können als eigenständige Adresse (z.B. 255.255.255.0) oder als Präfix hinter einer IP-Adresse (z.B. 192.168.10.1/24) beschrieben werden. Während alle linksbündig gesetzten Bits die Netzwerkadresse kennzeichnen (z.B. 24 Bits), erlauben die rechtsbündig ungesetzten Bits einen Rückschluss auf die Hostadresse (z.B. 8 Bits).

Multi- und Broadcast
Soll ein IP-Paket an mehrere Teilnehmer versendet werden, so können sowohl Multicast- als auch Broadcast-Adressen zum Einsatz kommen. Während Multicast-Adressen konfiguriert oder per IGMP angelegt werden müssen, sind Broadcast-Adressen mit Hilfe der Hostadressen ableitbar. Immer der höchste Wert eines Hostadressbereichs entspricht der zugehörigen Broadcast-Adresse (z.B. 192.168.10.255).

### IPv6 - Version 6

Hintergrund
IPv6 wurde hauptsächlich entwickelt um die Adressknappheit von IPv4 zu überwinden und den Routing-Prozess zu optimieren. Die Anzahl der Felder im IPv6 Header ist im Vergleich zu IPv4 von 12 auf 8 Felder reduziert worden.

Adressschreibweise
Die übliche Schreibweise von IPv6-Adressen ist die Gruppierung von jeweils zwei Byte im hexadezimalen Format mit Doppelpunkt als Trennzeichen. Vier Nullen werden typischerweise nur als eine Null geschrieben oder komplett weggelassen. Anders als bei IPv4 gibt es bei IPv6 keine Broadcast-Adressen. Ein Broadcast ist ein Sonderfall eines Multicasts.

Beispiele für IPv6-Adressen:

1080:0:0:0:8:800:200C:417A (Unicast-Adresse)
FF01:0:0:0:0:0:0:101 (Multicast-Adresse)
0:0:0:0:0:0:0:1 (Loopback-Adresse)
Aufeinanderfolgende Blöcke, die nur Nullen beinhalten, dürfen in IPv6-Adressen einmalig weggelassen werden. Entfallene Blöcke sind unabhängig von deren Anzahl mit zwei Doppelpunkten gekennzeichnet. In einer IPv6-Adresse können zwei aufeinanderfolgende Doppelpunkte somit nur einmalig vorkommen.

1080::8:800:200C:417A (Unicast-Adresse)
FF01::101 (Multicast-Adresse)
::1 (Loopback-Adresse)
IPv4- in IPv6-Adressen
IPv4-Adressen können auch in IPv6 umgesetzt werden. Hierzu steht auch eine Mischnotation zur Verfügung, die eine Kombination von hexadezimalen und dezimalen Werten erlaubt.

::13.1.68.3
::FFFF:129.144.52.38
Subnetzmasken
Bei IPv6-Adressen sind, falls nicht durch eine Subnetzmaske anders definiert, 64 Bit für die Netzwerk- und 64 Bit für die Hostadresse vorgesehen. Durch den hinreichend großen Adressraum ist die Verwendung von Subnetzmasken zwar möglich, allerdings wenig gebräuchlich.

### ARP, NDP, ICMP, IGMP, DHCP

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
