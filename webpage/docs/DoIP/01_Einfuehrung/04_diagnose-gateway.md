# Diagnose-Gateway (Edge Nodes) im Fahrzeug

## Rolle des Diagnose-Gateways

Das Diagnose-Gateway, auch als Edge Node bezeichnet, ist ein zentraler Bestandteil der modernen Fahrzeugdiagnose und -wartung. Es fungiert als Schnittstelle zwischen den verschiedenen Steuergeräten im Fahrzeug und externen Diagnosetools. Diese Einführung bietet einen detaillierten Überblick über die Funktionsweise und technischen Aspekte des Diagnose-Gateways.

## Aktivierungslinie

Die Aktivierungslinie ist eine wesentliche Komponente, um das Ethernet-Interface des Diagnose-Gateways zu aktivieren. Diese Linie wird typischerweise über einen WWH-OBD-Stecker (World-Wide Harmonized On-Board Diagnostics) aktiviert. Im Normalzustand ist das Ethernet-Interface ausgeschaltet, und erst durch die Aktivierungslinie wird die Kommunikation zwischen dem externen Diagnosetool und dem internen Fahrzeugnetzwerk ermöglicht.

### Wichtige Punkte:

- **Aktivierung:** Erfolgt über einen spezifischen Stecker, wie den WWH-OBD-Stecker.
- **Normalzustand:** Ohne Aktivierung bleibt das Ethernet-Interface ausgeschaltet.

## Logische Adressen

Jedes Steuergerät und das Diagnosetool müssen eindeutige logische Adressen haben, um eine fehlerfreie Kommunikation im Netzwerk zu ermöglichen. Diese Adressen sorgen dafür, dass es keine Verwechslungen oder Kommunikationsprobleme zwischen den verschiedenen Komponenten im Netzwerk gibt.

### Wichtige Punkte:

- **Eindeutigkeit:** Jede logische Adresse muss einzigartig sein.
- **Zuweisung:** Die Adressen werden den Steuergeräten und dem Diagnosetool zugewiesen, um die richtige Kommunikation sicherzustellen.

## Kommunikation über UDP/IP oder TCP/IP

Die Kommunikation zwischen dem Diagnose-Gateway und den Steuergeräten erfolgt über die Netzwerkeprotokolle UDP/IP (User Datagram Protocol/Internet Protocol) oder TCP/IP (Transmission Control Protocol/Internet Protocol). Diese Protokolle arbeiten auf verschiedenen Ebenen des OSI-Modells (Open Systems Interconnection Model) und ermöglichen eine zuverlässige Datenübertragung.

### Wichtige Punkte:

- **Schicht 3 (Netzwerkschicht):** Verwendet IP-Adressen zur Identifikation der Geräte, beispielsweise `192.168.1.10`.
- **Schicht 4 (Transportschicht):** Nutzt Ports zur Unterscheidung von Kommunikationskanälen, wie beispielsweise Port `13400`.

## Verbindungen und Netzwerkschnittstellen

Das Diagnose-Gateway (GW) ist über das Fahrzeugnetzwerk mit verschiedenen Steuergeräten verbunden, darunter Türsteuergeräte (Door), Dachsteuergeräte (Roof), und Sitzsteuergeräte (Seat). Diese Steuergeräte kommunizieren miteinander über den CAN-Bus (Controller Area Network), während das Gateway die Schnittstelle zu externen Systemen über Ethernet bereitstellt.

### Wichtige Punkte:

- **Netzwerktopologie:** Das Schaubild zeigt die Verbindungen zwischen dem Diagnose-Gateway und den Steuergeräten.
- **Kommunikationsbus:** Die interne Kommunikation zwischen den Steuergeräten erfolgt über den CAN-Bus.
