# DoIP Fahrzeugerkennung durch den Diagnosetester

## Einführung

Die DoIP (Diagnostics over Internet Protocol) Fahrzeugerkennung ermöglicht es einem Diagnosetester, verfügbare Fahrzeuge im Netzwerk zu identifizieren. Der Prozess besteht aus zwei Hauptschritten: der **Vehicle Identification Request** und der **Vehicle Identification Response**. In diesem Tutorial werden diese Schritte detailliert erklärt und wichtige technische Details sowie mögliche Unstimmigkeiten kritisch beleuchtet.

## 1. Fahrzeuganfrage durch den Diagnosetester

### Schritt 1: Vehicle Identification Request

Der Diagnosetester startet den Prozess, indem er eine **Vehicle Identification Request** (Fahrzeug-Identifikationsanfrage) als Broadcast-Nachricht an alle im Netzwerk befindlichen Fahrzeuge sendet. Dadurch wird sichergestellt, dass alle potenziellen Fahrzeuge im Netzwerk die Anfrage empfangen. Die technischen Details dieses Schrittes sind wie folgt:

- **Src. MAC:** 00:16:81:00:62:E0
  - Die Quell-MAC-Adresse des Testers.
- **Dst. MAC:** FF:FF:FF:FF:FF:FF
  - Die Broadcast-MAC-Adresse, um die Anfrage an alle Netzwerkgeräte zu senden.
- **Src. IP:** 192.168.1.1
  - Die Quell-IP-Adresse des Testers.
- **Dst. IP:** 192.168.1.255
  - Broadcast-IP-Adresse des Subnetzes.
- **Src. Port:** 52306 (zufällig)
  - Ein zufällig gewählter Quellport des Testers.
- **Dst. Port:** 13400 (UDP_DISCOVERY)
  - Der Standardport für DoIP-Entdeckungen.

Nach dem Senden der Anfrage wartet der Diagnosetester auf Antworten der im Netzwerk befindlichen Fahrzeuge.

### Schritt 2: DoIP-Pufferung

In diesem Schritt speichert der Diagnosetester die empfangenen DoIP-Informationen für die weitere Verarbeitung und um eine stabile Kommunikation mit den Fahrzeugen sicherzustellen.

## 2. Fahrzeugantwort vom Gateway (Vehicle GW)

### Schritt 2: Vehicle Identification Response

Nach dem Erhalt der Vehicle Identification Request antwortet das Gateway (DoIP edge node) mit einer **Vehicle Identification Response**. Diese Nachricht enthält spezifische Fahrzeuginformationen, die für die weitere Diagnose verwendet werden. Die technischen Details dieser Antwort sind wie folgt:

- **Src. MAC:** 00:A4:DF:1E:08:00
  - Die Quell-MAC-Adresse des Fahrzeuggateways.
- **Dst. MAC:** 00:16:81:00:62:E0
  - Die Ziel-MAC-Adresse des Testers.
- **Src. IP:** 192.168.1.2
  - Die Quell-IP-Adresse des Gateways.
- **Dst. IP:** 192.168.1.1
  - Die Ziel-IP-Adresse des Testers.
- **Src. Port:** 61824 (zufällig)
  - Ein zufällig gewählter Quellport des Gateways.
- **Dst. Port:** 52306
  - Der Quellport des Testers, der in der ursprünglichen Anfrage verwendet wurde.

Die Antwort enthält außerdem spezifische Fahrzeuginformationen:

- **VIN (Vehicle Identification Number):** VECT0RVEH1CLE8100
  - Die eindeutige Fahrzeugidentifikationsnummer.
- **EID (Entity Identifier):** 00:A4:DF:1E:08:00
  - Die eindeutige Identifikationsnummer des Gateways.
- **GID (Group Identifier):** FF:FF:FF:FF:FF:FF (leer)
  - Die Gruppenidentifikationsnummer, die in diesem Fall leer ist.
- **Logische Adresse:** 0x201 (GW)
  - Die logische Adresse des Gateways im DoIP-Netzwerk.

## Kritische Bewertung

Die Abbildung beschreibt den Prozess der Fahrzeugerkennung korrekt, dennoch gibt es einige Punkte, die genauer betrachtet werden sollten:

### 1. MAC- und IP-Adressen

Die Verwendung von Broadcast-MAC- und IP-Adressen ist korrekt dargestellt. In realen Netzwerken müssen jedoch die spezifischen MAC- und IP-Adressen für jedes Gerät korrekt konfiguriert sein, um sicherzustellen, dass keine Konflikte oder Kommunikationsprobleme auftreten. Es wäre hilfreich, auf mögliche IP-Konflikte in einem realen Netzwerk hinzuweisen.

### 2. Ports

Die zufällige Wahl der Quellports (wie 52306 und 61824) ist üblich. Allerdings sollten Sicherheitsaspekte berücksichtigt werden, um Port-Scanning-Angriffe oder ähnliche Bedrohungen zu vermeiden. Zudem ist es wichtig, auf die korrekte Handhabung der Ports durch den Diagnosetester und das Gateway zu achten.

### 3. DoIP-Protokoll

Das DoIP-Protokoll ist speziell für die Fahrzeugdiagnose entwickelt worden und bietet eine effiziente Möglichkeit, Fahrzeuge im Netzwerk zu identifizieren und zu diagnostizieren. Es ist jedoch wichtig, die spezifischen Implementierungsdetails des Herstellers zu berücksichtigen, da diese je nach Fahrzeugtyp oder Netzwerkarchitektur variieren können. Erweiterte Sicherheitsmaßnahmen oder Anpassungen für spezifische Netzwerktopologien könnten notwendig sein.
