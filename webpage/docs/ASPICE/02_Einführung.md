# Dokumentation zu ASPICE (Automotive SPICE)

## Einleitung

ASPICE, was für "Automotive SPICE" steht, ist ein Prozessmodell zur Entwicklung von softwaregesteuerten Komponenten in der Automobilindustrie. Das Akronym "SPICE" steht für "Software Process Improvement and Capability Evaluation". Dieses Dokument zielt darauf ab, ASPICE im Detail zu erläutern, insbesondere in Bezug auf seine Ziele, die Bestimmung der Prozessfähigkeit und die interne Verwendung des Begriffs "System" im Zusammenhang mit der Automobil-SPICE-Norm.

## ASPICE - Überblick

ASPICE ist ein etabliertes Framework, das die Anforderungen an Entwicklungprozesse für Projekte festlegt, die softwaregesteuerte Komponenten in der Automobilindustrie entwickeln. Es dient zur Bewertung der Reife von Entwicklungsprozessen in einem Projekt, was als "Bewertung" bezeichnet wird.

## Ziele der Prozessfähigkeitsbestimmung

Die Bestimmung der Prozessfähigkeit hat mehrere Ziele:

1. Zielgerichtete Analyse etablierter Entwicklungsprozesse: Dies beinhaltet die Untersuchung und Bewertung der Prozesse, die in einem Projekt zur Softwareentwicklung verwendet werden.
2. Identifizierung von Stärken und Schwächen: Durch die Analyse sollen Stärken und Schwächen des Prozesses identifiziert werden, um Möglichkeiten zur Prozessverbesserung aufzuzeigen.
3. Fähigkeitsbestimmung des Softwareentwicklungsprozesses gemäß ISO/IEC 330xx-Serie (SPICE): Die Bewertung erfolgt gemäß den Standards der ISO/IEC 330xx-Serie, die sich mit den Prozessen der System- und Softwareentwicklung beschäftigen.

## Interne Verwendung des Begriffs "System" in Automotive SPICE

Innerhalb des Kontexts von Automotive SPICE wird der Begriff "System" auf unterschiedliche Weise verwendet, abhängig davon, ob es sich um TIER1- oder OEM-Betrachtungen handelt.

### TIER1-Perspektive:

In der TIER1-Perspektive kann ein "System" verschiedene Bedeutungen haben:

- ECU (Electronic Control Unit): Ein System kann eine einzelne ECU oder einen Teil davon darstellen, einschließlich der darauf ausgeführten Software.
- Systemanforderungen: Dies umfasst die Spezifikationen des Produkts, das von der ECU gesteuert wird.
- Systemarchitektur: Beschreibt die Architektur der ECU, einschließlich der Hardwarekomponenten und der Softwarekomponenten.
- Systemintegration: Dies beinhaltet das Flashen der Software auf die ECU und das Einsetzen in das Gehäuse.
- Systemtest: Umfasst funktionale Tests sowie Umwelt- und EMC-Tests an der ECU.

### OEM-Perspektive:

Für OEMs, die ein gesamtes Fahrzeug oder komplexe Funktionen innerhalb eines Fahrzeugs entwickeln, hat der Begriff "System" eine andere Bedeutung:

- Fahrzeug (Car): Ein System repräsentiert das gesamte Fahrzeug oder eine umfassende Funktion innerhalb des Fahrzeugs.
- Systemarchitektur: Beschreibt die Kommunikationsnetzwerke im Fahrzeug, wie CAN, LIN oder Ethernet.
- Systemintegration: Dies umfasst die Integration verschiedener ECUs auf einem Teststand oder innerhalb des Fahrzeugs.
- Systemtest: Involviert Tests am Fahrzeug, entweder auf Teststrecken oder im realen Straßenverkehr.

## Fazit

ASPICE ist ein entscheidendes Framework in der Automobilindustrie, das dazu beiträgt, die Reife von Entwicklungsprozessen zu bewerten und Verbesserungsmöglichkeiten aufzuzeigen. Die interne Verwendung des Begriffs "System" in Automotive SPICE variiert je nach Perspektive, sei es von TIER1-Zulieferern oder OEMs. Es ist wichtig, diese Unterschiede zu verstehen, um eine effektive Implementierung von ASPICE in Entwicklungsprojekten sicherzustellen.
