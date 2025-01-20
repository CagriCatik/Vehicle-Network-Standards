# C

## CSMA/CA 

CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) ist ein Zugriffsprotokoll, das ebenfalls in Netzwerken eingesetzt wird, um den Zugriff auf das Übertragungsmedium zu regeln. Im Gegensatz zu CSMA/CR, das Kollisionen erkennt und behandelt, zielt CSMA/CA darauf ab, Kollisionen zu vermeiden. Das Protokoll überwacht das Übertragungsmedium, um festzustellen, ob es frei ist, bevor es Daten sendet. Wenn das Medium als frei erkannt wird, wartet der Sender jedoch zunächst eine zufällige Zeit, bevor er mit der Datenübertragung beginnt. Diese zufällige Wartezeit dient dazu, die Wahrscheinlichkeit von Kollisionen zu verringern, insbesondere in Situationen, in denen mehrere Teilnehmer gleichzeitig versuchen, Daten zu senden. Durch die Einführung dieser zufälligen Wartezeit verringert CSMA/CA die Wahrscheinlichkeit von Kollisionen und trägt so zur Verbesserung der Netzwerkeffizienz und -stabilität bei.

## CSMA/CR 

CSMA/CR (Carrier Sense Multiple Access with Collision Resolution) ist ein Zugriffsprotokoll, das in Netzwerken verwendet wird, um den Zugriff auf das gemeinsam genutzte Übertragungsmedium zu regulieren. Das Protokoll funktioniert, indem es zuerst den Zustand des Übertragungsmediums überwacht, um festzustellen, ob es frei ist oder von anderen Teilnehmern genutzt wird. Wenn das Medium frei ist, sendet der Sender seine Daten. Allerdings kann es vorkommen, dass mehrere Teilnehmer gleichzeitig versuchen, Daten zu senden, was zu einer Kollision führt. In solchen Fällen erkennt CSMA/CR die Kollision und löst sie auf, indem es einen Mechanismus zur Wiederholung der Übertragung oder zur Neuplanung einführt. Dies ermöglicht es den beteiligten Teilnehmern, ihre Daten erneut zu senden, um die Kollision zu beheben und die korrekte Übertragung sicherzustellen.

## CRC

CRC steht für "Cyclic Redundancy Check" und ist ein Verfahren zur Fehlererkennung in Datenübertragungen. 

## CDD 

CANdelaStudio diagnostic description

## CAN 

steht für "Controller Area Network" und ist ein serielles Bussystem, das in der Regel in Fahrzeugen und industriellen Anwendungen zur Kommunikation zwischen verschiedenen Steuergeräten verwendet wird. CAN ermöglicht eine robuste und zuverlässige Datenübertragung über kurze bis mittlere Entfernungen.

## CAN-FD 

steht für "Controller Area Network - Flexible Data-Rate" und ist eine Erweiterung des klassischen CAN-Protokolls. CAN-FD bietet höhere Datenübertragungsraten und größere Nutzlasten im Vergleich zum herkömmlichen CAN.