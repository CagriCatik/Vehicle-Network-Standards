# Routing-Aktivierungsanfrage/-antwort in DoIP

Die Routing-Aktivierung ist ein zentraler Prozess im Rahmen von Diagnostics over Internet Protocol (DoIP), der die Kommunikation zwischen einem Diagnosetester und den Steuergeräten (ECUs) eines Fahrzeugs über ein Gateway ermöglicht. Dieser Prozess stellt sicher, dass Diagnosebefehle die vorgesehenen Netzwerke, wie z. B. CAN-Busse im Fahrzeug, erreichen.

## Übersicht über die Routing-Aktivierung

Der Prozess der **Routing-Aktivierungsanfrage/-antwort** umfasst drei Hauptschritte:

1. **Routing-Aktivierungsanfrage**:  
   Der Diagnosetester initiiert eine Anfrage an das Gateway, um das Routing zu zusätzlichen fahrzeuginternen Netzwerken zu aktivieren, die für Diagnosen erforderlich sind (z. B. ein CAN-Bus).

2. **Netzwerkaktivierung durch das Gateway**:  
   Das Gateway aktiviert gegebenenfalls Verbindungen zu weiteren Netzwerken im Fahrzeug.

3. **Routing-Aktivierungsantwort**:  
   Das Gateway bestätigt die Anfrage, indem es eine Antwort mit wichtigen Informationen wie den logischen Adressen des Testers und des Gateways zurücksendet.



## Prozessablauf der Routing-Aktivierung

### Schritt 1: Routing-Aktivierungsanfrage
- Der Diagnosetester sendet eine **Routing-Aktivierungsanfrage** an das Gateway über TCP. 
- Diese Anfrage enthält Parameter, die das Gateway anweisen, Routing für Netzwerke zu aktivieren, die für die Diagnose benötigt werden.

#### Zweck:
Der Tester benötigt Zugriff auf nachgelagerte fahrzeuginterne Netzwerke (z. B. CAN), um Diagnosen an verschiedenen Steuergeräten durchzuführen.

#### Technische Details:
- Protokoll: TCP/IP
- Typische Ports: Diagnoseanfragen verwenden häufig Port 13400 für DoIP.
- Beispiel-Datenstruktur:
   ```plaintext
   Anfrageart: Routing-Aktivierung
   Quelladresse: Logische Adresse des Testers (z. B. 0x203)
   Authentifizierungsdaten: (Optional, abhängig vom Sicherheitsniveau)
   ```



### Schritt 2: Netzwerkaktivierung durch das Gateway
- Nach Empfang der **Routing-Aktivierungsanfrage** aktiviert das Gateway gegebenenfalls die erforderlichen nachgelagerten Netzwerke, wie z. B. CAN-Busse.
- Dieser Schritt stellt sicher, dass die mit diesen Netzwerken verbundenen Steuergeräte für Diagnosen erreichbar sind.

#### Beispiel-Szenarien:
- **CAN-Bus-Aktivierung**: Das Gateway ermöglicht die Kommunikation mit Steuergeräten auf dem CAN-Bus.
- **Energiemanagement**: Das Gateway stellt sicher, dass Steuergeräte im Energiesparmodus aufgeweckt werden, um auf Diagnoseanfragen zu reagieren.



### Schritt 3: Routing-Aktivierungsantwort
- Das Gateway sendet eine **Routing-Aktivierungsantwort** zurück an den Diagnosetester über TCP.
- Diese Antwort bestätigt, ob die Routing-Aktivierung erfolgreich war, und enthält die logischen Adressen der beteiligten Einheiten.

#### Wichtige Informationen in der Antwort:
1. **Logische Adresse des Testers**: Zum Beispiel `0x203`.
2. **Logische Adresse des Gateways**: Zum Beispiel `0x201`.

#### Beispiel-Datenstruktur:
   ```plaintext
   Antwortart: Routing-Aktivierungsantwort
   Quelladresse: Logische Adresse des Gateways (z. B. 0x201)
   Zieladresse: Logische Adresse des Testers (z. B. 0x203)
   Status: Erfolg oder Fehler
   ```

#### Fehlerbedingungen:
- Die Antwort kann Fehler enthalten, z. B. durch:
  - Ungültige Authentifizierungsdaten.
  - Nicht verfügbare nachgelagerte Netzwerke.
  - Interne Gateway-Fehler.



