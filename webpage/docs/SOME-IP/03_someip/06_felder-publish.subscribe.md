# Felder - Publish/Subscribe

## 3.6 **Felder - Publish/Subscribe in SOME/IP**

Das **Feld-basierte Publish/Subscribe-Modell** in SOME/IP ist eine spezielle Variante des allgemeinen Publish/Subscribe-Modells, die es ermöglicht, Änderungen an bestimmten Datenfeldern in einem Service zu überwachen und an Abonnenten zu verteilen. Dieses Modell unterscheidet sich vom ereignisbasierten Modell dadurch, dass es sich auf die kontinuierliche Überwachung und Übermittlung von Werten einzelner Felder konzentriert, anstatt auf die Benachrichtigung über bestimmte Ereignisse. In diesem Abschnitt wird das feldbasierte Publish/Subscribe-Modell detailliert beschrieben, einschließlich seiner Funktionsweise, der Unterschiede zum ereignisbasierten Modell und der typischen Anwendungen in der Automobilindustrie.

### 3.6.1 **Einführung in das Feld-basierte Publish/Subscribe-Modell**

**Definition und Funktionsweise:**
Im feldbasierten Publish/Subscribe-Modell werden spezifische Datenfelder innerhalb eines Dienstes überwacht und bei Änderungen an interessierte Abonnenten (Subscriber) gesendet. Dies ermöglicht eine feinkörnigere Kontrolle und Überwachung von Daten im Vergleich zum ereignisbasierten Modell, bei dem ganze Ereignisse veröffentlicht werden.

**Hauptmerkmale:**
- **Feldüberwachung:** Bestimmte Felder, die wichtige Daten enthalten, werden kontinuierlich überwacht. Sobald ein Feld aktualisiert wird, wird der neue Wert automatisch an alle registrierten Subscriber gesendet.
- **Feinkörnige Datenkontrolle:** Im Gegensatz zu einem allgemeinen Ereignis, das mehrere Datenwerte umfassen kann, fokussiert sich dieses Modell auf einzelne Felder, wodurch eine präzisere Datenverteilung möglich ist.
- **Asynchrone Kommunikation:** Wie beim ereignisbasierten Modell erfolgt die Kommunikation asynchron, das heißt, der Publisher muss nicht auf eine Rückmeldung der Subscriber warten.

**Diagramm: Feld-basiertes Publish/Subscribe-Muster**

```plaintext
+-------------------------------------------------------------+
|             Feld-basiertes Publish/Subscribe-Muster         |
| +---------------------------------------------------------+ |
| |  Publisher (z.B. Steuergerät)                            | |
| |  - Überwacht Feld: Motortemperatur                      | |
| |  - Veröffentlicht neuen Feldwert bei Änderung           | |
| +---------------------------------------------------------+ |
|               |                              |               |
|               v                              v               |
| +---------------------------------------------------------+ |
| |  Subscriber 1 (z.B. Klimasteuergerät)                    | |
| |  - Abonniert Feld: Passt Lüfterdrehzahl an               | |
+-------------------------------------------------------------+
|               |                              |               |
|               v                              v               |
| +---------------------------------------------------------+ |
| |  Subscriber 2 (z.B. Infotainment-System)                | |
| |  - Abonniert Feld: Zeigt Temperatur an                  | |
+-------------------------------------------------------------+
```

### 3.6.2 **Unterschiede zwischen Feld-basiertem und Ereignis-basiertem Publish/Subscribe**

**Feld-basiertes Modell:**
- **Fokus auf einzelne Datenfelder:** Überwacht und veröffentlicht Änderungen an spezifischen Datenfeldern innerhalb eines Dienstes.
- **Kontinuierliche Überwachung:** Der Zustand eines Feldes wird kontinuierlich überwacht, und jede Änderung wird an die Subscriber weitergegeben.
- **Granularität:** Bietet eine detaillierte, feldspezifische Datenüberwachung und -verteilung.

**Ereignis-basiertes Modell:**
- **Fokus auf gesamte Ereignisse:** Veröffentlicht komplette Ereignisse, die möglicherweise mehrere Datenfelder umfassen.
- **Zustand oder Ereignis:** Abonniert auf die Benachrichtigung von Zustandsänderungen oder spezifischen Ereignissen, die auftreten.
- **Verallgemeinerte Überwachung:** Verfolgt und übermittelt Ereignisse, die mehrere Daten oder Statusänderungen umfassen können.

**Diagramm: Vergleich Feld-basiertes vs. Ereignis-basiertes Modell**

