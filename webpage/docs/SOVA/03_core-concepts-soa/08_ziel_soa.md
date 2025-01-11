# Ziele der serviceorientierten Architektur
 Die Entwicklung einer service-orientierten Fahrzeugarchitektur verfolgt mehrere Ziele, von denen das Hauptziel die 
Entkopplung des Zugangs zu Fahrzeugressourcen über die Onboard Vehicle API als zentrale abstrahierende 
Schnittstelle im Fahrzeug ist. Diese Entkopplung wird mithilfe von Services realisiert, die über spezielle Client
Server-Schnittstellen, die Methodenaufrufe ermöglichen, einen generischen Zugang zu den Fahrzeugressourcen 
gewähren. Dabei bleibt die Fahrzeugressource selbst unverändert, sie kann jedoch je nach den Wünschen des 
Clients, der eine Anfrage stellt, unterschiedliche Zustände annehmen, um die gewünschten Funktionen zu erfüllen.
 Die Implementierung generischer Signale zur Steuerung und Nutzung von Fahrzeugressourcen stellt jedoch eine 
komplexe Aufgabe dar und birgt zahlreiche Herausforderungen. Zum Beispiel muss berücksichtigt werden, wie mit 
konkurrierenden Anfragen von mehreren Clients auf eine Ressource umgegangen wird.
 Um solche Fragen zu beantworten, beschäftigt sich die Forschung intensiv mit der Entwicklung von Design Patterns 
und Richtlinien für die SOA-Architektur und das Design der Onboard Vehicle API. Dies umfasst die Gestaltung der 
Schnittstellen für die Services der Onboard Vehicle API sowie die Auswahl geeigneter Technologien und Protokolle 
als Datenaustauschformat zwischen dem Service Provider und den anfragenden Clients, um die spezifischen 
Anforderungen im Bereich der Automobilindustrie zu erfüllen. Dabei ist eine sorgfältige Berücksichtigung von 
Sicherheit, Skalierbarkeit und Effizienz von entscheidender Bedeutung, um eine zuverlässige und leistungsfähige 
service-orientierte Fahrzeugarchitektur zu entwickeln.