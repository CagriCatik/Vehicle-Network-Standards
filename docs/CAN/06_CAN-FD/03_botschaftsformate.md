# Botschaftsformate

## Rahmenformate in CAN FD

CAN FD unterstützt, ähnlich wie das klassische CAN-Protokoll, zwei Arten von Datenrahmenformaten: Standard Frames und Extended Frames. Diese Formate sind entscheidend, um die Kompatibilität mit bestehenden Automobilnetzwerkprotokollen zu gewährleisten.

1. **Standard Rahmenformat (11-Bit-Identifier)**:
   - Das Standard Rahmenformat in CAN FD verwendet einen 11-Bit-Identifier, ähnlich wie das klassische CAN-Protokoll. Dieser kürzere Identifier wird typischerweise in Anwendungen verwendet, bei denen eine kleinere Anzahl von eindeutigen Identifikatoren ausreicht, was einen schnelleren Arbitrierungsprozess ermöglicht.

2. **Erweitertes Rahmenformat (29-Bit-Identifier)**:
   - Das erweiterte Rahmenformat verwendet einen 29-Bit-Identifier, der eine wesentlich größere Anzahl eindeutiger Identifikatoren zulässt. Dies ist in komplexen Systemen von entscheidender Bedeutung, in denen zahlreiche Geräte eindeutig kommunizieren müssen. Das erweiterte Identifier-Format stellt sicher, dass Protokolle wie CANopen und SAE J1939 weiterhin effektiv mit CAN FD funktionieren, indem sie ihren größeren Bereich von Identifikatoren aufnehmen.

Das System mit zwei Rahmenformaten stellt sicher, dass CAN FD die Rückwärtskompatibilität mit bestehenden Systemen beibehält und gleichzeitig die erweiterten Fähigkeiten bietet, die moderne Automobilanwendungen erfordern.

<img src="./image/README/1712277018285.png" alt="CAN-Netzwerk" style="max-width:50%; display: block; margin: 0 auto;" />

## Fehlen des CAN FD Remote Frames

Ein bemerkenswerter Unterschied zwischen CAN FD und dem klassischen CAN-Protokoll ist das Fehlen eines spezifischen Formats für Remote Frames in CAN FD. Im klassischen CAN-Protokoll werden Remote Frames verwendet, um die Übertragung eines Datenrahmens mit demselben Identifier anzufordern.

Im CAN FD:

- **Kein Spezifisches Remote Frame Format**: CAN FD führt kein eigenes Format für Remote Frames ein. Dies ist keine Einschränkung, sondern eine bewusste Designentscheidung, die auf der Betriebseffizienz des Protokolls beruht.
  
- **Datenratenüberlegungen**: Remote Frames tragen keine Datenmengen, und ihre Verwendung würde nicht von den erhöhten Datenraten profitieren, die CAN FD unterstützt. Daher würde die Definition eines separaten Remote Frame Formats die Leistung nicht verbessern.

- **Kompatibilität mit klassischem CAN**: CAN FD ermöglicht die Verwendung klassischer CAN Remote Frames zur Anforderung von CAN FD Datenrahmen. Dies stellt sicher, dass Systeme, die auf CAN FD migrieren, weiterhin die vorhandene Remote Frame-Funktionalität ohne Änderungen nutzen können.

## Kompatibilität mit bestehenden Protokollen

Das Design von CAN FD stellt sicher, dass bestehende Hochprotokolle wie CANopen und SAE J1939 weiterhin nahtlos mit den neuen Funktionen von CAN FD arbeiten können.

1. **CANopen**:
   - CANopen ist ein Kommunikationsprotokoll und eine Geräteprofilspezifikation für eingebettete Systeme in der Automatisierung. Die Fähigkeit von CAN FD, größere Datenmengen und schnellere Datenraten zu handhaben, kann CANopen-Anwendungen verbessern, insbesondere in Szenarien, die einen schnellen Datenaustausch und höhere Bandbreiten erfordern.

2. **SAE J1939**:
   - SAE J1939 ist ein Hochprotokoll, das in Nutzfahrzeugen zur Kommunikation und Diagnose zwischen Fahrzeugkomponenten verwendet wird. Das erweiterte Identifier-Rahmenformat in CAN FD unterstützt den umfangreichen Identifier-Bereich, der von SAE J1939 benötigt wird, und stellt sicher, dass es die erhöhten Datenraten und größeren Datenmengen von CAN FD nutzen kann.

## Schlussfolgerung

CAN FD stellt einen bedeutenden Fortschritt gegenüber dem klassischen CAN-Protokoll dar, indem es schnellere Datenübertragungsraten und die Möglichkeit zur Handhabung größerer Datenmengen bietet. Durch die Beibehaltung der Standard- und erweiterten Rahmenformate stellt CAN FD die Kompatibilität mit bestehenden Automobilprotokollen wie CANopen und SAE J1939 sicher. Die Entscheidung, kein spezifisches Remote Frame Format für CAN FD einzuführen, ist eine bewusste Wahl, die den Leistungszielen des Protokolls entspricht, während klassische CAN Remote Frames weiterhin zur Anforderung von CAN FD Datenrahmen verwendet werden können.
 