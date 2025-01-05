### LIN (Local Interconnect Network)
#### Einleitung

Das Local Interconnect Network (LIN) ist ein kostengünstiges serielles Kommunikationsprotokoll, das hauptsächlich in der Automobilindustrie verwendet wird. LIN ermöglicht die Vernetzung von Mikrocontrollern und Sensoren in einem Fahrzeug, insbesondere in Bereichen, die nicht die Leistungsfähigkeit und die Kosten eines vollständigen CAN-Busses (Controller Area Network) erfordern. Es ist ideal für Anwendungen, bei denen eine niedrige Datenrate und eine einfache Topologie ausreichen, wie beispielsweise für Beleuchtung, Klimaanlage und Sitzsteuerung.

#### Grundlegende Architektur und Funktionsweise des LIN-Busses

Der LIN-Bus verwendet eine **1-Draht-Verbindung**, ergänzt durch Masse (Gnd) und Batterieanschluss (Vbat), zur Kommunikation zwischen den verschiedenen Knotenpunkten. Die Architektur basiert auf einem **Master-Slave-Prinzip**, wobei immer nur **ein Master** und eine oder mehrere Slaves existieren. Der Master steuert den Zugriff auf den Bus und verwaltet die Kommunikation, indem er die Zeitschlitze für die Kommunikation auf dem Bus definiert.

Die Hauptkomponenten und Konzepte des LIN-Busses umfassen:

1. **Master-Slave-Konzept:**
   - Der LIN-Bus hat immer nur einen Master, der die gesamte Buskommunikation steuert.
   - Die Slaves agieren passiv und führen nur Befehle aus, die vom Master initiiert werden.

2. **Zeitsynchronisierte Kommunikation:**
   - Der Master bestimmt die Zeit, in der jeder Knoten auf den Bus zugreifen darf, indem er den Bus für eine bestimmte Zeitspanne zuweist. Dies geschieht durch das Senden eines bestimmten „Items“ oder Befehls, das den Slaves erlaubt, Daten zu senden.
   - Dadurch wird eine deterministische Kommunikation sichergestellt, die Störungen minimiert und Konflikte auf dem Bus vermeidet.

3. **Datenraten und Geschwindigkeit:**
   - Der LIN-Bus unterstützt typischerweise Datenraten zwischen **9600 und 19200 Bit/s**. 
   - Die maximale spezifizierte Geschwindigkeit gemäß der LIN-Spezifikation beträgt **20 Kbit/s**. Diese vergleichsweise niedrige Datenrate ist ausreichend für Anwendungen, bei denen Echtzeitdatenübertragung nicht kritisch ist.

#### Kommunikationsprotokoll

Das LIN-Protokoll folgt einem deterministischen Ansatz, bei dem der Master eine Zeitbasis vorgibt und so die Synchronisation der Slaves gewährleistet. Diese strukturierte Kommunikation macht es möglich, eine niedrige und stabile Datenrate zu erzielen. Der Kommunikationsfluss sieht wie folgt aus:

1. **Initiierung durch den Master:**
   - Der Master sendet einen Frame-Header, bestehend aus einer Synchronisations-Sequenz und einer Identifier-Sequenz, um die Slaves zu informieren, dass eine Übertragung beginnt.
   - Der Identifier bestimmt, welches Slave-Gerät Daten senden oder empfangen soll.

2. **Datenübertragung durch die Slaves:**
   - Die Slaves antworten basierend auf den vom Master erhaltenen Instruktionen.
   - Kein Slave darf ohne die ausdrückliche Erlaubnis des Masters auf den Bus zugreifen, was eine Kollisionsvermeidung sicherstellt.

3. **Fehlersicherheitsmechanismen:**
   - LIN enthält einfache Mechanismen zur Fehlererkennung und -korrektur, wie zum Beispiel Prüfsummen, um die Integrität der übertragenen Daten zu gewährleisten.
   - Da LIN primär für kostengünstige Systeme gedacht ist, sind die Fehlersicherheitsfunktionen einfacher als bei anderen Busprotokollen wie CAN.

#### Anwendungen im Fahrzeug

