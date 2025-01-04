# Glossar

## P 

### Parameter eines Signals

Das Signal „MotorTemperatur“ ist ein Beispiel für ein typisches Signal, das in einem automobilen Kommunikationssystem verwendet wird, um die Temperatur des Motors in Grad Celsius zu übermitteln. Um zu verstehen, wie dieses Signal definiert und interpretiert wird, sind folgende Parameter wichtig:

### **Parameter des Signals „MotorTemperatur“**

1. **Länge: 8 Bit (1 Byte)**
   - **Erläuterung:** Die Länge eines Signals gibt an, wie viele Bits (die kleinste Informationseinheit) zur Darstellung des Signals verwendet werden. In diesem Fall ist das Signal 8 Bit lang, was 1 Byte entspricht. Ein 8-Bit-Signal kann Werte im Bereich von 0 bis 255 darstellen, da 2⁸ = 256 mögliche Werte existieren. Diese 256 mögliche Werte müssen dann in den entsprechenden Temperaturbereich abgebildet werden.

2. **Skalierungsfaktor: 0,5**
   - **Erläuterung:** Der Skalierungsfaktor wird verwendet, um den digitalen Wert des Signals in eine physikalische Größe umzuwandeln. Er gibt an, wie viel physikalische Einheiten (z. B. Grad Celsius) einem Zählerwert von 1 im digitalen Signal entsprechen. In diesem Fall bedeutet ein digitaler Anstieg um 1 im Signal eine Erhöhung der Temperatur um 0,5 Grad Celsius.

   - **Beispielrechnung:** Wenn der digitale Wert des Signals 100 beträgt, entspricht dies einer physikalischen Temperatur von 100 * 0,5 = 50 °C.

3. **Offset: -40**
   - **Erläuterung:** Das Offset gibt an, wie viel zu dem skalierten Wert hinzugefügt oder davon abgezogen werden muss, um den tatsächlichen physikalischen Wert zu erhalten. Das Offset wird angewendet, um negative Werte oder eine Verschiebung des Messbereichs zu ermöglichen. In diesem Beispiel wird von dem berechneten Wert 40 abgezogen.

   - **Beispielrechnung:** Wenn das Signal einen digitalen Wert von 100 hat, ergibt sich der physikalische Wert durch die Formel: \( \text{Temperatur} = (\text{Digitaler Wert} \times \text{Skalierungsfaktor}) + \text{Offset} \)
     - Temperatur = (100 * 0,5) + (-40) = 50 - 40 = 10 °C

4. **Wertebereich: -40 bis 215 °C**
   - **Erläuterung:** Der Wertebereich gibt die physikalischen Extremwerte an, die das Signal darstellen kann. In diesem Beispiel bedeutet der Wertebereich, dass die niedrigste darstellbare Temperatur -40 °C und die höchste darstellbare Temperatur 215 °C beträgt. 

   - **Berechnung des Maximal- und Minimalwerts:**
     - **Minimalwert:** Wenn der digitale Wert 0 beträgt, ergibt sich der minimal mögliche physikalische Wert: \\
     \((0 \times 0,5) + (-40) = -40\) °C.
     - **Maximalwert:** Wenn der digitale Wert 255 beträgt (der maximale Wert bei 8 Bit), ergibt sich der maximal mögliche physikalische Wert: \\
     \((255 \times 0,5) + (-40) = 127,5 - 40 = 87,5\) °C.

   In der Praxis wird der Wertebereich oft so eingestellt, dass die tatsächlichen möglichen physikalischen Werte vollständig abgedeckt werden, manchmal auch über den tatsächlich genutzten Bereich hinaus, um Reservewerte für spezielle Bedingungen oder Fehlerzustände zu ermöglichen.


### PDU

Eine **PDU** (Protokolldateneinheit, englisch: Protocol Data Unit) ist ein grundlegendes Konzept in der Netzwerk- und Kommunikationsarchitektur, das die spezifische Form und Struktur beschreibt, in der Daten über ein Netzwerk übertragen werden. Im Kontext von AUTOSAR (AUTomotive Open System ARchitecture) und anderen Kommunikationsprotokollen wird eine PDU verwendet, um Daten zwischen verschiedenen elektronischen Steuergeräten (ECUs) innerhalb eines Fahrzeugs zu transportieren.

1. **Definition:**
   Eine PDU ist eine strukturierte Einheit von Daten, die für die Übertragung über ein Netzwerk formatiert ist. Sie enthält nicht nur die Nutzdaten (das eigentliche Signal oder die Informationen, die übertragen werden sollen), sondern auch Steuerinformationen, die benötigt werden, um die Daten sicher und korrekt über das Netzwerk zu transportieren. Diese Steuerinformationen können Adressen, Protokolltypen, Sequenznummern und Prüfsummen umfassen.

2. **Komponenten einer PDU:**
   Eine typische PDU besteht aus mehreren Teilen:
   - **Header:** Enthält Steuerinformationen, wie Absender- und Empfängeradresse, Protokollinformationen und andere Kontrollfelder.
   - **Payload (Nutzdaten):** Das sind die eigentlichen Daten, die übertragen werden sollen, wie z.B. ein Signal im AUTOSAR-Kontext.
   - **Trailer (optional):** Einige Protokolle fügen am Ende der PDU noch zusätzliche Informationen hinzu, wie z.B. eine Prüfsumme zur Fehlererkennung.

3. **PDU im AUTOSAR-Kontext:**
   Im AUTOSAR-Umfeld werden PDUs verwendet, um Signale zwischen den ECUs eines Fahrzeugs zu transportieren. AUTOSAR definiert klare Standards für die Struktur und den Inhalt von PDUs, um sicherzustellen, dass verschiedene ECUs, die möglicherweise von unterschiedlichen Herstellern stammen, nahtlos miteinander kommunizieren können.

   **Beispiel:**
   - Angenommen, eine ECU erfasst die Geschwindigkeit eines Fahrzeugs und möchte diese Information an das Steuergerät des Navigationssystems weitergeben. Die Geschwindigkeit wird als Signal kodiert, in eine PDU gepackt und über den CAN-Bus (oder ein anderes Netzwerkprotokoll) an die Ziel-ECU gesendet. Die PDU enthält die Geschwindigkeit als Nutzdaten, zusammen mit anderen notwendigen Steuerinformationen im Header, wie z.B. dem Zielort der Daten.

4. **Funktion der PDU:**
   - **Datenkapselung:** PDUs kapseln Signale und andere Informationen in einer standardisierten Form, sodass sie über das Netzwerk übertragen werden können.
   - **Fehlererkennung und -korrektur:** Durch Steuerinformationen wie Prüfsummen können Empfänger überprüfen, ob die Daten korrekt übertragen wurden, und Fehler erkennen und gegebenenfalls korrigieren.
   - **Multikasting:** In manchen Netzwerken kann eine PDU an mehrere Empfänger gesendet werden, wobei alle Empfänger dieselbe PDU gleichzeitig erhalten.

5. **Vorteile der PDU-Nutzung:**
   - **Standardisierung:** PDUs ermöglichen eine standardisierte Datenübertragung, was die Interoperabilität zwischen verschiedenen Systemen und Herstellern erleichtert.
   - **Modularität:** Da PDUs klar strukturierte Einheiten sind, können sie leicht in verschiedenen Teilen des Netzwerks verarbeitet und interpretiert werden.
   - **Effizienz:** Durch die Bündelung von Signalen in einer PDU können mehrere Daten gleichzeitig übertragen werden, was die Effizienz des Netzwerks erhöht.