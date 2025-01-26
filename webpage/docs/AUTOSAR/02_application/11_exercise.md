# Runnable Scheduling and Exercises

This document provides insights into **AUTOSAR Runnable Scheduling** in the context of a door and dimming system, along with two exercises to reinforce understanding of software design using AUTOSAR modeling concepts. The examples include **task prioritization**, **data exchange**, and **inter-ECU communication**.

---

## **1. Runnable Scheduling**

### **1.1 Overview**
In AUTOSAR, Runnables are scheduled tasks executed by the **Runtime Environment (RTE)**. These Runnables are mapped to OS tasks with specific priorities to ensure timely execution of functionalities, such as monitoring door states and controlling dimming.

### **1.2 Components and Tasks**

#### **Left Door**
- **Runnable Name**: `SA_Left`
- **Trigger**: Periodic, every 20 ms.
- **Task**: Monitors the state of the left door (`DoorOpen`) and sends the state to the **Door Contact** SWC.

#### **Door Contact**
- **Runnable Name**: `SA_Contact`
- **Trigger**: Event-based, triggered by input (`DoorOpen`).
- **Task**: Aggregates door states and sends contact information to the **Dimmer** SWC.

#### **Dimmer**
- **Runnables**:
  1. **`AP_Init`**:
     - Triggered during initialization to configure the dimmer.
  2. **`AP_Dim`**:
     - Triggered by the `Contact` signal from the **Door Contact** SWC.
     - Task: Adjusts dimming based on door state and time.

---

### **1.3 Task Prioritization**
- Tasks are assigned priorities to ensure deterministic execution:
  - **Task A**: Priority 1 (higher priority, faster response).
  - **Task B**: Priority 2 (lower priority, executed after Task A).

---

### **1.4 Data Flow**
1. The **Left Door** SWC sends the `DoorOpen` signal every 20 ms.
2. The **Door Contact** SWC processes the signal and triggers the **Dimmer** SWC.
3. The **Dimmer** adjusts the light intensity (`AP_Dim`) based on the input from the **Door Contact**.

---

## **2. Exercises**

### **Exercise 1: Interior Light Functionality**
#### Objective:
Design a system for **interior lighting** using AUTOSAR modeling objects.

#### Requirements:
1. **Model separate SWCs** for:
   - **Sensors** (e.g., Door and Switch).
   - **Actuators** (e.g., Light).
2. Implement an **Application SWC** to:
   - Interpret the door and switch states.
   - Pass the interpreted status to the actuator SWC.
3. Add functionality for:
   - **Shutoff delay** (turn off the light after a delay).
   - **Dimming behavior** (gradual brightness adjustment).

---

### **Exercise 2: Mapping SWCs Across ECUs**
#### Objective:
Map the SWCs designed in Exercise 1 to three ECUs (Rear, Front, and Roof).

#### Requirements:
1. Assign each SWC to one of the ECUs:
   - Example: Rear ECU for sensors, Roof ECU for lighting.
2. Identify and document the **information exchanged** between the ECUs:
   - Example: Door state from Rear ECU to Roof ECU for light control.

---

## **3. AUTOSAR Design Insights**

### **3.1 Modularity**
- By dividing functionalities into discrete SWCs (e.g., Door, Contact, Dimmer), the design is modular and reusable.

### **3.2 Prioritization**
- Assigning priorities ensures critical tasks like door monitoring (`SA_Left`) are executed promptly.

### **3.3 Inter-ECU Communication**
- Efficient data exchange between ECUs is essential for real-time operation of distributed systems.

---

## **4. Implementation Example**

### **Door Monitoring and Light Control**
1. **Left Door SWC**:
   ```c
   void SA_Left(void) {
       boolean DoorOpen = ReadDoorSensor(); // Check door state
       Rte_Write_LeftDoor_DoorOpen(DoorOpen); // Send to RTE
   }
   ```

2. **Door Contact SWC**:
   ```c
   void SA_Contact(void) {
       boolean DoorOpen;
       Rte_Read_LeftDoor_DoorOpen(&DoorOpen); // Read from RTE
       ProcessDoorState(DoorOpen); // Aggregate and process
   }
   ```

3. **Dimmer SWC**:
   ```c
   void AP_Dim(void) {
       boolean ContactSignal;
       Rte_Read_DoorContact_Contact(&ContactSignal); // Read from RTE
       AdjustBrightness(ContactSignal); // Adjust dimming
   }
   ```

---

## **5. Summary**

The provided examples illustrate how Runnables, priorities, and inter-ECU communication are used to implement a robust **interior lighting system** in AUTOSAR. By following the exercises, developers can practice designing modular, scalable, and efficient automotive software systems.

Let me know if further elaboration is needed!