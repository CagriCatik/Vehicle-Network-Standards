# Polling

XCP (Universal Measurement and Calibration Protocol) bietet zwei grundlegende Messmodi: den **Polling-Modus** und den **Synchronen Datenerfassungsmodus** (kurz **DAQ-Modus**). Diese Modi ermöglichen es Entwicklern und Ingenieuren, Fahrzeugdaten effizient zu erfassen und zu analysieren, um die Leistung und Funktionalität von Steuergeräten zu optimieren.

## Auswahl des Messmodus in CANape

Der CANape-Benutzer hat die Flexibilität, den bevorzugten Messmodus innerhalb der Messkonfiguration von CANape auszuwählen. Diese Auswahl hängt maßgeblich von den spezifischen Anforderungen des Projekts ab, einschließlich der Anzahl der zu messenden Signale, der erforderlichen Messgeschwindigkeit und der verfügbaren Systemressourcen.

## Vertiefung in den Polling-Modus

### Implementierung des Polling-Modus

Der **Polling-Modus** wird in XCP durch die Verwendung der Befehle `SHORT_UPLOAD` oder `UPLOAD` implementiert. Dieser Modus arbeitet, indem jedes angeforderte Signal einzeln aus dem Speicher des Steuergeräts gelesen wird. Die Abfrage erfolgt sequenziell, was bedeutet, dass jeder XCP-Befehl nacheinander verarbeitet wird. Ein Befehl muss vollständig verarbeitet und bestätigt werden, bevor der nächste Befehl vom Master gesendet werden kann.

#### Ablauf der Kommunikation im Polling-Modus

1. **Befehlsübermittlung:** Der Master (z.B. CANape) sendet einen `SHORT_UPLOAD`- oder `UPLOAD`-Befehl an das Steuergerät, um den Wert eines spezifischen Signals anzufordern.
2. **Verarbeitung und Bestätigung:** Das Steuergerät empfängt den Befehl, liest das angeforderte Signal aus dem Speicher und sendet eine entsprechende Bestätigung zurück.
3. **Nächster Befehl:** Erst nach Erhalt der Bestätigung kann der Master den nächsten Befehl senden, um ein weiteres Signal abzurufen.

### Kommunikationsstruktur und Buslast

Die sequenzielle Verarbeitung der XCP-Befehle hat direkte Auswirkungen auf die Kommunikationsstruktur und die Auslastung des Busses:

- **Asynchrone Messung:** Da die Befehle nacheinander abgearbeitet werden, ist es nicht möglich, mehrere Signale exakt gleichzeitig zu messen. Jedes Signal wird mit einer gewissen Zeitverzögerung nacheinander erfasst.
  
- **Hohe Buslast bei vielen Signalen:** Für jedes gemessene Signal werden mindestens zwei XCP-Nachrichten pro Zyklus benötigt (ein Befehl und eine Bestätigung). Bei einer großen Anzahl von Signalen kann dies zu einer erheblichen Belastung des Kommunikationsbusses führen, was die Gesamtleistung und Reaktionsfähigkeit des Systems beeinträchtigen kann.

### Vor- und Nachteile des Polling-Modus

**Vorteile:**

- **Einfachheit:** Der Polling-Modus ist einfach zu implementieren und eignet sich gut für Systeme mit wenigen Signalen und niedrigen Messraten.
- **Geringer Ressourcenverbrauch:** Bei einer begrenzten Anzahl von Signalen ist die Belastung des Kommunikationsbusses überschaubar.

**Nachteile:**

- **Eingeschränkte Messgenauigkeit:** Aufgrund der sequenziellen Verarbeitung können keine Signale exakt synchron erfasst werden, was die Genauigkeit in dynamischen Messanwendungen beeinträchtigen kann.
- **Hohe Buslast bei vielen Signalen:** Die Notwendigkeit, für jedes Signal separate Nachrichten zu senden, kann die Buskapazität schnell erschöpfen und die Systemleistung negativ beeinflussen.
- **Begrenzte Skalierbarkeit:** Der Polling-Modus ist weniger geeignet für komplexe Systeme mit einer großen Anzahl von Signalen oder hohen Messanforderungen.

### Anwendungsfälle für den Polling-Modus

Der Polling-Modus eignet sich insbesondere für die Messung weniger dynamischer Signale bei niedrigeren Messraten. Beispiele hierfür sind:

- **Temperaturvariablen:** Langsam wechselnde Größen wie Kühlmitteltemperaturen oder Motortemperaturen.
- **Statusanzeigen:** Zustände von Schaltern, Relais oder anderen binären Signalen, die selten wechseln.
- **Langsame Prozessvariablen:** Parameter wie Ölstand oder Luftdruck, die sich nur langsam ändern.

Sollten Sie weitere Anwendungsfälle oder spezifische Szenarien im Auge haben, in denen der Polling-Modus von Nutzen sein könnte, empfiehlt es sich, diese Fragen direkt an den Trainer Ihres bevorstehenden CANape-Trainings zu richten. Dort können praxisnahe Beispiele und tiefgehende Erklärungen angeboten werden.

