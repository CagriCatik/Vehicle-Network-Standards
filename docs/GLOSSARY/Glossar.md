# Glossar

## A

### ACK

**ACK** steht für "Acknowledgement" und wird verwendet, um den Empfang von Daten in einer Kommunikationsverbindung zu bestätigen. Es ist ein Signal, das von einem Empfänger an einen Sender gesendet wird, um anzuzeigen, dass die empfangenen Daten korrekt übertragen wurden.

## B

### Bitstuffing

**Bitstuffing** ist eine Methode zur Fehlererkennung und -korrektur in der Datenübertragung. Dabei werden spezielle Bits in die Daten eingefügt, um sicherzustellen, dass das empfangene Signal korrekt interpretiert wird. Dies geschieht durch das Einfügen zusätzlicher Bits, wenn eine bestimmte Bitfolge im Datenstrom auftritt, um zu verhindern, dass diese Bitfolge fälschlicherweise als Steuerzeichen interpretiert wird.

### Botschaftszähler

Ein Botschaftszähler (engl. Message Counter) ist ein wichtiges Konzept bei der Buskommunikation, wie beispielsweise beim CAN-Bus (Controller Area Network). Der Botschaftszähler dient dazu, doppelte oder verlorene Nachrichten zu erkennen und somit die Datenkonsistenz zu gewährleisten. Jede Nachricht, die über den Bus gesendet wird, erhält eine fortlaufende Nummer (den Botschaftszähler). Der Empfänger kann anhand dieser Nummer erkennen, ob eine Nachricht doppelt empfangen wurde (gleiche Nummer wie zuvor) oder ob eine Nachricht verloren ging (es fehlt eine Nummer in der Reihenfolge). Durch den Botschaftszähler können Fehler erkannt und behoben werden, indem z.B. verlorene Nachrichten erneut angefordert werden. Dies erhöht die Integrität und Zuverlässigkeit der Datenkommunikation über den Bus erheblich. Der Botschaftszähler ist besonders wichtig in sicherheitskritischen Systemen, wo eine korrekte Datenübertragung zwischen den verschiedenen Steuergeräten essentiell ist.

## C

### CAN

**CAN** steht für "Controller Area Network" und ist ein serielles Bussystem, das in der Regel in Fahrzeugen und industriellen Anwendungen zur Kommunikation zwischen verschiedenen Steuergeräten verwendet wird. CAN ermöglicht eine robuste und zuverlässige Datenübertragung über kurze bis mittlere Entfernungen.

### CAN-FD

**CAN-FD** steht für "Controller Area Network - Flexible Data-Rate" und ist eine Erweiterung des klassischen CAN-Protokolls. CAN-FD bietet höhere Datenübertragungsraten und größere Nutzlasten im Vergleich zum herkömmlichen CAN.

### CRC

**CRC** steht für "Cyclic Redundancy Check" und ist ein Verfahren zur Fehlererkennung in Datenübertragungen.

### DLC

**DLC** steht für "Data Length Code" und bezieht sich auf das Feld in einem CAN-Nachrichtenframe, das die Anzahl der Datenbytes in der Nachricht angibt.

## E

### EOF

**EOF** steht für "End of Frame" und markiert das Ende einer Nachricht in einem seriellem Datenübertragungsprotokoll wie CAN.

## I

### IDE

**IDE** steht für "Identifier Extension" und bezieht sich auf ein Bit im CAN-Nachrichtenrahmen, das angibt, ob der CAN-Identifier aus 11 oder 29 Bit besteht.

### ITM

**ITM** steht für

## M

### Multi-Master

Das Multi-Master-Prinzip in der Buskommunikation ermöglicht es mehreren Geräten, gleichzeitig die Rolle des Masters zu übernehmen, wodurch eine gleichzeitige Datenübertragung und eine flexible Kommunikation ermöglicht werden.

### Master-Slave

Das Master-Slave-Prinzip in der Buskommunikation bezeichnet eine Architektur, in der ein Hauptgerät (Master) die Kontrolle über den Kommunikationsbus hat und Daten an andere Geräte (Slaves) sendet. Die Slaves können nur auf Anforderung des Masters antworten.

## R

### RTR

**RTR** steht für "Remote Transmission Request" und wird in CAN verwendet, um anzuzeigen, dass der Sender eine Remote-Anforderung für Datenübertragung an den Empfänger sendet.

## S

### SOF

**SOF** steht für "Start of Frame" und markiert den Beginn einer Nachricht in einem seriellem Datenübertragungsprotokoll wie CAN.
