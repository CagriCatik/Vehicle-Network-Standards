# AUTOSAR Classic vs. AUTOSAR Adaptive

## 2.5 **AUTOSAR Classic vs. AUTOSAR Adaptive**

Die AUTOSAR-Architektur (AUTomotive Open System ARchitecture) ist ein wesentlicher Standard in der Automobilindustrie, der darauf abzielt, die Entwicklung von Software für elektronische Steuergeräte (ECUs) zu standardisieren und zu vereinfachen. AUTOSAR existiert in zwei Hauptvarianten: **AUTOSAR Classic** und **AUTOSAR Adaptive**. Diese beiden Plattformen sind auf unterschiedliche Anforderungen und Anwendungsbereiche ausgerichtet. In diesem Abschnitt werden die Unterschiede zwischen AUTOSAR Classic und AUTOSAR Adaptive detailliert erläutert, wobei der Fokus auf ihren jeweiligen Architekturen, Anwendungsfällen und unterstützten Applikationen liegt. Darüber hinaus wird der Übergang von Classic zu Adaptive und dessen Auswirkungen auf Automobilhersteller und Zulieferer diskutiert.

### 2.5.1 **Überblick über AUTOSAR Classic und AUTOSAR Adaptive**

**AUTOSAR Classic:**
AUTOSAR Classic ist die ursprüngliche Version der AUTOSAR-Plattform und wurde entwickelt, um die Entwicklung von softwaredefinierten Fahrzeugfunktionen in eingebetteten Systemen zu standardisieren. Es richtet sich hauptsächlich an ECUs mit festgelegten Echtzeit-Anforderungen, die in sicherheitskritischen Anwendungen wie Motorsteuerung, Bremsen und Fahrdynamik eingesetzt werden.

**AUTOSAR Adaptive:**
AUTOSAR Adaptive ist eine neuere Plattform, die entwickelt wurde, um die steigenden Anforderungen moderner, vernetzter und hochgradig automatisierter Fahrzeuge zu erfüllen. Sie bietet eine flexible, serviceorientierte Architektur (SOA), die für komplexe Anwendungen wie autonomes Fahren, V2X-Kommunikation und Infotainment optimiert ist.

### 2.5.2 **Vergleich der Architekturen**

**AUTOSAR Classic Architektur:**

- **Schichtenmodell:** AUTOSAR Classic verwendet eine klassische, schichtenbasierte Architektur, die aus dem Basis-Softwarestack (BSW), der Laufzeitumgebung (RTE) und den Anwendungsschichten besteht.
  
  - **Basissoftware (BSW):** Umfasst grundlegende Softwarekomponenten, die direkt mit der Hardware interagieren, einschließlich der Abstraktionsschichten und der Kommunikationsdienste.
  
  - **RTE (Runtime Environment):** Vermittelt zwischen den Anwendungssoftwarekomponenten und der Basissoftware, um eine hardwareunabhängige Entwicklung zu ermöglichen.
  
  - **Applikationsschicht:** Besteht aus den eigentlichen funktionalen Softwaremodulen, die spezifische Fahrzeugfunktionen implementieren.

- **Konfiguration und statische Verbindungen:** Die Softwarearchitektur in AUTOSAR Classic ist weitgehend statisch, was bedeutet, dass die Softwarekonfiguration im Voraus definiert und zur Compile-Zeit festgelegt wird. Dies sorgt für eine hohe Determinismus und Echtzeitfähigkeit.

- **Echtzeit-Anforderungen:** Die Architektur ist optimiert für Echtzeit- und sicherheitskritische Anwendungen, bei denen eine zuverlässige und zeitgerechte Ausführung der Software essenziell ist.

**Diagramm: AUTOSAR Classic Architektur**

```plaintext
+-------------------------------------------------------------+
|                 AUTOSAR Classic Architektur                 |
| +---------------------------------------------------------+ |
| |  Anwendungsschicht                                      | |
| |  - Softwarekomponenten (SWC)                            | |
| +---------------------------------------------------------+ |
| |  RTE (Runtime Environment)                               | |
| +---------------------------------------------------------+ |
| |  Basissoftware (BSW)                                     | |
| |  - Microcontroller Abstraction Layer (MCAL)             | |
| |  - ECU Abstraction Layer                                 | |
| |  - Complex Drivers                                       | |
+-------------------------------------------------------------+
|                 Hardware (Microcontroller, Sensoren)         |
+-------------------------------------------------------------+
```

