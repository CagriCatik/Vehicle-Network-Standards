# Diagnosetester im Fahrzeug

## Beschreibung der Rolle

Der Diagnosetester spielt eine zentrale Rolle in der Fahrzeugdiagnose und -wartung. Er wird verwendet, um die Steuergeräte (ECUs) im Fahrzeug zu überwachen, Fehler zu diagnostizieren und Kalibrierungen durchzuführen. Damit der Diagnosetester effektiv arbeiten kann, ist es entscheidend, dass er über eine Vielzahl von Funktionen und Informationen verfügt, die auf die jeweiligen Steuergeräte abgestimmt sind.

## Beschreibungsdateien

### CDD, ODX, etc.

Eine wesentliche Voraussetzung für den Einsatz eines Diagnosetesters ist die Verfügbarkeit von Beschreibungsdateien. Diese Dateien enthalten die nötigen Informationen über die Steuergeräte im Fahrzeug und die dazugehörigen Kommunikationsprotokolle. Zu den häufig verwendeten Dateiformaten gehören:

- **CDD (CANdela Diagnostic Description):**
  - Ein standardisiertes Format zur Beschreibung der Diagnosedaten und Funktionen von Steuergeräten.
  
- **ODX (Open Diagnostic Data Exchange):**
  - Ein XML-basiertes Format, das umfassende Informationen zu den Diagnosedaten, Fehlercodes und Funktionen der Steuergeräte bereitstellt.

Der Diagnosetester benötigt für jedes Steuergerät eine passende Beschreibungsdatei, um die korrekten Diagnosefunktionen durchführen zu können.

## Logische Adresse

Jedes Steuergerät und der Diagnosetester benötigen eine eindeutige logische Adresse, um miteinander im Netzwerk kommunizieren zu können. Diese logische Adresse gewährleistet, dass der Tester gezielt mit einem bestimmten Steuergerät interagieren kann, ohne dass es zu Adressierungsfehlern oder Verwechslungen kommt.

## Kommunikation über UDP/IP oder TCP/IP

Die Kommunikation zwischen dem Diagnosetester und den Steuergeräten erfolgt in der Regel über Netzwerke, die auf den Protokollen UDP/IP oder TCP/IP basieren, häufig unter Nutzung von Ethernet. Dabei spielen insbesondere zwei Protokollschichten eine wichtige Rolle:

- **Schicht 3: IP-Adressen**
  - Jede Komponente im Netzwerk erhält eine eindeutige IP-Adresse, beispielsweise `192.168.1.10`. Diese Adressen ermöglichen es, die Geräte im Netzwerk eindeutig zu identifizieren und zu adressieren.

- **Schicht 4: UDP/TCP-Ports**
  - Ports werden verwendet, um verschiedene Kommunikationskanäle auf derselben IP-Adresse zu unterscheiden. Ein Beispiel für einen Port wäre `13400`. Durch die Verwendung unterschiedlicher Ports kann ein Gerät mehrere Dienste parallel betreiben, ohne dass es zu Konflikten kommt.