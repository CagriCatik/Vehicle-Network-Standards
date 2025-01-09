# Internet Protocol - IPv4/IPv6

### Eigenschaften - Internet Protocol

Aufgabe
Das Internet Protocol (IP) ermöglicht eine Kommunikation über die Grenzen eines lokalen Netzes (LAN). Die unteren Schichten, die den tatsächlichen Transport von Daten durchführen, werden hierzu abstrahiert. So ist ein Zielknoten, ohne Anpassung des übertragenen Pakets, im gleichen Netzwerk oder über mehrere Netze hinweg (z.B. UMTS, WLAN, etc.) erreichbar.

IP-Paket
Die vereinheitlichte Kommunikation wird mit Hilfe des IP-Pakets realisiert. Dieses verfügt über einen festgelegten Header mit einer Ziel- und einer Absender-Adresse. Eine Zieladresse kann auch außerhalb eines lokalen Netzwerkes (LAN) sein. Dies ermöglicht, dass prinzipiell jeder Knoten weltweit adressierbar ist.

Router
Um verschiedene Netze miteinander zu verbinden wird ein Router als Koppelelement verwendet. Ein Router ist ein Knoten der zu mehr als einem Netz gehört und somit auch mehr als eine IP-Adresse besitzt.

Damit IP-Pakete im Fehlerfall nicht für längere Zeit im Internet kreisen, zählt ein Router beim Weiterleiten eines IP-Pakets von Netz zu Netz einen Parameter im IP-Header herunter (Time To Live bei IPv4, Hop Limit bei IPv6). Sobald der Wert Null erreicht ist, wird das Paket vom nächsten Router verworfen.