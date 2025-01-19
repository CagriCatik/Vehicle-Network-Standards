# Vehicle Identification Request

Die **Vehicle Identification Request** ist eine essenzielle Nachricht im DoIP-Protokoll (Diagnostics over Internet Protocol). Sie ermöglicht es einem Diagnosetester, spezifische Informationen über ein Fahrzeug anzufordern, wie die Fahrzeug-Identifikationsnummer (VIN) oder die Entity ID (EID). Dies ist der erste Schritt zur Identifikation eines Fahrzeugs und zur Etablierung einer Diagnosekommunikation.

---

## Nachrichtenstruktur

Die Vehicle Identification Request-Nachricht enthält die folgenden Felder:

| Feld                       | Länge       | Beschreibung                                                  |
|----------------------------|-------------|--------------------------------------------------------------|
| **Protocol Version**       | 1 Byte      | Version des verwendeten DoIP-Protokolls.                     |
| **Inverse Protocol Version** | 1 Byte    | Sicherheitsprüfung (Komplement der Protokollversion).         |
| **Payload Type**           | 2 Bytes     | Typ der Nachricht (`0x0002`, `0x0003` oder `0x0001`).         |
| **Payload Length**         | 4 Bytes     | Länge des Nutzdatenfeldes in Bytes.                          |
| **Payload**                | 0–17 Bytes  | VIN, EID oder leer (abhängig vom Payload Type).               |

---

## Beschreibung der Payload Types

### **Payload Type = 0x0002**: Anfrage mit EID
- **Einsatzbereich**: Wird verwendet, um ein Fahrzeug anhand seiner Entity ID (EID) zu identifizieren.
- **Payload-Länge**: 6 Bytes.
- **Payload-Inhalt**: EID (z. B. die MAC-Adresse des Gateways).
- **Verwendung**: Geeignet, wenn die EID des Fahrzeugs bekannt ist.

```plaintext
Beispiel:
Payload Type: 0x0002
Payload Length: 6 Bytes
Payload (EID): "00:16:81:00:62:E0"
```

---

### **Payload Type = 0x0003**: Anfrage mit VIN
- **Einsatzbereich**: Wird verwendet, um ein Fahrzeug anhand seiner Fahrzeug-Identifikationsnummer (VIN) zu identifizieren.
- **Payload-Länge**: 17 Bytes.
- **Payload-Inhalt**: VIN.
- **Verwendung**: Geeignet, wenn die VIN des Fahrzeugs bekannt ist.

```plaintext
Beispiel:
Payload Type: 0x0003
Payload Length: 17 Bytes
Payload (VIN): "1HGBH41JXMN109186"
```

---

### **Payload Type = 0x0001**: Anfrage ohne EID oder VIN
- **Einsatzbereich**: Wird verwendet, wenn weder VIN noch EID bekannt sind.
- **Payload-Länge**: 0 Bytes.
- **Verwendung**: Ermöglicht die Broadcast-Erkennung von Fahrzeugen im Netzwerk.

```plaintext
Beispiel:
Payload Type: 0x0001
Payload Length: 0 Bytes
Payload: Keine
```

---

## Ablauf der Vehicle Identification Request

1. **Senden der Anfrage**:  
   Der Diagnosetester sendet eine Vehicle Identification Request an das Fahrzeug-Gateway, um Informationen über das Fahrzeug zu erhalten.

2. **Payload Type bestimmen**:  
   Der Payload Type wird abhängig davon ausgewählt, ob VIN, EID oder keine dieser Informationen vorliegen.

3. **Antwort des Gateways**:  
   Das Gateway verarbeitet die Anfrage und antwortet mit einer **Vehicle Identification Response**, die die angeforderten Informationen enthält.

---

## Anwendungsfälle

### 1. Fahrzeugerkennung in einem Netzwerk
- Wenn mehrere Fahrzeuge in einem Netzwerk vorhanden sind, kann der Tester die Vehicle Identification Request nutzen, um ein spezifisches Fahrzeug durch VIN oder EID zu identifizieren.

### 2. Initialisierung einer Diagnoseverbindung
- Vor der Durchführung einer Diagnose ist es notwendig, das Ziel-Fahrzeug zu identifizieren. Die Vehicle Identification Request stellt diesen Schritt sicher.

---

## Beispielnachrichten

### Vehicle Identification Request mit EID (Payload Type = 0x0002)
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x0002
Payload Length: 6 Bytes
Payload (EID): "00:16:81:00:62:E0"
```

### Vehicle Identification Request mit VIN (Payload Type = 0x0003)
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x0003
Payload Length: 17 Bytes
Payload (VIN): "1HGBH41JXMN109186"
```

### Vehicle Identification Request ohne Payload (Payload Type = 0x0001)
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x0001
Payload Length: 0 Bytes
Payload: Keine
```

---

## Relevante Codebeispiele

### Beispiel: Senden einer Vehicle Identification Request
```python
import socket

# Verbindung zu einem DoIP-Gateway
gateway_ip = "192.168.1.2"
gateway_port = 13400

# Vehicle Identification Request (Payload Type = 0x0003 mit VIN)
request = bytearray([
    0x02, 0xFD,             # Protokollversion und Inverse Version
    0x00, 0x03,             # Payload Type (VIN)
    0x00, 0x00, 0x00, 0x11, # Payload Länge (17 Bytes)
    0x31, 0x48, 0x47, 0x42, # VIN: "1HGBH41JXMN109186"
    0x48, 0x34, 0x31, 0x4A,
    0x58, 0x4D, 0x4E, 0x31,
    0x30, 0x39, 0x31, 0x38,
    0x36
])

# Nachricht senden
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, gateway_port))
    s.send(request)
    response = s.recv(1024)

print("Empfangene Antwort:", response.hex())
```

---

## Häufige Probleme und Lösungen

### Problem 1: Keine Antwort vom Gateway
- **Ursache**: Das Gateway ist nicht erreichbar oder die Anfrage ist falsch formatiert.
- **Lösung**: Überprüfen Sie die Netzwerkverbindung und die Struktur der Nachricht.

### Problem 2: Falscher Payload Type
- **Ursache**: Der Payload Type stimmt nicht mit der Payload überein.
- **Lösung**: Stellen Sie sicher, dass die Payload-Länge und der Payload-Inhalt mit dem angegebenen Payload Type übereinstimmen.

### Problem 3: Zeitüberschreitung
- **Ursache**: Das Gateway reagiert nicht rechtzeitig.
- **Lösung**: Erhöhen Sie den Timeout-Wert und prüfen Sie die Verbindung.