```plaintext
+-------------------------------------------------------------+
|          Vergleich: Feld-basiertes vs. Ereignis-basiertes   |
| +------------------------+-------------------------------+ |
| |  Feld-basiertes Modell   |  Ereignis-basiertes Modell     | |
| +------------------------+-------------------------------+ |
| |  Fokus auf einzelne     |  Fokus auf gesamte Ereignisse  | |
| |  Datenfelder            |  (mehrere Datenfelder)         | |
| +------------------------+-------------------------------+ |
| |  Kontinuierliche        |  Überwachung von Zuständen     | |
| |  Überwachung von Feldern|  und Ereignissen              | |
| +------------------------+-------------------------------+ |
| |  Hohe Granularität      |  Verallgemeinerte Überwachung  | |
| |  (feldspezifisch)       |  (umfasst mehrere Felder)      | |
+-------------------------------------------------------------+
```

### 3.6.3 **Anwendungen des Feld-basierten Publish/Subscribe-Modells in der Automobilindustrie**

**Beispiel 1: Motortemperaturüberwachung**

- **Anwendung:** Das Steuergerät für die Motorsteuerung überwacht kontinuierlich die Motortemperatur. Dieser Wert wird als Feld innerhalb des Dienstes definiert, und Änderungen an diesem Feld werden automatisch an abonnierten Systeme, wie das Klimasteuergerät oder das Infotainment-System, gesendet.
- **Prozess:**
  - **Feldüberwachung:** Das Motorsteuergerät überwacht die aktuelle Motortemperatur.
  - **Publish:** Bei jeder Änderung der Temperatur wird der neue Wert veröffentlicht.
  - **Subscribe:** Das Klimasteuergerät passt die Lüfterdrehzahl basierend auf der neuen Temperatur an, während das Infotainment-System die Temperatur dem Fahrer anzeigt.

**Diagramm: Feld-basiertes Publish/Subscribe für Motortemperatur**

```plaintext
+-------------------------------------------------------------+
|                  Motortemperaturüberwachung                 |
| +---------------------------------------------------------+ |
| |  Publisher (Motorsteuergerät)                            | |
| |  - Überwacht Feld: Motortemperatur                      | |
| |  - Veröffentlicht neuen Feldwert bei Änderung           | |
| +---------------------------------------------------------+ |
|               |                              |               |
|               v                              v               |
| +---------------------------------------------------------+ |
| |  Subscriber 1 (z.B. Klimasteuergerät)                    | |
| |  - Abonniert Feld: Passt Lüfterdrehzahl an               | |
+-------------------------------------------------------------+
|               |                              |               |
|               v                              v               |
| +---------------------------------------------------------+ |
| |  Subscriber 2 (z.B. Infotainment-System)                | |
| |  - Abonniert Feld: Zeigt Temperatur an                  | |
+-------------------------------------------------------------+
```

**Beispiel 2: Batteriestatus in Elektrofahrzeugen**

- **Anwendung:** In einem Elektrofahrzeug überwacht das Batteriemanagementsystem (BMS) kontinuierlich den Ladezustand der Batterie. Der Ladezustand (State of Charge, SoC) ist ein spezifisches Feld, das von verschiedenen Systemen abonniert werden kann, um die Fahrzeugleistung zu optimieren und den Fahrer zu informieren.
- **Prozess:**
  - **Feldüberwachung:** Das BMS überwacht kontinuierlich den Ladezustand der Batterie.
  - **Publish:** Bei Änderungen des SoC wird der neue Wert veröffentlicht.
  - **Subscribe:** Das Antriebssteuergerät nutzt diese Information, um die Fahrzeugleistung anzupassen, während das Infotainment-System den Ladezustand auf dem Display anzeigt.

**Diagramm: Feld-basiertes Publish/Subscribe für Batteriestatus**

```plaintext
+-------------------------------------------------------------+
|                    Batteriestatusüberwachung                |
| +---------------------------------------------------------+ |
| |  Publisher (BMS)                                         | |
| |  - Überwacht Feld: Ladezustand                           | |
| |  - Veröffentlicht neuen Feldwert bei Änderung            | |
| +---------------------------------------------------------+ |
|               |                              |               |
|               v                              v               |
| +---------------------------------------------------------+ |
| |  Subscriber 1 (z.B. Antriebssteuergerät)                 | |
| |  - Abonniert Feld: Passt Fahrzeugleistung an             | |
+-------------------------------------------------------------+
|               |                              |               |
|               v                              v               |
| +---------------------------------------------------------+ |
| |  Subscriber 2 (z.B. Infotainment-System)                | |
| |  - Abonniert Feld: Zeigt Ladezustand an                 | |
+-------------------------------------------------------------+
```

### 3.6.4 **Vorteile des Feld-basierten Publish/Subscribe-Modells**

**1. Granulare Datenkontrolle:**
- Das Modell ermöglicht eine detaillierte Überwachung und Steuerung von spezifischen Datenfeldern, was besonders nützlich in komplexen Systemen ist, in denen einzelne Werte von kritischer Bedeutung sind.

