# Components View for Lighting Control

This documentation outlines the **Components View for Lighting Control** in an AUTOSAR-based application. The diagram illustrates the interaction between software components in an embedded system designed for vehicle lighting management. Each component plays a specific role, and their interconnection enables the overall functionality of the lighting control system.

---

## **1. Overview of the Components**

### **1.1 Right Door and Left Door**
- These components represent the software abstraction of the vehicle doors.
- Their primary function is to detect the status of the doors (open or closed).
- Each door component communicates with the **Door Contact** component to notify the current state.

#### Example Use Case:
When a door opens, the corresponding component triggers a signal to the **Door Contact** module, initiating further actions like lighting activation.

---

### **1.2 Door Contact**
- The **Door Contact** component aggregates signals from both the **Right Door** and **Left Door** components.
- It acts as a logical gateway, determining whether a door has been opened.
- Based on its evaluation, it communicates with the **Dimmer** and **Light** components to manage the vehicle's interior or exterior lighting.

#### Example Workflow:
1. Receives input from the **Right Door** or **Left Door**.
2. Processes the input to determine if lighting should be activated or dimmed.
3. Forwards the decision to the **Dimmer**.

#### Code Snippet:
```c
void DoorContact_Process(bool rightDoorStatus, bool leftDoorStatus) {
    if (rightDoorStatus || leftDoorStatus) {
        ActivateLighting();
    } else {
        DeactivateLighting();
    }
}
```

---

### **1.3 Switch**
- The **Switch** component acts as a manual control interface.
- It allows the user to override automatic operations and directly control the lighting system.

#### Use Case:
The driver can manually turn the lights on or off, regardless of door status.

---

### **1.4 Dimmer**
- The **Dimmer** component controls the brightness of the lights.
- It receives input from the **Door Contact** and/or **Switch** components.
- Based on these inputs, it adjusts the lighting intensity to match the desired behavior.

#### Key Functions:
- Gradually increase brightness when a door opens.
- Reduce brightness when transitioning to standby or off mode.

#### Code Snippet:
```c
void Dimmer_AdjustBrightness(int targetBrightness) {
    int currentBrightness = GetCurrentBrightness();
    while (currentBrightness != targetBrightness) {
        UpdateBrightness(currentBrightness++);
    }
}
```

---

### **1.5 Light**
- The **Light** component is the endpoint that controls the actual lighting hardware (e.g., LEDs or bulbs).
- It executes commands from the **Dimmer** or **Switch** components to modify the lighting state.

#### Example:
When the **Dimmer** sends a brightness value, the **Light** component applies the setting to the hardware.

---

## **2. Component Interactions**

### **2.1 Signal Flow**
- **Right Door/Left Door → Door Contact:** These components send their door status to the **Door Contact** module.
- **Door Contact → Dimmer:** The **Door Contact** determines whether the lighting system needs to activate or remain inactive.
- **Switch → Dimmer:** The **Switch** can override **Door Contact** decisions, providing manual control.
- **Dimmer → Light:** The **Dimmer** sends brightness levels to the **Light** module for implementation.

---

## **3. Functional Overview**

### **3.1 Door-Based Lighting**
- The system activates the lights when any door is open and dims or turns them off when all doors are closed.

#### Workflow:
1. **Right Door/Left Door** sends door status to the **Door Contact**.
2. The **Door Contact** evaluates the status and forwards the information to the **Dimmer**.
3. The **Dimmer** adjusts the brightness, sending the target value to the **Light**.

---

### **3.2 Manual Lighting Control**
- The **Switch** allows users to manually turn lights on or off, regardless of door states.
- The **Dimmer** prioritizes manual commands from the **Switch** over automatic inputs from the **Door Contact**.

#### Workflow:
1. The user interacts with the **Switch**.
2. The **Switch** sends the command to the **Dimmer**.
3. The **Dimmer** updates the light state and brightness accordingly.

---

## **4. Advanced Considerations**

### **4.1 Fault Tolerance**
- Ensure the system can handle inconsistent door signals (e.g., faulty sensors).
- Add redundancy checks in the **Door Contact** component to verify input validity.

#### Code Snippet:
```c
bool ValidateDoorInput(bool doorStatus) {
    // Logic to validate sensor input
    return (doorStatus == true || doorStatus == false);
}
```

### **4.2 Timing and Delays**
- Implement delays in the **Dimmer** to provide smooth transitions between brightness levels.

#### Example:
Use a timer or PWM to gradually increase or decrease light intensity.

---

## **5. Benefits of the Component Design**

1. **Scalability:** Modular components allow for easy integration of additional features, such as ambient lighting or advanced dimming controls.
2. **Maintainability:** Independent modules simplify debugging and testing.
3. **Reusability:** Standardized interfaces enable the reuse of components across different vehicle models.
