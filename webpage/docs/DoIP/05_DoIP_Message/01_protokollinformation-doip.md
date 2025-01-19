# Protokollinformation für DoIP

Diagnostics over Internet Protocol (DoIP) ist ein standardisiertes Kommunikationsprotokoll, das Diagnoseanfragen und -antworten zwischen einem Tester und Fahrzeugsteuergeräten (ECUs) über IP-basierte Netzwerke ermöglicht. Es basiert auf den ISO-Standards 13400-2 und 13400-3 und wird verwendet, um Fahrzeugdiagnosen über Ethernet effizient und zuverlässig durchzuführen.

## Grundlegende Merkmale von DoIP

### 1. Kommunikationsstruktur
- **Client-Server-Modell**:  
  Der Diagnosetester fungiert als Client, der Anfragen stellt, während das Gateway als Server agiert, das Anfragen verarbeitet und weiterleitet.
- **Einsatz von Ethernet und TCP/IP**:  
  DoIP nutzt Ethernet für die physische Verbindung und TCP/IP für die Datenübertragung.


### 2. Adressierung
- **Logische Adressen**:  
  Jeder Teilnehmer (Tester, Gateway, ECU) erhält eine eindeutige logische Adresse:
  - Tester: z. B. `0x203`
  - Gateway: z. B. `0x201`
  - ECU: z. B. `0x205`
- **MAC-Adressen und IP-Adressen**:  
  Die Kommunikation erfolgt über MAC- und IP-Adressen, die den physischen Netzwerkadaptern zugewiesen sind.


### 3. Transportprotokolle
- **TCP (Transmission Control Protocol)**:  
  Verwendet für verlässliche Diagnoseanfragen und -antworten.
- **UDP (User Datagram Protocol)**:  
  Wird für die Erkennung (Discovery) von Steuergeräten im Netzwerk genutzt.

## DoIP-Nachrichtenstruktur

### 1. Generelle Struktur
Jede DoIP-Nachricht besteht aus mehreren Abschnitten, die die Kommunikation eindeutig identifizieren und steuern:

| Feld               | Länge      | Beschreibung                                      |
|---------------------|------------|--------------------------------------------------|
| **Protokoll-ID**    | 2 Bytes    | Identifiziert DoIP (0xFE 0xCE).                  |
| **Payload-Type**    | 2 Bytes    | Typ der Nachricht (z. B. Diagnoseanfrage).       |
| **Payload-Länge**   | 4 Bytes    | Länge des Nutzdatenfeldes in Bytes.              |
| **Nutzdaten (Payload)** | Variabel | Die eigentlichen Diagnose- oder Steuerdaten.     |


### 2. Wichtige Payload-Typen
Die wichtigsten Payload-Typen sind im ISO-Standard definiert und bestimmen die Art der Nachricht:
- **0x0003**: Vehicle Announcement (Fahrzeugerkennung).
- **0x0005**: Routing Activation Request (Aktivierung von Netzwerken).
- **0x8001**: Diagnoseanfrage.
- **0x8002**: Diagnoseantwort.

## Ablauf einer typischen DoIP-Kommunikation

### 1. Fahrzeugerkennung (Vehicle Announcement)
- Das Fahrzeug (Gateway) sendet eine **Vehicle Announcement-Nachricht**, um dem Tester seine Erreichbarkeit mitzuteilen.  
- Nachrichtentyp: `0x0003`

### 2. Routing-Aktivierung (Routing Activation)
- Der Tester sendet eine **Routing Activation Request**, um die nachgelagerten Netzwerke im Fahrzeug zu aktivieren.
- Nachrichtentyp: `0x0005`
- Das Gateway antwortet mit einer **Routing Activation Response**.

### 3. Diagnosekommunikation
- Der Tester stellt eine **Diagnoseanfrage (Diagnostic Request)** an die Ziel-ECU über das Gateway.
- Nachrichtentyp: `0x8001`
- Die ECU verarbeitet die Anfrage und sendet die **Diagnoseantwort (Diagnostic Response)** zurück.
- Nachrichtentyp: `0x8002`

## Sicherheitsaspekte

### 1. Authentifizierung
DoIP unterstützt Mechanismen zur Authentifizierung des Testers, um sicherzustellen, dass nur autorisierte Geräte Zugriff auf die Fahrzeugsteuergeräte erhalten.

### 2. Verschlüsselung
Um die Sicherheit der Kommunikation zu gewährleisten, können DoIP-Nachrichten mit Verschlüsselungstechnologien wie TLS (Transport Layer Security) gesichert werden.

### 3. Zugriffskontrolle
Die Zielsteuergeräte können nur auf autorisierte Anfragen reagieren, basierend auf:
- Sicherheitslevel.
- Berechtigungsdaten.

## Netzwerkkonfiguration

### 1. Physikalische Verbindung
DoIP verwendet Ethernet als physische Verbindung:
- Typischerweise 100BASE-T1 (Single-Pair Ethernet).
- Alternativ: Standard-Ethernet (z. B. 100BASE-TX).

### 2. IP-Adressierung
DoIP unterstützt sowohl IPv4 als auch IPv6:
- **IPv4-Subnetztyp**: 192.168.x.x/24
- **Portnummern**: Standardmäßig `13400` für TCP und UDP.

## Vorteile von DoIP

1. **Höhere Geschwindigkeit**:  
   Durch den Einsatz von Ethernet ist DoIP deutlich schneller als traditionelle Diagnoseprotokolle wie CAN oder LIN.
   
2. **Erweiterte Netzwerke**:  
   DoIP ermöglicht den Zugriff auf komplexe Fahrzeugnetzwerke über ein zentrales Gateway.

3. **Zukunftssicherheit**:  
   Dank der Unterstützung moderner Netzwerktechnologien ist DoIP ein skalierbarer Standard.

## Relevante Codebeispiele

### Beispiel 1: Senden einer DoIP-Diagnoseanfrage
Das folgende Python-Skript zeigt, wie eine DoIP-Nachricht mit Diagnoseanfrage erstellt und gesendet wird:

```python
import socket

# Verbindungsparameter
gateway_ip = "192.168.1.2"
gateway_port = 13400

# DoIP-Nachricht erstellen
diagnostic_request = bytearray([
    0xFE, 0xCE,             # Protokoll-ID
    0x80, 0x01,             # Payload-Type (Diagnoseanfrage)
    0x00, 0x00, 0x00, 0x06, # Payload-Länge (6 Bytes)
    0x22, 0x12, 0x34,       # UDS: ReadDataByIdentifier (SID: 0x22, DID: 0x1234)
])

# Verbindung herstellen und Nachricht senden
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, gateway_port))
    s.send(diagnostic_request)
    response = s.recv(1024)

print("Empfangene Antwort:", response.hex())
```

## Häufige Probleme und Lösungen

### Problem 1: Keine Antwort vom Gateway
- **Ursache**: Das Gateway ist nicht erreichbar.
- **Lösung**: Überprüfen Sie die IP-Konfiguration und die physische Verbindung.

### Problem 2: Zeitüberschreitung bei Diagnoseanfragen
- **Ursache**: Die Ziel-ECU reagiert nicht rechtzeitig.
- **Lösung**: Erhöhen Sie den Timeout-Wert oder prüfen Sie die ECU auf Fehler.

### Problem 3: Falsche DoIP-Nachricht
- **Ursache**: Fehlerhafte Struktur oder ungültiger Payload-Type.
- **Lösung**: Überprüfen Sie die Nachricht gemäß ISO 13400-2.