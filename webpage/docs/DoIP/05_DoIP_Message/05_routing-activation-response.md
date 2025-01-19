# Routing Activation Response

Die **Routing Activation Response** ist eine wichtige Antwortnachricht im DoIP-Protokoll (Diagnostics over Internet Protocol). Sie wird vom Gateway an den Diagnosetester gesendet, um den Status der angeforderten Routing-Aktivierung zu bestätigen. Diese Nachricht zeigt an, ob die Aktivierung interner Fahrzeugnetzwerke erfolgreich war oder nicht.

---

## Nachrichtenstruktur

Die Routing Activation Response-Nachricht besteht aus folgenden Feldern:

| Feld                       | Länge       | Beschreibung                                                  |
|----------------------------|-------------|--------------------------------------------------------------|
| **Protocol Version**       | 1 Byte      | Version des verwendeten DoIP-Protokolls.                     |
| **Inverse Protocol Version** | 1 Byte    | Sicherheitsprüfung (Komplement der Protokollversion).         |
| **Payload Type**           | 2 Bytes     | Typ der Nachricht (`0x0006`).                                |
| **Payload Length**         | 4 Bytes     | Länge des Nutzdatenfeldes in Bytes.                          |
| **Logical Address of Tester** | 2 Bytes  | Logische Adresse des Diagnosetesters.                        |
| **Logical Address of DoIP entity** | 2 Bytes | Logische Adresse des angesprochenen DoIP-Moduls.              |
| **Routing Activation Response Code** | 1 Byte | Status der Routing-Aktivierung.                              |
| **Reserved by ISO 13400**  | 4 Bytes     | Reserviert für zukünftige Verwendungen (Standard: `0x00000000`). |
| **Reserved for OEM-specific use** | 4 Bytes | Optional, für herstellerspezifische Informationen.            |

---

## Beschreibung der Felder

### **Logical Address of Tester**
- **Länge**: 2 Bytes.  
- **Beschreibung**: Eindeutige logische Adresse des Diagnosetesters.  
- **Beispiel**: `0x0203` (Adresse des Testers).  

---

### **Logical Address of DoIP Entity**
- **Länge**: 2 Bytes.  
- **Beschreibung**: Logische Adresse des Gateways oder der spezifischen DoIP-Einheit im Fahrzeug.  
- **Beispiel**: `0x0201` (Adresse des Gateways).

---

### **Routing Activation Response Code**
- **Länge**: 1 Byte.  
- **Beschreibung**: Zeigt den Status der Routing-Aktivierung an.  
- **Mögliche Werte**:
  - `0x00`: Aktivierung erfolgreich.  
  - `0x01`: Aktivierung fehlgeschlagen (z. B. Sicherheitsprobleme).  
  - `0x02`: Unbekannter Activation Type.  

---

### **Reserved by ISO 13400**
- **Länge**: 4 Bytes.  
- **Beschreibung**: Reservierter Bereich für zukünftige Spezifikationen durch die ISO 13400.  
- **Standardwert**: `0x00000000`.

---

### **Reserved for OEM-specific use**
- **Länge**: 4 Bytes.  
- **Beschreibung**: Optionales Feld für OEM-spezifische Informationen.  
- **Beispiel**: Zusätzliche Statusinformationen oder herstellerspezifische Fehlercodes.

---

## Ablauf der Routing Activation Response

1. **Senden der Routing Activation Request**:  
   Der Diagnosetester initiiert eine Routing Activation Request-Nachricht.

2. **Verarbeitung durch das Gateway**:  
   Das Gateway verarbeitet die Anfrage, aktiviert die angeforderten Netzwerke und erstellt eine Routing Activation Response.

3. **Antwort an den Tester**:  
   Das Gateway sendet die Routing Activation Response zurück an den Tester, um den Status der Anfrage zu bestätigen.

---

## Beispielnachrichten

### Erfolgreiche Routing Activation Response
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x0006
Payload Length: 9 Bytes
Logical Address of Tester: 0x0203
Logical Address of DoIP entity: 0x0201
Routing Activation Response Code: 0x00 (Erfolg)
Reserved by ISO 13400: 0x00000000
Reserved for OEM-specific use: 0x00000000
```

### Fehlgeschlagene Routing Activation Response
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x0006
Payload Length: 9 Bytes
Logical Address of Tester: 0x0203
Logical Address of DoIP entity: 0x0201
Routing Activation Response Code: 0x01 (Fehler)
Reserved by ISO 13400: 0x00000000
Reserved for OEM-specific use: 0x00000000
```

---

## Relevante Codebeispiele

### Beispiel: Empfang einer Routing Activation Response
```python
import socket

# Verbindungsparameter
gateway_ip = "192.168.1.2"
gateway_port = 13400

# Verbindung herstellen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, gateway_port))
    
    # Nachricht senden (Routing Activation Request sollte zuvor gesendet werden)
    response = s.recv(1024)

# Antwort auswerten
if response:
    protocol_version = response[0]
    inverse_protocol_version = response[1]
    payload_type = int.from_bytes(response[2:4], "big")
    payload_length = int.from_bytes(response[4:8], "big")
    tester_address = int.from_bytes(response[8:10], "big")
    doip_entity_address = int.from_bytes(response[10:12], "big")
    response_code = response[12]

    print(f"Protokoll-Version: {protocol_version}")
    print(f"Payload-Typ: {payload_type}")
    print(f"Tester-Adresse: 0x{tester_address:04X}")
    print(f"DoIP-Entität-Adresse: 0x{doip_entity_address:04X}")
    print(f"Antwortcode: {response_code}")
else:
    print("Keine Antwort erhalten.")
```

---

## Häufige Probleme und Lösungen

### Problem 1: Keine Antwort vom Gateway
- **Ursache**: Die Routing Activation Request wurde nicht korrekt verarbeitet.  
- **Lösung**: Überprüfen Sie die Struktur der Request-Nachricht und stellen Sie sicher, dass die Netzwerkverbindung besteht.

### Problem 2: Aktivierung fehlgeschlagen
- **Ursache**: Unbekannter Activation Type oder Sicherheitsprobleme.  
- **Lösung**: Stellen Sie sicher, dass der Activation Type unterstützt wird und die Sicherheitsmechanismen korrekt konfiguriert sind.

### Problem 3: Unerwarteter Response Code
- **Ursache**: Kommunikationsfehler oder falsche Einstellungen.  
- **Lösung**: Prüfen Sie die Fehlermeldung im Response Code und debuggen Sie die Anfrage.

