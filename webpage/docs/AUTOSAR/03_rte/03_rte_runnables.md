# Runnables

In the AUTOSAR (AUTomotive Open System ARchitecture) framework, **Runnables** are the fundamental executable units that perform specific functions within Software Components (SWCs). Managed by the **Runtime Environment (RTE)**, Runnables are triggered based on predefined events and facilitate seamless communication between SWCs, the Operating System (OS), and the Basic Software (BSW). This chapter provides an in-depth exploration of Runnables, their mapping, execution, communication mechanisms, customization, and the benefits they offer within the AUTOSAR ecosystem.

---
    
## 1. RTE Overview
    
The **Runtime Environment (RTE)** serves as the middleware layer in AUTOSAR, orchestrating the interaction between SWCs, the OS, and the BSW. Its primary responsibility is to manage Runnables by ensuring they are executed efficiently and in response to relevant events. Understanding the RTE's role is crucial for effectively leveraging Runnables in automotive software development.
    
### Key Characteristics

1. **Configurable Middleware**:
    - **Description**: The RTE allows for the mapping of Runnables to specific OS tasks during the configuration phase.
    - **Implication**: This flexibility ensures that Runnables are executed within the appropriate context, adhering to system priorities and requirements.
    
2. **Event-Based Execution**:
    - **Description**: Runnables are triggered by events predefined in the RTE configuration.
    - **Implication**: Enables responsive and efficient execution of tasks based on system and external stimuli.
    
3. **Task Configuration**:
    - **Description**: Defines task priorities, alarms, and scheduling mechanisms to optimize execution.
    - **Implication**: Ensures that critical tasks receive the necessary resources and are executed in a timely manner.
    
4. **Customizable**:
    - **Description**: Each Electronic Control Unit (ECU) possesses a unique RTE tailored to the specific SWCs it hosts.
    - **Implication**: Facilitates modularity and scalability across different hardware configurations and application domains.
    
---
    
## 2. Mapping and Execution of Runnables
    
Runnables are central to the execution flow within AUTOSAR applications. Proper mapping and execution strategies are essential for achieving optimal system performance and reliability.
    
### 2.1 Mapping Runnables to OS Tasks
    
During the system design phase, each Runnable is mapped to an OS task. This mapping is based on several factors, including priority levels, execution frequency, and triggering events.
    
#### Example: Dimmer SWC

- **Runnables**:
    - `AP_Init`: Initializes the dimmer system at startup.
    - `AP_Dim`: Adjusts brightness based on external signals (e.g., `Contact`).
    
- **Mapping**:
    - `AP_Init`: Mapped to an initialization task with high priority to ensure the dimmer system is ready promptly.
    - `AP_Dim`: Mapped to an event-based task that is triggered by the `Contact` signal, allowing dynamic brightness adjustments.
    
#### Configuration Snippet:
```xml
<Task id="Task_DimmerInit" priority="High">
    <RunnableRef>AP_Init</RunnableRef>
</Task>
<Task id="Task_DimmerControl" priority="Medium" trigger="ContactSignal">
    <RunnableRef>AP_Dim</RunnableRef>
</Task>
```
    
### 2.2 RTE Event Triggers
    
Runnables are activated in response to specific events defined within the RTE configuration. These events determine when and how Runnables are executed, ensuring that system behavior aligns with real-time requirements.
    
#### Common RTE Events

| **Event**                      | **Description**                                   | **Example Use Case**                         |
|--------------------------------|---------------------------------------------------|----------------------------------------------|
| **Init**                       | Triggered during system initialization.           | SWC initialization (e.g., `AP_Init`).        |
| **TimingEvent**                | Periodic trigger based on a timer.                | Sensor data processing every 20ms.           |
| **DataReceivedEvent** (S/R)    | Triggered when new data is received.              | Adjusting brightness based on `Contact`.     |
| **DataReceiveErrorEvent** (S/R)| Triggered on data reception failure.              | Diagnostic monitoring and error reporting.   |
| **OperationInvokedEvent** (C/S)| Triggered when a server operation is called.      | Handling diagnostic service requests.        |
| **ModeSwitchEvent**            | Triggered when a mode switch occurs.              | Switching between normal and diagnostic modes.|

#### Example Workflow

1. A `Contact` signal is received by the RTE from a sensor.
2. The RTE identifies the associated Runnable (`AP_Dim`) mapped to the `Contact` event.
3. The RTE triggers the `AP_Dim` Runnable, initiating the brightness adjustment process.

---
    