LIN wird häufig in Anwendungen mit **niedrigen Datenanforderungen** eingesetzt, die nicht die Robustheit und Komplexität eines CAN-Busses erfordern. Typische Einsatzbereiche umfassen:

- **Ambiente- und Innenraumbeleuchtung**: Steuerung und Anpassung von Lichtelementen im Innenraum.
- **Tastenfelder und Bedienfelder**: Kommunikation zwischen Steuergeräten und Schaltflächen im Fahrzeug, wie Fensterheber und Sitzverstellung.
- **Klimasteuerung**: Regelung von Gebläsen und Klimakomponenten.
- **Aktuatoren und Motorensteuerung**: Steuerung kleiner Motoren für Spiegelverstellung, Sitzheizung und andere Komfortfunktionen.

Es ist nicht unüblich, dass ein Fahrzeug **mehrere LIN-Busse** besitzt, die jeweils unterschiedliche Funktionen abdecken. Beispielsweise könnte ein Bus für die Steuerung der Klimaanlage und ein anderer für die Sitzverstellung verantwortlich sein.

#### Vorteile und Einschränkungen des LIN-Busses

**Vorteile:**

- **Kostenersparnis:** LIN ist wesentlich kostengünstiger als CAN, da es eine einfachere Architektur und eine niedrigere Datenrate hat.
- **Einfache Verkabelung:** Der LIN-Bus benötigt nur eine einzige Datenleitung, ergänzt durch Masse und Versorgungsspannung, was die Verkabelung vereinfacht und Kosten reduziert.
- **Deterministische Kommunikation:** Der Master-Slave-Ansatz ermöglicht eine kontrollierte und vorhersagbare Kommunikation, die ideal für Anwendungen ist, die keine hohen Datenraten benötigen.

**Einschränkungen:**

- **Niedrige Datenrate:** Die maximale Geschwindigkeit von 20 Kbit/s begrenzt LIN auf Anwendungen mit geringen Datenanforderungen.
- **Kein Multi-Master-Betrieb:** Es kann immer nur ein Master vorhanden sein, was die Flexibilität des Systems einschränkt.
- **Begrenzte Fehlererkennung:** Die Fehlersicherheitsmechanismen sind weniger umfassend als bei CAN, wodurch LIN für sicherheitskritische Anwendungen weniger geeignet ist.

#### Vergleich mit anderen Bussystemen

- **CAN (Controller Area Network):** CAN ist leistungsfähiger und unterstützt höhere Datenraten (bis zu 1 Mbit/s), was es für sicherheitskritische Anwendungen und Systeme mit hohen Datenanforderungen prädestiniert. Im Gegensatz zu LIN kann CAN mehrere Master in einem Netzwerk haben und bietet umfassendere Mechanismen zur Fehlererkennung und -behebung.
- **FlexRay:** FlexRay ist ein Hochgeschwindigkeits-Bussystem, das für sicherheitskritische und zeitkritische Anwendungen wie Antrieb und Fahrwerkssteuerung entwickelt wurde. Es ist jedoch deutlich teurer und komplexer als LIN und CAN und wird in Hochleistungsbereichen eingesetzt.

#### Zusammenfassung

LIN ist ein ideales Bussystem für Anwendungen, die eine **kostengünstige, zuverlässige und deterministische Kommunikation** bei niedrigen Datenraten erfordern. Seine einfache Architektur und der Master-Slave-Ansatz machen es zu einer bevorzugten Lösung für Komfort- und Steuerungsanwendungen im Fahrzeug, wie Beleuchtung, Fensterheber, Klimasteuerung und Sitzverstellung.

Durch die Nutzung mehrerer LIN-Busse kann ein Fahrzeughersteller verschiedene Systeme effizient miteinander verbinden, ohne die Kosten und Komplexität eines CAN- oder FlexRay-Netzwerks in Kauf nehmen zu müssen. LIN ist somit eine ergänzende Technologie zu anderen Fahrzeugbussen und ermöglicht eine gezielte und wirtschaftliche Vernetzung von Komponenten im Niedrigdrehzahl- und Komfortbereich des Fahrzeugs.