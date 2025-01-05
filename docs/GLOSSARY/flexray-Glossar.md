# Glossar

## A

## B

### Bus Guardian

Bus Guardian ist eine Funktion im FlexRay-Kommunikationssystem, die aktiv die Integrität und Zuverlässigkeit der Datenkommunikation auf dem FlexRay-Bus überwacht, um potenzielle Fehler oder Anomalien zu erkennen und durch entsprechende Maßnahmen wie Blockieren fehlerhafter Nachrichten oder Auslösen von Warnungen die Sicherheit und Funktionsfähigkeit sicherzustellen.

## C

## D

## E

### ECU-Extract

Das "ECU Extract" ist eine Konfiguration der einzelnen Steuergeräte, die aus der formalen Beschreibung der Softwarefunktionen und Hardwarevoraussetzungen generiert wird und als Basis für die Erstellung der Steuergeräte-Konfigurationen dient, bevor Generatoren lauffähigen Code erzeugen.

## F

### Fault Tolerant Midpoint (FTM)

Der Fault Tolerant Midpoint (FTM) ist ein Algorithmus, der in FlexRay-Netzwerken verwendet wird, um die Synchronisation der lokalen Uhren der einzelnen Knoten innerhalb des Clusters sicherzustellen. Der Zweck des FTM-Algorithmus besteht darin, den Offsetkorrekturwert für die Uhren jedes Knotens zu berechnen, um sicherzustellen, dass alle Knoten den Kommunikationszyklus zum gleichen Zeitpunkt beginnen.

Hier ist eine kurze Erläuterung, wie der FTM-Algorithmus funktioniert:

1. **Sammeln von Zeitdifferenzen**: Jeder FlexRay-Knoten vergleicht die erwarteten Zeitpunkte für den Empfang der Sync-Botschaften mit den tatsächlichen Zeitpunkten, zu denen die Sync-Botschaften eintreffen. Anhand dieser Vergleiche berechnet jeder Knoten eine Liste von Zeitdifferenzen.
2. **Entfernen von Extremwerten**: Der FTM-Algorithmus eliminiert die Extremwerte aus der Liste der Zeitdifferenzen, um zu verhindern, dass stark abweichende lokale Uhren die Berechnung des Offsetkorrekturwerts beeinflussen.
3. **Berechnung des Mittelwerts**: Nachdem die Extremwerte entfernt wurden, werden die verbleibenden Zeitdifferenzen addiert und gemittelt, um den Offsetkorrekturwert zu erhalten.
4. **Anpassung der lokalen Uhr**: Basierend auf dem berechneten Offsetkorrekturwert passen die FlexRay-Knoten ihre lokalen Uhren entsprechend an, um sicherzustellen, dass alle Uhren synchronisiert sind und jeder Knoten den Kommunikationszyklus zum gleichen Zeitpunkt beginnt.

Der FTM-Algorithmus ist ein zentraler Bestandteil der Synchronisationsstrategie in FlexRay-Netzwerken und trägt dazu bei, eine präzise und zuverlässige Datenkommunikation zwischen den Knoten zu gewährleisten.

## I

## M

## R

## S
