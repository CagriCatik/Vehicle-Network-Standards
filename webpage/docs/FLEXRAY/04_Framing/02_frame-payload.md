
# Nachrichtenübertragung und Fehlererkennung

In diesem Tutorial werden wir uns intensiv mit dem FlexRay-Kommunikationsprotokoll beschäftigen, das in der Fahrzeugelektrik und -elektronik weit verbreitet ist. Wir werden die Struktur der Nachrichtenübertragung sowie die Mechanismen zur Fehlererkennung im FlexRay-Netzwerk untersuchen. Dabei werden wir die Spezifikationen und Funktionen präzise und detailliert erläutern.

##  Nachrichtenübertragung im FlexRay-Netzwerk

### Struktur der FlexRay-Nachricht

Eine FlexRay-Nachricht besteht aus mehreren Teilen:

- **Header**: Enthält Steuerinformationen, einschließlich des Payload Preamble Indicators und des Null Frame Indicators.
- **Payload**: Der eigentliche Nutzdatenbereich der Nachricht, der bis zu 254 Nutzbytes (Payload) transportieren kann.
- **Trailer**: Enthält die CRC-Sequenz zur Fehlererkennung.

### Payload Length

Der Parameter **Payload Length** gibt die Größe des Payloads in Words (ein Word entspricht zwei Bytes) an. Im statischen Segment haben alle übertragenen Nachrichten dieselbe Payload Length, die vom Systemdesigner während der Konfigurationsphase festgelegt wird. Im dynamischen Segment können Nachrichten verschiedene Payload Length-Werte haben, da sie nicht an eine feste Größe gebunden sind.

### Network Management Vector

Bei Nachrichten im statischen Segment können die ersten zwölf Nutzbytes für die Übertragung des **Network Management Vectors** verwendet werden. Dafür muss der **Payload Preamble Indicator** im Header gesetzt werden. Der Network Management Vector dient der Realisierung des Netzmanagements in einem FlexRay-Cluster.

### Dynamische Nachrichten und Message Identifier

Wenn der Payload Preamble Indicator bei einer dynamischen FlexRay-Nachricht gesetzt ist, signalisiert dies, dass die ersten zwei Nutzbytes den **Message Identifier** enthalten. Dieser Message Identifier ermöglicht eine differenziertere Akzeptanzfilterung der Nachricht durch den Systemdesigner.

### Null Frame

In speziellen Fällen kann eine Nachricht ausschließlich mit Nullen übertragen werden, wenn der zugehörige Puffer vom Host gesperrt ist. Dies geschieht, wenn der FlexRay-Controller eine statische Nachricht senden muss, aber keinen Zugriff auf den Puffer hat. Der Header der Nachricht enthält dann einen Null Frame Indicator, der den Wert „Null“ aufweist.

## Fehlererkennung im FlexRay-Netzwerk

### CRC-Verfahren

Zur Sicherung des Payloads wird das **Cyclic Redundancy Check (CRC)**-Verfahren eingesetzt. Dieses leistungsstarke Fehlererkennungsverfahren berechnet auf Basis des Headers und Payloads sowie einem durch die FlexRay-Spezifikation definierten Generatorpolynom eine CRC-Sequenz. Diese Sequenz wird dem Header und Payload als Trailer angehängt.

### Fehlererkennung und Hamming-Distanz

Die CRC-Checksumme stellt sicher, dass Übertragungsfehler mit hoher Sicherheit erkannt werden. Ein Fehler wird festgestellt, wenn die Division der empfangenen Nachricht durch das Generatorpolynom einen Rest ergibt. Die Fehlererkennungsfähigkeit des CRC-Verfahrens hängt von der Größe des Payloads ab:

- Bei einem Payload bis zu 248 Bytes wird eine **Hamming-Distanz** von sechs garantiert.
- Bei größeren Payloads liegt die Hamming-Distanz bei vier, was zu einer geringeren Fehlererkennungsfähigkeit führt.

Die Hamming-Distanz gibt an, wie viele Bitfehler auftreten müssen, damit ein Fehler nicht erkannt wird. Eine größere Hamming-Distanz bedeutet eine höhere Fehlererkennungsfähigkeit.
