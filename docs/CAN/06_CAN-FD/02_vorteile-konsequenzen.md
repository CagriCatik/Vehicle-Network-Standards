# Vorteile und Konsequenzen

## Verbesserung der Datenübertragungseffizienz

Einer der Hauptvorteile von CAN-FD ist die Fähigkeit, Nutzdaten schneller zu übertragen, was die Busbelegungszeit effektiv reduziert. Diese Reduzierung der Buslast ermöglicht es, mehr Daten innerhalb des gleichen Zeitrahmens wie bei einer klassischen CAN-Nachricht zu übertragen.

Wenn beispielsweise die Nutzdaten in einem CAN-FD-Frame mit der fünffachen Geschwindigkeit einer klassischen CAN-Nachricht übertragen werden, bleibt die Dauer des CAN-FD-Frames nahezu gleich, obwohl er fünfmal mehr Nutzdaten enthält. Daher kann CAN-FD bei vergleichbarer Buslast eine fünffache Steigerung der Datenübertragung erreichen.

## Vereinfachung der Entwicklung

Die Einführung von CAN-FD bringt mehrere bedeutende Vorteile und Vereinfachungen im Entwicklungsprozess mit sich:

1. **Entschärfung des Buslast-Problems**: CAN-FD mildert das Buslast-Problem erheblich, wodurch eine effizientere Datenverwaltung ermöglicht wird.

2. **Reduzierung der Anzahl der CAN-Busse**: Der Trend zur Vermehrung der CAN-Busse kann umgekehrt werden, was die Komplexität der Automobilnetzwerke reduziert.

3. **Vereinfachung von Gateways**: Mit CAN-FD wird der Bedarf an komplexen Gateways verringert und in einigen Fällen sogar vollständig eliminiert.

4. **Weniger Datensegmentierung**: Größere Nutzdatennutzlasten pro Nachricht reduzieren die Notwendigkeit der Datensegmentierung, was zu einer einfacheren Datenverarbeitung führt.

5. **Verbessertes Verhältnis von Nutzdaten zum Overhead**: Weniger Nachrichten mit größeren Nutzdatennutzlasten führen zu einem besseren Verhältnis von Nutzdaten zu Overhead, was die Gesamteffizienz steigert.

## Notwendigkeit neuer Controller

Um CAN-FD zu betreiben, sind neue CAN-FD-Controller erforderlich. Diese Controller sind abwärtskompatibel und unterstützen auch das klassische CAN-Protokoll. Steuergeräte können schrittweise auf die neue CAN-FD-Technologie aufgerüstet werden. Solange jedoch noch klassische CAN-Controller im Kommunikationsnetzwerk beteiligt sind, muss das klassische CAN-Protokoll weiterhin verwendet werden.

## Koexistenz von klassischen und CAN-FD-Controllern

Das Missverständnis, dass höhere Übertragungsraten nur möglich sind, wenn alle Steuergeräte an einem CAN-Bus mit CAN-FD-Controllern ausgestattet sind, muss angesprochen werden. Partial Networking bietet eine Option, bei der Steuergeräte mit klassischen CAN-Controllern in den Schlafmodus versetzt werden können, wodurch die verbleibenden CAN-FD-fähigen Steuergeräte mit höheren Geschwindigkeiten kommunizieren können. Diese Methode ist besonders nützlich bei Fahrzeugservice-Diagnosen oder beim Aufspielen neuer Software auf Steuergeräte, da höhere Datenraten die für solche Prozesse erforderliche Zeit erheblich verkürzen können.

## Nutzung des vorhandenen CAN-Wissens

Ein weiterer Vorteil von CAN-FD ist, dass es sich um eine Erweiterung des klassischen CAN-Protokolls handelt und nicht um eine völlig neue Technologie. Daher bleibt das bestehende Wissen, die Fähigkeiten und Erfahrungen mit CAN weiterhin relevant und anwendbar. Dieser Kontinuität gewährleistet, dass der Übergang von CAN zu CAN-FD ohne umfangreiche Schulungen oder den Verlust bisheriger Errungenschaften erfolgen kann.

## Schlussfolgerung

CAN-FD stellt eine bedeutende Weiterentwicklung im Bereich der Automobilnetzwerke dar, indem es höhere Datenraten und effizientere Kommunikation bietet und gleichzeitig die Kompatibilität mit bestehenden Systemen beibehält. Seine Implementierung kann Entwicklungsprozesse vereinfachen, die Anzahl der erforderlichen Busse reduzieren und die Gesamtleistung des Netzwerks verbessern. Durch die Nutzung des vorhandenen Wissens über das klassische CAN-Protokoll kann der Übergang zu CAN-FD reibungslos und kosteneffektiv gestaltet werden, wodurch die Vorteile dieser fortschrittlichen Technologie leicht zugänglich sind.
