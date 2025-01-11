# Allgemeines architektonisches Muster für serviceorientierte  Kommunikation

Das generelle Architekturpattern für service-orientierte Kommunikation, insbesondere im Kontext des 
Datenaustauschs zwischen einem Service Provider (Server) und den Clients, basiert auf dem Prinzip des 
Methodenaufrufs und der asynchronen Kommunikation. Im Folgenden wird erläutert, wie ein solcher 
Methodenaufruf für die Anfrage einer Fahrzeugresource abläuft:
 1.
 2.
 Initiierung des Methodenaufrufs: Der Prozess beginnt damit, dass ein Client, der auf eine bestimmte 
Ressource im Fahrzeug zugreifen möchte, die Initiatorrolle einnimmt. Der Client sendet eine Method Call 
Protocol Data Unit (PDU) an den Server, der hier als Service Provider fungiert. Diese Method Call PDU enthält 
IN-Parameter oder Argumente, die vom Server benötigt werden, um die gewünschte Anfrage für den Zugriff 
auf die Ressource auszuführen. Ein Beispiel hierfür könnte die Methode "requestWindowPosition" sein, die 
spezifische Argumente erfordert, um die gewünschte Position des Fensters zu signalisieren. Diese 
Argumente werden als IN-Parameter in der Method Call PDU festgelegt.

 Antwort des Servers: Nachdem der Server die Methodenaufrufanfrage erhalten hat, führt er die angeforderte 
Aktion aus oder plant deren Ausführung. Anschließend sendet der Server eine Return Protocol Data Unit 
(PDU) an den anfragenden Client zurück. Diese Return-PDU enthält in der Regel Informationen, die das 
Ergebnis des Methodenaufrufs beschreiben und dem Client mitteilen, ob die angeforderte Aktion erfolgreich 
ausgeführt wurde.


 Eine wichtige Neuerung im Rahmen der Service-orientierten Architektur (SOA) besteht darin, dass, wenn eine 
Änderung des Zustands einer Ressource von einem beliebigen Client angefordert wird, der Server zusätzlich zur 
einfachen Return-PDU ein sogenanntes State Event an alle Clients sendet, die sich auf den entsprechenden Service 
(Dienst) subscribed haben. Dieses State Event enthält Informationen über den neuen Zustand der Ressource, der 
sich aufgrund der durchgeführten Aktion geändert hat. Diese Mitteilung des neuen Ressourcenstatus an alle 
relevanten Clients ermöglicht eine koordinierte und konsistente Aktualisierung der Informationen über die 
Ressource in der gesamten Client-Community.

 Es ist wichtig anzumerken, dass die zugrundeliegende Kommunikationsprotokolltechnologie für OVAPI (Open 
Vehicle Application Programming Interface) das SOME/IP-Protokoll ist, das auf dem Ethernet-Stack basiert. Diese 
Technologie ermöglicht die effiziente und zuverlässige Kommunikation zwischen dem Service Provider (Server) und 
den Clients im Kontext der Fahrzeugdaten- und Ressourcennutzung.