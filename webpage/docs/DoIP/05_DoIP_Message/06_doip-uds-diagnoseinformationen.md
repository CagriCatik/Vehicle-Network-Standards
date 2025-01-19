# DoIP mit UDS-Diagnoseinformation

Das DoIP-Protokoll (Diagnostics over Internet Protocol) ermöglicht die Übertragung von UDS-Diagnoseinformationen (Unified Diagnostic Services) über IP-basierte Netzwerke. Diese Kommunikation erfolgt zwischen einem Diagnosetester und einem Zielgerät (ECU), indem UDS-Diagnosebotschaften in die DoIP-Nachrichten eingebettet werden.

## Nachrichtenstruktur

Die DoIP-Nachricht mit UDS-Diagnoseinformation besteht aus folgenden Feldern:

| Feld                       | Länge       | Beschreibung                                                  |
|----------------------------|-------------|--------------------------------------------------------------|
| **Protocol Version**       | 1 Byte      | Version des verwendeten DoIP-Protokolls.                     |
| **Inverse Protocol Version** | 1 Byte    | Sicherheitsprüfung (Komplement der Protokollversion).         |
| **Payload Type**           | 2 Bytes     | Typ der Nachricht (z. B. `0x8001` für Diagnoseanfrage).       |
| **Payload Length**         | 4 Bytes     | Länge des Nutzdatenfeldes in Bytes.                          |
| **Logical Source Address** | 2 Bytes     | Logische Adresse des Diagnosetesters.                        |
| **Logical Target Address** | 2 Bytes     | Logische Adresse des Zielgeräts (ECU).                       |
| **User Data**              | Variabel    | Enthält die UDS-Diagnoseinformationen, wie SID und DID.       |


## Beschreibung der Felder

### **Protocol Version**
- **Länge**: 1 Byte.  
- **Beschreibung**: Gibt die Version des DoIP-Protokolls an.  
- **Beispiel**: `0x02` (Version 2).

### **Inverse Protocol Version**
- **Länge**: 1 Byte.  
- **Beschreibung**: Sicherheitsprüfung, die die Inverse der Protokollversion darstellt.  
- **Beispiel**: `0xFD` (Komplement von `0x02`).


### **Payload Type**
- **Länge**: 2 Bytes.  
- **Beschreibung**: Bestimmt die Art der Diagnoseinformation.  
- **Beispiele**:
  - `0x8001`: Diagnoseanfrage (Diagnostic Request).  
  - `0x8002`: Diagnoseantwort (Diagnostic Response).

### **Payload Length**
- **Länge**: 4 Bytes.  
- **Beschreibung**: Gibt die Länge des Nutzdatenfeldes (Payload) in Bytes an.  
- **Beispiel**: `0x00000008` (8 Bytes).

### **Logical Source Address**
- **Länge**: 2 Bytes.  
- **Beschreibung**: Die logische Adresse des Diagnosetesters, der die Anfrage sendet.  
- **Beispiel**: `0x0203`.

### **Logical Target Address**
- **Länge**: 2 Bytes.  
- **Beschreibung**: Die logische Adresse des Zielgeräts (ECU), an das die Diagnoseanfrage gerichtet ist.  
- **Beispiel**: `0x0201`.

### **User Data**
- **Länge**: Variabel (abhängig vom UDS-Dienst).  
- **Beschreibung**: Enthält die UDS-Diagnoseinformationen, z. B.:
  - **SID (Service Identifier)**: Gibt den UDS-Dienst an, z. B. `0x22` für `ReadDataByIdentifier`.
  - **DID (Data Identifier)**: Gibt die angeforderten Daten an, z. B. `0x1234` für spezifische Fahrzeugdaten.

## Beispiel für eine UDS-Diagnosebotschaft

### UDS-Dienst: `ReadDataByIdentifier`
Eine Diagnoseanfrage, die Sensordaten oder Fahrzeuginformationen abruft.

| Feld                       | Beispielwert | Beschreibung                                |
|----------------------------|--------------|--------------------------------------------|
| **SID (Service Identifier)** | `0x22`       | UDS-Dienst: `ReadDataByIdentifier`.         |
| **DID (Data Identifier)**   | `0x1234`     | Angeforderte Daten, z. B. Fahrzeugstatus.   |


## Ablauf der DoIP-Nachricht mit UDS-Diagnoseinformation

1. **Erstellen der Diagnoseanfrage**:  
   Der Diagnosetester formuliert eine UDS-Diagnoseanfrage (z. B. `ReadDataByIdentifier`) und fügt diese in das User Data-Feld der DoIP-Nachricht ein.

2. **Senden der Nachricht**:  
   Die DoIP-Nachricht wird über das Netzwerk an das Gateway oder die Ziel-ECU gesendet.

3. **Verarbeitung durch die ECU**:  
   Die ECU verarbeitet die Diagnoseanfrage und generiert eine entsprechende Antwort (z. B. angeforderte Sensordaten).

4. **Antwort an den Tester**:  
   Die Diagnoseantwort wird vom Gateway zurück an den Diagnosetester gesendet.

## Beispielnachrichten

### Diagnoseanfrage: `ReadDataByIdentifier`
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x8001
Payload Length: 8 Bytes
Logical Source Address: 0x0203
Logical Target Address: 0x0201
User Data: 0x22 0x12 0x34
```

### Diagnoseantwort: Sensordaten
```plaintext
Protocol Version: 0x02
Inverse Protocol Version: 0xFD
Payload Type: 0x8002
Payload Length: 8 Bytes
Logical Source Address: 0x0201
Logical Target Address: 0x0203
User Data: 0x62 0x12 0x34 0x56 0x78
```

## Relevante Codebeispiele

### Beispiel: Senden einer Diagnoseanfrage
```python
import socket

# Verbindungsparameter
gateway_ip = "192.168.1.2"
gateway_port = 13400

# DoIP-Nachricht erstellen
request = bytearray([
    0x02, 0xFD,             # Protokollversion und Inverse Version
    0x80, 0x01,             # Payload Type (Diagnoseanfrage)
    0x00, 0x00, 0x00, 0x08, # Payload Länge (8 Bytes)
    0x02, 0x03,             # Logical Source Address (Diagnosetester)
    0x02, 0x01,             # Logical Target Address (Ziel-ECU)
    0x22, 0x12, 0x34        # UDS-Daten: SID (0x22) und DID (0x1234)
])

# Nachricht senden und Antwort empfangen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((gateway_ip, gateway_port))
    s.send(request)
    response = s.recv(1024)

print("Empfangene Antwort:", response.hex())
```

## Häufige Probleme und Lösungen

### Problem 1: Keine Antwort von der ECU
- **Ursache**: Die Zieladresse ist falsch oder die ECU unterstützt den angeforderten UDS-Dienst nicht.  
- **Lösung**: Überprüfen Sie die logische Zieladresse und den verwendeten UDS-Dienst.

### Problem 2: Falscher Payload Type
- **Ursache**: Der Payload Type stimmt nicht mit der Art der Nachricht überein.  
- **Lösung**: Stellen Sie sicher, dass der Payload Type korrekt definiert ist (z. B. `0x8001` für Anfragen).

### Problem 3: Zeitüberschreitung
- **Ursache**: Die ECU reagiert nicht rechtzeitig.  
- **Lösung**: Erhöhen Sie den Timeout-Wert oder überprüfen Sie die ECU auf Fehler.