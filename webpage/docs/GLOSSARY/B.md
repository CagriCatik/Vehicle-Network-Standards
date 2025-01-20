# B

## Bus Guardian

Bus Guardian ist eine Funktion im FlexRay-Kommunikationssystem, die aktiv die Integrität und Zuverlässigkeit der Datenkommunikation auf dem FlexRay-Bus überwacht, um potenzielle Fehler oder Anomalien zu erkennen und durch entsprechende Maßnahmen wie Blockieren fehlerhafter Nachrichten oder Auslösen von Warnungen die Sicherheit und Funktionsfähigkeit sicherzustellen.

## Bitstuffing

Bitstuffing ist eine Methode zur Fehlererkennung und -korrektur in der Datenübertragung. Dabei werden spezielle Bits in die Daten eingefügt, um sicherzustellen, dass das empfangene Signal korrekt interpretiert wird. Dies geschieht durch das Einfügen zusätzlicher Bits, wenn eine bestimmte Bitfolge im Datenstrom auftritt, um zu verhindern, dass diese Bitfolge fälschlicherweise als Steuerzeichen interpretiert wird.

## Botschaftszähler 

Ein Botschaftszähler (engl. Message Counter) ist ein wichtiges Konzept bei der Buskommunikation, wie beispielsweise beim CAN-Bus (Controller Area Network). Der Botschaftszähler dient dazu, doppelte oder verlorene Nachrichten zu erkennen und somit die Datenkonsistenz zu gewährleisten. Jede Nachricht, die über den Bus gesendet wird, erhält eine fortlaufende Nummer (den Botschaftszähler). Der Empfänger kann anhand dieser Nummer erkennen, ob eine Nachricht doppelt empfangen wurde (gleiche Nummer wie zuvor) oder ob eine Nachricht verloren ging (es fehlt eine Nummer in der Reihenfolge). Durch den Botschaftszähler können Fehler erkannt und behoben werden, indem z.B. verlorene Nachrichten erneut angefordert werden. Dies erhöht die Integrität und Zuverlässigkeit der Datenkommunikation über den Bus erheblich. Der Botschaftszähler ist besonders wichtig in sicherheitskritischen Systemen, wo eine korrekte Datenübertragung zwischen den verschiedenen Steuergeräten essentiell ist.

## BRS 

Bit Rate Switch
