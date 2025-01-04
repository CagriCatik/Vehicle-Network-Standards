# Kommunikation und Adressierung

## Botschafts-Adressierung

Im CAN-Netzwerk (Controller Area Network) wird die Kommunikation durch inhaltsbezogene Adressierung organisiert. Anders als bei vielen anderen Netzwerken, werden nicht die CAN-Knoten selbst, sondern die Daten- und Remote-Frames mit einer Kennung (Identifier - ID) versehen. Diese IDs bestimmen, welche Art von Nachricht gesendet wird und wer sie empfangen soll. Da alle CAN-Botschaften jedem Knoten im Netzwerk zur Verfügung stehen (Broadcasting), muss jeder Empfänger selbstständig die relevanten Botschaften auswählen und verarbeiten. Dies erfordert eine empfängerseitige Filterung der empfangenen Nachrichten, bekannt als Akzeptanzfilterung.

## Standard und Extended Format

Der CAN-Bus bietet zwei verschiedene Formate für Nachrichten: das Standard-Format und das Extended-Format. Diese Formate unterscheiden sich primär in der Länge des Identifiers:

1. **Standard-Format**:
   - Der Identifier (ID) umfasst 11 Bit.

2. **Extended-Format**:
   - Der Identifier umfasst 29 Bit.
   - Der 29-Bit-Identifier setzt sich aus einem 11-Bit-Basis-ID und einem 18-Bit-Extended-ID zusammen.
   - Zwischen Basis-ID und Extended-ID befinden sich die beiden Bits IDE (Identifier Extension) und SRR (Substitute Remote Request).

### Identifier und Kontrollbits

Im Standard-Format wird der ID mit 11 Bit übertragen. Dies bedeutet, dass bis zu 2048 verschiedene Nachrichten-IDs möglich sind. Im Extended-Format wird der ID auf 29 Bit erweitert, was eine viel größere Vielfalt an Nachrichten-IDs ermöglicht, nämlich bis zu 536.870.912 verschiedene IDs.

- **IDE-Bit**:
  - Ein dominantes IDE-Bit (0) kennzeichnet eine Nachricht im Standard-Format.
  - Ein rezessives IDE-Bit (1) kennzeichnet eine Nachricht im Extended-Format.
  
- **SRR-Bit**:
  - Im Extended-Format ersetzt das SRR-Bit das RTR-Bit (Remote Transmission Request) des Standard-Formats. Das SRR-Bit wird immer rezessiv übertragen.
  
- **Control Field (r0 und r1)**:
  - Im Extended-Format haben die beiden ersten Bits des Control-Fields keine Bedeutung und werden immer dominant übertragen.

## Bedeutung der Identifier und Flexibilität der Adressierung

Die inhaltsbezogene Adressierung im CAN-Bus ist besonders flexibel und effizient für die Kommunikation in Fahrzeugnetzwerken. Jeder Knoten kann so konfiguriert werden, dass er nur die relevanten Nachrichten empfängt und verarbeitet. Dies reduziert die Belastung des Systems und verbessert die Gesamtleistung des Netzwerks.

Durch die Erweiterung auf 29-Bit-Identifiers im Extended-Format wird die Skalierbarkeit des Systems erheblich erhöht, was besonders in modernen Fahrzeugen mit einer Vielzahl von Steuergeräten und Sensoren von Vorteil ist. Diese Flexibilität ist jedoch nur durch eine effektive Akzeptanzfilterung auf Empfängerseite gewährleistet.

## Schlussfolgerung

Die inhaltsbezogene Adressierung im CAN-Bus, kombiniert mit den beiden verfügbaren Botschaftsformaten, bietet eine hochflexible und skalierbare Kommunikationslösung für den Automobilbereich. Das Standard-Format mit 11-Bit-Identifiers ermöglicht eine einfache und schnelle Nachrichtenübertragung, während das Extended-Format mit 29-Bit-Identifiers eine erweiterte Adressierbarkeit für komplexere Systeme bietet.

Durch die klare Trennung und Definition von Kontrollbits und die effiziente Nutzung von Filtermechanismen können CAN-Netzwerke auch in sehr anspruchsvollen Anwendungen zuverlässig und performant arbeiten.
