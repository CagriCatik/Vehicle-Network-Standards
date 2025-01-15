
# Synchronisation

FlexRay ist ein deterministisches und fehlertolerantes Kommunikationssystem, das speziell für die hohen Anforderungen in der Fahrzeugelektronik entwickelt wurde. Ein wesentlicher Bestandteil von FlexRay ist die Synchronisation der lokalen Uhren innerhalb eines FlexRay Clusters, um eine präzise und koordinierte Kommunikation zu gewährleisten. In diesem Tutorial werden wir die Mechanismen und Algorithmen zur Uhrensynchronisation in FlexRay Clustern detailliert erläutern.

## Grundprinzip der Synchronisation

Die Synchronisation in einem FlexRay Cluster basiert darauf, dass alle Knoten (Nodes) die Sende- und Empfangszeitpunkte der statischen Botschaften im Voraus kennen. Dies ermöglicht es jedem Knoten, sowohl den Zeitversatz (Offset) als auch die Frequenzabweichung (Steigung) zu korrigieren, sodass nach wenigen Kommunikationszyklen alle Knoten synchronisiert sind.

## Synchronisationsknoten (Sync-Nodes)

In einem FlexRay Cluster gibt es mindestens 2 und maximal 15 Sync-Nodes, die in jedem Kommunikationszyklus eine Synchronisationsbotschaft (Sync-Botschaft) in einem festgelegten statischen Slot senden. Diese Botschaften sind keine zusätzlichen Nachrichten, sondern reguläre statische Botschaften, bei denen der Sync Frame Indicator gesetzt ist. Diese Sync-Botschaften sind entscheidend für die Synchronisation der Uhren im Cluster.

## Zeitabgleich und Offsetkorrektur

Jeder FlexRay Knoten vergleicht die vorab bekannten Zeitpunkte der Sync-Botschaften mit den tatsächlichen Empfangszeitpunkten. Aus den Differenzen dieser Zeitpunkte wird eine sortierte Liste erstellt. Die Berechnung des Offsetkorrekturwerts erfolgt durch den Fault Tolerant Midpoint (FTM) Algorithmus.

1. **Fault Tolerant Midpoint (FTM) Algorithmus:**
   - Bei bis zu sieben Sync-Nodes werden die Extremwerte (Minimum und Maximum) aus der Liste entfernt.
   - Bei mehr als sieben Sync-Nodes werden zusätzlich die zweitgrößten und zweitkleinsten Werte entfernt.
   - Die verbleibenden Werte werden addiert und gemittelt, um den Offsetkorrekturwert zu bestimmen.

Diese Methode stellt sicher, dass stark abweichende lokale Uhren die Synchronisation nicht stören.

## Steigungskorrektur

Die Steigungskorrektur erfolgt ähnlich der Offsetkorrektur, jedoch messen die FlexRay Knoten hierbei die Länge der Kommunikationszyklen. Der FTM Algorithmus wird auch hier angewendet, um einen robusten Mittelwert zu berechnen, der die Zykluslänge anpasst.

## Korrekturmechanismen

- **Offsetkorrektur:**

  - Ein Knoten gleicht den Offset durch Hinzufügen oder Entfernen einer bestimmten Anzahl von Mikroticks (kleinste Zeiteinheit) in der Network Idle Time (NIT) am Ende jedes ungeraden Zyklus aus. Dies verschiebt den Start des nächsten Zyklus und passt die lokale Uhr an die globalen Anforderungen an.
- **Steigungskorrektur:**

  - Die Steigungskorrektur verteilt die Anpassung gleichmäßig über gerade und ungerade Zyklen, um eine gleichmäßige Frequenzanpassung zu gewährleisten. Dadurch wird verhindert, dass die Steigungskorrektur wie eine zusätzliche Offsetkorrektur wirkt.

