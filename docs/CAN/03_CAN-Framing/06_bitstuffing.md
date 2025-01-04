# Synchronisation und Resynchronisation

## Einführung in die Synchronisation

Für eine korrekte und zuverlässige Datenübertragung im CAN-Bus (Controller Area Network) ist die Synchronisation der Kommunikationspartner von entscheidender Bedeutung. Eine präzise Synchronisation gewährleistet, dass alle Knoten im Netzwerk die Datenbits korrekt empfangen und interpretieren können.

## Synchronisation der Kommunikationspartner

Die Synchronisation der Kommunikationspartner beginnt mit dem Startbit, auch als Start of Frame (SOF) bezeichnet. Das SOF ist ein Signalwechsel von einem rezessiven (logisch "1") zu einem dominanten (logisch "0") Pegel und markiert den Beginn einer CAN-Botschaft. Dieser Signalwechsel dient als Referenzpunkt, um den Gleichlauf zwischen Sender und Empfänger herzustellen.

Nach dem SOF übernimmt ein Resynchronisationsmechanismus die Aufgabe, den Gleichlauf während der gesamten Botschaftsübertragung aufrechtzuerhalten. Dies ist notwendig, um sicherzustellen, dass die Bits korrekt ausgerichtet und interpretiert werden, auch wenn geringfügige Unterschiede in den Taktraten der Knoten vorhanden sind.

## Resynchronisation

Der Resynchronisationsmechanismus basiert auf der Auswertung der von rezessiv nach dominant wechselnden Signalflanken. Diese Signalflanken werden zur Korrektur eventueller Phasenabweichungen zwischen Sender und Empfänger verwendet.

Ein wesentlicher Bestandteil dieses Mechanismus ist der Bitstuffing-Mechanismus. Laut der Norm ISO 11898-1 müssen Sender nach spätestens fünf aufeinanderfolgenden Bits gleicher Polarität ein komplementäres Bit einfügen. Dies bedeutet, dass nach fünf identischen Bits (entweder fünf "0" oder fünf "1") ein Bit der entgegengesetzten Polarität eingefügt wird, um sicherzustellen, dass ausreichend Signalflanken zur Resynchronisation vorhanden sind.

## Bitstuffing und seine Bedeutung

Bitstuffing beginnt mit der Übertragung des SOF und endet mit dem letzten Bit der CRC-Sequenz (Cyclic Redundancy Check). Für einen Data Frame im Standard-Format mit einem maximalen Nutzdatenfeld von acht Bytes können im theoretischen Worst-Case-Fall bis zu 24 Stuffbits eingefügt werden. Dies führt dazu, dass der längstmögliche Data Frame im Standard-Format theoretisch aus 132 Bits besteht.

Der Bitstuffing-Mechanismus sorgt dafür, dass lange Sequenzen homogener Bits vermieden werden, wodurch der Resynchronisationsmechanismus effektiv arbeiten kann. Dadurch wird die zuverlässige Übertragung der Botschaft auch bei unterschiedlichen Taktraten und in Umgebungen mit elektrischen Störungen gewährleistet.

## Kritische Betrachtung und wissenschaftliche Genauigkeit

Es ist wichtig zu beachten, dass die theoretische maximale Anzahl von Stuffbits selten in der Praxis erreicht wird, da Datenfelder typischerweise eine Mischung aus "0" und "1" enthalten. Dennoch bietet diese Worst-Case-Betrachtung wertvolle Einblicke in die Grenzen und Kapazitäten des CAN-Bus-Systems.

Ein weiterer Punkt, der wissenschaftlich betrachtet werden muss, ist die mögliche Verzögerung durch das Bitstuffing. Jede eingefügte Stuffbit verlängert die Übertragungszeit eines Frames geringfügig, was bei sehr zeitkritischen Anwendungen berücksichtigt werden muss.

## Schlussfolgerung

Die Synchronisation und Resynchronisation sind essenzielle Mechanismen im CAN-Bus, um eine präzise und zuverlässige Datenübertragung zu gewährleisten. Der Bitstuffing-Mechanismus spielt dabei eine zentrale Rolle, indem er sicherstellt, dass stets genügend Signalflanken für die Resynchronisation vorhanden sind. Ein tiefgehendes Verständnis dieser Prozesse ist entscheidend für die Entwicklung und Analyse robuster CAN-Netzwerke im Automotive-Bereich.
