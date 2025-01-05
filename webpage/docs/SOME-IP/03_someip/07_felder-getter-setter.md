# Felder - Getter/Setter

## 3.7 **Felder - Getter/Setter in SOME/IP**

Das **Getter/Setter-Modell** in SOME/IP ist ein grundlegendes Konzept, das verwendet wird, um den Zugriff auf und die Verwaltung von Datenfeldern innerhalb von Diensten zu steuern. Dieses Modell ermöglicht es Diensten, Werte von Feldern sicher zu lesen (Getter) und zu ändern (Setter). In der Automobilindustrie ist dieses Modell besonders wichtig, da es eine kontrollierte Interaktion mit kritischen Systemparametern ermöglicht. In diesem Abschnitt wird das Getter/Setter-Modell detailliert erklärt, einschließlich seiner Anwendung in realen Fahrzeugarchitekturen.

### 3.7.1 **Einführung in das Getter/Setter-Modell**

**Definition und Funktionsweise:**
Das Getter/Setter-Modell in SOME/IP wird verwendet, um den Zugriff auf spezifische Datenfelder innerhalb eines Dienstes zu ermöglichen. Ein **Getter** erlaubt es einem Client, den aktuellen Wert eines Feldes zu lesen, während ein **Setter** es dem Client ermöglicht, den Wert des Feldes zu ändern. Dieses Modell stellt sicher, dass Datenfelder nur durch autorisierte Zugriffe gelesen oder modifiziert werden können und gewährleistet so die Integrität der Systemparameter.

**Hauptmerkmale:**
- **Sicherer Zugriff:** Nur autorisierte Clients können auf bestimmte Datenfelder zugreifen und deren Werte ändern.
- **Datenintegrität:** Durch den kontrollierten Zugriff über Getter und Setter bleibt die Integrität der Datenfelder gewahrt.
- **Kapselung:** Das Modell fördert die Kapselung, indem es direkten Zugriff auf die Daten verhindert und stattdessen definierte Schnittstellen für den Zugriff bereitstellt.

**Diagramm: Getter/Setter-Kommunikationsmuster**

```plaintext
+-------------------------------------------------------------+
|                 Getter/Setter-Muster in SOME/IP             |
| +---------------------------------------------------------+ |
| |  Client (z.B. Steuergerät A)                            | |
| |  - Sendet Getter-Anfrage: Liest aktuellen Wert           | |
| |  - Sendet Setter-Anfrage: Setzt neuen Wert               | |
| +---------------------------------------------------------+ |
|               |                              |               |
|               v                              v               |
| +---------------------------------------------------------+ |
| |  Server (z.B. Steuergerät B)                            | |
| |  - Verarbeitet Getter: Liefert aktuellen Wert           | |
| |  - Verarbeitet Setter: Ändert Feldwert                  | |
+-------------------------------------------------------------+
```

### 3.7.2 **Verwendung des Getter/Setter-Modells in SOME/IP**

**Schritte im Getter/Setter-Prozess:**

1. **Getter-Anfrage:**
   - Der Client sendet eine Anfrage, um den aktuellen Wert eines spezifischen Datenfeldes von einem Server zu lesen. Diese Anfrage enthält die Identifikation des Feldes, das gelesen werden soll.
   
2. **Getter-Verarbeitung:**
   - Der Server empfängt die Getter-Anfrage, liest den aktuellen Wert des angeforderten Feldes und sendet den Wert als Antwort an den Client zurück.
   
3. **Setter-Anfrage:**
   - Der Client sendet eine Anfrage, um den Wert eines spezifischen Datenfeldes zu ändern. Die Anfrage enthält den neuen Wert, der in das Feld geschrieben werden soll.
   
4. **Setter-Verarbeitung:**
   - Der Server empfängt die Setter-Anfrage und aktualisiert das angeforderte Feld mit dem neuen Wert. Der Server kann optional eine Bestätigung an den Client senden.

**Typische Nachrichtenstruktur in SOME/IP:**
- **Getter-Anfrage und -Antwort:**
  - **Header:** Enthält Informationen wie Nachrichtentypen, Service-IDs und Field-IDs.
  - **Payload:** Beinhaltet den aktuellen Wert des angeforderten Feldes.
  