**AUTOSAR Adaptive Architektur:**

- **Serviceorientierte Architektur (SOA):** AUTOSAR Adaptive basiert auf einer flexiblen und dynamischen serviceorientierten Architektur, die es ermöglicht, Dienste zur Laufzeit zu registrieren, zu entdecken und aufzurufen.

  - **Adaptive Platform Foundation:** Stellt grundlegende Funktionen wie Kommunikation, Persistenz, Sicherheit und Update-Mechanismen bereit.
  
  - **Adaptive Application Layer:** Beinhaltet die Applikationen und Dienste, die auf der Adaptive Platform ausgeführt werden. Diese können dynamisch gestartet und gestoppt werden, basierend auf den Anforderungen des Systems.

- **Dynamische Konfiguration:** Im Gegensatz zu AUTOSAR Classic ist die Architektur von AUTOSAR Adaptive dynamisch. Das bedeutet, dass Softwaremodule und Dienste zur Laufzeit konfiguriert und angepasst werden können. Dies ist besonders wichtig für Anwendungen, die sich im Laufe der Zeit ändern oder erweiterbar sein müssen, wie z. B. durch OTA-Updates.

- **Mehrkern- und Multithreading-Unterstützung:** Die Plattform unterstützt moderne Multicore-Prozessoren und ermöglicht die parallele Ausführung von Softwarekomponenten, was die Leistung für rechenintensive Aufgaben verbessert.

- **Integration von Standardtechnologien:** AUTOSAR Adaptive integriert moderne IT-Standards wie POSIX-kompatible Betriebssysteme, C++ und IP-basierte Kommunikationsprotokolle wie SOME/IP und DDS.

**Diagramm: AUTOSAR Adaptive Architektur**

```plaintext
+-------------------------------------------------------------+
|                 AUTOSAR Adaptive Architektur                |
| +---------------------------------------------------------+ |
| |  Adaptive Application Layer                             | |
| |  - Dienste und Anwendungen (SOA)                        | |
| +---------------------------------------------------------+ |
| |  Adaptive Platform Foundation                           | |
| |  - Kommunikation (SOME/IP, DDS)                         | |
| |  - Persistenz, Sicherheit                               | |
| |  - Update-Mechanismen (OTA)                             | |
+-------------------------------------------------------------+
|         POSIX-kompatibles Betriebssystem (Linux, QNX)       |
+-------------------------------------------------------------+
|                 Hardware (Multicore-Prozessoren)            |
+-------------------------------------------------------------+
```

### 2.5.3 **Vergleich der Anwendungsfälle**

**Anwendungsfälle für AUTOSAR Classic:**

- **Echtzeit- und sicherheitskritische Systeme:**
  - Anwendungen, die strikte Echtzeit-Anforderungen und hohe Sicherheitsstandards erfordern, wie z. B. Motorsteuerungen, Bremssysteme, Airbag-Steuerungen und Fahrdynamikregelungen, sind typischerweise auf AUTOSAR Classic angewiesen.
  
- **Deterministische Steuerungen:**
  - Systeme, bei denen eine deterministische Ausführung der Software von höchster Wichtigkeit ist, nutzen die statische Konfiguration und feste Verbindungen von AUTOSAR Classic.

- **Integration in traditionelle Fahrzeugarchitekturen:**
  - AUTOSAR Classic ist ideal für die Integration in bestehende Fahrzeugplattformen, die auf etablierten ECU-Architekturen basieren.

**Anwendungsfälle für AUTOSAR Adaptive:**

- **Autonomes Fahren:**
  - AUTOSAR Adaptive unterstützt die komplexen Rechenanforderungen autonomer Fahrzeuge, einschließlich Sensorfusion, künstliche Intelligenz und maschinelles Lernen, sowie die Fähigkeit zur dynamischen Anpassung und Update der Software während der Laufzeit.

- **V2X-Kommunikation und vernetzte Dienste:**
  - Adaptive Plattformen sind besonders gut geeignet für V2X-Kommunikation (Vehicle-to-Everything) und vernetzte Fahrzeugdienste, die hohe Bandbreiten und die Integration externer Dienste erfordern.

- **Infotainment- und Komfortsysteme:**
  - Die dynamischen und flexiblen Konfigurationsmöglichkeiten der Adaptive Plattform ermöglichen die Implementierung komplexer Infotainment- und Komfortsysteme, die regelmäßig aktualisiert und erweitert werden können.

