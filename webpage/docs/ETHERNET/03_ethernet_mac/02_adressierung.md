# Adressierung

Teilnehmeradressierung

Im Ethernet-Netzwerk kommt die Teilnehmeradressierung für die gezielte Zustellung von Botschaften zum Einsatz. Hierzu verfügt jeder Knoten über mindestens eine MAC-Adresse, die zur eindeutigen Kennung im lokalen Netzwerk (LAN) dient. Eine gesendete Botschaft beinhaltet immer eine Sender- und eine Empfängeradresse, sodass ein Rückschluss auf die Kommunikationsteilnehmer möglich ist.

![1712318298889](/img/eth/1712317769475.png)



![1712318298889](/img/eth/1712317744832.png)


## Unicast

Die eindeutige Adressierung der Teilnehmer erfolgt mit Hilfe von Unicast-Adressen. Diese Adressen gibt der Fahrzeughersteller entweder vor oder Zulieferer dürfen aus einem eigenen Adressbereich wählen. Adressbereiche können bei der IEEE Registry Authority beantragt sowie registriert werden und sind einem Unternehmen weltweit eindeutig zugewiesen.

## Multi- und Broadcast

Damit Botschaften mehreren Teilnehmern zustellbar sind, können neben Unicast- auch Multicast-Adressen verwendet werden. Mit deren Hilfe sind Knotengruppen definierbar, deren Mitglieder eine Nachricht über eine gemeinsame MAC-Adresse erhalten. Im Gegensatz zur Broadcast-Adresse, die das Versenden einer Botschaft an alle Teilnehmer erlaubt, müssen Multicast-Adressen im jeweiligen Knoten konfiguriert werden.

## VLAN

Als Erweiterung zur klassischen Adressierung kommen in der Automobilbranche häufig VLAN-Adressen zum Einsatz. Diese adressieren virtuelle Netzwerke, die innerhalb eines Gesamtnetzwerks vorhanden sind und eine Abgrenzung der Kommunikation erlauben. Auf diese Weise können Domänen für unterschiedliche Anwendungsbereiche festgelegt werden, deren Mitglieder auf die dort vorhandene Kommunikation zugreifen dürfen. Da ein Steuergerät üblicherweise in mehreren Anwendungsbereichen tätig ist, darf es auch Mitglied in mehreren Domänen und somit mehreren VLAN-Netzwerken sein.

![1712318298889](/img/eth/1712317815931.png)

## Prioritäten

VLAN bietet für eine Verbesserung des Echtzeitverhaltens außerdem die Festlegung von Prioritäten für Botschaften an. So kann wichtiger Datenverkehr bevorzugt durch Switches geleitet werden, was eine Reduzierung von Latenzzeiten zur Folge hat.