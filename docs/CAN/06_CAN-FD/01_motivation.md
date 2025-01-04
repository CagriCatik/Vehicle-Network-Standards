# CAN-FD

## Einleitung

Der Controller Area Network (CAN) ist seit Jahrzehnten ein grundlegendes Kommunikationsprotokoll in der Automobilindustrie. Ursprünglich eingeführt, um einige hundert Signale innerhalb eines Fahrzeugs zu verarbeiten, hat sich die Anzahl der Signale mit der Evolution eingebetteter Systeme im Automobilbereich erheblich erhöht und erreicht nun fünfstellige Bereiche. Dieses Tutorial behandelt die Feinheiten von CAN mit einem Fokus auf CAN-FD (Flexible Data-Rate), geht auf die Einschränkungen des klassischen CAN ein und erläutert, wie CAN-FD diese Herausforderungen zu überwinden versucht.

## Die Entwicklung eingebetteter Systeme in Fahrzeugen

### Zunahme der Signalübertragung

Das exponentielle Wachstum der innerhalb von Fahrzeugen übertragenen Signale hat die Landschaft eingebetteter Automobilsysteme drastisch verändert. Moderne Fahrzeuge erfordern die Übertragung von Zehntausenden von Signalen, was die ursprünglich für das CAN-Protokoll vorgesehene Kapazität weit übersteigt.

### Entstehung neuer Bussysteme

Um dem steigenden Datenaufkommen und dem Bedarf an deterministischem Systemverhalten gerecht zu werden, wurden mehrere neue Bussysteme entwickelt:

- **MOST (Media Oriented Systems Transport):** Entwickelt für Infotainmentsysteme und bietet Bandbreiten bis zu 150 Mbit/s.
- **FlexRay:** Ein deterministisches Bussystem mit Bandbreiten bis zu 10 Mbit/s, das hauptsächlich für Fahrerassistenzaufgaben genutzt wird.
- **LIN (Local Interconnect Network):** Ein kostengünstiges Bussystem, das für einfache Sensor-Aktor-Aufgaben mit niedrigeren Bandbreiten ausgelegt ist.

Diese spezialisierten Bussysteme besetzen spezifische Nischen im Automobilnetzwerk, während der universell einsetzbare CAN-Bus weiterhin vorherrschend bleibt.

## Einschränkungen und Lösungen für den klassischen CAN

### Beschränkungen des klassischen CAN

Trotz der Entwicklung neuer Bussysteme ist der Ersatz von CAN durch Alternativen mit höherer Bandbreite wie FlexRay oft unpraktisch aufgrund der hohen Kosten und des erheblichen Entwicklungsaufwands. Stattdessen werden die Übertragungskapazitätsbeschränkungen von CAN häufig durch den Einsatz mehrerer CAN-Busse und Gateways, die eine Kommunikation über Busgrenzen hinweg ermöglichen, gemildert.

### Leistungsengpässe

Der Hauptfaktor, der die Übertragungskapazität von CAN einschränkt, liegt in der Art der Bit-Arbitrierung und der Bestätigung:

- **Arbitrierungsphase:** Während dieser Phase können mehrere Netzknoten gleichzeitig im Sendemodus sein, was eine Mindestbitdauer erfordert, um eine ordnungsgemäße Arbitrierung sicherzustellen.
- **Übertragung des Bestätigungsbits:** Die gleichzeitige Bestätigung durch alle empfangenden Knoten am Ende einer Nachricht erfordert die Berücksichtigung der Ausbreitungsverzögerung über die Buslänge hinweg.

Beispielsweise muss bei einem 40-Meter-CAN-Bus die Bitdauer die Ausbreitungsverzögerung berücksichtigen, was die Datenrate auf maximal 1 Mbit/s begrenzt.

## Einführung in CAN-FD

### Konzept und Motivation

CAN-FD wurde entwickelt, um die Bandbreitenbeschränkungen des klassischen CAN zu überwinden. Die innovative Idee hinter CAN-FD besteht darin, die Datenübertragungsgeschwindigkeit innerhalb einer Nachricht zu variieren. Durch die Nutzung höherer Geschwindigkeiten während des Datenfelds und standardmäßiger Geschwindigkeiten während der Arbitrierungs- und Bestätigungsphasen erhöht CAN-FD die gesamte Datenübertragungsrate erheblich.

### Technische Details

- **Bitratenumschaltung:** CAN-FD ermöglicht den Wechsel zwischen zwei Bitraten: einer niedrigeren Rate für die Arbitrierungs- und Bestätigungsphasen und einer höheren Rate für die Datenphase.
- **Erweiterte Datenlänge:** CAN-FD unterstützt längere Datenrahmen und ermöglicht bis zu 64 Byte pro Rahmen im Vergleich zu den 8 Byte des klassischen CAN.
- **Protokolleffizienz:** Die Fähigkeit, Daten während der Datenphase mit höheren Geschwindigkeiten zu übertragen, verbessert die Effizienz und reduziert die Buslast.

## Vorteile von CAN-FD

### Erhöhte Bandbreite

CAN-FD kann je nach Netzwerkkonfiguration und Hardwarekapazitäten Datenraten von bis zu 8 Mbit/s erreichen, was deutlich höher ist als die des klassischen CAN.

### Kompatibilität und Skalierbarkeit

CAN-FD ist abwärtskompatibel zum klassischen CAN ausgelegt und ermöglicht so einen reibungslosen Übergang und die Integration in bestehende CAN-basierte Netzwerke. Diese Skalierbarkeit macht es zu einer idealen Lösung für moderne Automobilanwendungen, die höhere Datenraten erfordern, ohne eine vollständige Überholung der Netzwerkinfrastruktur.

### Deterministisches Verhalten

Trotz der höheren Datenraten bewahrt CAN-FD das deterministische Verhalten, das für Automobilanwendungen entscheidend ist, und gewährleistet eine zuverlässige und vorhersehbare Kommunikation zwischen kritischen Systemen.

## Schlussfolgerung

CAN-FD stellt einen bedeutenden Fortschritt im CAN-Protokoll dar und adressiert die wachsenden Anforderungen an höhere Bandbreiten und effiziente Datenübertragung in modernen Fahrzeugen. Durch die Integration variabler Bitraten und erweiterter Datenlängen bietet CAN-FD eine robuste Lösung, die die Leistung von Automobilnetzwerken verbessert und gleichzeitig die Kompatibilität mit bestehenden Systemen aufrechterhält. Angesichts der fortschreitenden Entwicklung der Automobiltechnologie ist CAN-FD eine entscheidende Innovation, die sicherstellt, dass die Kommunikation innerhalb von Fahrzeugen effizient, zuverlässig und skalierbar bleibt.