# Fehlererkennung und -behandlung im CAN-Netzwerk

Das Controller Area Network (CAN) ist ein weit verbreitetes serielles Kommunikationsprotokoll, das in Automobilen und vielen anderen Anwendungen eingesetzt wird. Eine der größten Herausforderungen bei der seriellen Kommunikation in Kraftfahrzeugen besteht darin, eine äußerst hohe Übertragungssicherheit zu garantieren. Ein zentraler Mechanismus zur Fehlererkennung im CAN-Netzwerk ist das CRC-Verfahren (Cyclic Redundancy Check). Dieses Tutorial bietet eine detaillierte und wissenschaftlich fundierte Beschreibung des CRC-Verfahrens und der Acknowledgement-Mechanismen im CAN-Protokoll gemäß der ISO 11898-1 Norm.

## Cyclic Redundancy Check (CRC)

### Funktionsweise des CRC-Verfahrens

Das CRC-Verfahren dient zur Erkennung von Übertragungsfehlern in Datenpaketen. Hierbei wird eine CRC-Sequenz auf Basis der zu übertragenden Bits berechnet. Diese Bits umfassen den Start-of-Frame (SOF) bis einschließlich des Data Fields. Zur Berechnung der CRC-Sequenz wird ein Generatorpolynom G(x) verwendet, das in der ISO 11898-1 Norm definiert ist.

Die CRC-Sequenz wird wie folgt berechnet:

1. **Polynomdarstellung der Datenbits:** Die zu übertragenden Bits werden als Polynom interpretiert.
2. **Division durch das Generatorpolynom:** Dieses Datenpolynom wird durch das Generatorpolynom G(x) dividiert. Der Rest dieser Division stellt die CRC-Sequenz dar.
3. **Anfügen der CRC-Sequenz:** Die CRC-Sequenz wird an die ursprünglichen Datenbits angehängt und zusammen mit diesen übertragen.

### Fehlererkennung durch den Empfänger

Der Empfänger erhält das Gesamtpolynom (Originaldaten + CRC-Sequenz) und führt erneut eine Division durch das gleiche Generatorpolynom G(x) durch. Ergibt diese Division einen Rest von Null, so ist die Übertragung fehlerfrei. Andernfalls wurde ein Übertragungsfehler erkannt.

## Acknowledgement (ACK)

### Quittierungsmechanismus

Nach der Berechnung und Überprüfung der CRC-Sequenz durch den Empfänger erfolgt die Quittierung der empfangenen Nachricht im Acknowledgement-Slot (ACK-Slot). Jeder Empfänger steuert das Acknowledgement unabhängig von der Akzeptanzfilterung:

- **Dominanter Pegel:** Ein dominanter Pegel im ACK-Slot signalisiert eine positive Quittung (korrekte Datenübertragung).
- **Rezessiver Pegel:** Ein rezessiver Pegel im ACK-Slot signalisiert eine negative Quittung (fehlerhafte Datenübertragung).

### ACK-Delimiter

Der ACK-Delimiter folgt unmittelbar auf den ACK-Slot und wird immer rezessiv übertragen. Dieser Mechanismus stellt sicher, dass der ACK-Slot eindeutig interpretierbar ist.

### Knotenneutrales positives Acknowledgement

Da der Sender sowohl den ACK-Slot als auch den ACK-Delimiter rezessiv überträgt, reicht eine einzige positive Quittung (dominanter Pegel) eines beliebigen Empfängers aus, um die Korrektheit der Botschaft zu bestätigen. Dies wird als knotenneutrales positives Acknowledgement bezeichnet, da es unabhängig von der Anzahl der Empfänger funktioniert.

## Fehlerbehandlung: ACK-Fehler und Error Flag

### ACK-Fehler

Ein ACK-Fehler tritt auf, wenn keine einzige positive Quittung von den Empfängern erfolgt. Das bedeutet, dass der rezessive Pegel im ACK-Slot nicht überschrieben wird. Ein ACK-Fehler kann auf folgende Ursachen hinweisen:

- **Fehlerhafte Übertragung durch den Sender:** Der Sender hat möglicherweise einen Fehler bei der Übertragung der Nachricht verursacht.
- **Nicht vorhandene Empfänger:** Es gibt keine Empfänger, die die Nachricht erfolgreich empfangen und positiv quittieren konnten.

### Error Flag

Wenn ein ACK-Fehler erkannt wird, bricht der Sender die laufende Nachrichtenübertragung sofort ab und sendet ein Error Flag. Dieses Error Flag signalisiert allen Knoten im Netzwerk, dass ein Fehler aufgetreten ist und stellt sicher, dass keine fehlerhaften Daten im Netzwerk verbleiben.

## Schlussbemerkungen

Die beschriebenen Mechanismen zur Fehlererkennung und -behandlung im CAN-Netzwerk sind von zentraler Bedeutung, um eine hohe Übertragungssicherheit zu gewährleisten. Das CRC-Verfahren ermöglicht eine zuverlässige Erkennung von Übertragungsfehlern, während der Acknowledgement-Mechanismus sicherstellt, dass nur korrekte Nachrichten im Netzwerk akzeptiert werden. Bei Erkennung eines Fehlers erfolgt sofort eine Fehlerbehandlung, um die Datenkonsistenz im gesamten Netzwerk zu wahren. Diese Mechanismen tragen maßgeblich zur Robustheit und Zuverlässigkeit des CAN-Netzwerks bei.
