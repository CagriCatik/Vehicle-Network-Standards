# Runnables

In AUTOSAR, **Runnables** are the fundamental executable units within **Atomic Software Components (SWCs)**. They define the actual behavior of an SWC and are invoked by the **Runtime Environment (RTE)** based on specific triggers, such as timer events, received data, or operation calls. This document explains the concept, structure, and implementation of Runnables in the AUTOSAR Classic Platform.

---

## **1. What are Runnables?**

### **Definition**
- A Runnable is a function within an Atomic SWC that implements a specific part of the component’s behavior.
- It is the smallest schedulable unit in the AUTOSAR architecture.

### **Key Features**
1. **Internal Behavior**:
   - Runnables encapsulate the functional logic of an SWC.
2. **Trigger Mechanism**:
   - Invoked by the RTE when predefined triggers occur (e.g., timer expiration, data reception, or service calls).
3. **Flexibility**:
   - Multiple Runnables can exist within a single SWC to implement various functionalities.

---

## **2. Runnable Structure**

### **Atomic Software Component Example**
In the provided image, the **Left Door** SWC contains a Runnable named `SA_Left`.

### **Implementation**:
- The Runnable is triggered every 200 milliseconds.
- It reads the door status and sends it to the RTE for further processing.

#### Runnable Example Code:
```c
// Runnable triggered every 200 msec
void SA_Left(void) {
    /* Example implementation start */
    Std_ReturnType status;
    boolean DoorOpen;

    // Logic to determine the door state (e.g., from a sensor)
    DoorOpen = ReadDoorSensor();

    // Write the door state to the RTE for other components to use
    status = Rte_Write_<Port>_<Data>(DoorOpen);

    /* Example implementation end */
}
```

---

## **3. Trigger Mechanisms**

Runnables are executed when specific triggers occur. Common trigger types include:

### **3.1 Timer Triggers**
- Invoked periodically based on a timer configured in the RTE.
- Example: `SA_Left` is triggered every 200 ms.

### **3.2 Data Reception**
- Triggered when new data is received by the SWC via its Require Port (R-Port).
- Example: A Runnable processes updated sensor data from another SWC.

### **3.3 Operation Calls**
- Triggered when a service or operation is invoked by another SWC or RTE.
- Example: A diagnostic operation request triggers a Runnable to process the request.

---

## **4. Communication with RTE**

Runnables interact with the RTE to:
1. **Read Inputs**:
   - Access data from Require Ports (R-Ports).
2. **Write Outputs**:
   - Send data to Provide Ports (P-Ports).
3. **Call Services**:
   - Invoke server operations or services.

#### Code Example:
1. **Reading Data from RTE**:
   ```c
   boolean DoorOpen;
   Rte_Read_<Port>_<Data>(&DoorOpen);  // Read door status from RTE
   ```

2. **Writing Data to RTE**:
   ```c
   Rte_Write_<Port>_<Data>(DoorOpen);  // Write door status to RTE
   ```

---

## **5. Runnable Timing and Scheduling**

### **5.1 Timing**
- The timing for Runnable execution is defined in the RTE configuration.
- Timers ensure deterministic behavior, especially for safety-critical systems.

### **5.2 Scheduling**
- Runnables are mapped to tasks, and their execution order is determined by the OS scheduler.
- Priority and timing constraints are managed to meet real-time requirements.

---

## **6. Advantages of Runnables**

### **6.1 Modularity**
- Runnables encapsulate specific functionality, enabling modular development and testing.

### **6.2 Reusability**
- Atomic SWCs and their Runnables can be reused across projects with minimal changes.

### **6.3 Scalability**
- Multiple Runnables can be added to a single SWC to implement additional features.

### **6.4 Determinism**
- Timers and trigger-based execution ensure predictable behavior.

---

## **7. Use Case: Door Monitoring System**

In the provided example:
1. The **Left Door** SWC monitors the state of the door using a sensor.
2. The Runnable `SA_Left` executes every 200 ms to:
   - Read the door state (open/closed).
   - Send the state to the RTE for other components (e.g., lighting control) to process.

---

## **8. Summary**

**Runnables** are essential building blocks in the AUTOSAR architecture, providing a mechanism to implement and execute the functional behavior of SWCs. By leveraging triggers and RTE interaction, Runnables enable modular, reusable, and scalable development of automotive software systems.
