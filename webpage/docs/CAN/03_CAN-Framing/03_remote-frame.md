# Anforderung von Daten im CAN-Netzwerk

## Einleitung

Im Bereich der automobilen Netzwerktechnik spielt das Controller Area Network (CAN) eine zentrale Rolle bei der Kommunikation zwischen verschiedenen elektronischen Steuergeräten (ECUs). Dieses Tutorial beleuchtet die Funktion und Anwendung von Remote Frames zur Anforderung von Daten innerhalb eines CAN-Netzwerks. Besondere Aufmerksamkeit wird den Unterschieden zu Data Frames, der Rolle des RTR-Bits und der Implementierung in realen Anwendungen gewidmet.

## Überblick über CAN-Frames

### Data Frames

Data Frames sind die grundlegenden Elemente für die Datenübertragung in einem CAN-Netzwerk. Sie enthalten Nutzdaten, die von einem CAN-Knoten an andere Knoten im Netzwerk gesendet werden.

### Remote Frames

Remote Frames sind eine spezielle Art von CAN-Frames, die verwendet werden, um Nutzdaten von anderen Knoten anzufordern. Im Vergleich zu Data Frames fehlt ihnen das Data Field. Remote Frames können sowohl im Standard- als auch im Extended-Format übertragen werden.

### Unterschiede zwischen Data und Remote Frames

Der Hauptunterschied zwischen Data und Remote Frames liegt im RTR-Bit (Remote Transmission Request):

- **Data Frame**: Das RTR-Bit wird dominant gesendet.
- **Remote Frame**: Das RTR-Bit wird rezessiv gesendet.

## Implementierung und Nutzung von Remote Frames

### Definition und Identifikation

Für jeden existierenden Data Frame im CAN-Netzwerk kann ein entsprechender Remote Frame definiert werden. Es ist dabei sicherzustellen, dass die Identifier der Remote Frames mit denen der assoziierten Data Frames übereinstimmen. Wenn ein CAN-Knoten einen Remote Frame mit einer ID empfängt, die mit der ID eines seiner Data Frames identisch ist, antwortet er mit dem entsprechenden Data Frame.

### Automatische und manuelle Beantwortung

Die Beantwortung eines Remote Frames kann auf zwei Arten erfolgen:

1. **Automatische Beantwortung**: Bei CAN-Controllern mit Objektespeicherung wird die Beantwortung eines Remote Frames automatisch durch den CAN-Controller durchgeführt.
2. **Manuelle Beantwortung**: CAN-Controller ohne Objektespeicherung müssen den Host benachrichtigen, damit dieser die Beantwortung des Remote Frames initiiert.

### Priorität und Verzögerung

Im Idealfall erfolgt die Beantwortung eines Remote Frames sofort durch das entsprechende Data Frame. Allerdings kann es zu Verzögerungen kommen, wenn sich CAN-Botschaften mit höherer Priorität zwischen die Anfrage und die Beantwortung schieben.

## Kritische Betrachtung und Anwendung in der Praxis

### Geringe Anwendung im Automobilbereich

Trotz der Möglichkeit, Daten mittels Remote Frames anzufordern, findet diese Methode im Automobilbereich kaum Anwendung. Dies liegt daran, dass die Datenübertragung in Fahrzeugnetzwerken primär durch die Informationserzeuger initiiert wird und nicht auf Nachfrage erfolgt. Diese Praxis stellt sicher, dass wichtige Daten kontinuierlich und zuverlässig übertragen werden, ohne dass erst eine Anforderung erfolgen muss.

### Potenzielle Einsatzgebiete

Remote Frames könnten in speziellen Fällen nützlich sein, beispielsweise in Diagnoseanwendungen oder in Netzwerken, wo eine gezielte Datenanforderung notwendig ist. Allerdings ist die praktische Relevanz im Automobilbereich begrenzt, weshalb die Implementierung und der Einsatz von Remote Frames wohlüberlegt erfolgen sollten.

### Sicherheits- und Leistungsaspekte

Bei der Implementierung von Remote Frames müssen Sicherheits- und Leistungsaspekte berücksichtigt werden. Unbeabsichtigte oder böswillige Nutzung von Remote Frames könnte zu unnötigem Datenverkehr und erhöhtem Netzwerklast führen, was die Leistung und Zuverlässigkeit des Gesamtsystems beeinträchtigen kann.

## Zusammenfassung

Remote Frames bieten eine Möglichkeit, Nutzdaten im CAN-Netzwerk anzufordern, werden jedoch im Automobilbereich aufgrund der überwiegend ereignisgesteuerten Kommunikation selten genutzt. Das Verständnis des Aufbaus und der Funktion von Remote Frames sowie deren Vor- und Nachteile ist für die Planung und Implementierung von CAN-Netzwerken essenziell. Die Entscheidung, Remote Frames zu nutzen, sollte sorgfältig abgewogen werden, insbesondere in sicherheitskritischen und leistungsabhängigen Anwendungen.
 