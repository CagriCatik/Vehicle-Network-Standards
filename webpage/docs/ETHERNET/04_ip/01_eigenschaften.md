# Internet Protocol - IPv4/IPv6

Das Internet Protocol (IP) ist eine zentrale Komponente moderner Kommunikationssysteme, die es ermöglicht, Daten über lokale Netzwerke hinaus zu übertragen. Es bildet die Grundlage für die Datenkommunikation im Internet, indem es verschiedene Netzwerke und Technologien miteinander verbindet. Im Folgenden wird detailliert auf die Eigenschaften, die Funktionsweise und die technischen Aspekte von IPv4 und IPv6 eingegangen.

---

## Eigenschaften des Internet Protocols

### Aufgabe des IP
Das Internet Protocol (IP) abstrahiert die zugrunde liegenden physikalischen Übertragungstechnologien und ermöglicht so eine nahtlose Kommunikation zwischen Knoten in unterschiedlichen Netzwerken. Dabei übernimmt IP folgende Kernaufgaben:
- **Adressierung**: Jeder Knoten im Netzwerk wird durch eine eindeutige IP-Adresse identifiziert.
- **Routing**: Datenpakete können über mehrere Netzwerke hinweg an das richtige Ziel weitergeleitet werden.
- **Abstraktion der Übertragungsschichten**: IP abstrahiert die unteren Schichten (wie Ethernet, WLAN oder UMTS) und ermöglicht so die Übertragung über heterogene Netzwerke.

Durch diese Eigenschaften gewährleistet IP eine zuverlässige und skalierbare Datenkommunikation, unabhängig von der Art des verwendeten Netzwerks.

### IP-Paket
Das Herzstück des Internet Protocols ist das **IP-Paket**, das die vereinheitlichte Kommunikation ermöglicht. Ein IP-Paket besteht aus:
1. **Header**: Enthält Kontrollinformationen, wie:
   - **Quelladresse**: Die Adresse des sendenden Knotens.
   - **Zieladresse**: Die Adresse des empfangenden Knotens, die auch außerhalb des lokalen Netzwerks liegen kann.
   - **Protokollinformationen**: Gibt an, welches Transportprotokoll (z. B. TCP oder UDP) verwendet wird.
   - **Time To Live (TTL)** bei IPv4 oder **Hop Limit** bei IPv6: Begrenzung der maximalen Lebensdauer des Pakets, um endlose Schleifen zu verhindern.
2. **Payload (Nutzdaten)**: Enthält die eigentlichen zu übertragenden Daten.

Die Struktur des IP-Pakets erlaubt es, prinzipiell jeden Knoten weltweit anzusprechen, was IP zur Grundlage des globalen Internets macht.

### Router
Router spielen eine zentrale Rolle im Internet Protocol. Sie dienen als Koppelelemente zwischen Netzwerken und sorgen dafür, dass IP-Pakete ihren Zielknoten erreichen. Die wichtigsten Funktionen eines Routers umfassen:
- **Netzwerkverbindung**: Ein Router gehört zu mehreren Netzwerken und besitzt für jedes Netzwerk eine eigene IP-Adresse.
- **Paketweiterleitung**: Der Router analysiert den Zieladressbereich des IP-Headers und leitet das Paket entsprechend der Routing-Tabelle an das nächste Netzwerk weiter.
- **TTL- oder Hop-Limit-Handling**: Beim Weiterleiten eines Pakets wird der TTL- oder Hop-Limit-Wert um eins reduziert. Erreicht dieser Wert null, wird das Paket verworfen, um Schleifen und unnötige Netzwerkauslastung zu vermeiden.

---

## IPv4 vs. IPv6

### Adressierung
- **IPv4**: Nutzt 32-Bit-Adressen, die maximal etwa 4,3 Milliarden eindeutige Adressen ermöglichen. Beispiel: `192.168.0.1`.
- **IPv6**: Nutzt 128-Bit-Adressen, die eine nahezu unerschöpfliche Anzahl eindeutiger Adressen bereitstellen. Beispiel: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.

### Header-Struktur
- **IPv4**: Der Header ist variabel und umfasst mindestens 20 Bytes. Er enthält Felder wie TTL, Prüfsummen und Optionen.
- **IPv6**: Der Header ist fix und kompakter gestaltet, mit einer Größe von 40 Bytes. Einige Funktionen, wie Prüfsummen, wurden entfernt, um die Verarbeitungsgeschwindigkeit zu erhöhen.

### Erweiterungen und Verbesserungen
- **IPv4**:
  - Begrenzte Adressverfügbarkeit führte zur Einführung von NAT (Network Address Translation).
  - Keine eingebauten Mechanismen für Sicherheit.
- **IPv6**:
  - Unterstützt direkt **IPsec** für Sicherheit.
  - Vereinfacht die Adresszuweisung durch **stateless address autoconfiguration (SLAAC)**.
  - Bietet native Unterstützung für Multicast und Anycast.

### Lebensdauer und Fragmentierung
- **Time To Live (TTL)**: IPv4 verwendet TTL, um die Lebensdauer eines Pakets zu begrenzen.
- **Hop Limit**: IPv6 ersetzt TTL durch Hop Limit, um Konsistenz in der Terminologie zu gewährleisten.
- **Fragmentierung**: In IPv4 können Router Pakete fragmentieren, während in IPv6 die Fragmentierung ausschließlich vom Absender durchgeführt wird.

---

## Rolle der Router im IP-Netzwerk

Router sind entscheidend für die Funktionalität von IPv4 und IPv6. Sie verbinden verschiedene Netzwerke, analysieren IP-Header und leiten Pakete effizient weiter. Die Schlüsselmerkmale eines Routers sind:
1. **Routing-Tabellen**: Enthalten Informationen über die Topologie des Netzwerks und ermöglichen die Auswahl des besten Pfads zum Ziel.
2. **Netzwerksegmentierung**: Router trennen Netzwerke physikalisch und logisch, um die Effizienz und Sicherheit zu erhöhen.
3. **Fehlerhandling**: Wenn ein Paket nicht zugestellt werden kann, sendet der Router häufig eine Fehlermeldung an den Absender zurück, z. B. mit dem ICMP-Protokoll.
