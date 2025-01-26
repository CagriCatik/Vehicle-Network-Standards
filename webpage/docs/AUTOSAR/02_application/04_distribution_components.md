# Distribution of Components

This document details the **distributed software architecture** in an AUTOSAR-based lighting control system, as shown in the diagram. The components are distributed across multiple ECUs (Electronic Control Units), with communication managed by the **Runtime Environment (RTE)** and the underlying **Basic Software (BSW)**.

The distribution of components is optimized for scalability, modularity, and efficient communication within a multi-ECU system.

---

## **1. Overview of ECU Distribution**

### **1.1 Roof ECU**
The **Roof ECU** hosts the following software components:
- **Switch**
- **Dimmer**
- **Light**

This ECU primarily handles the **lighting functionality** by:
- Receiving input from the **Switch** component.
- Controlling the brightness via the **Dimmer**.
- Directly managing the hardware for the lights.

---

### **1.2 Front ECU**
The **Front ECU** is responsible for:
- **Door Contact**
- **Left Door**
- **Right Door**

This ECU focuses on monitoring **door status** and communicating the results to the **Roof ECU** for lighting adjustments.

---

### **1.3 Communication Bus**
The two ECUs communicate over a **vehicle communication bus** (e.g., CAN, LIN, or FlexRay), ensuring real-time data transfer between the components distributed across the ECUs.

---

## **2. Architectural Layers**

### **2.1 Application Layer**
The software components (SWCs) are part of the **Application Layer**, where each SWC implements a specific functionality (e.g., door monitoring, dimming).

---

### **2.2 Runtime Environment (RTE)**
The **RTE** provides an abstraction layer between the Application Layer and the underlying Basic Software (BSW). It handles:
- Communication between SWCs, even if they are located on different ECUs.
- Data routing via the **Virtual Function Bus (VFB)**.

---

### **2.3 Basic Software (BSW)**
The **BSW** is responsible for low-level hardware abstraction, providing the Application Layer with a uniform API to interact with the ECU hardware.

Key features include:
- Drivers for the microcontroller and peripherals.
- Communication stacks for handling the bus protocols.

---

### **2.4 Controller**
The **Controller** refers to the hardware-level microcontroller in each ECU. It executes all software operations and provides the physical interfaces to sensors, actuators, and the communication bus.

---

## **3. Functional Flow Across ECUs**

### **3.1 Door Status Monitoring (Front ECU)**
1. The **Left Door** and **Right Door** SWCs monitor the door states (`OPEN` or `CLOSED`).
2. The **Door Contact** component aggregates the status of both doors and determines if lighting adjustments are required.
3. This information is sent to the **Roof ECU** over the communication bus.

#### Example:
```c
// Door Contact SWC: Sending aggregated status
void DoorContact_SendStatus(bool leftDoor, bool rightDoor) {
    bool doorOpen = leftDoor || rightDoor;
    VFB_Send("DoorStatus", doorOpen);
}
```

---

### **3.2 Lighting Control (Roof ECU)**
1. The **Roof ECU** receives the door status from the **Front ECU** via the communication bus.
2. The **Dimmer** component adjusts the brightness based on door status or manual input from the **Switch**.
3. The **Light** component applies the brightness to the physical lights.

#### Example:
```c
// Dimmer SWC: Adjusting brightness based on inputs
void Dimmer_AdjustBrightness(bool doorOpen, int switchInput) {
    int brightness = switchInput > 0 ? switchInput : (doorOpen ? 100 : 0);
    VFB_Send("LightBrightness", brightness);
}
```

---

## **4. Key Features of Distributed Architecture**

### **4.1 Modularity**
- Functional separation of SWCs into different ECUs allows independent development and testing.
- Components like **Door Contact** and **Dimmer** can be reused across vehicle models with minimal modification.

---

### **4.2 Scalability**
- New features (e.g., ambient lighting or additional sensors) can be added to the system by extending the software components or adding new ECUs.

---

### **4.3 Fault Tolerance**
- The distributed design ensures partial functionality in case of a single ECU failure. For example:
  - If the **Roof ECU** fails, door monitoring by the **Front ECU** remains operational.
  - If the **Front ECU** fails, manual lighting control via the **Switch** on the **Roof ECU** remains functional.

---

## **5. Configuration and Integration**

### **5.1 RTE Configuration**
The **RTE** must be configured to define:
- The communication paths between SWCs on different ECUs.
- The timing and scheduling of messages over the communication bus.

#### Example ARXML Snippet:
```xml
<Sender-Receiver-Interface>
    <ShortName>DoorStatus</ShortName>
    <DataElement>
        <ShortName>DoorOpen</ShortName>
        <Type>Boolean</Type>
    </DataElement>
</Sender-Receiver-Interface>
```

---

### **5.2 Communication Bus Configuration**
The bus protocol (e.g., CAN) must be configured for:
- Message IDs and priorities.
- Timing and synchronization requirements.

---

## **6. Challenges and Solutions**

### **6.1 Synchronization Across ECUs**
- **Challenge:** Ensuring real-time updates between the **Front ECU** and **Roof ECU**.
- **Solution:** Use deterministic protocols like FlexRay or configure CAN messages with high priority for critical signals (e.g., door status).

### **6.2 Fault Handling**
- **Challenge:** Handling communication failures between ECUs.
- **Solution:** Implement fallback modes (e.g., default lighting behavior if door status is unavailable).

---

## **7. Summary**

The distribution of components across the **Roof ECU** and **Front ECU** in this AUTOSAR-based system highlights the following:
- **Efficient Communication:** The RTE and VFB manage seamless data flow across ECUs.
- **Hardware Abstraction:** The BSW and RTE abstract hardware details, enabling scalable and reusable designs.
- **Robust Functionality:** Fault-tolerant design ensures reliable system operation even with partial failures.

This architecture exemplifies the principles of AUTOSAR, promoting modularity, scalability, and maintainability in embedded system design.