- **Setter-Anfrage und -Bestätigung:**
  - **Header:** Enthält Informationen wie Nachrichtentypen, Service-IDs und Field-IDs.
  - **Payload:** Beinhaltet den neuen Wert, der im Feld gesetzt werden soll.

### 3.7.3 **Beispiele für das Getter/Setter-Modell in der Automobilindustrie**

**Beispiel 1: Steuerung der Klimaanlage**

- **Anwendung:** Ein Steuergerät für die Klimaanlage in einem Fahrzeug verwendet das Getter/Setter-Modell, um die gewünschte Temperatur zu lesen und zu ändern. Der Fahrer kann über die Benutzeroberfläche eine neue Zieltemperatur einstellen, die dann an das Steuergerät übermittelt wird.
- **Prozess:**
  - **Getter:** Der Client (z.B. Benutzeroberfläche) liest den aktuellen Sollwert der Temperatur vom Klimaanlagensteuergerät.
  - **Setter:** Der Client sendet einen neuen Sollwert für die Temperatur, um die Klimaanlage entsprechend anzupassen.

**Diagramm: Getter/Setter für Klimaanlage**

```plaintext
+-------------------------------------------------------------+
|                Steuerung der Klimaanlage                    |
| +---------------------------------------------------------+ |
| |  Client (z.B. Benutzeroberfläche)                       | |
| |  - Sendet Getter: Liest aktuelle Solltemperatur          | |
| |  - Sendet Setter: Setzt neue Solltemperatur              | |
| +---------------------------------------------------------+ |
|               |                              |               |
|               v                              v               |
| +---------------------------------------------------------+ |
| |  Server (z.B. Klimaanlagensteuergerät)                  | |
| |  - Verarbeitet Getter: Sendet aktuelle Solltemperatur    | |
| |  - Verarbeitet Setter: Ändert Solltemperatur             | |
+-------------------------------------------------------------+
```

**Beispiel 2: Anpassung der Fahrmodi in einem Elektrofahrzeug**

- **Anwendung:** In einem Elektrofahrzeug kann der Fahrer den Fahrmodus (z.B. Eco, Sport, Comfort) ändern, um die Fahrzeugdynamik anzupassen. Das Steuergerät für das Fahrverhalten verwendet das Getter/Setter-Modell, um den aktuellen Fahrmodus zu lesen und einen neuen Fahrmodus festzulegen.
- **Prozess:**
  - **Getter:** Der Client liest den aktuellen Fahrmodus vom Steuergerät.
  - **Setter:** Der Client setzt einen neuen Fahrmodus basierend auf der Auswahl des Fahrers.

**Diagramm: Getter/Setter für Fahrmodi**

```plaintext
+-------------------------------------------------------------+
|                  Anpassung der Fahrmodi                     |
| +---------------------------------------------------------+ |
| |  Client (z.B. Fahrmodus-Schalter)                       | |
| |  - Sendet Getter: Liest aktuellen Fahrmodus              | |
| |  - Sendet Setter: Setzt neuen Fahrmodus                  | |
| +---------------------------------------------------------+ |
|               |                              |               |
|               v                              v               |
| +---------------------------------------------------------+ |
| |  Server (z.B. Fahrverhaltenssteuergerät)                | |
| |  - Verarbeitet Getter: Sendet aktuellen Fahrmodus       | |
| |  - Verarbeitet Setter: Ändert Fahrmodus                 | |
+-------------------------------------------------------------+
```

### 3.7.4 **Vorteile des Getter/Setter-Modells**

**1. Kontrollierter Datenzugriff:**
- Das Getter/Setter-Modell stellt sicher, dass nur autorisierte Clients auf bestimmte Datenfelder zugreifen und diese ändern können, was die Sicherheit und Integrität des Systems erhöht.

**2. Kapselung und Modularität:**
- Die Verwendung von Getter- und Setter-Methoden fördert die Kapselung, da direkte Zugriffe auf Datenfelder vermieden werden. Dies führt zu einer modulareren und wartungsfreundlicheren Systemarchitektur.

**3. Flexibilität und Anpassungsfähigkeit:**
- Das Modell ermöglicht eine flexible Anpassung der Systemparameter durch einfaches Lesen und Ändern von Feldern, ohne dass tiefe Eingriffe in die Systemarchitektur erforderlich sind.

