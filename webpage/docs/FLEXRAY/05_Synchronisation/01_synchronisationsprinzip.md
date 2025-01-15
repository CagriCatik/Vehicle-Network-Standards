# Zeit-Synchronisation

FlexRay ist ein hochleistungsfähiges Kommunikationsprotokoll, das speziell für den Einsatz in Fahrzeugnetzwerken entwickelt wurde. Es bietet deterministische und fehlerresistente Datenübertragung und wird häufig in sicherheitskritischen Anwendungen verwendet. Ein entscheidender Aspekt von FlexRay ist die Synchronisation der Knoten innerhalb des Clusters, um eine reibungslose Datenkommunikation zu gewährleisten.

Der reibungslose Ablauf der Datenkommunikation in einem FlexRay-Cluster setzt voraus, dass alle FlexRay-Knoten dasselbe Zeitverständnis haben. Dies ist essenziell, da alle Aktivitäten des Kommunikationssystems durch das Erreichen bestimmter Zeitpunkte ausgelöst werden. Das bedeutet, dass alle Kommunikationszyklen aus der Sicht aller FlexRay-Knoten immer zum selben Zeitpunkt beginnen und gleich lang sind. Ebenso müssen alle statischen Slots der FlexRay-Knoten immer an der gleichen Stelle innerhalb des Zyklus beginnen.

## Herausforderungen der Synchronisation

Ein globales Zeitverständnis ist notwendig, damit alle Knoten synchronisiert arbeiten können. FlexRay basiert auf einer Multi-Master-Architektur, was bedeutet, dass kein einzelner Knoten die absolute Zeit vorgibt. Stattdessen müssen die lokalen Zeitbasen der Knoten kooperativ eine globale Zeitbasis bilden. Diese Synchronisation stellt eine Herausforderung dar, da Frequenztoleranzen und Toleranzen der passiven Bauelemente in der Quarzbeschaltung zu unterschiedlichen Frequenzen und Phasen führen können, selbst wenn die nominale Frequenz identisch ist.

## Toleranzgrenzen und Lebensdauer

Laut FlexRay-Spezifikation dürfen die lokalen Taktgeber über die gesamte Lebensdauer eines Fahrzeugs eine maximale Frequenzabweichung von 1500 ppm (parts per million) nicht überschreiten. Diese Abweichung berücksichtigt mehrere Faktoren:

1. Quarztoleranzen über eine Laufzeit von etwa zehn Jahren (ca. 250 ppm).
2. Toleranzen der passiven Bauelemente in der Quarz-Beschaltung (ähnlich hoch wie die Quarztoleranzen).
3. Ein Sicherheitsfaktor, der die Gesamtfrequenzabweichung auf maximal 1500 ppm begrenzt.

## Algorithmische Synchronisation

Um eine netzwerkweite Zeitbasis herzustellen, ist es notwendig, die lokalen Zeitbasen regelmäßig zu synchronisieren. FlexRay-Knoten verwenden dazu spezielle Algorithmen, die ihre lokalen Uhren korrigieren, sodass alle lokalen Uhren im FlexRay-Cluster bis auf eine definierte Abweichung zu einer globalen Uhr synchron laufen. Es werden zwei Hauptverfahren zur Korrektur verwendet:

- **Phasenkorrektur (Offsetkorrektur)**: Diese Korrektur justiert den Zeitpunkt, zu dem ein Knoten seine lokale Zeitbasis anpasst, um die Differenz zur globalen Zeitbasis zu minimieren.
- **Frequenzkorrektur (Steigungskorrektur)**: Diese Korrektur passt die Geschwindigkeit an, mit der die lokale Uhr läuft, um sicherzustellen, dass die Frequenz der lokalen Uhr mit der globalen Zeitbasis übereinstimmt.
