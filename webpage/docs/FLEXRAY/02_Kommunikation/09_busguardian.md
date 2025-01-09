# Busguardian

## Kommunikationszyklus und Zeitschlitze

Ein FlexRay-Kommunikationszyklus besteht aus zwei Hauptsegmenten:

1. **Statisches Kommunikationssegment:** Hier sind die Zeitschlitze fest zugewiesen, und jeder Knoten hat spezifische Zeiten, in denen er senden darf.
2. **Dynamisches Kommunikationssegment:** Die Zeitschlitze werden bedarfsabhängig genutzt, was eine größere Flexibilität, aber auch ein höheres Kollisionsrisiko mit sich bringt.

## Die Rolle der Busguardians

Busguardians spielen eine entscheidende Rolle bei der Sicherstellung der Ordnung im Kommunikationsablauf. Sie verhindern, dass FlexRay-Knoten außerhalb ihrer zugewiesenen Zeitschlitze senden und so die Kommunikation stören. Es gibt zwei Haupttypen von Busguardians: lokale und zentrale Busguardians.

## Lokaler Busguardian

Ein lokaler Busguardian ist jedem FlexRay-Transceiver zugeordnet und erlaubt dem Transceiver nur dann, Daten auf den Bus zu senden, wenn dies gemäß dem Kommunikationsplan vorgesehen ist.

## Funktionsweise

- **Zeit- und Kommunikationsplan-Kenntnis:** Der Busguardian muss sowohl den Kommunikationsplan als auch die Zeit im FlexRay-Cluster kennen.
- **Unabhängige Zeitbasis:** Ideal ist es, wenn der Busguardian seine eigene, unabhängige Zeitbasis hat. Dies erhöht die Sicherheit, da der Busguardian unabhängig vom FlexRay-Controller agiert und alle zeitlichen Fehler des Controllers erkennen kann.

## Herausforderungen

Die Implementierung eines lokalen Busguardians erfordert eine ähnliche Komplexität wie die eines FlexRay-Controllers, was die Kosten erhöht. Trotz der theoretischen Vorteile gibt es bisher keine praktischen Implementierungen eines lokalen Busguardians. Die Spezifikation (Version 2.0.9) ist noch vorläufig.

## Zentraler Busguardian

Ein zentraler Busguardian wird auf einem aktiven Sternkoppler platziert. Dieser Ansatz ist ebenfalls noch nicht implementiert und die entsprechende Spezifikation ist ebenfalls in der Version 2.0.9 vorläufig.

## Funktionsweise

- **Kommunikationszweig-Aktivierung:** Innerhalb jedes Kommunikationszyklus aktiviert der zentrale Busguardian nur den Kommunikationszweig, der zu dem Knoten führt, der laut Kommunikationsplan senden darf.
- **Vermeidung von Signalkollisionen:** Durch diese selektive Aktivierung können Signalkollisionen effektiv vermieden werden.
