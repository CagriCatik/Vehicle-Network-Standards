# Faults and failures

In the realm of automotive functional safety, understanding the intricacies of faults and failures is paramount. ISO 26262, the international standard for the functional safety of electrical and electronic systems in road vehicles, provides a comprehensive framework for identifying, categorizing, and mitigating these faults to ensure vehicle safety. This documentation delves into the detailed concepts of faults and failures as defined by ISO 26262, offering clear explanations, practical examples, and best practices to guide automotive engineers in designing safer systems.

## Key Concepts

### Definitions

- **Fault**: A condition in a system component that can lead to a failure. According to IEC 60050, Part 191, a fault is a state that precedes a failure.
  
- **Failure**: An event that occurs when a fault manifests, resulting in the system not performing its intended function.

### Types of Failures

ISO 26262 categorizes failures based on their origin and behavior. Understanding these classifications is essential for implementing effective safety measures.

1. **Random Failures**
   - **Definition**: Failures that occur unpredictably during the lifetime of a hardware element, following a probability distribution.
   - **Characteristics**:
     - Limited to hardware elements.
     - Cannot be prevented; only detected and controlled.
     - Have a specific failure rate and failure mode.
   - **Handling**:
     - Implement safety mechanisms to detect and mitigate these failures in real-time.

2. **Systematic Failures**
   - **Definition**: Failures related deterministically to a specific cause, such as design flaws or manufacturing defects.
   - **Characteristics**:
     - Applicable to hardware, software, and processes.
     - Can be eliminated through changes in design, manufacturing, or operational procedures.
   - **Handling**:
     - Implement safety measures to prevent, detect, or control these failures through robust design and quality assurance processes.

## Failure Rates and Failure Modes

### Failure Rate

- **Definition**: The probability of a hardware element failing, expressed as FIT (Failures In Time).
  - **1 FIT** = 1 failure per billion (10⁹) hours of operation.
  
- **Calculation**: According to ISO 26262, the failure rate is the probability density of failure divided by the probability of survival for a hardware element.

### Failure Mode

- **Definition**: The manner in which an element or system fails to perform its intended function.
  
- **Examples**:
  - **Open Circuit**: A break in the circuit causing it to stop conducting.
  - **Short Circuit**: An unintended connection between two points in the circuit.
  - **Stuck-at Fault**: A signal line that is stuck at a logical high or low value.

## Safety Mechanisms and Diagnostic Coverage

### Safety Mechanism

- **Definition**: A technical solution implemented by electrical/electronic functions or elements to detect and mitigate faults, control or avoid failures, and maintain intended functionality or achieve a safe state.
  
- **Examples**:
  - **Cyclic Redundancy Check (CRC)**: Ensures data integrity.
  - **Watchdog Timers**: Detect unresponsive hardware or software components.
  - **Redundant Sensors**: Provide backup data in case of sensor failure.

### Diagnostic Coverage

- **Definition**: The percentage of the failure rate of a hardware element or failure mode that is detected or controlled by the implemented safety mechanism.
  
- **Standard Coverage Rates**:
  - **60%**
  - **90%**
  - **99%**
  
- **Importance**: Determines the effectiveness of safety mechanisms in identifying and mitigating faults.

## Classification of Faults

ISO 26262 further classifies faults based on their impact and behavior within the system.

### Single Point Faults

- **Definition**: Faults in a single hardware element without any safety mechanism, leading directly to the violation of a safety goal.
  
- **Example**: An unsupervised resistor stuck in an open state that can disrupt the steering mechanism.

### Residual Faults

- **Definition**: Portions of random hardware faults not covered by safety mechanisms, potentially leading to safety goal violations.
  
- **Example**: A torque sensor with a safety mechanism that only detects "stuck at open" faults, leaving "stuck at short" faults as residual.

### Latent Dual Point Faults (Latent Faults)

- **Definition**: Multiple faults that are not detected by safety mechanisms or perceived by the driver within a specified time interval, leading to safety goal violations only when combined.
  
- **Example**: 
  - **Scenario**: A microcontroller and its watchdog timer both fail, preventing the system from detecting and responding to a critical sensor fault.

### Detected Dual Point Faults

- **Definition**: Multiple faults where at least one fault is detected by a safety mechanism, preventing the combination from violating safety goals.
  
- **Example**: 
  - **Scenario**: A flash memory protected by ECC (Error Correction Code) fails, but the ECC logic detects the fault and triggers a safe state transition.

### Perceived Dual Point Faults

- **Definition**: Multiple faults that are detected or perceived by the driver within a specified time interval, preventing the combination from violating safety goals.
  
- **Example**: 
  - **Scenario**: Both a steering sensor and its safety mechanism fail, but the driver perceives the steering issue and takes corrective action.

