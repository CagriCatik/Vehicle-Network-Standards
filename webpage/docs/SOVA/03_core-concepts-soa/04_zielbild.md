# Zielbild einer serviceorientierten Fahrzeugarchitektur

 In der angestrebten Service-Orientierten Fahrzeugarchitektur (SOA) nehmen sowohl service-orientierte 
Kommunikation auf dem Ethernet als auch signalbasierte Kommunikation auf mechatronischer Ebene eine 
zentrale Rolle ein. Diese hybride SOA-Architektur ermöglicht eine effiziente Vernetzung von Fahrzeugfunktionen 
und -Daten, wobei eine entscheidende Abstraktionsschicht durch die Onboard Vehicle API geschaffen wird.

 Die Onboard Vehicle API fungiert als eine standardisierte Schnittstelle, die den Zugang zu verschiedenen 
Fahrzeugfunktionen und -Daten über sorgfältig konzipierte Services erleichtert. Es ist von besonderer Bedeutung zu 
beachten, dass die Onboard Vehicle API ausschließlich im Ethernet-Backbone existiert. Dies resultiert aus der 
Tatsache, dass SOME/IP eine Technologie des Ethernet-Stacks ist und dementsprechend auf dieser Infrastruktur 
basiert.

 Dennoch wird durch die Funktionsarchitektur und die entscheidende Rolle der Service Provider ein innovatives 
Konzept in unserer Architektur umgesetzt. Mithilfe des Schlüsselelements der Service Providers ist es möglich, 
Services mit einer Schnittstelle auf der Onboard Vehicle API auch für Systeme und Funktionen bereitzustellen, die 
auf LIN/CAN oder FlexRay Steuergeräten lokalisiert sind. Dieses Konzept bildet das zentrale Design unserer 
Architektur.

 Unser vorrangiges Ziel ist es, SOME/IP Services mit einer Schnittstelle auf der Onboard Vehicle API für eine 
möglichst breite Palette von Systemen und Funktionen verfügbar zu machen. Mit anderen Worten, wir streben 
danach, Services zu entwerfen und zu implementieren, wo immer dies technisch realisierbar ist.

 Diese Herangehensweise ist entscheidend für die Schaffung einer flexiblen und service-orientierten 
Fahrzeugarchitektur, die den Anforderungen an Vernetzung, Datenaustausch und Funktionalität in modernen 
Fahrzeugen gerecht wird. Sie ermöglicht eine nahtlose Integration und Kommunikation von Systemen auf 
verschiedenen Ebenen der Fahrzeugarchitektur und trägt somit zur Realisierung innovativer und zukunftsfähiger 
Fahrzeugkonzepte bei