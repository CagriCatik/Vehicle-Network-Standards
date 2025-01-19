# Diagnoseanfrage und -antwort

Die **Diagnoseanfrage und -antwort** ist ein zentraler Bestandteil des Kommunikationsprozesses im Rahmen von DoIP (Diagnostics over Internet Protocol). Dieser Prozess ermöglicht es einem Diagnosetester, Informationen von Steuergeräten (ECUs) im Fahrzeug zu erhalten, Diagnosen durchzuführen und Fehlercodes auszulesen oder Steuergeräte zu programmieren.

---

## Ablauf einer Diagnoseanfrage und -antwort

Der Prozess besteht aus zwei Hauptschritten:

### Schritt 1: Diagnoseanfrage (Diagnostic Request)

Der Diagnosetester sendet eine Diagnoseanfrage an das Gateway, das diese Anfrage an die entsprechenden Steuergeräte (ECUs) weiterleitet. Die Anfrage enthält spezifische Parameter, die angeben, welche Daten oder Funktionen angefordert werden.

#### Typische Parameter einer Diagnoseanfrage:
- **Quell-MAC-Adresse**: Identifiziert die Hardware des Testers.
- **Ziel-MAC-Adresse**: Identifiziert die Hardware des Gateways.
- **Quell-IP-Adresse**: IP-Adresse des Testers.
- **Ziel-IP-Adresse**: IP-Adresse des Gateways.
- **Quell-Port**: Zufälliger Port, der vom Tester generiert wird.
- **Ziel-Port**: Standardmäßig `13400` für DoIP.
- **Diagnosedaten**: Informationen über die angeforderten Daten oder Befehle, wie:
  - **SID (Service Identifier)**: Gibt die spezifische Diagnosefunktion an (z. B. `0x22` für Datenabruf).
  - **DID (Data Identifier)**: Gibt den Datensatz an, der angefordert wird.

#### Beispiel für eine Diagnoseanfrage:
Die Anfrage kann beispielsweise den aktuellen Fahrzeugstatus (z. B. Sensordaten) oder Fehlercodes aus einer ECU anfordern.

```plaintext
Tester → Gateway:
Diagnostic Request
SID: 0x22 (Read Data by Identifier)
DID: 0x1234 (Requested Data)
```

---

### Schritt 2: Diagnoseantwort (Diagnostic Response)

Das Gateway leitet die Diagnoseanfrage an die entsprechende ECU weiter. Nachdem die ECU die Anfrage verarbeitet hat, sendet sie eine Antwort zurück, die über das Gateway an den Tester weitergeleitet wird.

#### Typische Parameter einer Diagnoseantwort:
- **Quell-MAC-Adresse**: Identifiziert die Hardware des Gateways.
- **Ziel-MAC-Adresse**: Identifiziert die Hardware des Testers.
- **Quell-IP-Adresse**: IP-Adresse des Gateways.
- **Ziel-IP-Adresse**: IP-Adresse des Testers.
- **Diagnosedaten**: Die angeforderten Daten oder die Bestätigung des Befehls.

#### Beispiel für eine Diagnoseantwort:
Die Antwort enthält die angeforderten Daten oder einen Statuscode, der den Erfolg oder Fehler der Anfrage anzeigt.

```plaintext
Gateway → Tester:
Diagnostic Response
Data: 0x5678 (Requested Data)
Status: Success
```

---

## Typische Diagnosefunktionen

Die Diagnoseanfrage und -antwort basiert auf standardisierten Diensten, die im UDS-Protokoll (Unified Diagnostic Services, ISO 14229) definiert sind. Hier sind einige der häufig verwendeten Dienste:

1. **Datenabruf (Read Data by Identifier, SID: 0x22)**:
   - Zweck: Abrufen von Sensordaten, Softwareversionen oder Fahrzeugstatusinformationen.
   - Beispiel: Abrufen der Fahrgestellnummer (VIN).

2. **Fehlercode-Auslese (Read DTCs, SID: 0x19)**:
   - Zweck: Abrufen von Diagnose-Fehlercodes (DTCs) aus einer ECU.
   - Beispiel: Anfordern aller gespeicherten DTCs.

3. **Steuergeräte-Reset (ECU Reset, SID: 0x11)**:
   - Zweck: Zurücksetzen eines Steuergeräts, z. B. nach einem Softwareupdate.

4. **Datenprogrammierung (Write Data by Identifier, SID: 0x2E)**:
   - Zweck: Schreiben neuer Daten in eine ECU, z. B. Kalibrierungswerte.

---

## Ablaufdiagramm einer Diagnoseanfrage und -antwort

1. **Diagnosetester (Tester)**:
   - Stellt eine Anfrage mit spezifischen Daten (SID und DID).
   - Sendet die Anfrage über TCP/IP an das Gateway.

2. **Gateway**:
   - Leitet die Anfrage an die Ziel-ECU weiter.
   - Empfängt die Antwort von der ECU.
   - Sendet die Antwort zurück an den Tester.

3. **ECU (Steuergerät)**:
   - Verarbeitet die Anfrage.
   - Stellt die angeforderten Daten bereit oder führt den angeforderten Befehl aus.
   - Sendet eine Antwort mit den Ergebnissen zurück.

---

## Relevante Codebeispiele

### Beispiel 1: Senden einer Diagnoseanfrage
Das folgende Python-Skript zeigt, wie eine Diagnoseanfrage über TCP an ein Gateway gesendet wird:

```python
import socket

# Verbindungsparameter
tester_ip = "192.168.1.1"
gateway_ip = "192.168.1.2"
tester_port = 18945  # Zufällig generierter Port
gateway_port = 13400  # Zielport für DoIP

# Diagnoseanfrage erstellen (SID: 0x22, DID: 0x1234)
diagnostic_request = bytearray([0x22, 0x12, 0x34])

# Verbindung herstellen und Anfrage senden
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, gateway_port))
    s.send(diagnostic_request)
    response = s.recv(1024)

print("Diagnoseantwort erhalten:", response.hex())
```

### Beispiel 2: Auswerten einer Diagnoseantwort
Das folgende Skript zeigt, wie eine Diagnoseantwort analysiert werden kann:

```python
def parse_diagnostic_response(response):
    sid = response[0]  # Service Identifier
    data = response[1:]  # Antwortdaten
    
    if sid == 0x62:  # Positive Response Code für Read Data by Identifier
        print("Diagnose erfolgreich!")
        print("Erhaltene Daten:", data.hex())
    else:
        print("Fehlercode erhalten:", hex(sid))

# Beispielantwort
response = bytearray([0x62, 0x56, 0x78])
parse_diagnostic_response(response)
```

---

## Häufige Probleme und Lösungen

### Problem 1: Keine Antwort vom Gateway
- **Ursache**: Falsche Zieladresse oder Gateway nicht erreichbar.
- **Lösung**: Prüfen Sie die Netzwerkverbindung und die IP-Konfiguration.

### Problem 2: Fehlercode in der Antwort
- **Ursache**: Die ECU hat die Anfrage abgelehnt (z. B. wegen falscher Sicherheitsstufe).
- **Lösung**: Stellen Sie sicher, dass die Sicherheitsstufe korrekt ist und die Anfrage zulässig ist.

### Problem 3: Zeitüberschreitung
- **Ursache**: Die ECU reagiert nicht rechtzeitig.
- **Lösung**: Erhöhen Sie den Timeout-Wert oder überprüfen Sie die ECU auf Fehler.
