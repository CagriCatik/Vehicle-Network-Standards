# Buspegel

## Physikalische Signalübertragung

Die physikalische Signalübertragung in einem FlexRay-Cluster basiert auf der Differenzsignalübertragung. Dies bedeutet, dass die Informationen durch Spannungsdifferenzen zwischen zwei Leitungen, „Bus Plus“ (BP) und „Bus Minus“ (BM), übertragen werden. Diese beiden Leitungen bilden zusammen das Übertragungsmedium, den FlexRay-Bus.

### Buspegel und Buszustände

Die Electrical Physical Layer Specification des FlexRay-Protokolls definiert vier Buspegel, die in zwei Zustände unterteilt sind: rezessiv und dominant.

#### Rezessiver Buszustand

Der rezessive Buszustand ist durch eine Differenzspannung von 0 Volt gekennzeichnet. Dieser Zustand tritt in zwei Varianten auf:

1. **Idle**: Beide Leitungen, BP und BM, haben ein Potenzial von 2,5 Volt, was zu einer Differenzspannung von 0 Volt führt. Der gültige Spannungsbereich für den Idle-Buspegel liegt zwischen 1,8 Volt und 3,2 Volt.
2. **Idle Low Power**: Dieser Zustand tritt ein, wenn sich alle FlexRay-Transceiver im Low Power Mode befinden. Beide Leitungen haben ein Potenzial von 0 Volt, wodurch ebenfalls eine Differenzspannung von 0 Volt entsteht. Der gültige Spannungsbereich für den Idle Low Power Buspegel liegt zwischen -0,2 Volt und 0,2 Volt.

#### Dominanter Buszustand

Der dominante Buszustand ist durch eine Differenzspannung von ungleich 0 Volt gekennzeichnet und kann in zwei Buspegel unterteilt werden:

1. **Data_1**: Die Busleitung BP hat ein Potenzial von 3,5 Volt und die Busleitung BM ein Potenzial von 1,5 Volt. Die resultierende Differenzspannung beträgt 2 Volt. Der Buspegel „Data_1“ repräsentiert die logische Eins.
2. **Data_0**: Die Busleitung BP hat ein Potenzial von 1,5 Volt und die Busleitung BM ein Potenzial von 3,5 Volt. Die Differenzspannung beträgt -2 Volt. Der Buspegel „Data_0“ repräsentiert die logische Null.

## Signalinterpretation und Schwellenwerte

Die FlexRay-Kommunikation basiert auf der präzisen Interpretation der Spannungsdifferenzen zwischen BP und BM. Sender und Empfänger müssen die definierten Spannungspegel und deren Schwellenwerte korrekt interpretieren, um die Daten zuverlässig zu übertragen und zu empfangen.

### Sende- und Empfangsschwellen

Die Spezifikation gibt genaue Schwellenwerte vor, die Sender und Empfänger einhalten müssen, um die Buspegel korrekt zu erkennen und zu verarbeiten. Diese Schwellenwerte sind entscheidend, um Signalstörungen zu minimieren und eine fehlerfreie Datenübertragung zu gewährleisten.

