# Routing Activation Request

Die **Routing Activation Request** ist eine zentrale Nachricht im DoIP-Protokoll (Diagnostics over Internet Protocol). Sie wird verwendet, um den Zugriff auf interne Fahrzeugnetzwerke (z. B. CAN-Busse) zu aktivieren, sodass Diagnosetests und andere Steuergerätekommunikationen über das Gateway ermöglicht werden.

## Nachrichtenstruktur

Die Nachricht besteht aus den folgenden Feldern:

| Feld                       | Länge       | Beschreibung                                                  |
|----------------------------|-------------|--------------------------------------------------------------|
| **Protocol Version**       | 1 Byte      | Version des verwendeten DoIP-Protokolls.                     |
| **Inverse Protocol Version** | 1 Byte    | Sicherheitsprüfung (Komplement der Protokollversion).         |
| **Payload Type**           | 2 Bytes     | Gibt den Nachrichtentyp an (`0x0005`).                       |
| **Payload Length**         | 4 Bytes     | Länge des Nutzdatenfeldes in Bytes.                          |
| **Source Address**         | 2 Bytes     | Logische Adresse des Diagnosetesters.                        |
| **Activation Type**        | 1 Byte      | Art der Aktivierung interner Netzwerke (z. B. `default`).    |
| **Reserved by ISO 13400**  | 4 Bytes     | Reserviert für zukünftige Verwendungen (Standard: `0x00000000`). |
| **Reserved for OEM-specific use** | 4 Bytes | Optional, für herstellerspezifische Informationen.            |


## Beschreibung der Felder

### **Source Address**
- **Länge**: 2 Bytes.  
- **Beschreibung**: Eindeutige logische Adresse des externen Diagnosetesters.  
- **Beispiel**: `0x0203` (Adresse des Testers).

### **Activation Type**
- **Länge**: 1 Byte.  
- **Beschreibung**: Gibt die Art der Netzwerkkonfiguration an, die aktiviert werden soll.  
- **Mögliche Werte**:
  - `0x00`: Default (Standardaktivierung).  
  - `0x01`: WWH-OBD (Worldwide Harmonized OBD).  
  - `0x02`: Central Security.  

### **Reserved by ISO 13400**
- **Länge**: 4 Bytes.  
- **Beschreibung**: Reservierter Bereich für zukünftige Spezifikationen durch die ISO 13400.  
- **Standardwert**: `0x00000000`.

### **Reserved for OEM-specific use**
- **Länge**: 4 Bytes.  
- **Beschreibung**: Optionales Feld für OEM-spezifische Informationen.  
- **Beispiel**: Sicherheits- oder Konfigurationsdaten, die von Fahrzeugherstellern benötigt werden.

## Ablauf der Routing Activation Request

1. **Anfrage des Testers**:  
   Der Tester sendet die Routing Activation Request über TCP an das Gateway, um den Zugriff auf nachgelagerte Fahrzeugnetzwerke zu aktivieren.

2. **Verarbeitung durch das Gateway**:  
   Das Gateway überprüft die Nachricht und aktiviert die angeforderten Netzwerke (z. B. CAN-Busse).

3. **Antwort durch das Gateway**:  
   Das Gateway antwortet mit einer **Routing Activation Response**, um den Erfolg oder mögliche Fehler zu bestätigen.

## Beispielnachrichten

### Routing Activation Request mit Default-Aktivierung
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x0005
Payload Length: 11 Bytes
Source Address: 0x0203
Activation Type: 0x00 (Default)
Reserved by ISO 13400: 0x00000000
Reserved for OEM-specific use: 0x00000000
```

## Relevante Codebeispiele

### Beispiel: Senden einer Routing Activation Request
```python
import socket

# Verbindungsparameter
gateway_ip = "192.168.1.2"
gateway_port = 13400

# Routing Activation Request erstellen
request = bytearray([
    0x02, 0xFD,             # Protokollversion und Inverse Version
    0x00, 0x05,             # Payload Type
    0x00, 0x00, 0x00, 0x0B, # Payload Länge (11 Bytes)
    0x02, 0x03,             # Source Address (0x0203)
    0x00,                   # Activation Type (Default)
    0x00, 0x00, 0x00, 0x00, # Reserved by ISO 13400
    0x00, 0x00, 0x00, 0x00  # Reserved for OEM-specific use
])

# Verbindung herstellen und Nachricht senden
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, gateway_port))
    s.send(request)
    response = s.recv(1024)

print("Empfangene Antwort:", response.hex())
```

## Häufige Probleme und Lösungen

### Problem 1: Keine Antwort vom Gateway
- **Ursache**: Das Gateway ist nicht erreichbar oder die Nachricht ist fehlerhaft formatiert.
- **Lösung**: Überprüfen Sie die IP-Adresse und die Nachrichtenspezifikationen.

### Problem 2: Aktivierung fehlgeschlagen
- **Ursache**: Das Gateway unterstützt den angegebenen Activation Type nicht.
- **Lösung**: Überprüfen Sie die unterstützten Werte für den Activation Type.

### Problem 3: Zeitüberschreitung
- **Ursache**: Das Gateway reagiert nicht rechtzeitig.
- **Lösung**: Erhöhen Sie den Timeout-Wert oder prüfen Sie die Verbindung.