**4. Unterstützung für Remote-Interaktionen:**
- Der Zugriff auf Felder über Getter und Setter kann auch über Netzwerke hinweg erfolgen, was die Interoperabilität und die Fernsteuerung von Fahrzeugfunktionen erleichtert.

**Diagramm: Vorteile des Getter/Setter-Modells**

```plaintext
+-------------------------------------------------------------+
|                   Vorteile des Getter/Setter-Modells        |
| +---------------------------------------------------------+ |
| |  Kontrollierter Datenzugriff                            | |
| |  - Nur autorisierte Clients können auf Daten zugreifen   | |
| +---------------------------------------------------------+ |
| |  Kapselung und Modularität                              | |
| |  - Förderung einer wartungsfreundlichen Systemarchitektur | |
| +---------------------------------------------------------+ |
| |  Flexibilität und Anpassungsfähigkeit                   | |
| |  - Einfache Anpassung von Systemparametern               | |
| +---------------------------------------------------------+ |
| |  Unterstützung für Remote-Interaktionen                 | |
| |  - Ermöglicht Fernsteuerung und Interoperabilität        | |
+-------------------------------------------------------------+
```

### 3.7.5 **Best Practices für die Implementierung des Getter/Setter-Modells**

**1. Zugriffskontrollen implementieren:**
- Stellen Sie sicher, dass nur autorisierte Clients Zugriff auf die Getter und Setter für sicherheitskritische oder sensitive Felder haben. Dies kann durch Authentifizierungs- und Autorisierungsmechanismen erreicht werden.

**2. Datenvalidierung in Settern:**
- Implementieren Sie in den Setter-Methoden eine gründliche Datenvalidierung, um sicherzustellen, dass nur gültige und zulässige Werte in die Felder geschrieben werden.

**3. Effiziente Kommunikation sicherstellen:**
- Optimieren Sie die Kommunikation zwischen Clients und Servern, um sicherzustellen, dass die Anfragen für Getter und Setter minimalen Overhead haben und die Systemressourcen effizient nutzen.

**4. Logging und Überwachung:**
- Führen Sie Protokollierungs- und Überwachungsmechanismen ein,

 um den Zugriff auf Getter und Setter zu verfolgen und potenzielle Missbrauchsfälle oder Fehler zu erkennen.

**Diagramm: Best Practices für Getter/Setter**

```plaintext
+-------------------------------------------------------------+
|               Best Practices für Getter/Setter              |
| +---------------------------------------------------------+ |
| |  Zugriffskontrollen implementieren                      | |
| |  - Authentifizierungs- und Autorisierungsmechanismen     | |
| +---------------------------------------------------------+ |
| |  Datenvalidierung in Settern                            | |
| |  - Sicherstellen der Datenintegrität durch Validierung   | |
| +---------------------------------------------------------+ |
| |  Effiziente Kommunikation                               | |
| |  - Minimaler Overhead bei Anfragen und Antworten         | |
| +---------------------------------------------------------+ |
| |  Logging und Überwachung                                | |
| |  - Verfolgen und Überwachen von Zugriffen auf Datenfelder | |
+-------------------------------------------------------------+
```

### 3.7.6 **Zusammenfassung**

Das Getter/Setter-Modell in SOME/IP bietet eine strukturierte und sichere Methode zur Verwaltung und zum Zugriff auf Datenfelder innerhalb von Fahrzeugdiensten. Es fördert die Kapselung und Modularität der Systemarchitektur und stellt sicher, dass Systemparameter nur durch autorisierte Zugriffe geändert werden können. Durch die Implementierung von Best Practices können Ingenieure sicherstellen, dass ihre Systeme sowohl sicher als auch effizient arbeiten und den Anforderungen moderner Fahrzeuge gerecht werden.

---

Dieses Kapitel bietet eine detaillierte Analyse des Getter/Setter-Modells in SOME/IP und zeigt auf, wie es in der Automobilindustrie eingesetzt werden kann, um eine kontrollierte und sichere Interaktion mit Fahrzeugdiensten zu gewährleisten. Ingenieure und technische Fachkräfte können diese Informationen nutzen, um robuste und sichere Kommunikationssysteme in ihren Fahrzeugprojekten zu entwickeln.