### Safe Faults

- **Definition**: Faults that do not significantly increase the probability of violating a safety goal.
  
- **Characteristics**:
  - Can occur in both safety-relevant and non-safety-relevant hardware elements.
  - Typically, non-safety-relevant components should only have safe faults.
  
- **Exception**:
  - **Triple Point Faults**: Faults involving three independent elements are considered safe due to their low probability.

## Failure Rate Standards

To determine failure rates and failure modes, ISO 26262 recommends using established standards:

- **IEC 61709**
  - **Description**: Provides methods for determining failure rates of electrical and electronic components.
  
- **SN 29500** (Less Accessible)
  - **Description**: Another standard for deriving failure rates, though less commonly used due to accessibility issues.
  
- **IEC 61508**
  - **Description**: A broader functional safety standard applicable to various industries, offering principles used in ISO 26262.

## Diagnostic Coverage Evaluation

### Annex D of ISO 26262 Part 5

- **Content**: Provides tables and guidelines to evaluate the diagnostic coverage of safety mechanisms.
  
- **Usage**: Helps determine the appropriate diagnostic coverage rates (60%, 90%, 99%) for different safety mechanisms based on their roles and the associated failure rates.

## Practical Example: Steering Wheel Position Sensor

### Sensor Characteristics

- **Analog Signal**: Translated to digital form using a conversion formula.
- **Minimum Angle Detection**: 0.1 degrees.
- **Accuracy**: 0.01 degrees.
- **Initialization Period**: Output unusable for 10 milliseconds.
- **Hardware Reset Time**: 5 milliseconds.
- **Safety Goal**: Assigned ASIL D, decomposed into torque and angle sensor components.

### Derived Hardware Safety Requirements

1. **Fault Detection**:
   - Detect failure mode "stuck at" for element X within 150 milliseconds.
   
2. **Data Integrity**:
   - Implement CRC for memory area K to detect memory faults.
   
3. **Power Supply Monitoring**:
   - Establish a readback channel for power supply channels X and Y to monitor voltage levels.
   
4. **Watchdog Timer Configuration**:
   - Configure the watchdog timer with a separate time base and defined time window to detect unresponsive hardware.

## Handling Random Failures

### Designing Safety Mechanisms

- **Detection**: Implement real-time monitoring systems to detect faults as they occur.
- **Mitigation**: Ensure that once a fault is detected, the system can transition to a safe state within the Fault Tolerant Time Interval (FTTI).

### Example: Fault Injection Testing

- **Objective**: Verify the effectiveness of safety mechanisms by simulating faults.
  
- **Procedure**:
  - Introduce voltage anomalies to sensor inputs (e.g., feed the sensor +5.5V for 10 seconds).
  - Test if the monitoring mechanism detects the anomaly (e.g., detecting 6V, 7V, 8V).

## Classification Based on Root Cause

1. **Common Cause Failures**
   - **Definition**: Failures of two or more elements resulting directly from a specific event or root cause.
   - **Example**: A fault in the cooling system leading to multiple systemic failures due to overtemperature.

2. **Cascading Failures**
   - **Definition**: A failure in one element causes a failure in another element.
   - **Example**: Failure of one transistor in a parallel configuration causing excessive load on another, leading to its failure.

3. **Dependent Failures**
   - **Definition**: Failures that are not statistically independent, where the combined probability of failure is not the product of individual probabilities.
   - **Includes**:
     - Common Cause Failures
     - Cascading Failures

## Permanent vs. Transient Faults

1. **Permanent Faults**
   - **Definition**: Faults that occur and remain until they are removed or repaired.
   - **Examples**: "Stuck at," "open," "short," "drift."

2. **Transient Faults**
   - **Definition**: Faults that occur temporarily and disappear without intervention.
   - **Examples**: Bit flips, electromagnetic interference (EMI) issues.

### Handling Transient Faults

- **Implementation**: Develop safety mechanisms that can detect and react to transient faults to prevent safety goal violations.
  
- **Example**: Implement error correction codes (ECC) to detect and correct bit flips in memory.

## Best Practices

### Comprehensive Documentation

- **Thorough Records**:
  - Document all types of faults, their rates, modes, and associated safety mechanisms.
  
- **Traceability**:
  - Maintain traceability between safety goals, requirements, design elements, and verification activities.
  
- **Standardized Formats**:
  - Use consistent documentation formats for clarity and ease of reference.

### Early and Continuous Safety Integration

- **Safety from the Outset**:
  - Integrate safety considerations during the initial design phases to identify and mitigate risks early.
  
- **Ongoing Assessments**:
  - Continuously assess and update safety measures based on new insights and testing feedback.

### Iterative Development and Refinement

