### LIN-Bus - Dominante und Rezessive Zustände

Der LIN-Bus (Local Interconnect Network) arbeitet mit zwei fundamentalen Logikzuständen, die als **dominante** und **rezessive Zustände** bezeichnet werden. Diese Zustände ermöglichen es, die Kommunikation im Netzwerk zu steuern und die Informationen zu übertragen, indem die Spannung auf der Busleitung variiert wird. Dieses Konzept ist entscheidend für die Effizienz und Stabilität der LIN-Kommunikation.

#### Übersicht über die Dominanten und Rezessiven Zustände

1. **Dominanter Zustand (Low State):**
   - Tritt auf, wenn **mindestens ein Knoten seinen Ausgangsschalter schließt** und dadurch die Busleitung aktiv auf Masse (GND) zieht.
   - Ein einzelner Knoten kann den dominanten Zustand erzwingen, was die Effizienz der Steuerung und die Koordination der Knoten im Netzwerk verbessert.
   - Der dominante Zustand entspricht einem **Low-Signal** auf dem Bus.

2. **Rezessiver Zustand (High State):**
   - Dieser Zustand tritt ein, wenn **alle Ausgangsschalter der Knoten offen** sind, sodass die Busleitung durch Pull-Up-Widerstände auf die Betriebsspannung (typisch 12 V) gezogen wird.
   - Der rezessive Zustand entspricht einem **High-Signal** auf dem Bus und signalisiert, dass kein Knoten aktiv die Leitung steuert.
   - Der rezessive Zustand wird nur erreicht, wenn alle Knoten in einem passiven Zustand sind.

#### Funktionsweise der Zustandswechsel im LIN-Bus

Das Umschalten zwischen dominantem und rezessivem Zustand wird durch die zeitliche Steuerung der Schalter (Tx) der einzelnen Knoten ermöglicht:

- **Wechsel zum Dominanten Zustand:** Ein Knoten zieht die Busleitung auf Masse, was zur Interpretation eines Low-Signals führt.
- **Wechsel zum Rezessiven Zustand:** Alle Schalter sind offen, wodurch die Busleitung durch die parallel geschalteten Pull-Up-Widerstände auf die hohe Spannung gezogen wird.

#### Hardwareimplementierung der Zustände

- **Pull-Up-Widerstände:** 
  - Die Pull-Up-Widerstände sind parallel über die Knoten verteilt, was die Leitung im Normalzustand auf die Betriebsspannung (High-Level) bringt.
  - Der effektive Widerstand der Pull-Up-Schaltung entspricht der Parallelschaltung aller beteiligten Widerstände, was die Stabilität der Signalpegel im rezessiven Zustand sicherstellt.

- **Signalkodierung:** 
  - Der Informationsaustausch im LIN-Bus erfolgt über die zeitliche Abfolge der dominanten und rezessiven Zustände. Ein LIN-Knoten kann durch ein bestimmtes Timing die Bedeutung eines Signals kodieren, was durch die chronologische Reihenfolge der Zustände festgelegt wird.
  
#### Zusammenfassung der LIN-Bus-Zustände

Der LIN-Bus arbeitet in zwei logischen Zuständen, um die Kommunikation zwischen den Knoten zu steuern:

1. **Rezessiver High-Zustand:** Alle Schalter offen, Busleitung wird durch Pull-Up-Widerstände auf die Betriebsspannung gezogen.
2. **Dominanter Low-Zustand:** Mindestens ein Schalter geschlossen, wodurch die Busleitung auf Masse gezogen wird.

Diese beiden Zustände sind ausreichend, um alle nötigen Informationen im LIN-Bus zu übertragen, indem die Wechsel zwischen dominantem und rezessivem Zustand zeitlich gesteuert werden.