**2. Effiziente Ressourcennutzung:**
- Da nur Änderungen an spezifischen Feldern veröffentlicht werden, wird das Netzwerk nicht mit unnötigen Daten überlastet, was zu einer effizienteren Nutzung der Bandbreite führt.

**3. Verbesserung der Reaktionszeit:**
- Änderungen an kritischen Feldern können sofort an alle relevanten Systeme weitergeleitet werden, was die Reaktionsfähigkeit des Gesamtsystems verbessert.

**4. Vereinfachte Wartung und Erweiterbarkeit:**
- Durch die Trennung von Datenfeldern und deren Überwachung wird die Systemarchitektur modularer, was die Wartung und Erweiterung des Systems erleichtert.

**Diagramm: Vorteile des Feld-basierten Publish/Subscribe-Modells**

```plaintext
+-------------------------------------------------------------+
|               Vorteile des

 Feld-basierten Modells           |
| +---------------------------------------------------------+ |
| |  Granulare Datenkontrolle                                | |
| |  - Detaillierte Überwachung einzelner Werte               | |
| +---------------------------------------------------------+ |
| |  Effiziente Ressourcennutzung                            | |
| |  - Nur relevante Änderungen werden veröffentlicht         | |
| +---------------------------------------------------------+ |
| |  Verbesserung der Reaktionszeit                          | |
| |  - Sofortige Weiterleitung kritischer Änderungen          | |
| +---------------------------------------------------------+ |
| |  Vereinfachte Wartung und Erweiterbarkeit                | |
| |  - Modularere Systemarchitektur                          | |
+-------------------------------------------------------------+
```

### 3.6.5 **Best Practices für die Implementierung des Feld-basierten Publish/Subscribe-Modells**

**1. Auswahl relevanter Felder:**
- Identifizieren und überwachen Sie nur die Felder, die wirklich kritisch für die Anwendung sind, um die Effizienz und Performance des Systems zu maximieren.

**2. Schwellenwerte und Filter implementieren:**
- Implementieren Sie Schwellenwerte und Filter, um sicherzustellen, dass nur signifikante Änderungen an Feldern veröffentlicht werden. Dies reduziert die Anzahl der Nachrichten im Netzwerk und verhindert unnötige Belastungen.

**3. Sicherstellung der Datenkonsistenz:**
- Stellen Sie sicher, dass die Datenkonsistenz zwischen Publisher und Subscriber gewährleistet ist, insbesondere in sicherheitskritischen Anwendungen. Dies kann durch regelmäßige Überprüfungen und Synchronisationen unterstützt werden.

**4. Überwachung und Protokollierung:**
- Implementieren Sie Überwachungs- und Protokollierungssysteme, um sicherzustellen, dass die Feldüberwachung korrekt funktioniert und alle relevanten Änderungen erfasst und verteilt werden.

**Diagramm: Best Practices für Feld-basiertes Publish/Subscribe**

```plaintext
+-------------------------------------------------------------+
|            Best Practices für Feld-basiertes Modell         |
| +---------------------------------------------------------+ |
| |  Auswahl relevanter Felder                               | |
| |  - Nur kritische Felder überwachen und veröffentlichen    | |
| +---------------------------------------------------------+ |
| |  Schwellenwerte und Filter                               | |
| |  - Nur signifikante Änderungen veröffentlichen            | |
| +---------------------------------------------------------+ |
| |  Sicherstellung der Datenkonsistenz                      | |
| |  - Regelmäßige Überprüfungen und Synchronisationen       | |
| +---------------------------------------------------------+ |
| |  Überwachung und Protokollierung                         | |
| |  - Sicherstellen der korrekten Funktion der Feldüberwachung | |
+-------------------------------------------------------------+
```

### 3.6.6 **Zusammenfassung**

Das feldbasierte Publish/Subscribe-Modell in SOME/IP bietet eine detaillierte und effiziente Möglichkeit zur Überwachung und Verteilung von Daten in serviceorientierten Fahrzeugarchitekturen. Durch die gezielte Überwachung und Veröffentlichung von Änderungen an spezifischen Feldern können Automobilingenieure sicherstellen, dass kritische Daten effizient und in Echtzeit an die relevanten Systeme weitergeleitet werden. Die Implementierung von Best Practices hilft, die Systemleistung zu optimieren und eine robuste, skalierbare Architektur zu gewährleisten, die den Anforderungen moderner Fahrzeuge gerecht wird.

---

Dieses Kapitel bietet eine umfassende Analyse des feldbasierten Publish/Subscribe-Modells in SOME/IP und erklärt, wie es in der Automobilindustrie eingesetzt werden kann, um eine granulare Überwachung und Verteilung von kritischen Daten zu ermöglichen. Ingenieure und technische Fachkräfte können diese Informationen nutzen, um leistungsstarke und effiziente Kommunikationssysteme in ihren Fahrzeugprojekten zu entwickeln.