## Vergleich mit dem DAQ-Modus

Um Signale synchronisiert zu messen, also genau zur gleichen Zeit, muss der **DAQ-Modus** verwendet werden. Dieser Modus bietet eine effizientere Methode zur Erfassung mehrerer Signale gleichzeitig und minimiert die Buslast durch gebündelte Datenübertragung. Im nächsten Kapitel werden wir den DAQ-Modus detailliert untersuchen, seine Implementierung und Vorteile im Vergleich zum Polling-Modus erläutern und aufzeigen, wann der Einsatz des DAQ-Modus vorzuziehen ist.

## Best Practices für den Einsatz des Polling-Modus

Um den Polling-Modus effizient zu nutzen und dessen Einschränkungen zu minimieren, sollten folgende Best Practices beachtet werden:

1. **Minimierung der Anzahl der Signale:** Beschränken Sie die Anzahl der im Polling-Modus zu messenden Signale auf das notwendige Minimum, um die Buslast zu reduzieren.
2. **Optimierung der Messfrequenz:** Passen Sie die Messrate an die Dynamik der zu messenden Signale an. Für langsam wechselnde Signale sind niedrigere Messfrequenzen ausreichend.
3. **Priorisierung wichtiger Signale:** Priorisieren Sie kritische Signale, um sicherzustellen, dass diese trotz hoher Buslast zuverlässig erfasst werden.
4. **Effiziente Speicherverwaltung:** Stellen Sie sicher, dass die Signale effizient im Speicher des Steuergeräts organisiert sind, um die Lesezeiten zu minimieren.
5. **Monitoring der Buslast:** Überwachen Sie die Busauslastung kontinuierlich, um Engpässe frühzeitig zu erkennen und gegebenenfalls Anpassungen vorzunehmen.

Durch die Einhaltung dieser Best Practices kann der Polling-Modus effektiv eingesetzt werden, insbesondere in Szenarien, in denen die Anforderungen an die Synchronisation und die Anzahl der zu messenden Signale moderat sind.

## Fazit

Der Polling-Modus stellt eine grundlegende Methode zur Signalerfassung in XCP dar, die sich durch ihre Einfachheit und geringe Ressourcennutzung auszeichnet. Dennoch ist er aufgrund seiner sequenziellen Natur und der daraus resultierenden Buslast bei der Messung vieler Signale nur für spezifische Anwendungsfälle geeignet. Für umfassendere und dynamischere Messanforderungen bietet der DAQ-Modus eine leistungsfähigere Alternative, die im nächsten Kapitel detailliert behandelt wird.

Der Polling-Modus in XCP bietet eine einfache und direkte Methode zur Signalerfassung, ist jedoch durch seine sequenzielle Natur und die daraus resultierende Buslast begrenzt. Für Anwendungen mit wenigen, wenig dynamischen Signalen und niedrigen Messraten ist er ideal geeignet. Bei komplexeren Anforderungen, die eine hohe Synchronisation und eine große Anzahl an Signalen erfordern, stellt der DAQ-Modus eine überlegene Alternative dar. Die Wahl des richtigen Messmodus hängt somit maßgeblich von den spezifischen Projektanforderungen ab.

## Beispielkonfiguration für den Polling-Modus in CANape

Um den Polling-Modus in CANape einzurichten, folgen Sie diesen Schritten:

1. **Messkonfiguration öffnen:**
   - Starten Sie CANape und öffnen Sie Ihr Projekt.
   - Navigieren Sie zur Messkonfiguration über das Menü **"Measurement"** > **"Configuration"**.

2. **Messmodus auswählen:**
   - Im Bereich **"XCP Settings"** wählen Sie den **"Polling-Modus"** aus der Dropdown-Liste der verfügbaren Messmodi.

3. **Signale hinzufügen:**
   - Fügen Sie die gewünschten Signale zur Messkonfiguration hinzu, die im Polling-Modus erfasst werden sollen.
   - Stellen Sie sicher, dass die Signale korrekt adressiert und ihre Adressen im Steuergerät bekannt sind.

4. **Befehle konfigurieren:**
   - Konfigurieren Sie die XCP-Befehle `SHORT_UPLOAD` oder `UPLOAD` für jedes Signal.
   - Legen Sie die Abfragefrequenz fest, die der Dynamik der jeweiligen Signale entspricht.

5. **Messlauf starten:**
   - Starten Sie die Messung und überwachen Sie die erfassten Daten in Echtzeit.
   - Überprüfen Sie die Buslast und passen Sie bei Bedarf die Konfiguration an, um eine optimale Performance zu gewährleisten.

## Tipps zur Fehlerbehebung

- **Verzögerungen bei der Datenübertragung:**
  - Überprüfen Sie die Netzwerkkonfiguration und stellen Sie sicher, dass die physikalischen Verbindungen stabil sind.
  - Reduzieren Sie die Anzahl der gleichzeitig abgefragten Signale, um die Buslast zu verringern.

