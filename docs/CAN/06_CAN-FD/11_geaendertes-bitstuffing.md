# Bitstuffing bei CAN und CAN FD: Ein umfassendes Tutorial

## Einführung

Das Bitstuffing ist eine zentrale Technik im Controller Area Network (CAN), die dazu dient, Synchronisationsprobleme zu vermeiden und eine zuverlässige Datenübertragung sicherzustellen. Sowohl im klassischen CAN-Protokoll als auch im CAN Flexible Data-Rate (CAN FD) Protokoll wird das Bitstuffing angewendet, jedoch mit unterschiedlichen Regeln und Bereichen. Dieser Teil bietet eine detaillierte Erklärung der Bitstuffing-Mechanismen bei CAN und CAN FD, einschließlich der Behandlung von Stuffbits im CRC-Feld.

## Bitstuffing im klassischen CAN

Im klassischen CAN-Protokoll wird Bitstuffing angewendet, um die Takt-Synchronisation zwischen Sender und Empfänger aufrechtzuerhalten. Die Grundregel des Bitstuffings lautet: Nach jeweils fünf aufeinanderfolgenden Bits mit gleichem Wert (entweder 0 oder 1) wird ein komplementäres Bit eingefügt. Dieses eingefügte Bit wird als "Stuffbit" bezeichnet.

**Beispiel:**

- Wenn eine Nachricht die Bitfolge `111110` enthält, wird ein Stuffbit eingefügt, wodurch die Folge `1111101` entsteht.
- Wichtig ist, dass die Stuffbits nicht in die Berechnung der Prüfsumme (CRC) einfließen.
- Dies bedeutet, dass beim Empfangen der Nachricht die Stuffbits entfernt werden, bevor die CRC-Prüfung durchgeführt wird.

## Bitstuffing bei CAN FD

Das CAN FD-Protokoll erweitert das klassische CAN-Protokoll um höhere Datenraten und größere Datenfelder. Daher sind die Regeln für das Bitstuffing bei CAN FD etwas anders und spezifischer.

**Bitstuffing-Regel:**

- Stuffbits werden ab dem Start of Frame (SOF) eingefügt.
- Das Bitstuffing endet mit dem Ende des Datenfeldes.
- Nach dem Ende des Datenfeldes wird die Anzahl der eingefügten Stuffbits (Modulo 8) berechnet und ein zusätzliches Paritätsbit eingefügt.

**CRC-Berechnung bei CAN FD:**

Der sendende Knoten berechnet die Prüfsumme (CRC), einschließlich der bis zu diesem Punkt eingefügten Stuffbits. Dies unterscheidet sich vom klassischen CAN, wo die Stuffbits nicht in die CRC-Berechnung einfließen.

## Bitstuffing im CRC-Feld bei CAN FD

Zusätzlich zur allgemeinen Bitstuffing-Regel bei CAN FD gibt es spezielle Regeln für das CRC-Feld:

1. Das CRC-Feld beginnt immer mit einem Stuffbit.
2. Nach jeweils vier weiteren CRC-Feld-Bits wird ein weiteres Stuffbit eingefügt, unabhängig davon, ob die Bits gleichnamig sind oder nicht.
3. Der Wert eines CRC-Stuffbits ist komplementär zu seinem Vorgängerbit.

**Beispiel:**

- Angenommen, das CRC-Feld beginnt mit der Bitfolge `1101`.
- Es wird ein Stuffbit eingefügt, wodurch die Folge `11011` entsteht.
- Nach vier weiteren Bits, z.B. `1000`, wird ein weiteres Stuffbit eingefügt, was `10001` ergibt.

## Keine Stuffbits nach dem CRC-Feld

Nach dem CRC-Feld werden, wie beim klassischen CAN, keine weiteren Stuffbits mehr eingefügt. Das bedeutet, dass der Rest des Frames (Acknowledge Slot, End of Frame, etc.) ohne zusätzliche Stuffbits gesendet wird.

### Schlussfolgerung

Bitstuffing ist ein wesentlicher Bestandteil der CAN-Kommunikation, um die Synchronisation zwischen Sender und Empfänger zu gewährleisten und Fehler zu minimieren. Im klassischen CAN-Protokoll werden Stuffbits nach jeweils fünf gleichnamigen Bits eingefügt, jedoch nicht in die CRC-Berechnung einbezogen. Bei CAN FD erstreckt sich das Bitstuffing bis zum Ende des Datenfeldes, und die Stuffbits werden in die CRC-Berechnung einbezogen. Zusätzlich gibt es im CRC-Feld von CAN FD spezielle Bitstuffing-Regeln, die unabhängig von der Bitfolge angewendet werden.
