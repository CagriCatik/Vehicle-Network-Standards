# TCP Verbindungsaufbau

Der **TCP Verbindungsaufbau** ist ein essenzieller Prozess innerhalb des DoIP-Protokolls (Diagnostics over Internet Protocol), der die zuverlässige und stabile Kommunikation zwischen einem Tester und einem Gateway (GW) ermöglicht. Der Aufbau erfolgt über das standardisierte **Three-Way-Handshake-Verfahren**, welches sicherstellt, dass beide Kommunikationspartner synchronisiert sind und Daten korrekt übertragen werden können.



## Ablauf des TCP Verbindungsaufbaus

### Schritt 1: Verbindungsanfrage
- Der Tester sendet als TCP-Client eine Verbindungsanfrage (`SYN`) an das Gateway, das als TCP-Server fungiert.  
- Die Anfrage enthält folgende wichtige Parameter:
  - **Quell-MAC-Adresse** des Testers: `00:16:81:00:62:E0`
  - **Ziel-MAC-Adresse** des Gateways: `00:A4:DF:1E:08:00`
  - **Quell-IP-Adresse** des Testers: `192.168.1.1`
  - **Ziel-IP-Adresse** des Gateways: `192.168.1.2`
  - **Quell-Port**: Zufälliger Port, z. B. `18945`
  - **Ziel-Port**: Standardmäßig `13400` für UDP_DISCOVERY im DoIP.

#### Technische Beschreibung:
Die Verbindungsanfrage wird durch das TCP-Flag `SYN` (Synchronize) gekennzeichnet und enthält die **Sequenznummer A**, mit der die Kommunikation initialisiert wird.

```plaintext
Tester → Gateway:
SYN (SeqNo A)
```



### Schritt 2: Verbindungsanfrage mit Bestätigung
- Nach Erhalt der Verbindungsanfrage antwortet das Gateway mit einer `SYN-ACK`-Nachricht (Synchronize-Acknowledge).  
- Diese Nachricht enthält:
  - Eine neue **Sequenznummer B**, die vom Gateway generiert wurde.
  - Eine Bestätigung der vom Tester gesendeten Sequenznummer A (`AckNo A+1`).

- Zusätzliche technische Details:
  - **Quell-MAC-Adresse** des Gateways: `00:A4:DF:1E:08:00`
  - **Ziel-MAC-Adresse** des Testers: `00:16:81:00:62:E0`
  - **Quell-IP-Adresse** des Gateways: `192.168.1.2`
  - **Ziel-IP-Adresse** des Testers: `192.168.1.1`
  - **Quell-Port**: `13400`
  - **Ziel-Port**: `18945`

```plaintext
Gateway → Tester:
SYN-ACK (SeqNo B, AckNo A+1)
```



### Schritt 3: Bestätigung der Verbindung
- Der Tester bestätigt die Verbindung, indem er eine `ACK`-Nachricht (Acknowledgement) zurücksendet.  
- Diese Nachricht enthält:
  - **Sequenznummer A+1**.
  - **AckNo B+1** zur Bestätigung der Sequenznummer des Gateways.

#### Ergebnis:
Nach Abschluss dieses Schritts gilt die TCP-Verbindung als erfolgreich aufgebaut, und beide Parteien sind synchronisiert.

```plaintext
Tester → Gateway:
ACK (SeqNo A+1, AckNo B+1)
```



## Zusammenfassung des Prozesses

Der komplette Verbindungsaufbau kann wie folgt zusammengefasst werden:

1. **SYN**: Der Tester initiiert die Verbindung und sendet eine Synchronisationsnachricht mit Sequenznummer A.
2. **SYN-ACK**: Das Gateway antwortet mit einer Synchronisations- und Bestätigungsnachricht, die Sequenznummer B und `AckNo A+1` enthält.
3. **ACK**: Der Tester bestätigt die Synchronisation und schickt `AckNo B+1` zurück.

Dieses Verfahren gewährleistet:
- Den synchronisierten Datenaustausch.
- Die Verlässlichkeit der Verbindung.
- Die Korrektheit der Datenübertragung.



## Relevante Codebeispiele

### Beispiel: Aufbau einer TCP-Verbindung
Das folgende Python-Skript veranschaulicht, wie eine TCP-Verbindung zwischen einem Tester (Client) und einem Gateway (Server) hergestellt werden kann:

```python
import socket

# TCP-Client (Tester)
tester_ip = "192.168.1.1"
gateway_ip = "192.168.1.2"
tester_port = 18945  # Zufälliger Port
gateway_port = 13400  # Zielport

# Socket erstellen und Verbindung aufbauen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((tester_ip, tester_port))  # Quell-IP und Port
    s.connect((gateway_ip, gateway_port))  # Ziel-IP und Port
    
    # SYN senden (automatisch beim Verbindungsaufbau)
    print("TCP-Verbindung erfolgreich aufgebaut!")
```

### Beispiel: Paketanalysen mit Wireshark
Die folgende Beschreibung zeigt, wie die einzelnen Schritte des Verbindungsaufbaus in einem Tool wie Wireshark visualisiert werden können:
1. **Filter verwenden**:  
   ```plaintext
   tcp.flags.syn == 1 || tcp.flags.ack == 1
   ```
2. Beobachten Sie:
   - SYN-Paket des Testers.
   - SYN-ACK des Gateways.
   - ACK-Paket des Testers.



## Häufige Probleme und Lösungen

### Problem 1: Zeitüberschreitung bei der Verbindung
- **Ursache**: Gateway nicht erreichbar.
- **Lösung**: Prüfen Sie die IP-Adressen, Ports und Netzwerkeinstellungen.

### Problem 2: SYN-ACK wird nicht empfangen
- **Ursache**: Firewall blockiert die Kommunikation.
- **Lösung**: Konfigurieren Sie die Firewall, um TCP-Port 13400 zuzulassen.

### Problem 3: Verbindung wird sofort abgelehnt
- **Ursache**: Gateway ist nicht im Diagnosemodus.
- **Lösung**: Stellen Sie sicher, dass das Gateway für DoIP konfiguriert ist.
