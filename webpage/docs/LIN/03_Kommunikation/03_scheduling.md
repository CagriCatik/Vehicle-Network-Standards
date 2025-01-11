# Scheduling im LIN-Bus

Im LIN-Bus-System wird die Kommunikation innerhalb eines Clusters zentral vom Master-Knoten gesteuert. Der Master verwendet ein festgelegtes **Sendeschema**, das die zeitliche Abfolge der Datenübertragung bestimmt. Dieses Sendeschema, auch als **Schedule** bezeichnet, ist im **LIN Description File (LDF)** beschrieben und wird vom Systemdesigner im Voraus geplant. Durch diese strikte Planung wird eine **deterministische Kommunikation** gewährleistet, bei der die Reihenfolge und die zeitlichen Intervalle der Datenübertragungen im gesamten Netzwerk vorhersagbar sind.

Das Sendeschema teilt die verfügbare Zeit in klar definierte Einheiten ein, sogenannte **Slots**, die jeweils für die Übertragung eines einzelnen Frames reserviert sind. Jeder Frame wird innerhalb seines zugewiesenen Slots übertragen, wodurch eine geordnete und kollisionsfreie Kommunikation im Netzwerk ermöglicht wird.

## Slots und Minislots

Das Sendeschema basiert auf einer fein abgestimmten Zeitstruktur, die durch **Slots** und **Minislots** definiert wird:

1. **Slot:** 
   - Ein Slot ist eine Zeiteinheit, die der Übertragung eines vollständigen Frames dient. Dazu gehören alle Komponenten des Frames, einschließlich Break-Feld, Synchronisationsfeld, Identifier-Feld, Datenfeld und Checksum-Feld.
   - Die Slot-Dauer wird so festgelegt, dass sie die vollständige Übertragung des zugewiesenen Frames einschließlich einer Sicherheitsmarge abdeckt.

2. **Minislot:**
   - Ein Minislot ist die kleinste Zeiteinheit, die im Sendeschema verwendet wird. Die Master-Aufgabe arbeitet das Sendeschema in Minislots ab.
   - Die Dauer eines Slots ergibt sich aus der Anzahl der für den Frame benötigten Minislots.

Die Verwendung von Slots und Minislots ermöglicht eine präzise zeitliche Planung der Kommunikation im LIN-Netzwerk. Dies ist besonders wichtig für Anwendungen, bei denen es auf eine regelmäßige und zuverlässige Datenübertragung ankommt.

## Jitter und Inter Frame Space (IFS)

Bei der zeitlichen Planung der Slots wird ein sogenannter **Jitter-Wert** berücksichtigt. Dieser Wert stellt die Abweichung zwischen dem nominalen und dem tatsächlichen Beginn eines Slots dar, die durch hardwarebedingte oder prozessabhängige Verzögerungen verursacht werden kann. Die Berücksichtigung von Jitter ist essenziell, um sicherzustellen, dass der Start jedes Slots innerhalb der zulässigen Toleranzen erfolgt.

### Inter Frame Space (IFS)
Falls ein Frame weniger Zeit benötigt als der ihm zugewiesene Slot, entsteht ein verbleibender Zeitraum bis zum Beginn des nächsten Slots. Dieser Zeitraum wird als **Inter Frame Space (IFS)** bezeichnet. Der IFS dient dazu:
- Eine klare Trennung zwischen aufeinanderfolgenden Frames zu gewährleisten.
- Den Slaves genügend Zeit zu geben, um sich auf die nächste Kommunikation vorzubereiten.

Die IFS-Zeit wird im Sendeschema berücksichtigt und ist entscheidend, um eine geordnete und kollisionsfreie Kommunikation im Netzwerk sicherzustellen.

## Zeitreserve und zeitliche Planung

Die zeitliche Planung des Sendeschemas erfordert eine präzise Berechnung der benötigten Slot-Dauer für jeden Frame. Diese Berechnung muss mehrere Faktoren berücksichtigen:
1. **Länge des Frames:** Die Zeit, die für die Übertragung aller Bits eines Frames benötigt wird.
2. **Jitter-Wert:** Die mögliche Abweichung vom nominalen Startzeitpunkt.
3. **Zeitreserve:** Ein zusätzlicher Puffer, der Schwankungen und Verzögerungen im Übertragungsprozess ausgleicht.

Insbesondere bei der Verwendung von preisgünstigen und weniger leistungsstarken Prozessoren in den Knoten ist eine großzügige Zeitreserve wichtig. Typischerweise wird den Knoten eine Zeitreserve von bis zu **40 %** der berechneten Slot-Dauer eingeräumt. Diese Reserve gewährleistet, dass Frames auch bei minimalen Verzögerungen oder Schwankungen zuverlässig übertragen werden können.

## Herausforderungen und Lösungen bei der Slot-Planung

Die Planung der Slots im Sendeschema ist ein komplexer Prozess, der verschiedene Herausforderungen mit sich bringt:
1. **Vermeidung von Kollisionen:** Es muss sichergestellt werden, dass sich die Übertragungen der Knoten nicht überschneiden.
2. **Optimierung der Slot-Dauer:** Die Slots dürfen nicht zu knapp bemessen sein, um Übertragungsfehler zu vermeiden, aber auch nicht zu großzügig, um die Effizienz des Netzwerks zu erhalten.
3. **Berücksichtigung von Jitter und IFS:** Diese Faktoren müssen in die Berechnung der Slot-Dauer einfließen, um eine stabile und geordnete Kommunikation sicherzustellen.

Die Lösung dieser Herausforderungen erfordert eine sorgfältige Analyse der Kommunikationsanforderungen sowie die präzise Implementierung des Sendeschemas im LDF. Durch die optimale Gestaltung des Schedules kann die Effizienz und Zuverlässigkeit des LIN-Netzwerks maximiert werden.
