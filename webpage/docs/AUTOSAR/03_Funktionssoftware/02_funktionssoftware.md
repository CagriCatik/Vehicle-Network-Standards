# Funktionssoftware

Basis für die Konfiguration eines AUTOSAR Steuergerätes ist der ECU Extract of System Description (ECUEX). Hierbei handelt es sich um eine XML-Datei (*.arxml) in einem von AUTOSAR definierten Schema. Sie enthält Vorgaben für die ECU Konfiguration und wird typischerweise vom OEM erzeugt.

Bezüglich des genauen Inhaltes dieser Datei lässt AUTOSAR grundsätzlich einen Freiraum. Das bedeutet, dass bestimmte Inhalte dieser Datei optional sind. Der konkrete Inhalt hängt damit vom OEM ab. Folgende generelle Inhaltsvarianten sind denkbar:

* Netzwerkbeschreibung (Anwendungsfall 1)
* Netzwerkbeschreibung und Softwarekomponenten als Spezifikation (Anwendungsfall 2)
* Netzwerkbeschreibung und implementierte Softwarekomponenten (Anwendungsfall 3)

Auf Basis des ECUEX muss der Tier1 die ECU Configuration Description (ECUC) erzeugen. Darin wird die detaillierte Konfiguration der Basissoftware gespeichert.

In der Übergangszeit werden sicherlich nicht alle Teilnehmer die reine AUTOSAR Methode leben. Deshalb ist es sehr gut vorstellbar, dass in dieser Zeit der Zulieferer von seinem OEM lediglich eine .dbc-, .ldf- oder FIBEX-Datenbasis bekommt und auf dieser Basis die ECUC erzeugen muss.

### Softwarekomponenten

Die Funktionssoftware eines Steuergerätes ist in AUTOSAR über Softwarekomponenten realisiert. Das Kernprinzip besteht darin, eine formale Beschreibung der SWC zu erstellen (SWC Description), aus der sich die C-Schnittstellen der SWC ableiten. Die SWC Description wird in einer XML-Datei in einem von AUTOSAR definierten Schema abgelegt.

Passend zur SWC Description wird die Implementierung der SWC erstellt. Hierbei gibt es folgende Möglichkeiten:

* Manuelle Entwicklung
  Die Implementierung der SWC wird traditionell durch manuelle C-Codierung erstellt.
* Modellbasierte Entwicklung
  Zur Implementierung wird ein Verhaltensmodell der SWC erstellt. Basierend auf diesem Modell wird der C-Code automatisch generiert.

### Hardwareunabhängigkeit

Das AUTOSAR Konzept der SWC zeichnet sich dadurch aus, dass die Implementierung der SWC ausschließlich vom Mikrocontroller unabhängige Schnittstellen hat. Damit sind die technischen Voraussetzungen gegeben, um die SWC auf unterschiedlichen Hardware-Plattformen betreiben zu können und damit eine bessere Wiederverwendung der SWC in verschiedenen Steuergeräten zu erreichen. Selbstverständlich gibt es Randbedingungen, die eine beliebige Inbetriebnahme einer SWC auf jedem beliebigen Steuergerät verhindern. So erscheint es heute nicht sinnvoll, eine Motorsteuerungsfunktion auf einem Türsteuergerät laufen zu lassen, selbst wenn dieses seitens der Schnittstellen möglich wäre.

### Wiederverwendung

Um eine Wiederverwendung in realen Entwicklungsprozessen zu ermöglichen, ist neben der Schnittstellenkompatibilität auch die Absicherung der SWC-Funktion an sich relevant. Dank der definierten Schnittstellen der SWC lassen sich nun auch Testkonzepte wie ein Unit-Test der SWC durchführen. Damit kann eine SWC unabhängig von anderen SWCs entwickelt werden und als in sich getestete Einheit in einer Bibliothek bereitgestellt werden. Dies kann sogar soweit führen, dass eine SWC als COTS erhältlich ist.