- **Design-Analyze-Verify Cycle**:
  - Adopt an iterative approach, refining hardware and software designs based on continuous analysis and verification feedback.
  
- **Responsive to Feedback**:
  - Incorporate feedback from testing and validation activities to enhance system safety and performance.

### Cross-Functional Collaboration

- **Unified Safety Approach**:
  - Encourage collaboration among hardware engineers, software developers, safety analysts, and other stakeholders to ensure a comprehensive safety strategy.
  
- **Joint Reviews**:
  - Conduct joint design and safety reviews to identify and address cross-domain risks effectively.

### Adherence to Standards

- **Strict Compliance**:
  - Follow ISO 26262 guidelines meticulously to ensure that all safety requirements are met.
  
- **Leverage Best Practices**:
  - Incorporate industry best practices in hardware and software design to enhance system reliability and safety.

### Utilize Advanced Tools

- **ALM and Modeling Tools**:
  - Use tools like CodeBeamer ALM, IBM Suite, UML, or SysML to manage requirements, traceability, and system modeling effectively.
  
- **Automated Testing Tools**:
  - Implement automated testing tools to streamline verification processes and ensure comprehensive test coverage.

## Practical Example: Steer-by-Wire System

### System Overview

A steer-by-wire system replaces traditional mechanical steering connections with electronic controls, enhancing precision and enabling advanced driver assistance features.

### Integration Steps

1. **Hardware-Software Integration**:
   - **Compilation and Building**: Compile steering control software and integrate it with the ECU.
   - **Loading Software**: Flash the compiled software onto the ECU memory.
   - **Calibration**: Apply calibrations to fine-tune steering response based on test data.

2. **System Integration**:
   - **Subsystem Assembly**: Combine steering sensors, actuators, and control units.
   - **Interface Connection**: Ensure correct communication between sensors and ECU through defined interfaces.
   - **Functional Testing**: Validate that steering commands result in accurate actuator responses.

3. **Vehicle Integration**:
   - **System Installation**: Install the steer-by-wire system into a test vehicle, connecting it with other vehicle systems.
   - **Operational Testing**: Conduct tests to verify system functionality within the vehicle environment.
   - **Safety Validation**: Ensure that the system maintains safety standards during real-world operation.

### Verification

- **Safety Measures Verification**:
  - **Redundant Steering Sensors**: Perform fault injection tests to ensure that redundant sensors detect and respond to faults.
  - **CRC Checks**: Verify that data integrity checks are functioning correctly by introducing data corruption scenarios.

- **Functional Testing**:
  - **Steering Response**: Test that steering inputs result in precise and reliable actuator movements.
  - **Fault Detection**: Simulate sensor failures and ensure that the system transitions to a safe state within the Fault Tolerant Time Interval (FTTI).

### Validation

- **Simulation**:
  - **Hardware-in-the-Loop (HIL)**: Use HIL simulations to mimic various steering scenarios and validate system responses without physical prototypes.

- **Real-World Testing**:
  - **On-Road Tests**: Conduct driving tests under different conditions to ensure the system performs reliably and safely.

- **Evidence Collection**:
  - **Test Results**: Document results from simulations and real-world tests showing compliance with safety goals.
  - **Validation Report**: Compile a comprehensive report detailing all testing activities, results, and evidence supporting safety compliance.

- **Approval**:
  - **Expert Review**: Engage safety engineers and system designers to review validation results.
  - **Final Approval**: Obtain approval from responsible safety authorities, confirming that the steer-by-wire system meets all safety requirements.

## Conclusion

Understanding faults and failures is fundamental to achieving functional safety in automotive systems as per ISO 26262. By meticulously identifying and categorizing faults, implementing robust safety mechanisms, and adhering to best practices in hardware and software design, automotive engineers can ensure that their systems are both reliable and safe. Comprehensive documentation, traceability, and continuous safety assessments are integral to maintaining high safety standards throughout the system lifecycle.

## Recommended Resources

- **The Risks Digest**: An online forum moderated by Peter Neumann, focused on the security and safety of computers, software, and technological systems. It serves as an invaluable resource for staying informed about the latest discussions and developments in safety-critical systems.
  
- **Electropedia**: The world's online electrotechnical vocabulary, as defined by IEC 60050. It provides comprehensive definitions and explanations of technical terms related to electronics and safety.
  
- **IEC 61508**: A broader functional safety standard applicable to various industries, offering principles that complement ISO 26262.

## Next Steps

In the upcoming sessions, we will delve deeper into the specifics of software development and hardware design, providing detailed methodologies and techniques to ensure that your systems are both functional and safe. Topics will include software architectural design, hardware detail design, and the integration of safety mechanisms to achieve compliance with ISO 26262.