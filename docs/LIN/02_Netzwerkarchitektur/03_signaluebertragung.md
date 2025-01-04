### Tutorial zur LIN-Bus-Technologie in Fahrzeugen

Die LIN (Local Interconnect Network)-Bus-Technologie ist ein weit verbreitetes System zur Kommunikation zwischen verschiedenen elektronischen Steuergeräten (ECUs) in Fahrzeugen. Diese Anleitung erläutert die grundlegenden Konzepte und technischen Spezifikationen von LIN, um ein fundiertes Verständnis zu vermitteln.

#### Physikalische Signalübertragung

Im LIN-Bus werden keine Differenzspannungssignale verwendet. Stattdessen erfolgt die Signalübertragung über eine gewöhnliche Eindrahtleitung (Single Wire), die definierte Spannungspegel für die logische Eins und Null nutzt. Die typische Topologie des LIN-Busses ist der Linien-Bus.

#### Spannungen und logische Pegel

Um eine ausreichende Störfestigkeit zu gewährleisten, wird die Versorgungsspannung der Steuergeräte-Elektronik zusammen mit der Fahrzeugmasse als Bezugspotential für die Buspegel verwendet. Ein Pegel unterhalb von 40% der Versorgungsspannung wird vom Empfänger als logische Null interpretiert. Pegel oberhalb von 60% der Versorgungsspannung werden als logische Eins interpretiert. Sender übertragen eine logische Null mit einem Spannungspegel unter 20% und eine logische Eins mit einem Spannungspegel über 80%.

#### Open-Collector-Schaltung

Ein LIN-Bus-Cluster entspricht schaltungstechnisch einer Open-Collector-Schaltung. Alle Knoten sind passiv über Transceiver an den Bus angeschlossen. Ein Pull-Up-Widerstand sorgt dafür, dass der Buspegel nahezu der Versorgungsspannung (High Pegel) entspricht, wenn alle Sendetransistoren der Knoten sperren. Sobald ein Sendetransistor leitet, wird der Buspegel nahezu auf Masse (Low Pegel) gezogen. Der Low-Zustand ist daher ein dominanter Pegel, der den rezessiven High-Zustand überschreibt.

#### Pull-Up- und Master-Widerstand

Der Pull-Up-Widerstand eines LIN-Transceivers beträgt 30 kΩ. Am Master muss zusätzlich ein 1 kΩ-Widerstand (Master-Widerstand) parallelgeschaltet werden. Eine Diode im Kollektorzweig verhindert die Stromversorgung des Knotens über den Bus, falls keine Versorgungsspannung anliegt.

Diese strukturierten und detaillierten technischen Spezifikationen sind entscheidend für das Verständnis und die korrekte Implementierung der LIN-Bus-Technologie in Fahrzeugen. Durch die Berücksichtigung dieser Aspekte können Ingenieure und Techniker die Zuverlässigkeit und Effizienz der Kommunikation zwischen den elektronischen Steuergeräten sicherstellen.