## Erklärung der Abbildung

Die bereitgestellte Abbildung veranschaulicht den Prozess der Routing-Aktivierung wie folgt:

1. **Schritt 1 (Gelbes Feld)**:  
   Der Diagnosetester sendet eine `Routing-Aktivierungsanfrage` über TCP an das Gateway. Dieser Schritt löst aus, dass das Gateway sich auf die Diagnose vorbereitet, indem es nachgelagerte Netzwerke aktiviert.

2. **Schritt 2 (Rotes Feld)**:  
   Das Gateway aktiviert, falls erforderlich, relevante Netzwerke im Fahrzeug, wie z. B. einen CAN-Bus. Dies stellt sicher, dass alle Steuergeräte für die Diagnose erreichbar sind.

3. **Schritt 3 (Blaues Feld)**:  
   Das Gateway antwortet mit einer `Routing-Aktivierungsantwort` und bestätigt dabei die logischen Adressen des Testers und des Gateways.


## Wichtige Konzepte und praktische Implikationen

### Logische Adressen
Logische Adressen sind eindeutige Identifikatoren, die im Rahmen von DoIP verwendet werden, um verschiedene Entitäten (z. B. Tester, Gateway und Steuergeräte) zu unterscheiden. Sie ermöglichen ein präzises Routing von Diagnose-Nachrichten.

- **Beispiel**:  
   - Tester-Adresse: `0x203`
   - Gateway-Adresse: `0x201`

### Sicherheitsaspekte
Die Routing-Aktivierung kann Authentifizierungsmechanismen erfordern, um sicherzustellen, dass nur autorisierte Tester auf Diagnosenetzwerke zugreifen können.

- **Authentifizierungsmethoden**:
  - Passwortbasiert.
  - Sichere Schlüssel oder Zertifikate.

### Netzwerkabhängigkeiten
- **TCP/IP** dient als Transportprotokoll für die Kommunikation über DoIP.
- Das Gateway kann für die Kommunikation mit nachgelagerten Netzwerken auf **Ethernet**, **CAN** oder andere fahrzeugspezifische Netzwerke zurückgreifen.


##  Herausforderungen und Lösungen

### Herausforderung 1: Netzwerklatenz
- **Problem**: Hohe Latenzen bei der TCP/IP-Kommunikation können die Routing-Aktivierung verzögern.
- **Lösung**: Optimierung der Gateway-Verarbeitung und Priorisierung von Diagnoseanfragen.

### Herausforderung 2: Authentifizierungsfehler
- **Problem**: Falsche Authentifizierungsdaten können die Routing-Aktivierung blockieren.
- **Lösung**: Sicherstellung der Synchronisation der Anmeldedaten zwischen Tester und Gateway.

### Herausforderung 3: Nicht verfügbare nachgelagerte Netzwerke
- **Problem**: CAN- oder andere Netzwerke sind möglicherweise inaktiv.
- **Lösung**: Verwendung von Aufwachmechanismen im Gateway oder erneutes Senden der Anfrage.



## Codebeispiele zur Implementierung

### Beispiel: Senden einer Routing-Aktivierungsanfrage
```python
import socket

# TCP-Verbindung einrichten
gateway_ip = "192.168.0.10"
port = 13400
tester_logical_address = 0x203

# Socket erstellen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, port))
    
    # Routing-Aktivierungsanfrage erstellen
    routing_request = bytearray([0x02, tester_logical_address])  # Vereinfachtes Beispiel
    s.send(routing_request)
    
    # Routing-Aktivierungsantwort empfangen
    response = s.recv(1024)
    print("Routing-Aktivierungsantwort:", response)
```

### Beispiel: Parsen der Routing-Aktivierungsantwort
```python
def parse_response(response):
    status = response[0]
    gateway_address = response[1:3]
    tester_address = response[3:5]
    
    if status == 0x00:
        print("Routing-Aktivierung erfolgreich")
        print("Gateway-Adresse:", gateway_address)
        print("Tester-Adresse:", tester_address)
    else:
        print("Routing-Aktivierung fehlgeschlagen, Statuscode:", status)

# Beispielantwort
response = b'\x00\x02\x01\x02\x03'
parse_response(response)
```