- **Fehlende Bestätigungen:**
  - Stellen Sie sicher, dass die Adressen und Speicherorte der Signale korrekt konfiguriert sind.
  - Überprüfen Sie die Firmware-Version des Steuergeräts und die Kompatibilität mit der verwendeten XCP-Implementierung.

- **Unstabile Messwerte:**
  - Kalibrieren Sie die Messumgebung und prüfen Sie, ob elektromagnetische Störungen die Kommunikation beeinträchtigen.
  - Nutzen Sie Filteroptionen in CANape, um Rauschen und unerwünschte Signalabweichungen zu minimieren.

Durch systematisches Vorgehen und gezielte Anpassungen können die meisten Probleme im Polling-Modus schnell identifiziert und behoben werden.

## Fragen

1. **Was sind die Hauptunterschiede zwischen dem Polling-Modus und dem DAQ-Modus in XCP?**
   - Der Polling-Modus arbeitet sequenziell, indem jedes Signal einzeln abgefragt wird, während der DAQ-Modus mehrere Signale gleichzeitig erfasst. Der Polling-Modus erfordert für jedes Signal eine separate Nachricht, was die Buslast erhöht, während der DAQ-Modus effizienter ist und die Buslast durch gebündelte Übertragung reduziert.

2. **Wie wird der Polling-Modus in XCP implementiert, und welche Befehle werden dabei verwendet?**
   - Der Polling-Modus wird durch die Befehle `SHORT_UPLOAD` oder `UPLOAD` implementiert. Der Master sendet einen dieser Befehle, um ein Signal vom Steuergerät zu lesen. Nach der Verarbeitung und Bestätigung des Befehls kann der Master den nächsten Befehl senden.

3. **Welche Auswirkungen hat die sequenzielle Verarbeitung der Befehle im Polling-Modus auf die Buslast?**
   - Die sequenzielle Verarbeitung führt dazu, dass für jedes Signal mindestens zwei Nachrichten (Befehl und Bestätigung) gesendet werden. Dies kann die Buslast erheblich erhöhen, insbesondere wenn viele Signale erfasst werden, und die Leistung des Systems beeinträchtigen.

4. **Welche Vorteile bietet der Polling-Modus?**
   - Der Polling-Modus ist einfach zu implementieren und verbraucht bei wenigen Signalen und niedrigen Messraten nur geringe Ressourcen. Er eignet sich besonders gut für Systeme, in denen die Messgenauigkeit und Synchronität keine entscheidenden Faktoren sind.

5. **Welche Nachteile hat der Polling-Modus im Vergleich zum DAQ-Modus?**
   - Der Polling-Modus erfasst Signale nicht synchron, was die Messgenauigkeit bei dynamischen Signalen beeinträchtigt. Außerdem erzeugt er eine hohe Buslast bei vielen Signalen und skaliert schlecht bei größeren oder komplexeren Systemen.

6. **Für welche Anwendungsfälle ist der Polling-Modus besonders geeignet?**
   - Der Polling-Modus ist besonders geeignet für langsam wechselnde Signale wie Temperaturmessungen, Statusanzeigen oder Prozessvariablen, die sich nicht schnell ändern. Er wird häufig verwendet, wenn keine hohe Synchronität zwischen den Signalen erforderlich ist.

7. **Welche Best Practices sollten bei der Verwendung des Polling-Modus beachtet werden?**
   - Um den Polling-Modus effizient zu nutzen, sollten die Anzahl der gemessenen Signale minimiert, die Messfrequenz den Signaldynamiken angepasst und wichtige Signale priorisiert werden. Eine effiziente Speicherverwaltung im Steuergerät und die kontinuierliche Überwachung der Buslast sind ebenfalls entscheidend.

8. **Wie wird der Polling-Modus in CANape konfiguriert?**
   - In CANape wird der Polling-Modus in den **XCP Settings** ausgewählt. Anschließend werden die zu messenden Signale hinzugefügt, die `SHORT_UPLOAD`- oder `UPLOAD`-Befehle konfiguriert und die Abfragefrequenz angepasst. Nach dem Start der Messung wird die Buslast überwacht und die Konfiguration bei Bedarf optimiert.

9. **Welche Kommunikationsprobleme können im Polling-Modus auftreten und wie werden diese behoben?**
   - Häufige Probleme umfassen Verzögerungen bei der Datenübertragung, fehlende Bestätigungen und unstabile Messwerte. Diese können durch Überprüfung der Netzwerkkonfiguration, Reduzierung der Buslast, Anpassung der Adressen und Speicherorte sowie die Kalibrierung der Messumgebung behoben werden.

10. **Wie kann die Messgenauigkeit im Polling-Modus optimiert werden, obwohl die Signale nicht synchron erfasst werden?**
    - Die Messgenauigkeit kann durch die Anpassung der Abfragefrequenzen und die Priorisierung wichtiger Signale optimiert werden. Außerdem hilft die Minimierung der Anzahl abgefragter Signale, die Gesamtperformance und Zuverlässigkeit der Messungen zu verbessern.