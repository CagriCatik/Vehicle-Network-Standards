# Fahrzeugankündigung im DoIP-Prozess

## Beschreibung des Prozesses

### Fahrzeugankündigung (Vehicle Announcement)

Sobald einem Fahrzeuggateway (DoIP edge node) eine IP-Adresse zugewiesen wurde, sendet das Gateway dreimal eine Fahrzeugankündigung (Vehicle Announcement) als Broadcast im Netzwerk. Diese Ankündigungen dienen dazu, das Fahrzeug im Netzwerk bekannt zu machen, sodass ein Diagnosetester es erkennen und mit ihm kommunizieren kann.

### Beispiel einer Fahrzeugankündigung

- **Src. MAC:** 00:A4:DF:1E:08:00
- **Dst. MAC:** FF:FF:FF:FF:FF:FF (Broadcast)
- **Src. IP:** 192.168.1.2
- **Dst. IP:** 192.168.1.255 (Broadcast)
- **Src. Port:** 24777 (zufällig)
- **Dst. Port:** 13400 (UDP_DISCOVERY)
- **VIN:** VECTORVEH1CLE8100
- **EID:** 00:A4:DF:1E:08:00
- **GID:** FF:FF:FF:FF:FF:FF (leer)
- **Logische Adresse:** 0x201 (GW)

### Analyse der Angaben

#### MAC-Adressen
- **Quell-MAC-Adresse (Src. MAC):** Dies ist die physische Adresse des Fahrzeuggateways. Sie identifiziert das Gateway eindeutig im Netzwerk.
- **Ziel-MAC-Adresse (Dst. MAC):** Diese ist als Broadcast-Adresse gesetzt (FF:FF:FF:FF:FF:FF), was bedeutet, dass alle Geräte im Netzwerk diese Nachricht empfangen können.

#### IP-Adressen
- **Quell-IP-Adresse (Src. IP):** Dies ist die IP-Adresse, die dem Fahrzeuggateway zugewiesen wurde, und wird für die Kommunikation mit anderen Geräten im Netzwerk genutzt.
- **Ziel-IP-Adresse (Dst. IP):** Auch die IP-Adresse ist als Broadcast-Adresse (192.168.1.255) gesetzt, um sicherzustellen, dass alle Geräte im Netzwerk die Nachricht empfangen.

#### Ports
- **Quellport (Src. Port):** Dieser Port wird zufällig gewählt und dient zur Identifikation der Sitzung.
- **Zielport (Dst. Port):** Der Zielport 13400 ist standardmäßig für UDP_DISCOVERY reserviert und wird in DoIP-Netzwerken häufig verwendet, um die Fahrzeugerkennung zu ermöglichen.

#### VIN (Vehicle Identification Number)
- Die **VIN** ist die eindeutige Fahrzeugidentifikationsnummer, die in der Ankündigung enthalten ist, um das Fahrzeug zu identifizieren.

#### EID (Entity Identifier)
- Der **EID** ist eine eindeutige Kennung des Fahrzeuggateways, die das Gateway im Netzwerk identifiziert.

#### GID (Group Identifier)
- Der **GID** ist in diesem Beispiel leer (FF:FF:FF:FF:FF:FF), was darauf hindeutet, dass keine Gruppenzuordnung vorgenommen wurde. In anderen Szenarien könnte der GID zur Organisation mehrerer Fahrzeuge oder Gateways verwendet werden.

#### Logische Adresse
- Die **logische Adresse** 0x201 identifiziert das Fahrzeuggateway im DoIP-Netzwerk. Diese Adresse ist innerhalb des Netzwerks einzigartig und wird verwendet, um gezielte Kommunikation zu ermöglichen.

## DoIP-Pufferung

Nach der erfolgreichen Fahrzeugankündigung speichert der Diagnosetester die DoIP-Informationen. Diese Informationen beinhalten die erhaltenen MAC- und IP-Adressen sowie die zugehörigen Ports und Identifikatoren. Dies gewährleistet eine stabile und konsistente Kommunikation zwischen dem Tester und dem Fahrzeug während der Diagnose.

## Kritische Analyse

Die bereitgestellten Informationen sind weitgehend korrekt, jedoch gibt es einige Punkte, die näher erläutert werden sollten:

### MAC-Adresse
- Die Verwendung einer Broadcast-MAC-Adresse (FF:FF:FF:FF:FF:FF) sollte detaillierter erklärt werden, insbesondere im Hinblick darauf, wie sie sicherstellt, dass alle Geräte im Netzwerk die Ankündigung empfangen können. Die Rolle der Broadcast-Adresse in Netzwerken könnte präziser dargestellt werden.

### Ports
- Der Zielport 13400 ist standardmäßig für UDP_DISCOVERY reserviert. Es sollte jedoch darauf hingewiesen werden, dass dieser Port konfigurierbar ist und je nach Netzwerkumgebung angepasst werden kann.

### GID (Group Identifier)
- Der GID ist in diesem Beispiel leer. Es wäre hilfreich, ein Szenario zu beschreiben, in dem der GID nicht leer ist und wie dies die Kommunikation im Netzwerk beeinflusst. Der GID könnte verwendet werden, um Gruppen von Fahrzeugen oder Gateways zu identifizieren, was in komplexeren Netzwerken nützlich sein kann.
