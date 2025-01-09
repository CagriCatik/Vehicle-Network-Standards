# Fehlererkennungsmechanismen

Das CAN-Protokoll (Controller Area Network) ist ein robustes Kommunikationssystem, das speziell für die Automobilindustrie entwickelt wurde, um den Austausch von Daten zwischen verschiedenen elektronischen Steuergeräten zu ermöglichen. Ein wesentlicher Bestandteil des CAN-Protokolls ist die Fähigkeit, Fehler in der Datenübertragung zu erkennen und zu behandeln. Hierfür definiert das Protokoll fünf wesentliche Fehlererkennungsmechanismen:

1. **Bitmonitoring**
2. **Überwachung des Botschaftsformats (Form-Check)**
3. **Überwachung der Bitcodierung (Stuff-Check)**
4. **Auswertung des Acknowledgements (ACK-Check)**
5. **Auswertung der Prüfsumme (Cyclic Redundancy Check, CRC)**


![CAN-Netzwerk](/img/can/1712276705185.png)

### Aufgabenverteilung zwischen Sender und Empfänger

- **Sender**: Zuständig für Bitmonitoring und ACK-Check.
- **Empfänger**: Verantwortlich für Form-Check, Stuff-Check und Cyclic Redundancy Check (CRC).

### Detaillierte Beschreibung der Fehlererkennungsmechanismen

#### 1. Stuff-Check (Empfänger)

Der Stuff-Check überprüft den Bitstrom auf Bit-Stuffing-Fehler. Das CAN-Protokoll verlangt, dass nach fünf aufeinanderfolgenden Bits gleicher Polarität ein komplementäres Bit eingefügt wird, um die Synchronisation zu gewährleisten. Wird nach fünf gleichen Bits ein weiteres Bit derselben Polarität entdeckt, liegt ein Stuffingfehler vor.

#### 2. Bitmonitoring (Sender)

Das Bitmonitoring ist ein Mechanismus, bei dem der Sender jedes gesendete Bit mit dem tatsächlichen Buspegel vergleicht. Ein Bitfehler tritt auf, wenn eine Diskrepanz zwischen dem gesendeten und dem empfangenen Bit festgestellt wird. Dieser Mechanismus gewährleistet, dass sowohl globale Fehler als auch Fehler, die lokal beim Sender auftreten, erkannt werden.

#### 3. Form-Check (Empfänger)

Der Form-Check dient der Überprüfung des Formats einer CAN-Botschaft. Bestimmte Bitsequenzen müssen an festgelegten Stellen immer gleich sein, wie zum Beispiel der CRC-Delimiter, der ACK-Delimiter und das Ende der Botschaft (EOF). Diese Felder müssen vom Sender rezessiv gesendet werden. Ein Formatfehler wird erkannt, wenn der Empfänger in diesen Feldern einen dominanten Pegel feststellt.

#### 4. Cyclic Redundancy Check (CRC) (Empfänger)

Der CRC ist ein wesentliches Werkzeug zur Erkennung von Übertragungsfehlern. Dabei wird das ankommende Daten- oder Remote-Frame durch ein Polynom R(x) dargestellt, welches ein Vielfaches des durch die ISO 11898-1 spezifizierten Generatorpolynoms G(x) sein sollte. Wenn dies nicht der Fall ist, wurde das Frame während der Übertragung verfälscht, was zu einem CRC-Fehler führt.

#### 5. ACK-Check (Sender)

Das CAN-Protokoll beinhaltet einen Bestätigungsmechanismus, bei dem alle Empfänger einer CAN-Botschaft diese nach dem CRC prüfen und bestätigen müssen. Eine positive Bestätigung reicht aus, um dem Sender mitzuteilen, dass die Botschaft korrekt empfangen wurde. Bleibt diese Bestätigung aus, tritt ein ACK-Fehler auf.
