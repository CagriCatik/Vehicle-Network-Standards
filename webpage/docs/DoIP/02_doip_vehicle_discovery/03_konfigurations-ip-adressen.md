# Konfiguration der IP-Adressen

Die Sequenzdiagramme zeigen den Ablauf der IP-Adresskonfiguration mittels DHCP (Dynamic Host Configuration Protocol) in einem DoIP (Diagnostics over IP) Netzwerk. Dieses Netzwerk besteht aus drei Hauptkomponenten: dem Tester, dem DHCP-Server und dem Fahrzeug-Gateway (GW). Der Prozess wird für beide Komponenten, den Tester und das Fahrzeug-Gateway, parallel dargestellt. Im Folgenden wird der Ablauf detailliert beschrieben und analysiert.

## 1. Verbindung und Aktivierung

Bevor der DHCP-Prozess beginnt, muss eine physische Verbindung zwischen den Komponenten hergestellt werden, und die Aktivierungsleitung muss Spannung führen. Dies stellt sicher, dass alle Geräte betriebsbereit sind und eine Kommunikation im Netzwerk möglich ist.

## 2. DHCP-Prozess für den Tester

### T1. DHCP: Discover

Der Tester beginnt den DHCP-Prozess, indem er eine DHCP-Discover-Nachricht sendet, um eine IP-Adresse anzufordern. Diese Nachricht wird an den DHCP-Server gesendet, um die Verfügbarkeit von IP-Adressen im Netzwerk zu ermitteln.

### T2. DHCP: Offer

Der DHCP-Server empfängt die Discover-Nachricht und antwortet mit einer DHCP-Offer-Nachricht. Darin bietet er eine verfügbare IP-Adresse an und liefert zusätzliche Konfigurationsinformationen wie Subnetzmaske und Gateway-Adresse.

### T3. DHCP: Request

Der Tester sendet daraufhin eine DHCP-Request-Nachricht, in der er die angebotene IP-Adresse anfordert. Dies signalisiert dem DHCP-Server, dass der Tester die angebotene IP-Adresse akzeptieren möchte.

### T4. DHCP: Ack

Der DHCP-Server bestätigt die Zuweisung der IP-Adresse mit einer DHCP-Ack-Nachricht. Damit wird dem Tester mitgeteilt, dass die IP-Adresse erfolgreich zugewiesen wurde und nun verwendet werden kann.

## 3. DHCP-Prozess für das Fahrzeug-Gateway (GW)

### V1. DHCP: Discover

Das Fahrzeug-Gateway sendet ebenfalls eine DHCP-Discover-Nachricht, um eine IP-Adresse anzufordern. Dieser Prozess ist analog zum Tester.

### V2. DHCP: Offer

Der DHCP-Server antwortet mit einer DHCP-Offer-Nachricht, die eine verfügbare IP-Adresse sowie Konfigurationsinformationen wie Subnetzmaske und Gateway-Adresse für das Fahrzeug-Gateway enthält.

### V3. DHCP: Request

Das Fahrzeug-Gateway antwortet darauf mit einer DHCP-Request-Nachricht, in der es die angebotene IP-Adresse anfordert. Dies signalisiert dem DHCP-Server, dass das Gateway die angebotene IP-Adresse akzeptieren möchte.

### V4. DHCP: Ack

Der DHCP-Server bestätigt die Zuweisung der IP-Adresse mit einer DHCP-Ack-Nachricht, die dem Fahrzeug-Gateway mitteilt, dass die IP-Adresse erfolgreich zugewiesen wurde und nun verwendet werden kann.

## Kritische Analyse und Genauigkeit

1. **Synchronisation und Timing:**
   - Die Synchronisation der Discover- und Offer-Nachrichten ist entscheidend, um Kollisionen oder Missverständnisse zu vermeiden. In realen Szenarien können Netzwerkverzögerungen oder Paketverluste diesen Prozess beeinflussen.
   
2. **Vermeidung doppelter IP-Adressen:**
   - Der Prozess sollte sicherstellen, dass keine doppelten IP-Adressen im Netzwerk vergeben werden. Dies wird durch die sorgfältige Verwaltung der verfügbaren IP-Adressen durch den DHCP-Server gewährleistet.

3. **Erweiterte Konfigurationsoptionen:**
   - Neben der Zuweisung der IP-Adresse können weitere DHCP-Optionen konfiguriert werden, wie z. B. DNS-Server, NTP-Server und andere Netzwerkdienste, um eine vollständige Netzwerkkonfiguration sicherzustellen.
