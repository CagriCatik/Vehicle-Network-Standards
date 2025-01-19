# Routing Activation Sequenz

Die **Routing Activation Sequenz** im Rahmen von Diagnostics over Internet Protocol (DoIP) beschreibt den Prozess, durch den ein Tester das Gateway anweist, den Datenverkehr für nachgelagerte Netzwerke im Fahrzeug zu aktivieren. Dieser Prozess gewährleistet den Zugriff auf Fahrzeugsteuergeräte, die über Netzwerke wie CAN-Busse verbunden sind.

---

## Ablauf der Routing Activation Sequenz

Die Routing Activation Sequenz besteht aus zwei Hauptschritten: 

### Schritt 1: Routing Activation Request

Der Tester sendet eine **Routing Activation Request** an das Gateway, um den Zugriff auf weitere fahrzeuginternen Netzwerke (z. B. CAN) zu aktivieren. Die Anfrage enthält spezifische Informationen zur Identifizierung des Testers und zur Aktivierung.

#### Wichtige Parameter der Anfrage:
- **Quell-MAC-Adresse**: `00:16:81:00:62:E0`  
  → Identifiziert die Hardware des Testers.  
- **Ziel-MAC-Adresse**: `00:A4:DF:1E:08:00`  
  → Identifiziert die Hardware des Gateways.  
- **Quell-IP-Adresse**: `192.168.1.1`  
  → Die IP-Adresse des Testers.  
- **Ziel-IP-Adresse**: `192.168.1.2`  
  → Die IP-Adresse des Gateways.  
- **Quell-Port**: `18945` (zufällig generiert).  
- **Ziel-Port**: `13400` (standardmäßig für DoIP).  
- **Logische Adresse**: `0x203` (logische Adresse des Testers).  
- **Activation Type**: `Default` (gibt an, welche Art der Routing-Aktivierung angefordert wird).

#### Technischer Ablauf:
Der Tester schickt die Routing Activation Request an das Gateway, um den Zugang zu nachgelagerten Netzwerken zu aktivieren. Die Anfrage wird über eine TCP-Verbindung übertragen.

```plaintext
Tester → Gateway:
Routing Activation Request
```

---

### Schritt 2: Routing Activation Response

Nachdem das Gateway die Routing Activation Request empfangen hat, prüft es die Anforderung und aktiviert gegebenenfalls die nachgelagerten Netzwerke (z. B. CAN). Anschließend wird eine **Routing Activation Response** zurück an den Tester gesendet.

#### Wichtige Parameter der Antwort:
- **Quell-MAC-Adresse**: `00:A4:DF:1E:08:00`  
  → Identifiziert die Hardware des Gateways.  
- **Ziel-MAC-Adresse**: `00:16:81:00:62:E0`  
  → Identifiziert die Hardware des Testers.  
- **Quell-IP-Adresse**: `192.168.1.2`  
  → Die IP-Adresse des Gateways.  
- **Ziel-IP-Adresse**: `192.168.1.1`  
  → Die IP-Adresse des Testers.  
- **Quell-Port**: `13400` (DoIP-Port des Gateways).  
- **Ziel-Port**: `18945` (zufälliger Port des Testers).  
- **Logische Adresse (Tester)**: `0x203`  
- **Logische Adresse (Gateway)**: `0x201`  
- **Status**: Routing erfolgreich vorbereitet.

#### Technischer Ablauf:
Das Gateway aktiviert die erforderlichen Netzwerke und antwortet mit der Routing Activation Response, die den erfolgreichen Abschluss des Prozesses bestätigt.

```plaintext
Gateway → Tester:
Routing Activation Response
```

---

## Zusammenfassung der Sequenz

1. **Routing Activation Request**: Der Tester fordert das Gateway auf, den Zugriff auf weitere Netzwerke im Fahrzeug (z. B. CAN) zu aktivieren.
2. **Netzwerkaktivierung durch Gateway**: Das Gateway schaltet die angeforderten Netzwerke frei.
3. **Routing Activation Response**: Das Gateway bestätigt dem Tester, dass die Aktivierung erfolgreich durchgeführt wurde.

Diese Sequenz stellt sicher, dass Diagnosedaten über das Gateway an die richtigen Netzwerke weitergeleitet werden.

---

## Codebeispiel zur Umsetzung

### Beispiel: Senden einer Routing Activation Request

Das folgende Python-Skript zeigt, wie eine Routing Activation Request an ein Gateway gesendet wird:

```python
import socket

# TCP-Verbindung einrichten
tester_ip = "192.168.1.1"
gateway_ip = "192.168.1.2"
tester_port = 18945  # Zufällig generierter Port
gateway_port = 13400  # Zielport für DoIP

# Routing Activation Request erstellen
routing_request = {
    "logical_address": 0x203,
    "activation_type": "Default",
    "source_mac": "00:16:81:00:62:E0",
    "destination_mac": "00:A4:DF:1E:08:00"
}

# Verbindung herstellen und Anfrage senden
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, gateway_port))
    s.send(str(routing_request).encode('utf-8'))
    response = s.recv(1024)

print("Routing Activation Response erhalten:", response.decode('utf-8'))
```

---

## Häufige Probleme und Lösungen

### Problem 1: Netzwerk nicht aktiviert
- **Ursache**: Das Gateway hat die Anfrage abgelehnt.
- **Lösung**: Überprüfen Sie, ob das Gateway die korrekten Sicherheits- und Authentifizierungsdaten erhalten hat.

### Problem 2: Keine Antwort vom Gateway
- **Ursache**: Das Gateway ist nicht erreichbar.
- **Lösung**: Stellen Sie sicher, dass die IP-Adressen und Ports korrekt konfiguriert sind.

### Problem 3: Falsche logische Adresse
- **Ursache**: Die logische Adresse des Testers wurde falsch übermittelt.
- **Lösung**: Prüfen Sie die Adresse in der Routing Activation Request und stellen Sie sicher, dass sie mit der Gateway-Konfiguration übereinstimmt.
