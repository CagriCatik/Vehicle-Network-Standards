# DoIP Fahrzeugentdeckung

Die Diagnose über Internetprotokoll (DoIP) ist eine wesentliche Technologie in der modernen Fahrzeugdiagnose, die Ethernet als Kommunikationsmedium nutzt. DoIP ermöglicht eine schnellere und effizientere Kommunikation zwischen Diagnosetestern und den Steuergeräten im Fahrzeug. In diesem Leitfaden werden die Konzepte der **Fahrzeugankündigung** (Vehicle Announcement) und **Fahrzeugidentifikation** (Vehicle Identification) detailliert erläutert.

## Fahrzeugankündigung (Vehicle Announcement)

### Beschreibung

Die Fahrzeugankündigung ist der erste Schritt im DoIP-Kommunikationsprozess. Dabei sendet das Gateway im Fahrzeug dreimal eine Fahrzeugankündigungsnachricht als Broadcast über UDP (User Datagram Protocol). Diese Nachricht enthält wichtige Identifikationsinformationen, die für den Diagnoseprozess benötigt werden.

### Inhalte der Fahrzeugankündigung

- **VIN (Vehicle Identification Number):** Die Fahrzeug-Identifikationsnummer, die eine eindeutige Identifikation des Fahrzeugs ermöglicht.
- **EID (Entity Identification):** Eine eindeutige Kennung des Gateways oder des Steuergeräts innerhalb des Fahrzeugs.
- **Logische Adresse des Gateways:** Die Adresse, die das Gateway im Fahrzeugnetzwerk identifiziert.

Die Fahrzeugankündigung wird dreimal gesendet, um sicherzustellen, dass die Nachricht auch bei möglichen Übertragungsfehlern oder Paketverlusten empfangen wird. Dies ist besonders wichtig in Umgebungen mit hohem Netzwerkverkehr, wo Datenpakete verloren gehen können. Die Verwendung von UDP als Transportprotokoll ermöglicht eine schnelle und effiziente Übertragung, da es keinen Overhead für Verbindungsaufbau und -abbau wie TCP erfordert.

## Fahrzeugidentifikation (Vehicle Identification)

### Beschreibung

Im zweiten Schritt des Prozesses kann der Diagnosetester eine Anfrage zur Fahrzeugidentifikation als Broadcast über UDP senden. Das Gateway antwortet auf diese Anfrage mit einer Fahrzeugidentifikationsantwort, die die gleichen Informationen wie die Fahrzeugankündigung enthält.

### Prozess der Fahrzeugidentifikation

1. **Anfrage vom Diagnosetester:** Der Diagnosetester sendet eine Broadcast-Anfrage zur Fahrzeugidentifikation.
2. **Antwort vom Gateway:** Das Gateway antwortet mit einer Fahrzeugidentifikationsantwort, die die VIN, EID und die logische Adresse des Gateways enthält.

Die Möglichkeit, dass der Diagnosetester aktiv eine Anfrage zur Fahrzeugidentifikation senden kann, erhöht die Flexibilität des Diagnoseprozesses. Diese Funktion ist nützlich, wenn das Gateway aus irgendeinem Grund keine Fahrzeugankündigung gesendet hat oder wenn die ursprüngliche Nachricht verloren ging. Die Broadcast-Kommunikation stellt sicher, dass alle relevanten Geräte im Netzwerk die Anfrage empfangen, was besonders in komplexen Fahrzeugnetzwerken mit mehreren Steuergeräten von Vorteil ist.