## 3. Communication Through RTE
    
Effective communication is paramount in complex automotive systems. The RTE facilitates this by managing data exchange between SWCs and between SWCs and the underlying OS/BSW. AUTOSAR supports two primary communication paradigms: **Sender/Receiver (S/R)** and **Client/Server (C/S)**.
    
### 3.1 Sender/Receiver Communication
    
In the Sender/Receiver model, SWCs exchange data through ports managed by the RTE. This model is ideal for scenarios where data flow is straightforward and does not require complex interactions.
    
#### Example

- **Sensor SWC** sends the `DoorOpen` signal:
    ```c
    Std_ReturnType status = Rte_Write_Sensor_DoorOpen(doorState);
    if (status != E_OK) {
        // Handle write failure
    }
    ```
    
- **Actuator SWC** reads the `DoorOpen` signal:
    ```c
    boolean doorState;
    Std_ReturnType status = Rte_Read_Actuator_DoorOpen(&doorState);
    if (status == E_OK) {
        // Actuate based on doorState
    } else {
        // Handle read failure
    }
    ```
    
### 3.2 Client/Server Communication
    
The Client/Server model is suited for more complex interactions where SWCs need to invoke operations or services provided by other components. This paradigm supports request-response mechanisms essential for functionalities like diagnostics.
    
#### Example

- **Client SWC** invokes a diagnostic operation:
    ```c
    DiagnosticDataType diagnosticData;
    Std_ReturnType status = Rte_Call_DiagnosticService_ReadData(&diagnosticData);
    if (status == E_OK) {
        // Process diagnosticData
    } else {
        // Handle invocation failure
    }
    ```
    
- **Server SWC** implements the diagnostic operation:
    ```c
    Std_ReturnType DiagnosticService_ReadData(DiagnosticDataType* data) {
        // Populate diagnostic data
        *data = GetDiagnosticInfo();
        return E_OK;
    }
    ```
    
---
    
## 4. RTE Customization
    
Customization of the RTE is essential to align it with the specific requirements of each ECU and its hosted SWCs. This involves configuring task priorities, event mappings, and ensuring that the RTE accurately reflects the ECU's role within the system.
    
### Key Considerations

1. **ECU-Specific Configuration**:
    - **Description**: Each ECU possesses a unique RTE configuration tailored to its specific set of SWCs and system responsibilities.
    - **Implementation**: Define distinct mappings and event triggers based on the ECU's functional role (e.g., lighting control, engine management).
    
2. **Task Configuration**:
    - **Description**: Establishes the priorities and scheduling parameters for tasks associated with Runnables.
    - **Implementation**: Assign higher priorities to critical Runnables to ensure they are executed promptly, while less critical tasks are assigned lower priorities.
    
3. **Event Mapping**:
    - **Description**: Associates Runnables with specific events to control their triggering mechanisms.
    - **Implementation**: Ensure that each Runnable is linked to the appropriate event type (e.g., `TimingEvent`, `DataReceivedEvent`) to maintain system responsiveness and reliability.
    
#### Example Configuration Snippet:
```xml
<RunnableMapping>
    <Runnable id="AP_Init">
        <TaskRef>Task_DimmerInit</TaskRef>
        <EventRef>Init</EventRef>
    </Runnable>
    <Runnable id="AP_Dim">
        <TaskRef>Task_DimmerControl</TaskRef>
        <EventRef>DataReceivedEvent_Contact</EventRef>
    </Runnable>
</RunnableMapping>
```
    
---
    
## 5. RTE Code Generation
    
The RTE is responsible for generating executable code based on the system's configuration. This automated process ensures consistency and adherence to the defined mappings and event triggers.
    
### Components of RTE Code Generation

1. **Task Routines**:
    - **Description**: Code that executes Runnables within the context of OS tasks.
    - **Example**:
        ```c
        void Rte_Task_DimmerInit(void) {
            // Execute initialization Runnable
            AP_Init();
        }
        
        void Rte_Task_DimmerControl(void) {
            // Execute dimming Runnable upon Contact event
            AP_Dim();
        }
        ```
    
2. **Event Handlers**:
    - **Description**: Logic that listens for and responds to events by triggering the associated Runnables.
    - **Example**:
        ```c
        void Event_Handler_Contact(void) {
            // Trigger the AP_Dim Runnable when Contact signal is received
            AP_Dim();
        }
        ```
    
