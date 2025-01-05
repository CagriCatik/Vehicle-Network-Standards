## AUTOSAR Schichtenmodell Tutorial

### Einleitung

AUTOSAR (AUTomotive Open System ARchitecture) ist ein weltweit anerkannter Standard, der die Softwarearchitektur für elektronische Steuergeräte (ECUs) im Automobilbereich definiert. Das AUTOSAR-Schichtenmodell ist ein zentrales Konzept dieses Standards und teilt die Softwarearchitektur in verschiedene Abstraktionsschichten auf. Jede Schicht hat ihre eigene spezifische Funktionalität und Interaktionsweise. In diesem Tutorial werden wir das Schichtenmodell detailliert erläutern und auf die einzelnen Komponenten eingehen, wie sie in dem bereitgestellten Bild dargestellt sind.

### Übersicht des Schichtenmodells

Das AUTOSAR-Schichtenmodell besteht aus mehreren Schichten, die die Softwarekomponenten von der Hardware abstrahieren und so eine flexible und wiederverwendbare Softwarearchitektur ermöglichen. Die Hauptschichten sind:

1. **Microcontroller Abstraction Layer (MCAL)**
2. **ECU Abstraction Layer**
3. **Service Layer**
4. **Runtime Environment (RTE)**
5. **Application Layer**

In der Abbildung sehen wir eine spezifische Implementierung für eine Tür-ECU, die Komponenten wie die Steuerung der linken und rechten Tür sowie Türkontakte enthält.

### Microcontroller Abstraction Layer (MCAL)

Die unterste Schicht im AUTOSAR-Schichtenmodell ist die MCAL. Diese Schicht abstrahiert die Hardwaredetails des Mikrocontrollers und bietet standardisierte Schnittstellen zu den höheren Softwareebenen. In der Abbildung ist die MCAL durch den Bereich „Microcontroller“ und „Dio“ (Digital Input/Output) dargestellt.

**Aufgaben der MCAL:**

- Bereitstellung von Treibern für Mikrocontroller-Peripheriegeräte.
- Abstraktion der Hardware, sodass die darüber liegenden Schichten hardwareunabhängig entwickelt werden können.

### ECU Abstraction Layer

Die ECU Abstraction Layer befindet sich über der MCAL und abstrahiert die spezifischen Hardwaredetails der ECU. Sie bietet eine weitere Abstraktionsstufe und ermöglicht die Wiederverwendbarkeit der Software auf unterschiedlichen ECUs.

In der Abbildung wird diese Schicht durch Komponenten wie „IoHwAb“ (Input/Output Hardware Abstraction) repräsentiert.

**Aufgaben der ECU Abstraction Layer:**

- Abstraktion der ECU-spezifischen Hardware.
- Bereitstellung von einheitlichen Schnittstellen für die darüber liegenden Schichten.

### Service Layer

Die Service Layer stellt grundlegende Dienste für die Anwendungsschicht und andere BSW-Schichten bereit. In der Abbildung sind dies Komponenten wie „Com“ (Kommunikation), „PduR“ (Protocol Data Unit Router), „CanIf“ (CAN Interface) und „Can“ (Controller Area Network).

**Aufgaben der Service Layer:**

- Bereitstellung von Netzwerkkommunikationsdiensten.
- Speicher- und Diagnosedienste.
- Abstraktion der Kommunikationsprotokolle.

### Runtime Environment (RTE)

Die RTE ist eine Vermittlungsschicht, die die Interaktion zwischen der Anwendungsschicht und der Basissoftware (BSW) ermöglicht. Sie stellt sicher, dass die Softwarekomponenten unabhängig von der Hardware und den spezifischen Implementierungen der Basissoftware funktionieren können.

**Aufgaben der RTE:**

- Vermittlung der Kommunikation zwischen Softwarekomponenten und Basissoftware.
- Verwaltung der Schnittstellen und Datenkommunikation.

### Application Layer

Die oberste Schicht im AUTOSAR-Schichtenmodell ist die Application Layer. Diese Schicht enthält die eigentlichen Softwarekomponenten, die die spezifischen Funktionen der ECU realisieren. In der Abbildung sind dies die Komponenten „Left Door“, „Right Door“ und „Door Contact“.

**Aufgaben der Application Layer:**

- Implementierung der funktionalen Anforderungen der ECU.
- Nutzung der Dienste, die von den unteren Schichten bereitgestellt werden.

### Detaillierte Analyse der Abbildung

Die Abbildung zeigt eine beispielhafte Implementierung des AUTOSAR-Schichtenmodells für eine Tür-ECU.

- **Left Door, Right Door, Door Contact:** Diese Blöcke repräsentieren die Anwendungskomponenten, die die Steuerungslogik für die Türen und Türkontakte implementieren.
- **RTE:** Die RTE-Schicht, dargestellt in rot, vermittelt die Kommunikation zwischen den Anwendungskomponenten und der Basissoftware.
- **IoHwAb, Dio:** Diese Blöcke repräsentieren die Abstraktionsschichten, die die Hardwarezugriffe der Anwendungskomponenten auf die physische Tür-Hardware ermöglichen.
- **Com, PduR, CanIf, Can:** Diese Blöcke repräsentieren die Kommunikationsdienste, die für die Netzwerkkommunikation der ECU verantwortlich sind.

### Fazit

Das AUTOSAR-Schichtenmodell ist ein essenzielles Konzept für die Entwicklung moderner, modularer und wiederverwendbarer Fahrzeugsoftware. Es ermöglicht eine klare Trennung der Softwarekomponenten und ihrer Funktionen, wodurch die Entwicklung, Wartung und Erweiterung der Software vereinfacht wird. Durch die Verwendung von standardisierten Schnittstellen und Abstraktionsschichten können Softwarekomponenten unabhängig von der zugrunde liegenden Hardware entwickelt und eingesetzt werden.
