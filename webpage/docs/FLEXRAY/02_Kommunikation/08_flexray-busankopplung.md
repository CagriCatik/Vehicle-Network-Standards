# FlexRay - Busankopplung

## Einleitung

FlexRay ist ein robustes und zuverlässiges Kommunikationsprotokoll, das speziell für den Einsatz in der Fahrzeugelektronik entwickelt wurde. Es bietet eine hohe Datenrate und deterministische Kommunikation, was es ideal für sicherheitskritische Anwendungen macht. In diesem Tutorial werden wir die Rolle des FlexRay Controllers und des FlexRay Transceivers erläutern und auf die technische Umsetzung und Herausforderungen bei der Integration in Fahrzeuge eingehen.

## FlexRay Controller und physikalisches Übertragungsmedium

Der FlexRay Controller ist das Herzstück eines FlexRay Netzwerks. Er generiert und verarbeitet binäre Datenströme, die zur Kommunikation über das Netzwerk verwendet werden. Der FlexRay Controller kann jedoch nicht direkt an das physikalische Übertragungsmedium angeschlossen werden, da dieses auf Differenzsignalübertragung basiert. Differenzsignale sind notwendig, um eine hohe Störsicherheit und Zuverlässigkeit zu gewährleisten, da sie weniger anfällig für elektromagnetische Störungen sind.

## FlexRay Transceiver: Die Schnittstelle zwischen Controller und Bus

Der FlexRay Transceiver übernimmt die wichtige Aufgabe, die vom FlexRay Controller kommenden logischen Signale in Differenzsignale umzuwandeln und umgekehrt. Dies ermöglicht die effektive Kommunikation über das FlexRay Netzwerk. Der Transceiver hat folgende Hauptfunktionen:

1. **Umwandlung von Signalen**: Er konvertiert die binären Signale des Controllers in Differenzsignale und die Differenzsignale vom Bus in binäre Signale.
2. **Steuerung durch den Host**: Der Transceiver verfügt über Steuerleitungen (STBN und EN), die vom Host-System kontrolliert werden, um den Betriebszustand des Transceivers festzulegen.
3. **Betriebszustände**: Der Transceiver kann in verschiedene Zustände versetzt werden: „Normal“, „Standby“, „Sleep“, und „ReceiveOnly“. Die letzten beiden Zustände sind optional und dienen der Energieeinsparung bzw. dem Empfangsmodus ohne Senden.

## Elektromagnetische Verträglichkeit (EMV) und Entstörung

Ein kritischer Aspekt des FlexRay Transceivers ist seine elektromagnetische Verträglichkeit (EMV). Trotz hoher EMV lassen sich durch den Einsatz von Entstördrosseln (LC-Filter) die Emissionen weiter reduzieren. Dies ist wichtig, um Störungen anderer empfindlicher Elektroniksysteme im Fahrzeug zu minimieren.

## LC-Entstörschaltungen

LC-Entstörschaltungen bestehen aus Induktivitäten (Drosseln) und Kondensatoren. Sie unterdrücken hochfrequente Störungen und sorgen für eine saubere Signalübertragung. Die Spezifikationen für die Entstördrosseln im FlexRay System sind:

- **Leitungswiderstand**: < 2 Ohm
- **Induktivität**: > 50 μH
- **Streuinduktivität**: < 1 μH

Diese Werte stellen sicher, dass die Drosseln ausreichend Störströme unterdrücken, ohne die Signalqualität zu beeinträchtigen.

## Herausforderungen und Lösungen

Ein kleiner Nachteil der LC-Entstörschaltungen ist die Bildung eines Schwingkreises durch die Kombination von Streuinduktivität und Kopplungskondensator. Dieser Schwingkreis kann bei den Schaltvorgängen des FlexRay Transceivers zu einem Überschwingen der Bussignale führen. Um dieses Problem zu minimieren, muss die Streuinduktivität sorgfältig überwacht und kontrolliert werden.