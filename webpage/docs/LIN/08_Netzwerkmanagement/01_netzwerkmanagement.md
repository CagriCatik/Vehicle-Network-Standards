# Netzwerkmanagement


Zustandsmodell
Im Protokoll ist ein eigenes Netzwerkmanagement definiert. Es sieht für die Slaves vier Zustände vor: Power Off, Initialisierung, Betrieb und Sleep. Auch die Zustandsübergänge sind definiert (siehe interaktive Grafik Slave Zustandsmodell). Durch Power On wechselt ein Slave in den Zustand Initialisierung. Dieser muss nach 100 ms abgeschlossen sein. Dann wechselt der Slave selbsttätig in den Betriebszustand.


Sleep-Kommando
Mit Übertragung des Goto-sleep-Kommandos kann der Master alle Slaves in den Zustand Sleep versetzen. Bei diesem Kommando handelt es sich um einen Master Request Frame, der im ersten Datenbyte den Wert 0x00 aufweist (entspricht NAD=0). Die sieben weiteren Datenbytes werden mit 0xFF übertragen.


Automatischer Sleep Mode
Die Slaves wechseln auch dann in den Zustand Sleep, wenn vier bis zehn Sekunden lang keine Busaktivität vorhanden ist. Laut Spezifikation ist dabei nicht zwingend erforderlich, dass der Übergang in diesen Zustand mit dem Übergang in den Zustand Low Power einhergehen muss. Das bedeutet, dass der Mikrocontroller nicht zwingend in einen Energiesparmodus umgeschaltet wird, in dem nicht benötigte Hardware Ressourcen abgeschaltet sind.

Wakeup
Neben dem Master besitzt jeder Slave die Möglichkeit das Cluster aufzuwecken. Dazu wird ein Wecksignal (Wakeup) am Bus angelegt (siehe interaktive Grafik Slave Zustandsmodell). Hierbei handelt es sich um einen dominanten Puls, der mindestens 250 µs und maximal 5 ms andauert. Nach Erkennung eines Wakeup verlassen die Knoten den Zustand Sleep und wechseln in den Initialisierungszustand. Nach weiteren 100 ms wechseln sie in den Betriebszustand.

"Schläfriger" Master
Wenn ein Slave für das Aufwecken verantwortlich ist und nach der Initialisierung für weitere 150 ms keinen Header erkennt, so überträgt der Knoten ein weiteres Wecksignal (siehe interaktive Grafik Wakeup Prozedur). Sollte auch dieser und der nächste Aufweckversuch fehlschlagen (3 Wecksignale = 1 Wakeup Block), setzt der Slave die Aufweckprozedur für 1,5 s aus, um im Anschluss eventuell erneut zu beginnen. Dies hängt von den Vorgaben im Systemdesign ab.


![slave](/img/lin/slave_zustandsmodell.png)

![wakeup prozedur](/img/lin/wakeup_prozedur.png)