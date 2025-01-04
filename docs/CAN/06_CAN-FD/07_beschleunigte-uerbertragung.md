# Bitratenumschaltung und Übertragungsraten

## Einleitung

Das Controller Area Network mit flexibler Datenrate (CAN-FD) ist eine Weiterentwicklung des klassischen CAN-Protokolls und bietet höhere Datenraten sowie größere Datenpakete. Dieses Tutorial zielt darauf ab, ein detailliertes Verständnis von CAN-FD zu vermitteln, wobei der Fokus auf der Bitratenumschaltung (BRS) und den Übertragungsraten liegt. Dabei werden wichtige Aspekte wie Synchronisation und Implementierungsherausforderungen in Automobilumgebungen kritisch behandelt.

## Bitratenumschaltung (BRS)

Das CAN-FD-Protokoll führt mehrere neue Funktionen im Vergleich zum klassischen CAN ein. Eine der wichtigsten Funktionen ist die Bitratenumschaltung (BRS).

**Definition und Funktionalität:**

Das BRS-Bit folgt einem reservierten Bit 'r', das für zukünftige Protokollerweiterungen vorgesehen ist. Die Aufgabe des BRS-Bits besteht darin, den Wechsel zwischen zwei unterschiedlichen Baudraten innerhalb eines einzigen CAN-FD-Rahmens zu steuern.

- **Dominantes BRS-Bit:** Wenn das BRS-Bit dominant ist, wird der gesamte CAN-FD-Rahmen mit der nominalen Baudrate (Baudrate 1) übertragen.
- **Rezessives BRS-Bit:** Wenn das BRS-Bit rezessiv ist, wird das Datenfeld des CAN-FD-Rahmens mit einer höheren Baudrate (Baudrate 2) übertragen. Dieser Wechsel ermöglicht eine schnellere Datenübertragung innerhalb des Rahmens und gleichzeitig die Beibehaltung der Kompatibilität mit den bestehenden Netzgeschwindigkeiten für den Rest des Rahmens.

**Konfiguration:**

Beide Baudraten müssen einheitlich für alle CAN-FD-Controller im Netzwerk konfiguriert werden, um eine nahtlose Kommunikation zu gewährleisten. Inkonsequente Baudrateneinstellungen können zu Kommunikationsausfällen und Datenintegritätsproblemen führen.

## Übertragungsraten von 5 Mbit/s

CAN-FD verbessert die Datenübertragungsraten im Vergleich zum klassischen CAN erheblich. Der Anstieg der Datenrate wird besonders in der Datenphase des CAN-FD-Rahmens deutlich.

**Empirische Beweise:**

Laborversuche haben gezeigt, dass die meisten Transceiver, die ursprünglich für den klassischen CAN entwickelt wurden, Übertragungsraten von bis zu 5 Mbit/s problemlos bewältigen können, ohne dass Modifikationen erforderlich sind. Diese Fähigkeit ist entscheidend für Anwendungen, die höhere Bandbreiten erfordern, wie z.B. fortschrittliche Fahrerassistenzsysteme (ADAS) und Infotainmentsysteme im Fahrzeug.

**Technische Überlegungen:**

- **Konsistenz der Datenrate:** Es ist wichtig zu beachten, dass die Datenrate (z.B. 5 Mbit/s) der Baudrate entspricht, da eine direkte Beziehung zwischen Bits pro Sekunde und der physikalischen Darstellung der Spannungspegel besteht.
- **Umweltfaktoren:** Während die Laborbedingungen vielversprechende Ergebnisse gezeigt haben, sind reale Automobilumgebungen elektromagnetisch störanfällig. Daher können die tatsächlich erreichbaren Datenraten variieren, und weitere Tests unter Betriebsbedingungen sind notwendig, um diese Ergebnisse zu validieren.

## Höhere Geschwindigkeitsübertragung zwischen BRS und CRC-Delimiter

Der Wechsel zwischen Baudrate 1 und Baudrate 2 erfolgt an bestimmten Punkten innerhalb des CAN-FD-Rahmens:

- **Wechsel zur höheren Baudrate:** Dies erfolgt am Abtastpunkt des BRS-Bits.
- **Wechsel zurück zur niedrigeren Baudrate:** Dies erfolgt am Abtastpunkt des CRC-Delimiters, unmittelbar vor dem Bestätigungsfeld.

**Synchronisation:**

Um sicherzustellen, dass die Empfänger die Hochgeschwindigkeits-Datenphase effektiv verarbeiten können, wird unmittelbar vor der Bitratenumschaltung eine zweite, harte Synchronisation durchgeführt. Diese harte Synchronisation stellt sicher, dass die Zeitabstimmung zwischen Sender und Empfänger perfekt aufeinander abgestimmt ist, um das Risiko von Datenkorruption oder -verlust zu minimieren.

## Schlussfolgerung

CAN-FD, mit seiner Bitratenumschaltung und den erhöhten Datenraten, bietet erhebliche Verbesserungen gegenüber dem klassischen CAN und ist somit geeignet für moderne Automobilanwendungen, die höhere Bandbreiten und Effizienz erfordern. Das Verständnis und die korrekte Implementierung von Funktionen wie BRS und das Management der Übertragungsraten sind entscheidend, um das volle Potenzial von CAN-FD in Automobilnetzwerken auszuschöpfen. Zukünftige Entwicklungen und Tests in realen Umgebungen werden diese Implementierungen weiter verfeinern und eine robuste und zuverlässige Kommunikation in zunehmend komplexeren Fahrzeugumgebungen sicherstellen.