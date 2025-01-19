# Vehicle Announcement / Vehicle Identification Response

Die **Vehicle Announcement** und die **Vehicle Identification Response** sind essenzielle Nachrichten im DoIP-Protokoll (Diagnostics over Internet Protocol). Sie dienen der Identifikation des Fahrzeugs durch den Diagnosetester und ermöglichen den Aufbau einer spezifischen Kommunikationsverbindung zwischen Tester und Fahrzeug.

## Vehicle Announcement (Fahrzeugerkennung)

Die **Vehicle Announcement-Nachricht** wird vom Gateway des Fahrzeugs ausgesendet, um dem Diagnosetester die Erreichbarkeit des Fahrzeugs mitzuteilen. Diese Nachricht enthält grundlegende Informationen über das Fahrzeug und wird typischerweise per UDP übertragen.

### Nachrichtenstruktur
Die Vehicle Announcement-Nachricht umfasst die folgenden Felder:

| Feld                       | Länge       | Beschreibung                                                   |
|----------------------------|-------------|----------------------------------------------------------------|
| **Protocol Version**       | 1 Byte      | Aktuelle DoIP-Protokollversion.                                |
| **Inverse Protocol Version** | 1 Byte    | Sicherheitsprüfung (Komplement der Protokollversion).          |
| **Payload Type**           | 2 Bytes     | Gibt den Nachrichtentyp an (`0x0004`).                         |
| **Payload Length**         | 4 Bytes     | Länge der Nutzdaten in Bytes.                                  |
| **VIN**                    | 17 Bytes    | Fahrzeug-Identifikationsnummer (Vehicle Identification Number). |
| **Logische Adresse**       | 2 Bytes     | Eindeutige DoIP-Adresse des Gateways.                          |
| **EID** (Entity ID)        | 6 Bytes     | Identifikationseinheit, typischerweise die MAC-Adresse.        |
| **GID** (Group ID)         | 6 Bytes     | Gruppierung für Fahrzeuge ohne VIN.                           |
| **Further Action Required** | 1 Byte     | OEM-spezifische Anforderungen, z. B. Sicherheitsmethoden.      |
| **VIN/GID Sync. Status**   | 1 Byte      | Synchronisationsstatus der VIN/GID-Informationen.              |


### Ablauf
1. **Aussendung der Nachricht**:  
   Das Gateway des Fahrzeugs sendet eine Vehicle Announcement-Nachricht aus, sobald es betriebsbereit ist. Diese Nachricht wird über das Netzwerk an alle potenziellen Tester gesendet (Broadcast oder Multicast).

2. **Inhalt**:  
   Die Nachricht informiert den Diagnosetester über:
   - Die Identität des Fahrzeugs (VIN).
   - Die logische Adresse des Gateways (z. B. `0x201`).
   - Weitere relevante Informationen wie Sicherheitsanforderungen oder Synchronisationsstatus.

3. **Reaktion des Testers**:  
   Der Diagnosetester nutzt die erhaltenen Informationen, um eine gezielte Diagnosekommunikation mit dem Fahrzeug aufzubauen.

## Vehicle Identification Response (Fahrzeugidentifikationsantwort)

Die **Vehicle Identification Response** wird vom Gateway als Antwort auf eine spezifische Fahrzeugidentifikationsanfrage (Vehicle Identification Request) des Testers gesendet. Sie dient der Bestätigung und Übermittlung detaillierter Fahrzeuginformationen.

### Nachrichtenstruktur
Die Vehicle Identification Response hat eine ähnliche Struktur wie die Vehicle Announcement-Nachricht:

