# Steer-by-Wire

In der modernen Fahrzeugtechnik spielt die Elektronik eine immer größere Rolle, insbesondere bei sicherheitskritischen Systemen wie der Lenkung. Dieser Artikel behandelt das Steer-by-Wire-Prinzip, das auf der FlexRay-Kommunikation basiert, und analysiert die technischen Aspekte sowie die sicherheitsrelevanten Herausforderungen dieses Systems.

## Mechanische Lenkung

Traditionelle Lenksysteme in Kraftfahrzeugen nutzen mechanische Verbindungen, um den Lenkeingriff des Fahrers auf die gelenkten Räder zu übertragen. Diese Systeme können mit hydraulischen, elektrohydraulischen oder elektrischen Lenkhilfen ausgestattet sein, um die notwendige Lenkunterstützung bereitzustellen. Ein wesentlicher Vorteil dieser Systeme ist die mechanische Verbindung über die Lenksäule, die auch bei einem Ausfall der Servounterstützung einen mechanischen Durchgriff gewährleistet.

## Elektrische Lenkung

Beim elektrischen Lenksystem wird die mechanische Verbindung durch elektronische Komponenten ersetzt. Das vom Fahrer betätigte Lenkrad sendet ein Signal an ein Steuergerät, welches die Eingaben verarbeitet und Befehle an die entsprechenden Aktoren weiterleitet. Diese Aktoren umfassen:

1. **Handkraftaktor:** Simuliert die Rückstellkräfte am Lenkrad, die normalerweise durch die mechanische Verbindung vermittelt werden.
2. **Radwinkelsteller:** Positioniert die Räder entsprechend den Lenkbefehlen.

Der Lenkungsregler koordiniert die Interaktion zwischen Handkraftaktor und Radwinkelsteller, um eine präzise und sichere Lenkung zu gewährleisten.

## Steer-by-Wire-Prinzip

Das Steer-by-Wire-System ersetzt die mechanische Lenksäule vollständig durch elektronische Komponenten und Kommunikationsleitungen, was mehrere Vorteile bietet:

1. **Variable Lenkunterstützung und Lenkübersetzung:** Anpassung der Lenkunterstützung und -übersetzung an die Fahrsituation.
2. **Individuelle Einstellung der Lenkcharakteristik:** Fahrer können die Lenkcharakteristik nach ihren Vorlieben einstellen.
3. **Integration in die Fahrdynamikregelung:** Erhöhung der aktiven Sicherheit durch Einbindung der Lenkung in Systeme wie ESP II, das durch aktive Lenkregelfunktionen neue Dimensionen der Fahrdynamik und Fahrstabilität eröffnet.

## Abbildung: Steer-by-Wire-Prinzip

![alt text](../images/sbw.png)

Die Abbildung illustriert das Steer-by-Wire-System mit seinen Hauptkomponenten:

- Handkraftaktor (Handkraftaktor)
- Lenkungsregler (Lenkungsregler)
- Radwinkelsteller (Radwinkelsteller)
- Die Kommunikation erfolgt über FlexRay-Leitungen, die eine schnelle und zuverlässige Datenübertragung sicherstellen.

Durch die beschriebenen Technologien und Sicherheitsmaßnahmen kann das Steer-by-Wire-System einen bedeutenden Beitrag zur Weiterentwicklung der Fahrzeugsicherheit und -dynamik leisten.


## Sicherheitsaspekte und Herausforderungen

Die Lenkung zählt zu den sicherheitskritischsten Systemen im Fahrzeug. Der Verzicht auf eine mechanische Rückfallebene im Steer-by-Wire-System stellt besondere Anforderungen an die Zuverlässigkeit der elektronischen Komponenten. Zu den wesentlichen Herausforderungen gehören:

1. **Fehlertoleranz:** Entwicklung von Systemen, die auch bei einem Teilausfall der Elektronik die Kontrolle über das Fahrzeug ermöglichen.
2. **Redundanz:** Implementierung von redundanten Systemen und Kommunikationswegen, um den Ausfall einzelner Komponenten zu kompensieren.
3. **Sicherheitsüberprüfungen:** Strenge Tests und Validierungen, um die Funktionssicherheit und Zuverlässigkeit zu gewährleisten.

## Fazit

Das Steer-by-Wire-Prinzip, unterstützt durch FlexRay-Kommunikation, bietet erhebliche Vorteile hinsichtlich Flexibilität, Anpassbarkeit und Integration in moderne Fahrassistenzsysteme. Dennoch erfordert die Umsetzung dieses Prinzips eine sorgfältige Berücksichtigung der Sicherheitsanforderungen und die Entwicklung robuster Fehlertoleranzstrategien. Die fortschreitende Forschung und Entwicklung auf diesem Gebiet wird die Einführung zuverlässiger und sicherer Steer-by-Wire-Systeme in Serienfahrzeugen ermöglichen.