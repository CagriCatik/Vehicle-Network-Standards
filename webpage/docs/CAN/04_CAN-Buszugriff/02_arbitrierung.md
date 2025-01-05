
# Bitweise Arbitrierung

## Einleitung

Die bitweise Arbitrierung ist ein wesentliches Element des Controller Area Network (CAN), das in der ISO 11898-1 normiert ist. Diese Technik ermöglicht es mehreren Steuergeräten (ECUs) in einem Fahrzeug, über ein gemeinsames Netzwerk zu kommunizieren, ohne dass es zu Datenkollisionen kommt. In diesem detaillierten und wissenschaftlich fundierten Tutorial werden die Mechanismen und Abläufe der bitweisen Arbitrierung im CAN-Netzwerk erläutert, basierend auf der bereitgestellten Abbildung und ergänzenden Informationen.

## Grundlagen der bitweisen Arbitrierung

Die bitweise Arbitrierung stellt sicher, dass in einem CAN-Netzwerk nur ein Steuergerät zur gleichen Zeit auf den Bus zugreifen und Daten senden kann. Dieses Verfahren, das auch als Carrier Sense Multiple Access mit Collision Resolution (CSMA/CR) oder Collision Avoidance (CSMA/CA) bekannt ist, verhindert Kollisionen und ermöglicht eine prioritätsbasierte Übertragung von Nachrichten.

## Ablauf der bitweisen Arbitrierung

Der Ablauf der bitweisen Arbitrierung im CAN-Netzwerk ist detailliert in der Abbildung dargestellt und lässt sich in folgende Schritte unterteilen:

1. **Sendewunsch**: Ein Steuergerät möchte eine Nachricht senden.
2. **Busmonitoring**: Das Steuergerät überwacht den CAN-Bus, um dessen Zustand zu prüfen.
3. **Prüfung: Ist der CAN-Bus frei?**:
   - **Ja**: Das Steuergerät sendet das Start-of-Frame (SOF)-Bit.
   - **Nein**: Das Steuergerät wartet weiter und überwacht den Bus erneut.
4. **Senden des nächsten ID-Bits**: Das Steuergerät sendet das nächste Bit der Nachricht-Identifier (ID).
5. **Prüfung: Buspegel = Sendepegel?**:
   - **Ja**: Das Steuergerät sendet das nächste ID-Bit.
   - **Nein**: Es folgt eine Dominanzprüfung:
     - **Dominanter Buspegel & rezessiver Sendepegel?**:
       - **Ja**: Das Steuergerät geht in den Fehlerzustand.
       - **Nein**: Das Steuergerät wechselt in den Empfangszustand.
6. **Prüfung: Arbitrierungsfeld gesendet?**:
   - **Ja**: Das Steuergerät hat alle ID-Bits gesendet und wechselt in den Sendestatus.
   - **Nein**: Das Steuergerät sendet weiterhin die ID-Bits, bis das Arbitrierungsfeld vollständig gesendet ist.

## Eindeutige Buspegel

Alle sendebereiten Steuergeräte legen nach der netzwerkweiten Synchronisierung den Identifier der zu übertragenden CAN-Botschaft bitweise auf den CAN-Bus. Die Wired-AND-Buslogik des CAN-Netzwerks stellt dabei sicher, dass immer ein eindeutiger Buspegel vorliegt. Dieses Verfahren sorgt dafür, dass das dominante Bit auf dem Bus verbleibt und nur der Knoten mit der höchsten Priorität senden kann.

## Arbitrierungslogik

Die Arbitrierungslogik entscheidet, welches Steuergerät nach der Synchronisation weiter senden darf und welches aufhören muss. Dies erfolgt durch einen Vergleich der gesendeten Bits:

- Das Steuergerät, das ein rezessives Bit sendet und ein dominantes Bit empfängt, verliert die Arbitrierung und wechselt in den Empfangszustand.
- Das Steuergerät, das ein dominantes Bit sendet und kein rezessives Bit empfängt, gewinnt die Arbitrierung und darf weiter senden.

## Ende der Arbitrierungsphase

Am Ende der Arbitrierungsphase hat das Steuergerät mit der Nachricht mit der kleinsten ID die Berechtigung zu senden. Alle anderen Steuergeräte wechseln in den Empfangszustand und versuchen erneut zu senden, sobald der Bus wieder frei ist.

## Schlussfolgerung

Die bitweise Arbitrierung im CAN-Netzwerk ist ein komplexer, aber effizienter Mechanismus, der sicherstellt, dass nur das Steuergerät mit der höchsten Priorität seine Nachricht senden kann. Dies verhindert Datenkollisionen und sorgt für eine zuverlässige Kommunikation zwischen den Steuergeräten in einem Fahrzeug.

Die detaillierte Abbildung des Buszugriffsprozesses und die Erklärung der einzelnen Schritte bieten eine umfassende Übersicht über die Funktionsweise der bitweisen Arbitrierung und deren Bedeutung für die Fahrzeugkommunikation. Diese Methode ist entscheidend für die hohe Zuverlässigkeit und Robustheit moderner Fahrzeugsysteme.