| Feld                       | Länge       | Beschreibung                                                   |
|----------------------------|-------------|----------------------------------------------------------------|
| **Protocol Version**       | 1 Byte      | Aktuelle DoIP-Protokollversion.                                |
| **Inverse Protocol Version** | 1 Byte    | Sicherheitsprüfung (Komplement der Protokollversion).          |
| **Payload Type**           | 2 Bytes     | Nachrichtentyp (`0x0004`).                                     |
| **Payload Length**         | 4 Bytes     | Länge der Nutzdaten in Bytes.                                  |
| **VIN**                    | 17 Bytes    | Fahrzeug-Identifikationsnummer.                                |
| **Logische Adresse**       | 2 Bytes     | DoIP-Adresse des Gateways.                                     |
| **EID**                    | 6 Bytes     | Identifikationseinheit des Gateways.                           |
| **GID**                    | 6 Bytes     | Gruppierung bei Fahrzeugen ohne VIN.                           |
| **Further Action Required** | 1 Byte     | OEM-spezifische Aktionen (z. B. Sicherheitsmethoden).          |
| **VIN/GID Sync. Status**   | 1 Byte      | Synchronisationsstatus.                                        |


### Ablauf
1. **Anfrage durch den Tester**:  
   Der Diagnosetester stellt eine Vehicle Identification Request-Nachricht an das Gateway.

2. **Verarbeitung durch das Gateway**:  
   Das Gateway verarbeitet die Anfrage und stellt die angeforderten Informationen zusammen.

3. **Antwort durch das Gateway**:  
   Die Vehicle Identification Response enthält alle relevanten Informationen, um den Tester über das Fahrzeug zu informieren. Dies umfasst insbesondere:
   - VIN.
   - Logische Adresse des Gateways.
   - Sicherheitsstatus und Synchronisationsinformationen.

## Anwendungsfälle

### Fahrzeugerkennung bei Mehrfachverbindungen
In Szenarien mit mehreren Fahrzeugen im selben Netzwerk ermöglicht die Vehicle Announcement-Nachricht dem Tester, gezielt ein spezifisches Fahrzeug basierend auf dessen VIN oder logischer Adresse auszuwählen.

### Sicherheitsprüfungen
Die Synchronisation von VIN/GID und die Angabe von weiteren Sicherheitsanforderungen (z. B. Authentifizierung) gewährleisten, dass nur autorisierte Diagnosetester Zugriff auf die Fahrzeugdaten erhalten.

### Diagnoseaufbau
Nach der Identifikation des Fahrzeugs leitet der Tester die nächsten Schritte wie Routing-Aktivierung oder Diagnoseanfragen ein.

## Beispielnachrichten

### Vehicle Announcement (UDP)
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x0004
Payload Length: 33 Bytes
VIN: "1HGBH41JXMN109186"
Logische Adresse: 0x201
EID: "00:16:81:00:62:E0"
GID: "FF:FF:FF:FF:FF:FF"
Further Action Required: 0x00
VIN/GID Sync. Status: 0x01
```

### Vehicle Identification Response (TCP)
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x0004
Payload Length: 33 Bytes
VIN: "1HGBH41JXMN109186"
Logische Adresse: 0x201
EID: "00:16:81:00:62:E0"
GID: "FF:FF:FF:FF:FF:FF"
Further Action Required: 0x01
VIN/GID Sync. Status: 0x01
```

## Relevanter Code

### Beispiel: Empfang einer Vehicle Announcement-Nachricht
```python
import socket

# UDP-Socket erstellen
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("0.0.0.0", 13400))  # Port für Vehicle Announcement

print("Warten auf Vehicle Announcement...")
while True:
    data, addr = udp_socket.recvfrom(1024)
    print(f"Nachricht von {addr}: {data.hex()}")
```

### Beispiel: Senden einer Vehicle Identification Request
```python
import socket

# TCP-Verbindung zum Gateway
gateway_ip = "192.168.1.2"
gateway_port = 13400

# Vehicle Identification Request erstellen
request = bytearray([
    0x02, 0xFD,             # Protokollversion und Inverse Version
    0x00, 0x04,             # Payload Type
    0x00, 0x00, 0x00, 0x00  # Payload Length (0 Bytes, Anfrage ohne Daten)
])

# Nachricht senden und Antwort empfangen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, gateway_port))
    s.send(request)
    response = s.recv(1024)

print("Empfangene Antwort:", response.hex())
```