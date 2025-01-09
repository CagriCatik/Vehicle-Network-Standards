# Kommunikationsarchitektur

## FlexRay Knoten und Topologien

Ein FlexRay-Cluster setzt sich aus mehreren FlexRay-Knoten zusammen, die durch ein physikalisches Übertragungsmedium verbunden sind. FlexRay unterstützt verschiedene Topologien:

- **Punkt-zu-Punkt-Verbindung**: Direkte Verbindung zwischen zwei Knoten.
- **Linientopologie**: Mehrere Knoten sind in einer Linie verbunden.
- **Passive Sterntopologie**: Knoten sind sternförmig um einen passiven Hub angeordnet.
- **Aktive Sterntopologie**: Knoten sind sternförmig um einen aktiven Hub angeordnet, der Signale verstärken und weiterleiten kann.

## Redundanz und Datenrate

FlexRay bietet die Möglichkeit der redundanten Auslegung des Kommunikationskanals, um das Ausfallrisiko zu minimieren. Jeder der beiden Kommunikationskanäle (Channel A und Channel B) kann unabhängig mit einer Datenrate von bis zu 10 MBit/s betrieben werden. Alternativ können beide Kanäle kombiniert werden, um die Datenrate auf bis zu 20 MBit/s zu erhöhen. Dies bietet eine flexible Wahl zwischen Fehlertoleranz und erhöhter Übertragungsrate für jede einzelne FlexRay-Botschaft.

## Zeitgesteuerte Kommunikationsarchitektur

FlexRay basiert auf einer zeitgesteuerten Kommunikationsarchitektur. Dies bedeutet, dass alle Aktionen im System zu festgelegten Zeitpunkten aktiviert werden. Diese Eigenschaft ermöglicht eine deterministische Datenkommunikation, die besonders wichtig für sicherheitskritische Anwendungen ist.

## TDMA-Verfahren

Das Time Division Multiple Access (TDMA)-Verfahren ist das Kernprinzip von FlexRay. Im Gegensatz zu anderen Kommunikationsprotokollen wie CAN, bei denen der Buszugriff ereignisgesteuert erfolgt, basiert FlexRay auf einem strikten Zeitplan. Jeder Knoten im Netzwerk erhält zu festgelegten Zeitpunkten Zugriff auf den Bus, was durch einen Kommunikationsablaufplan (Schedule) definiert wird. Dieser Plan ordnet jeder FlexRay-Botschaft einen spezifischen Zeitschlitz in jedem Kommunikationszyklus zu.

## Kommunikationsablaufplan und TDMA-Prinzip

Ein typischer Kommunikationsablaufplan für ein FlexRay-System kann beispielsweise wie folgt aussehen:

1. **Kommunikationszyklus**: Der gesamte Kommunikationszyklus ist in mehrere statische und dynamische Segmente unterteilt.

   - **Statisches Segment**: In diesem Segment werden Nachrichten in festgelegten Zeitschlitzen gesendet. Jeder Knoten sendet in seinem zugewiesenen Zeitschlitz, was eine deterministische Kommunikation gewährleistet.
   - **Dynamisches Segment**: Hier können Nachrichten flexibler gesendet werden, was eine höhere Effizienz bei der Busauslastung ermöglicht.
2. **Beispielhafter Ablauf**: Angenommen, ein Kommunikationssystem besteht aus vier Knoten (A, B, C, D). Der Kommunikationsplan könnte vorsehen, dass:

   - Knoten A sendet seine Botschaften in den Zeitschlitzen 1 und 5.
   - Knoten B sendet in den Zeitschlitzen 2 und 6.
   - Knoten C sendet in den Zeitschlitzen 3 und 7.
   - Knoten D sendet in den Zeitschlitzen 4 und 8.

Durch diesen präzisen Zeitplan wird sichergestellt, dass keine Kollisionen auf dem Bus auftreten und jede Nachricht deterministisch und zeitgerecht übermittelt wird.

