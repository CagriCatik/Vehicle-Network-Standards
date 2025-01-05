### LIN-Kommunikation in Fahrzeugen

#### Sendeschema

Im LIN-Bus-System (Local Interconnect Network) übernimmt der Master-Knoten die Regelung der gesamten Kommunikation innerhalb eines Clusters. Der Master-Knoten besitzt daher ein festgelegtes Sendeschema, das vom Systemdesigner geplant und im LIN Description File (LDF) beschrieben wird. Dieses geplante Sendeschema sorgt für eine vorhersagbare Kommunikation im Netzwerk, da die zeitliche Abfolge der Datenübertragung festgelegt ist.

#### Slots und Minislots

Das Sendeschema ist in sogenannte Slots unterteilt, wobei jeder Slot für die Übertragung eines einzelnen Frames vorgesehen ist. Die Größe dieser Slots wird durch Minislots bestimmt. Ein Minislot stellt dabei die Zeiteinheit dar, mit der die Master-Aufgabe das Sendeschema abarbeitet. Die Dauer der Minislots bildet somit die Zeitbasis für die kontinuierliche Kommunikation im LIN-Netzwerk.

#### Jitter

Bei der Berechnung der Slotgröße wird ein Jitter-Wert hinzugefügt. Dieser Wert repräsentiert die mögliche Zeitdifferenz zwischen dem nominalen und dem tatsächlichen Beginn eines Slots. Falls ein Frame den vorgesehenen Slot nicht vollständig ausfüllt, muss der verbleibende Zeitbereich abgewartet werden, bis der nächste Slot verfügbar ist. Dieser Wartezeitraum wird als Inter Frame Space (IFS) bezeichnet.

#### Zeitreserve

Um Kollisionen während des Kommunikationsbetriebs zu vermeiden, muss der Systemdesigner sicherstellen, dass die zeitlichen Bedingungen für alle Frames korrekt berechnet sind. Jeder Slot muss groß genug sein, um die vollständige Übertragung der entsprechenden Frames zu gewährleisten. Insbesondere bei der Verwendung preisgünstiger und weniger leistungsstarker Prozessoren wird den Knoten eine Zeitreserve von bis zu 40 % für die Nachrichtenübertragung eingeräumt. Diese Zeitreserve ist notwendig, um Schwankungen und Verzögerungen im Übertragungsprozess auszugleichen.
