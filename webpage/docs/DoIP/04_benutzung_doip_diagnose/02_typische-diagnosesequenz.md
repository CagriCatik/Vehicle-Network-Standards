# Typische Diagnosesequenz

Die **typische Diagnosesequenz** beschreibt den Ablauf einer Kommunikation zwischen einem Diagnosetester und einem Fahrzeugsteuergerät (ECU) im Rahmen von DoIP (Diagnostics over Internet Protocol). Diese Sequenz stellt sicher, dass Diagnoseanfragen zuverlässig verarbeitet und Antworten korrekt übermittelt werden.

## Ablauf der Diagnosesequenz

Die Diagnosesequenz umfasst vier Hauptschritte:

### Schritt 1: Diagnoseanfrage
Der Tester initiiert eine Diagnoseanfrage und sendet sie über TCP an das Gateway. Die Anfrage wird im UDS-Format (Unified Diagnostic Services) formuliert und enthält die folgenden Informationen:

#### Details der Anfrage:
- **Logische Adresse des Testers**: `0x203`  
  → Identifiziert den Diagnosetester.  
- **Logische Adresse der ECU**: `0x205`  
  → Gibt die Ziel-ECU an.  
- **UDS-Service**: `ReadDataByIdentifier (SID: 0x22)`  
  → Fordert spezifische Daten von der ECU an, wie z. B. Sensordaten oder Fahrzeugstatusinformationen.

```plaintext
Tester → Gateway:
Diagnoseanfrage
```

#### Erklärung:
Der Tester fordert bestimmte Daten von der ECU an, indem er die logische Adresse und den UDS-Service in der Nachricht spezifiziert. Diese Anfrage wird vom Gateway weitergeleitet.

### Schritt 2: DoIP-Bestätigung (DoIP Ack)
Das Gateway bestätigt den Empfang der Diagnoseanfrage und leitet diese an die Ziel-ECU weiter. Die Bestätigung (DoIP Ack) enthält keine Diagnosedaten, sondern dient lediglich der Kommunikation, dass die Anfrage erfolgreich empfangen wurde.

#### Ablauf:
- Das Gateway überprüft die Anfrage und leitet sie an die Ziel-ECU weiter.
- Eine Bestätigungsnachricht wird an den Tester zurückgesendet.

```plaintext
Gateway → Tester:
DoIP-Bestätigung (DoIP Ack)
```

#### Bedeutung:
Die Bestätigung zeigt an, dass die Anfrage korrekt verarbeitet wird und das Gateway mit der Ziel-ECU kommuniziert.

### Schritt 3: Diagnose-Response
Die Ziel-ECU verarbeitet die Diagnoseanfrage und generiert eine Antwort. Diese Antwort wird über das Gateway an den Tester zurückgeleitet.

#### Details der Antwort:
- **Logische Adresse des Testers**: `0x203`  
- **Logische Adresse der ECU**: `0x205`  
- **UDS-Service**: `ReadDataByIdentifier (SID: 0x22)`  
- **UDS-Daten**: Die angeforderten Daten (z. B. Fahrzeugstatus oder Sensordaten).

```plaintext
Gateway → Tester:
Diagnose-Response
```

#### Erklärung:
Die Antwort enthält die vom Tester angeforderten Daten oder Statusinformationen und wird innerhalb des festgelegten UDS-Timeouts (P6) zurückgesendet.

### Schritt 4: Empfang der Antwort
Der Diagnosetester erwartet die Antwort vor Ablauf des P6-Intervalls. Dieses Intervall ist ein UDS-spezifischer Timeout für die Kommunikation mit der Ziel-ECU.

#### P6-Timeout:
- **Definition**: Zeitrahmen, in dem die ECU die Antwort bereitstellen muss.
- **Typischer Wert**: Standardmäßig zwischen 50 ms und 500 ms, je nach Konfiguration.

```plaintext
Tester → Empfang der Antwort innerhalb von P6
```

#### Bedeutung:
Das P6-Timeout stellt sicher, dass die Kommunikation in einem vordefinierten Zeitrahmen erfolgt und bei Verzögerungen Fehler gemeldet werden.

## Ablaufdiagramm der Diagnosesequenz

1. **Diagnoseanfrage**: Der Tester sendet die Anfrage über TCP an das Gateway.
2. **DoIP-Bestätigung**: Das Gateway bestätigt den Empfang und leitet die Anfrage weiter.
3. **Diagnose-Response**: Die ECU verarbeitet die Anfrage und antwortet über das Gateway.
4. **Empfang der Antwort**: Der Tester erhält die Antwort innerhalb des festgelegten Zeitrahmens (P6).

## Relevante Codebeispiele

### Beispiel: Senden einer Diagnoseanfrage
Das folgende Python-Skript zeigt, wie eine Diagnoseanfrage an ein Gateway gesendet wird:

```python
import socket

# Verbindungsparameter
tester_ip = "192.168.1.1"
gateway_ip = "192.168.1.2"
tester_port = 18945  # Zufällig generierter Port
gateway_port = 13400  # Zielport für DoIP

# Diagnoseanfrage erstellen (UDS: ReadDataByIdentifier, SID: 0x22, DID: 0x1234)
diagnostic_request = bytearray([0x22, 0x12, 0x34])

# Verbindung herstellen und Anfrage senden
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, gateway_port))
    s.send(diagnostic_request)
    response = s.recv(1024)

print("Diagnoseantwort erhalten:", response.hex())
```

### Beispiel: Validierung des P6-Timeouts
Dieses Skript überprüft, ob die Antwort innerhalb des P6-Timeouts empfangen wurde:

```python
import time

# Maximales P6-Timeout (in Sekunden)
P6_TIMEOUT = 0.5

# Startzeit
start_time = time.time()

# Warten auf Antwort
try:
    response = s.recv(1024)
    elapsed_time = time.time() - start_time
    if elapsed_time > P6_TIMEOUT:
        print("P6-Timeout überschritten!")
    else:
        print("Antwort erhalten innerhalb:", elapsed_time, "Sekunden")
except socket.timeout:
    print("Keine Antwort innerhalb des P6-Timeouts.")
```

## Häufige Probleme und Lösungen

### Problem 1: Keine Antwort innerhalb des P6-Timeouts
- **Ursache**: Die ECU benötigt zu lange für die Verarbeitung.
- **Lösung**: Prüfen Sie die ECU-Konfiguration und erhöhen Sie ggf. den P6-Wert.

### Problem 2: DoIP-Bestätigung fehlt
- **Ursache**: Netzwerkprobleme oder fehlerhafte Gateway-Konfiguration.
- **Lösung**: Stellen Sie sicher, dass das Gateway erreichbar ist und korrekt konfiguriert wurde.

### Problem 3: Fehlerhafte Daten in der Antwort
- **Ursache**: Die Anfrage enthielt falsche Parameter (z. B. ungültiger DID).
- **Lösung**: Überprüfen Sie die Anfragedaten auf Richtigkeit.