3. **Communication Interfaces**:
    - **Description**: Code that manages data exchange through ports, ensuring that Sender/Receiver and Client/Server communications are handled correctly.
    - **Example**:
        ```c
        Std_ReturnType Rte_Write_Sensor_DoorOpen(boolean doorState) {
            // Code to write the DoorOpen signal to the RTE port
            // ...
            return E_OK;
        }
        
        Std_ReturnType Rte_Call_DiagnosticService_ReadData(DiagnosticDataType* data) {
            // Code to invoke the DiagnosticService_ReadData operation
            // ...
            return DiagnosticService_ReadData(data);
        }
        ```
    
#### Example Code Snippet:
```c
// Runnables Execution within OS Task
void Rte_Task_DimmerControl(void) {
    // Check if Contact event has triggered the Runnable
    if (ContactEventTriggered()) {
        AP_Dim();
    }
}

// Event Handler for Contact Signal
void Event_Handler_Contact(void) {
    // Trigger the AP_Dim Runnable when Contact signal is received
    AP_Dim();
}
```
    
---
    
## 6. Key Benefits of the RTE
    
The **Runtime Environment (RTE)** offers numerous advantages that enhance the development and operation of automotive software systems. Its capabilities contribute significantly to the overall efficiency, reliability, and scalability of the AUTOSAR architecture.
    
1. **Hardware Abstraction**:
    - **Benefit**: SWCs remain independent of the underlying hardware, allowing developers to focus on application logic without concerning themselves with hardware specifics.
    - **Impact**: Facilitates easier migration and scalability across different hardware platforms.
    
2. **Scalability**:
    - **Benefit**: Supports both simple and complex systems, accommodating multiple ECUs and numerous SWCs seamlessly.
    - **Impact**: Enables the development of scalable automotive systems that can evolve with increasing functional requirements.
    
3. **Interoperability**:
    - **Benefit**: Standardized communication protocols and interfaces ensure consistent and reliable data exchange between SWCs.
    - **Impact**: Reduces integration challenges and enhances the reliability of inter-component communications.
    
4. **Deterministic Behavior**:
    - **Benefit**: Ensures predictable execution of critical tasks through prioritized scheduling and event-based triggers.
    - **Impact**: Essential for safety-critical applications where timing and reliability are paramount.
    
5. **Modularity and Reusability**:
    - **Benefit**: Encourages the development of modular SWCs that can be reused across different projects and platforms.
    - **Impact**: Reduces development time and costs while promoting a clean and maintainable codebase.
    
6. **Ease of Configuration and Maintenance**:
    - **Benefit**: Simplifies the configuration process through standardized tools and methodologies.
    - **Impact**: Enhances maintainability and facilitates easier system updates and troubleshooting.
    
---
    
## 7. Use Case: Interior Lighting System
    
To illustrate the practical application of Runnables within the AUTOSAR framework, consider the following use case focused on an **Interior Lighting System**. This example demonstrates how Runnables interact with each other and with the RTE to achieve the desired functionality.
    
### Workflow
    
1. **SWC1: Door Monitoring**
    - **Function**: Monitors the state of the vehicle's doors.
    - **Runnable**: `MonitorDoorState`
    - **Action**: Sends a `Contact` signal when a door is opened or closed.
    
    ```c
    // SWC1: Door Monitoring
    void MonitorDoorState(void) {
        boolean doorState = ReadDoorSensor();
        Std_ReturnType status = Rte_Write_Sensor_Contact(doorState);
        if (status != E_OK) {
            // Handle write failure
        }
    }
    ```
    
2. **SWC2: Dimmer**
    - **Functions**:
        - `AP_Init`: Initializes the dimmer system at startup.
        - `AP_Dim`: Adjusts brightness based on the `Contact` signal.
    
    ```c
    // SWC2: Dimmer
    void AP_Init(void) {
        // Initialize dimmer hardware
        InitializeDimmingHardware();
    }
    
    void AP_Dim(void) {
        boolean doorOpen;
        Std_ReturnType status = Rte_Read_Sensor_Contact(&doorOpen);
        if (status == E_OK) {
            uint8_t brightness = doorOpen ? 75 : 0; // 75% if door open, else off
            Std_ReturnType writeStatus = Rte_Write_Actuator_Lighting(brightness);
            if (writeStatus != E_OK) {
                // Handle write failure
            }
        } else {
            // Handle read failure
        }
    }
    ```
    
