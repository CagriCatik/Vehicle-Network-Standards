# Mehr Daten bei gleichbleibender Sicherheit

## Einführung in CAN-FD

CAN-FD (Controller Area Network with Flexible Data-Rate) ist eine Erweiterung des klassischen CAN-Protokolls, das in den 1980er Jahren von Bosch entwickelt wurde. Es bietet höhere Datenraten und größere Nutzlasten, wodurch es besser für moderne Anforderungen im Automotive-Bereich geeignet ist. Während klassisches CAN auf 1 Mbit/s und 8 Byte Daten pro Frame limitiert ist, ermöglicht CAN-FD Datenraten von bis zu 5 Mbit/s und Nutzlasten bis zu 64 Byte pro Frame.

## Technische Details von CAN-FD

### Größeres CRC-Feld für mehr Daten

Eine der bedeutenden Änderungen in CAN-FD im Vergleich zum klassischen CAN ist die Anpassung des Cyclic Redundancy Check (CRC)-Feldes. Die CRC-Prüfung ist entscheidend, um die Integrität der Daten zu gewährleisten. Aufgrund der erhöhten Anzahl an Bits und der höheren Datenrate bei CAN-FD steigt die Wahrscheinlichkeit von Bitfehlern. Dies resultiert aus zwei Hauptfaktoren:

1. **Kürzere Bitzeiten:** Die Erhöhung der Datenrate führt zu kürzeren Bitzeiten, was die Anfälligkeit für Störungen erhöht.
2. **Größere Datenfelder:** Mit der Möglichkeit, bis zu 64 Byte Daten zu übertragen, steigt die Gesamtanzahl der Bits pro Frame erheblich.

Um diesen erhöhten Risiken entgegenzuwirken, wurden die CRC-Felder bei CAN-FD vergrößert:

- Für Datenfelder bis 16 Byte wird ein 17-Bit-CRC verwendet.
- Für größere Datenfelder wird ein 21-Bit-CRC eingesetzt.

Die Generatorpolynome für diese CRC-Berechnungen sind wie folgt:

- **CRC17:** 0x3685B
- **CRC21:** 0x302899

## CRC-Berechnung in CAN-FD

Die CRC-Berechnung ist ein kritischer Bestandteil der CAN-FD-Spezifikation, da sie sicherstellt, dass Übertragungsfehler erkannt werden. Die Verwendung von Generatorpolynomen ermöglicht es, den CRC-Wert effizient zu berechnen und Fehler zu erkennen, die während der Übertragung auftreten könnten.

### CRC17-Berechnung für Datenfelder bis 16 Byte

Das Generatorpolynom 0x3685B wird verwendet, um den 17-Bit-CRC zu berechnen. Der CRC-Wert wird über das gesamte Datenfeld, einschließlich der Kontrollinformationen, berechnet. Der genaue Ablauf der Berechnung beinhaltet folgende Schritte:

1. Initialisierung des CRC-Registers.
2. Bitweise Verarbeitung des Datenfeldes und Anwendung des Generatorpolynoms.
3. Ergebnis ist der 17-Bit-CRC-Wert, der an den Frame angehängt wird.

### CRC21-Berechnung für größere Datenfelder

Für Datenfelder, die größer als 16 Byte sind, wird das Generatorpolynom 0x302899 verwendet. Der Prozess ist ähnlich der CRC17-Berechnung, jedoch mit einem 21-Bit-Register und entsprechenden Anpassungen in der Polynomberechnung.

## Vorteile von CAN-FD

CAN-FD bietet mehrere Vorteile gegenüber dem klassischen CAN-Protokoll:

- **Höhere Datenrate:** Durch die flexible Datenrate können kritische Daten schneller übertragen werden, was die Reaktionszeit von Systemen verbessert.
- **Größere Nutzlast:** Mit bis zu 64 Byte pro Frame können mehr Daten in einem einzelnen Frame übertragen werden, was die Effizienz der Kommunikation erhöht.
- **Verbesserte Fehlererkennung:** Durch die erweiterten CRC-Felder wird die Wahrscheinlichkeit von unentdeckten Fehlern reduziert, was die Zuverlässigkeit des Netzwerks erhöht.

## Implementierung von CAN-FD in Automobilen

Die Implementierung von CAN-FD in Automobilen erfordert eine sorgfältige Planung und Anpassung der bestehenden Netzwerke. Es ist wichtig, dass sowohl die Hardware als auch die Software der Steuergeräte (ECUs) CAN-FD unterstützen. Dazu gehören:

- **CAN-FD-fähige Transceiver und Controller:** Diese müssen die höheren Datenraten und die neuen Frame-Formate unterstützen.
- **Angepasste Software-Stacks:** Die Software muss in der Lage sein, die neuen CRC-Berechnungen und die flexiblen Datenraten zu handhaben.

## Schlussfolgerung

CAN-FD stellt einen wichtigen Fortschritt im Bereich der automobilen Netzwerke dar, indem es höhere Datenraten und größere Nutzlasten ermöglicht. Die Erweiterung der CRC-Felder und die Einführung von robusteren Fehlererkennungsmechanismen tragen dazu bei, die Zuverlässigkeit der Datenübertragung in modernen Fahrzeugen zu erhöhen. Bei der Implementierung von CAN-FD müssen jedoch sorgfältig die erhöhten Anforderungen an Hardware und Software berücksichtigt werden, um die Vorteile vollständig auszuschöpfen.

Dieses Tutorial bietet einen Überblick über die wesentlichen Aspekte von CAN-FD und dessen Vorteile gegenüber dem klassischen CAN-Protokoll. Durch die detaillierte Beschreibung der CRC-Berechnung und die Hervorhebung der technischen Vorteile wird die Bedeutung von CAN-FD für moderne Automobile verdeutlicht.