- **OTA-Updates und Cybersecurity:**
  - Fahrzeuge, die OTA-Updates und fortschrittliche Cybersicherheitsmaßnahmen erfordern, profitieren von der Flexibilität und den Sicherheitsfunktionen, die AUTOSAR Adaptive bietet.

### 2.5.4 **Übergang von AUTOSAR Classic zu AUTOSAR Adaptive**

Der Übergang von AUTOSAR Classic zu AUTOSAR Adaptive stellt sowohl für Fahrzeughersteller als auch für Zulieferer eine signifikante Veränderung dar. Dieser Übergang ist notwendig, um den Anforderungen moderner Fahrzeuge gerecht zu werden, die eine höhere Rechenleistung, flexible Softwarearchitekturen und dynamische Systemkonfigurationen erfordern.

**Herausforderungen beim Übergang:**

- **Koexistenz von Classic und Adaptive:**
  - In der Übergangsphase müssen viele Fahrzeuge sowohl AUTOSAR Classic als auch AUTOSAR Adaptive unterstützen, was die Integration beider Plattformen innerhalb desselben Fahrzeugs erfordert. Dies kann durch die Verwendung von Gateways und Middleware-Lösungen erleichtert werden, die eine nahtlose Kommunikation zwischen den beiden Plattformen ermöglichen.

- **Migration von Softwarekomponenten:**
  - Bestehende Softwarekomponenten, die auf AUTOSAR Classic basieren, müssen möglicherweise auf AUTOSAR Adaptive migriert werden. Dies erfordert eine gründliche Planung, da die beiden Plattformen unterschiedliche Entwicklungsansätze und Laufzeitumgebungen verwenden.

- **Schulung und Umschulung:**
  - Entwickler und Ingenieure müssen in den neuen Technologien und Methoden von AUTOSAR Adaptive geschult werden. Dies umfasst nicht nur die Verwendung von neuen Programmiersprachen und Werkzeugen, sondern auch das Verständnis von serviceorientierten Architekturen und dynamischen Systemkonfigurationen.

**Vorteile des Übergangs:**

- **Zukunftssicherheit:**
  - AUTOSAR Adaptive bietet eine zukunftssichere Plattform, die für die Anforderungen der nächsten Generation von Fahrzeugen entwickelt wurde, einschließlich autonomer Systeme und vernetzter Dienste.

- **Erhöhte Flexibilität und Anpassungsfähigkeit:**
 

 - Die dynamische Natur von AUTOSAR Adaptive ermöglicht es, neue Funktionen und Dienste schnell zu integrieren und auf veränderte Marktanforderungen zu reagieren.

- **Skalierbarkeit und Multicore-Unterstützung:**
  - Die Plattform ist für moderne Mehrkernprozessoren optimiert und ermöglicht es, rechenintensive Anwendungen parallel auszuführen, was zu einer höheren Systemleistung und Effizienz führt.

### 2.5.5 **Zusammenfassung**

AUTOSAR Classic und AUTOSAR Adaptive sind zwei verschiedene Plattformen, die auf die spezifischen Anforderungen unterschiedlicher Fahrzeuganwendungen ausgerichtet sind. Während AUTOSAR Classic ideal für sicherheitskritische, echtzeitfähige Systeme mit festen Anforderungen ist, bietet AUTOSAR Adaptive die Flexibilität und Dynamik, die für moderne, vernetzte und autonome Fahrzeuge erforderlich ist. Der Übergang von Classic zu Adaptive stellt eine große Herausforderung dar, bietet jedoch enorme Vorteile für die zukünftige Fahrzeugentwicklung, indem er eine skalierbare, flexible und zukunftssichere Plattform bereitstellt, die den steigenden Anforderungen an Software- und Fahrzeugarchitekturen gerecht wird.

---

Dieses Kapitel bietet eine detaillierte Analyse der Unterschiede zwischen AUTOSAR Classic und AUTOSAR Adaptive und beleuchtet die spezifischen Anwendungsfälle, für die jede Plattform am besten geeignet ist. Es dient als Leitfaden für Ingenieure und technische Fachkräfte, die die Implementierung dieser Plattformen in ihren Projekten planen und den Übergang von klassischen zu modernen, serviceorientierten Architekturen in der Automobilindustrie bewältigen möchten.