3. **RTE Configuration**
    - **Mapping**:
        - `AP_Init` is mapped to an initialization task triggered during system startup.
        - `AP_Dim` is mapped to an event-based task triggered by the `Contact` signal.
    
    ```xml
    <RunnableMapping>
        <Runnable id="AP_Init">
            <TaskRef>Task_DimmerInit</TaskRef>
            <EventRef>Init</EventRef>
        </Runnable>
        <Runnable id="AP_Dim">
            <TaskRef>Task_DimmerControl</TaskRef>
            <EventRef>DataReceivedEvent_Contact</EventRef>
        </Runnable>
    </RunnableMapping>
    ```
    
4. **Execution Flow**
    - **Initialization**:
        1. System starts, triggering the `Init` event.
        2. RTE executes `AP_Init` Runnable to initialize the dimmer system.
    
    - **Runtime Operation**:
        1. A door is opened, triggering the `DataReceivedEvent_Contact`.
        2. RTE executes `AP_Dim` Runnable to adjust the interior lighting based on the door state.
        3. The actuator receives the brightness value and adjusts the lights accordingly.
    
    #### Diagram:
    ```plaintext
    [Door Sensor] --> [RTE] --> [SWC1: MonitorDoorState] --> [RTE] --> [SWC2: AP_Dim] --> [RTE] --> [Actuator: Lighting Control] --> [MCAL] --> [Interior Lights]
    ```
    
    #### Combined Code Example:
    ```c
    // SWC1: Door Monitoring
    void MonitorDoorState(void) {
        boolean doorState = ReadDoorSensor();
        Std_ReturnType status = Rte_Write_Sensor_Contact(doorState);
        if (status != E_OK) {
            // Handle write failure
        }
    }
    
    // SWC2: Dimmer
    void AP_Init(void) {
        InitializeDimmingHardware();
    }
    
    void AP_Dim(void) {
        boolean doorOpen;
        Std_ReturnType status = Rte_Read_Sensor_Contact(&doorOpen);
        if (status == E_OK) {
            uint8_t brightness = doorOpen ? 75 : 0;
            Std_ReturnType writeStatus = Rte_Write_Actuator_Lighting(brightness);
            if (writeStatus != E_OK) {
                // Handle write failure
            }
        } else {
            // Handle read failure
        }
    }
    
    // Actuator Control via MCAL
    void AdjustLightIntensity(void) {
        uint8_t brightness;
        Std_ReturnType status = Rte_Read_Actuator_Lighting(&brightness);
        if (status == E_OK) {
            uint16_t dutyCycle = (brightness * MAX_PWM_VALUE) / 100;
            Pwm_SetDutyCycle(PWM_CHANNEL_LIGHT, dutyCycle);
        } else {
            // Handle read failure
        }
    }
    ```
    
---
    
## 8. Summary
    
Runnables are the smallest executable units within the AUTOSAR framework, orchestrated by the RTE to perform specific functions in response to defined events. This chapter has delved into the intricacies of Runnables, covering their mapping to OS tasks, execution triggers, communication mechanisms, customization, and the benefits they provide.
    
### Key Takeaways

- **Runnable Management**: The RTE efficiently maps and triggers Runnables based on system events, ensuring timely and prioritized execution.
- **Communication Paradigms**: AUTOSAR supports both **Sender/Receiver** and **Client/Server** communication models, enabling flexible data exchange between SWCs.
- **Customization**: Each ECU's RTE is uniquely configured to reflect its specific set of SWCs and system roles, promoting modularity and scalability.
- **Code Generation**: Automated RTE code generation ensures consistency and adherence to defined configurations, reducing manual coding errors.
- **Benefits**:
    - **Hardware Abstraction**: Runnables operate independently of hardware specifics, facilitating portability and scalability.
    - **Scalability and Interoperability**: The RTE supports complex systems with multiple ECUs and SWCs, ensuring standardized communication and execution.
    - **Deterministic Behavior**: Predictable execution patterns are maintained through prioritized scheduling and event-based triggers, crucial for safety-critical applications.

By effectively managing Runnables, the RTE plays a pivotal role in the AUTOSAR architecture, enabling the development of robust, efficient, and scalable automotive software systems.

---
    
# Conclusion
    
This comprehensive documentation has provided an extensive overview of **Runnables** within the AUTOSAR framework, highlighting their critical role in automotive software development. By understanding how Runnables are managed, mapped, and executed through the RTE, developers can design modular, scalable, and efficient automotive systems. Whether you are a beginner seeking foundational knowledge or an advanced practitioner aiming to refine your expertise, this guide offers valuable insights into leveraging Runnables to their fullest potential within the AUTOSAR ecosystem.