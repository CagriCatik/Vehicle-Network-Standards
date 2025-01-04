# Local Interconnect Network (LIN)


<div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Logo_lin_bus.svg/2880px-Logo_lin_bus.svg.png" alt="CAN Logo" style="width:30%; max-width:800px;">
</div>



Dieses Repository enthält Informationen und Erklärungen zum Local Interconnect Network. Es bietet Einblicke in die Funktionsweise, die Protokolle und die Technologien hinter diesem Netzwerk. LIN steht für "Local Interconnect Network". Es handelt sich um ein serielles Netzwerkprotokoll, das speziell für die Kommunikation zwischen verschiedenen elektronischen Steuergeräten in Fahrzeugen entwickelt wurde. Im Gegensatz zu CAN (Controller Area Network) ist LIN eher für einfache und kostengünstige Anwendungen gedacht, bei denen keine hohe Datenübertragungsrate erforderlich ist. LIN wird oft für Aufgaben wie die Steuerung von Beleuchtung, Fensterhebern, Spiegeln und anderen weniger kritischen Funktionen in Fahrzeugen eingesetzt. Es bietet eine kostengünstige Möglichkeit zur Vernetzung von Steuergeräten in einem Fahrzeug und ergänzt damit andere Kommunikationsprotokolle wie CAN.

## 📚 Inhaltsverzeichnis

1. [Einführung 🚀](./mdbook/src/01_Einfuehrung/README.md)
   * [1.1. Motivation]()
   * [1.2. Spezifikation]()
   * [1.3. Workflow]()
2. [Netzwerkarchitektur 🌐](./mdbook/src/02_Netzwerkarchitektur/README.md)
   * [2.1. Grundaufbau]()
   * [2.2. Serielle Schnittstelle]()
   * [2.3. Signalübertragung]()
3. [Kommunikation 📡](./mdbook/src/03_Kommunikation/README.md)
   * [3.1. Prinzip]()
   * [3.2. Prozesse]()
   * [3.3. Scheduling]()
4. [Botschaftsstruktur 📜](./mdbook/src/04_Botschaftsstruktur/README.md)
   * [4.1. Frame Header]()
   * [4.2. Synchronisation]()
   * [4.3. Protected Identifier]()
   * [4.4. Frame Response]()
5. [Botschaftstypen 📧](./mdbook/src/05_Botschaftstypen/README.md)
   * [5.1. Unconditional Frame]()
   * [5.2. Event Triggered Frame]()
   * [5.3. Sporadic Frame]()
   * [5.4. Diagnostic Frame]()
6. [Datensicherung 🔒](./mdbook/src/06_Datensicherung/README.md)
   * [6.1. Mechanismen]()
   * [6.2. Prüfsumme]()
7. [Diagnose 🩺](./mdbook/src/07_Diagnose/README.md)
   * [7.1. Diagnose]()
8. [Netzwerkmanagement 🖥️](./mdbook/src/08_Netzwerkmanagement/README.md)
   * [8.1. Netzwerkmanagement]()

## Quellen

* [LIN: Lernmodul Einführung in LIN | Vector E-Learning](https://elearning.vector.com/mod/page/view.php?id=199)
* [Bussysteme in der Fahrzeugtechnik: Protokolle, Standards und Softwarearchitektur | SpringerLink](https://link.springer.com/book/10.1007/978-3-658-02419-2)
* [Elektrik/Elektronik-Architekturen im Kraftfahrzeug: Modellierung und Bewertung von Echtzeitsystemen | SpringerLink](https://link.springer.com/book/10.1007/978-3-642-25478-9)
