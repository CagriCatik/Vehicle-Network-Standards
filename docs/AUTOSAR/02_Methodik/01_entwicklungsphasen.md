# AUTOSAR-Methodik

## Einleitung

AUTOSAR (AUTomotive Open System ARchitecture) ist eine standardisierte Plattform für die Entwicklung und Konfiguration von Steuergerätesoftware in der Automobilindustrie. Dieses Tutorial bietet eine detaillierte Einführung in die AUTOSAR-Methodik, Architektur und die Konfiguration von Steuergeräten. Wir werden die einzelnen Schritte kritisch beleuchten und sicherstellen, dass jede Information korrekt und präzise vermittelt wird.

## Methodik

Die AUTOSAR-Methodik unterteilt den Entwicklungsprozess von Steuergerätesoftware in klar definierte Aktionen und standardisiert den Datenaustausch zwischen den Entwicklungspartnern. Dies wird durch den Einsatz von XML-Dateien erreicht, die eine einheitliche Kommunikationsbasis bieten.

1. **Systementwurf**:
   - **Architektur der Anwendung**: Der erste Schritt besteht darin, die Systemarchitektur festzulegen. Dies umfasst die Definition von Softwarekomponenten (SWCs) und deren Zuordnung zu den Steuergeräten. Dabei wird auch die Netzwerkkommunikation bestimmt.
   - **System Description**: Das Ergebnis des Systementwurfs ist die System Description, eine AUTOSAR XML-Datei. Diese Datei bildet die Grundlage für den spezifischen ECU Extract of System Description, der für jedes Steuergerät erzeugt wird.

## Architektur

Die Architektur in AUTOSAR basiert auf einem mehrschichtigen Modell, das die Trennung von Applikations- und Basissoftware ermöglicht.

1. **Software-Komponenten (SWCs)**:

   - SWCs sind modular und bieten definierte Schnittstellen, die in den SWC Descriptions beschrieben werden.
   - Diese Modularität erlaubt es, die SWCs unabhängig voneinander zu entwickeln und zu testen, was die Zusammenarbeit zwischen OEMs und Tier1-Zulieferern erleichtert.
2. **RTE (Runtime Environment)**:

   - Die RTE stellt die Verbindung zwischen den SWCs und der Basissoftware her. Sie wird für jedes Steuergerät spezifisch generiert, basierend auf der System Description und der ECU Configuration Description.

## Konfiguration des Steuergeräts

1. **Implementierung der SWCs**:

   - In dieser Phase werden die SWCs gemäß den in den SWC Descriptions festgelegten Schnittstellen implementiert.
2. **Konfiguration von BSW und RTE**:

   - Die Basissoftware (BSW) und die RTE werden konfiguriert. Dies beinhaltet die Anpassung der BSW-Module an die spezifischen Anforderungen des Projekts.
   - **ECU Configuration Description**: Das Ergebnis der Konfiguration ist eine ECU Configuration Description (AUTOSAR XML-Datei), die auf den ECU Extract of System Description abgestimmt ist.
3. **Code-Generierung**:

   - Basierend auf der ECU Configuration Description wird die Basissoftware durch den Einsatz von Codegeneratoren erzeugt oder angepasst.
   - Auch die RTE wird spezifisch für das jeweilige Steuergerät generiert.

## Anwendung

Die Applikationsentwicklung kann unabhängig von der Konfiguration der Steuergeräte betrachtet werden.

1. **SWC Descriptions**:
   - Die Schnittstellen der SWCs werden in den SWC Descriptions beschrieben. Dies ermöglicht eine unabhängige Implementierung und Testung der SWCs.
   - **Zusammenspiel der Komponenten**: Durch die standardisierten Schnittstellen können Applikationskomponenten von verschiedenen Entwicklungsparteien (OEMs und Tier1) einfach integriert und miteinander kombiniert werden.

## Fazit

Die AUTOSAR-Methodik bietet eine strukturierte und standardisierte Vorgehensweise für die Entwicklung von Steuergerätesoftware. Durch die klare Trennung von Systementwurf, Konfiguration und Applikationsentwicklung wird eine hohe Flexibilität und Wiederverwendbarkeit der Softwarekomponenten erreicht. Die Verwendung von XML-Dateien für den Datenaustausch gewährleistet eine einheitliche und transparente Kommunikation zwischen allen Beteiligten im Entwicklungsprozess.

Dieses Tutorial hat die wichtigsten Aspekte der AUTOSAR-Methodik detailliert und wissenschaftlich fundiert erläutert. Bei der Implementierung in der Praxis ist es entscheidend, die Vorgaben und Standards von AUTOSAR genau zu beachten, um die gewünschten Vorteile in Bezug auf Modularität, Wiederverwendbarkeit und Effizienz zu erzielen.
