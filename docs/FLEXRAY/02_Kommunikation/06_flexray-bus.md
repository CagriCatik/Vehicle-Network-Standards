
# FlexRay Bus

## Herausforderungen der elektromagnetischen Verträglichkeit

Die hohe Datenrate und der Verzicht auf geschirmte Leitungen stellen große Herausforderungen für die elektromagnetische Verträglichkeit (EMV) dar. Zur Erhöhung der Immunität gegenüber hochfrequenten Störfeldern und elektrostatischen Entladungen (ESD) sowie zur Reduzierung der Emissionen werden im FlexRay Physical Layer spezifische Maßnahmen definiert.

### Physikalische Signalübertragung

Die physikalische Signalübertragung im FlexRay-Cluster basiert auf der Übertragung von Spannungsdifferenzen. Durch Motoren, Zündanlagen und Schaltkontakte induzierte Störspannungen werden durch diese Übertragungsweise unschädlich gemacht. Dies wird durch die vergleichsweise geringen Differenzspannungen (2 Volt für den Buspegel „Data_1“, -2 Volt für den Buspegel „Data_0“) erreicht, wodurch die Emissionen gering gehalten werden.

### Busstruktur und Terminierung

Der FlexRay-Bus besteht aus zwei Leitungen: Bus Plus (BP) und Bus Minus (BM). Durch das Verdrillen dieser Leitungen wird das magnetische Feld erheblich reduziert, wodurch verdrillte Leiterpaare ohne Abschirmung in der Praxis üblich sind.

#### Reflexionen und Terminierung

Bei hohen Datenraten und großen Busausdehnungen können Signalausgleichsvorgänge (Reflexionen) auftreten. Diese Reflexionen werden durch die Terminierung der Enden des Kommunikationskanals mittels Abschlusswiderständen verhindert. Die FlexRay-Spezifikation schreibt eine Last zwischen 40 und 55 Ohm vor, weshalb die Abschlusswiderstände zwischen 80 und 110 Ohm liegen müssen. Folglich sollte das verwendete Kabel einen Wellenwiderstand in diesem Bereich aufweisen.

#### Geteilter Busabschluss

Anstelle eines einzelnen Busabschlusswiderstandes kann auch ein geteilter Busabschluss verwendet werden. Dieser wirkt wie ein Tiefpassfilter und kurzschließt hochfrequente Signale gegen Masse, ohne die Gleichspannungsverhältnisse zu beeinflussen. Dies trägt zur weiteren Reduzierung von Störungen bei und verbessert die EMV.

## Kritische Bewertung

Während die FlexRay-Technologie erhebliche Fortschritte in der Fahrzeugelektrik ermöglicht, gibt es auch kritische Punkte zu beachten:

1. **Kosten für ungeeignete Kabel**: Obwohl FlexRay ungeeignete, nicht abgeschirmte Kabel verwendet, ist es wichtig, dass diese Kabel von hoher Qualität sind, um Störungen zu minimieren.
2. **Komplexität der Implementierung**: Die genaue Einhaltung der Spezifikationen und die korrekte Terminierung sind entscheidend, um Reflexionen und Störungen zu vermeiden.
3. **EMV-Maßnahmen**: Trotz der Maßnahmen zur EMV muss die Systemumgebung sorgfältig überwacht und getestet werden, um sicherzustellen, dass die elektromagnetische Verträglichkeit gewährleistet ist.

## Fazit

FlexRay bietet eine leistungsfähige und robuste Lösung für die Datenkommunikation in Fahrzeugen, die hohe Datenraten und deterministische Übertragung ermöglicht. Durch die sorgfältige Implementierung und Berücksichtigung der EMV-Maßnahmen kann FlexRay effektiv eingesetzt werden, um den steigenden Anforderungen moderner Fahrzeuge gerecht zu werden. Dieses Tutorial hat die wesentlichen Aspekte und Herausforderungen der FlexRay-Technologie erläutert und bietet eine solide Grundlage für deren Anwendung in der Praxis.
