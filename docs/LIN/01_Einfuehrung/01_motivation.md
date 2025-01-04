## Elektronifizierung

In den letzten Jahrzehnten wurden immer mehr Funktionen für Kraftfahrzeuge entwickelt, die das Autofahren komfortabler, sicherer und umweltfreundlicher machen sollen. Dabei werden zunehmend Funktionen mithilfe elektronischer Komponenten realisiert, die einen wachsenden Bedarf an Informationsaustausch haben. Zu diesen elektronischen Komponenten gehören sowohl Steuergeräte als auch Sensoren und Aktoren.

## Motivation

Es war lange Zeit üblich, dass Sensoren und Aktoren mittels einzelner Leitungen mit einem Steuergerät verbunden wurden. Diese konventionelle Vernetzung führte jedoch zu immer dickeren und schwereren Kabelbäumen, die einen größeren Gewichts- und Platzbedarf erforderten. Zudem wurde die Herstellung für unterschiedliche Fahrzeugvarianten komplizierter, da viele individuelle Anpassungen vorgenommen werden mussten. Ergänzend nahm die Fehleranfälligkeit durch die erhöhte Anzahl an Leitungen zu. Diese Probleme führten letztendlich zu steigenden Kosten für die Fahrzeugvernetzung.

## CAN als Vorreiter

1983 wurde der Controller Area Network (CAN) von der Robert Bosch GmbH entwickelt und 1986 auf dem Kongress der SAE als neues serielles Bussystem vorgestellt. Die Einführung von CAN ermöglichte die bitserielle Übertragung mehrerer Signale auf einem Leiterpaar, wodurch die benötigte Anzahl an Leitungen reduziert werden konnte.

## Kostenreduktion

Für die Anbindung kostengünstiger Sensoren und Aktoren im Komfortbereich war CAN jedoch zu teuer. So begannen Mitte der 1990er Jahre einige Fahrzeughersteller und Zulieferer mit der Entwicklung preiswerterer Lösungen. Da diese herstellerspezifischen Bussysteme allerdings zu geringen Stückzahlen führten, war eine umfassende Kostenreduktion nur bedingt möglich. Aus diesem Grund schlossen sich einige Hersteller zum LIN Consortium zusammen, um ein einheitliches, standardisiertes und kostengünstiges Kommunikationssystem zu entwickeln.

## LIN (Local Interconnect Network)

LIN, oder Local Interconnect Network, ist ein Kommunikationssystem, das speziell entwickelt wurde, um die Anforderungen der Automobilindustrie an eine kostengünstige, zuverlässige und einfache Vernetzung von Sensoren und Aktoren zu erfüllen. Es wurde als Ergänzung zum CAN-Bus entwickelt und ermöglicht eine kosteneffiziente Integration einfacher, nicht sicherheitskritischer Funktionen.

### Eigenschaften des LIN-Busses

1. **Kosteneffizienz**: LIN ist deutlich kostengünstiger als CAN, da es mit einfacheren Hardwarekomponenten auskommt und weniger komplexe Software erfordert.
2. **Topologie**: LIN verwendet eine einfache Bus-Topologie, die die Verkabelung vereinfacht und die Installationskosten reduziert.
3. **Datenrate**: LIN arbeitet mit einer niedrigeren Datenrate (typischerweise bis zu 20 kbit/s), was für viele Komfort- und Bedienelemente ausreicht.
4. **Master-Slave-Architektur**: Ein LIN-Bus besteht aus einem Master-Steuergerät und mehreren Slave-Komponenten. Der Master initiiert die Kommunikation, was die Implementierung vereinfacht.
5. **Fehlererkennung**: LIN bietet grundlegende Mechanismen zur Fehlererkennung und -behebung, die für nicht sicherheitskritische Anwendungen ausreichend sind.

### Anwendungen des LIN-Busses

LIN findet Anwendung in vielen Bereichen des Fahrzeugs, insbesondere dort, wo niedrige Kosten und einfache Implementierung entscheidend sind. Typische Anwendungen umfassen:

- Fensterhebersteuerung
- Sitzverstellung
- Klimaanlagensteuerung
- Beleuchtungssysteme
- Türmodule

<img src="./image/1716459892814.png" alt="drawing" width="400"/>

## Zusammenfassung

Die zunehmende Elektronifizierung im Automobilsektor hat zu einem wachsenden Bedarf an effizienten Kommunikationssystemen geführt. Während CAN den Weg für serielle Bussysteme ebnete und eine Reduzierung der Verkabelungskomplexität ermöglichte, bietet LIN eine kostengünstige Lösung für weniger anspruchsvolle Anwendungen. Die Kombination beider Systeme erlaubt eine flexible und wirtschaftliche Gestaltung moderner Fahrzeugnetzwerke.

In der Entwicklung und Implementierung solcher Systeme ist es essenziell, die spezifischen Anforderungen und Einschränkungen der jeweiligen Anwendung zu berücksichtigen. Durch die richtige Auswahl und Integration von CAN und LIN können Hersteller die Balance zwischen Kosten, Leistung und Komplexität optimal gestalten.
