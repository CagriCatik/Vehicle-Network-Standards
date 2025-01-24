# Specify and design hardware and software

In the automotive industry, the integration of hardware and software is pivotal to ensuring functional safety. ISO 26262, the international standard for functional safety of electrical and electronic systems in road vehicles, provides a comprehensive framework for developing safe and reliable automotive systems. This documentation delves into the specification and design of hardware and software components, emphasizing their role in achieving functional safety. Through clear explanations, practical examples, and best practices, this guide aims to equip automotive engineers with the knowledge required to design systems that comply with ISO 26262.

## Importance of Hardware and Software Development for Functional Safety

Functional safety refers to the absence of unreasonable risk due to hazards caused by malfunctioning behavior of electrical and electronic systems. Effective hardware and software development are crucial in mitigating these risks by implementing safety measures and mechanisms that ensure systems behave safely under both normal and fault conditions.

## Hardware Safety Requirements

### Derivation of Hardware Safety Requirements

Hardware safety requirements are derived from higher-level requirements and are informed by the technical safety concept and hardware safety analysis. These requirements specify how safety mechanisms are implemented at the hardware level to prevent, detect, and mitigate faults that could compromise safety goals.

### ISO 26262 Part 5 and 6 Clause 5

Clause 5 of ISO 26262 Parts 5 (Product Development at the Hardware Level) and 6 (Product Development at the Software Level) addresses general topics related to both hardware and software development. The primary goal of this clause is to establish a consistent framework for hardware and software development across the entire system, ensuring that all components adhere to the same safety standards and processes.

#### Key Objectives of Clause 5

1. **Consistent Development Framework**:
   - Establish uniform tools, processes, and methods for developing hardware and software.
   - Ensure consistency across different teams and departments within an organization.

2. **Information Flow from Higher Levels**:
   - Ensure that information from the technical safety concept and functional safety concept is effectively communicated and integrated into both hardware and software domains.

3. **Quality Evaluation**:
   - Implement methods to consistently evaluate the quality of processes and methods used in hardware and software development.
   - Ensure that all development activities meet predefined quality standards.

#### Organizational Considerations

Large organizations often compartmentalize development teams into divisions, departments, centers of competence, platform teams, project teams, and subteams. It is essential to distinguish between entities that follow the same set of rules and processes versus those that operate independently. If multiple entities are involved in developing a system, a **Development Interface Agreement (DIA)** should be established to ensure consistency in processes and adherence to safety standards.

#### Outputs of Clause 5

- **Updated Processes**: Refinement of development processes to align with safety requirements.
- **Quality Management**: Enhanced quality assurance measures to maintain high safety standards.
- **Team Management**: Improved coordination and collaboration among development teams.
- **Safety Plan Updates**: Revision of safety plans to incorporate new safety measures and mechanisms.

## Writing Safety Requirements for Hardware and Software

### Hardware Safety Requirements Specification

Hardware safety requirements describe how safety mechanisms are implemented at the hardware level. These requirements should cover aspects such as fault detection, fault tolerance, and mitigation strategies to ensure that hardware components do not compromise safety goals.

#### Key Components of Hardware Safety Requirements

- **Fault Coverage**:
  - Describe how hardware elements address transient and external faults.
  - Specify the tolerance of safety mechanisms to different types of faults.

- **Fault Detection Mechanisms**:
  - Detail how internal and external faults are detected by hardware components.
  - Include specifications for diagnostic features and monitoring systems.

- **Safety Mechanisms**:
  - Outline the technical solutions implemented to mitigate detected faults.
  - Examples include Cyclic Redundancy Checks (CRC), watchdog timers, and redundant sensors.

#### Practical Example: Steering Wheel Position Sensor

Consider a sensor that measures the steering wheel's position in a steer-by-wire system:

- **Characteristics**:
  - Outputs an analog signal translated into digital form using a conversion formula.
  - Detects minimum angle changes of 0.1 degrees with an accuracy of 0.01 degrees.
  - Initialization period: Output unusable for 10 milliseconds after startup.
  - Hardware reset time: 5 milliseconds.

- **Safety Goal**: Prevent unintended steering maneuvers with ASIL D assigned, which can be decomposed into torque and angle sensor components.

#### Example Hardware Safety Requirements

1. **Fault Detection**:
   - Detect failure mode "stuck at" for element X within 150 milliseconds.
   
2. **Data Integrity**:
   - Implement CRC for memory area K to detect memory faults.
   
3. **Power Supply Monitoring**:
   - Establish a readback channel for power supply channels X and Y to monitor voltage levels.
   
4. **Watchdog Timer Configuration**:
   - Configure the watchdog timer with a separate time base and defined time window to detect unresponsive hardware.

### Software Safety Requirements Specification

Software safety requirements specify how safety mechanisms are implemented within software components to ensure reliable and safe operation.

#### Key Components of Software Safety Requirements

- **Software Modules and Functions**:
  - Define critical software modules and their functions that contribute to safety mechanisms.
  
- **Software Interfaces**:
  - Detail the interfaces between software components and hardware elements.
  
- **Thread and Process Management**:
  - Specify how threads and processes are managed to prevent deadlocks and ensure real-time performance.
  
- **Error Handling and Recovery**:
  - Describe mechanisms for detecting and recovering from software errors and faults.

#### Practical Example: Adaptive Cruise Control (ACC) Software

- **Functions**:
  - Maintain safe following distance.
  - Adjust speed based on traffic conditions.

- **Safety Measures**:
  - Redundant algorithms to verify speed and distance calculations.
  - Timeout monitoring to detect unresponsive components.

- **Design Strategy**:
  - Implement dual algorithms to cross-verify critical measurements.
  - Use watchdog timers to reset the ACC system if delays or failures are detected.

## Hardware-Software Interface (HSI) Specification

### Definition and Purpose

The Hardware-Software Interface (HSI) specifies the interactions between hardware components and software controls, ensuring seamless communication and functionality between the two domains.

### Key Elements of HSI Specification

- **Controlled Components**:
  - Identify hardware parts managed by software functions.
  
- **Hardware Resources**:
  - Detail the hardware resources required for software operations.
  
- **Interface Definitions**:
  - Define communication protocols and data exchange mechanisms between hardware and software.
  
- **Operational Conditions**:
  - Specify the conditions under which hardware and software interact safely.

### Integration with Technical Safety Concept

- **Combined Work Products**:
  - In some cases, integrate HSI specifications into the Technical Safety Concept to streamline verification and validation processes.
  
- **Verification Concept**:
  - Develop a unified verification approach for both HSI and Technical Safety Concept to ensure consistency and completeness.

## Design of Hardware and Software

### Hardware Design

#### Architectural Design

- **Definition**: Represents all hardware components and their interactions through block diagrams.
  
- **Purpose**: Establishes traceability between safety requirements and hardware design elements.
  
- **Best Practices**:
  - **Modular Design**: Simplifies integration and fault isolation.
  - **Redundancy Implementation**: Enhances reliability through redundant components.

#### Detail Design

- **Definition**: Involves detailed schematics, PCB layouts, and interactions between specific hardware parts like transistors and resistors.
  
- **Purpose**: Provides granular information on the implementation of hardware components.
  
- **Best Practices**:
  - **Traceability**: Link detailed design elements to safety requirements.
  - **Comprehensive Testing**: Conduct stress, environmental, and lifecycle testing to ensure reliability.

### Software Design

#### Architectural Design

- **Definition**: Outlines software components, their functions, and interactions using models such as UML or SysML.
  
- **Purpose**: Ensures robust and reliable software architecture that supports safety mechanisms.
  
- **Best Practices**:
  - **Hierarchical Structure**: Facilitates organized and scalable software design.
  - **Bidirectional Traceability**: Maintains linkage between software components and safety requirements.
  - **Timing Behavior**: Incorporate real-time performance requirements to meet safety goals.

#### Detail Design

- **Definition**: Focuses on the implementation details of software components, including code structure, algorithms, and interfaces.
  
- **Purpose**: Translates architectural design into executable software code.
  
- **Best Practices**:
  - **Adherence to Coding Standards**: Follow standards like MISRA to ensure code reliability.
  - **Automated Testing**: Implement unit tests and continuous integration pipelines to detect defects early.
  - **Comprehensive Documentation**: Use comments and traceability tags to link code with safety requirements.

## Traceability and Safety Analysis

### Importance of Traceability

Traceability ensures that all safety requirements are systematically addressed throughout the hardware and software development processes. It facilitates compliance verification, simplifies audits, and ensures comprehensive coverage of safety goals.

### Methods to Ensure Traceability

- **Traceability Matrices**:
  - Link safety goals to specific requirements, design elements, and test cases.
  
- **Application Lifecycle Management (ALM) Tools**:
  - Utilize tools like CodeBeamer ALM or IBM Suite to manage and automate traceability.
  
- **Regular Reviews**:
  - Conduct periodic traceability reviews to identify and rectify gaps or inconsistencies.

### Specialized Safety Analysis for Hardware and Software

- **Hardware-Specific Analysis**:
  - Focus on physical failures, environmental impacts, and component reliability.
  - Example: Thermal analysis to ensure components operate within safe temperature ranges.
  
- **Software-Specific Analysis**:
  - Concentrate on logical errors, algorithm reliability, and software robustness.
  - Example: Failure Mode and Effects Analysis (FMEA) for software modules to identify potential faults and their impacts.

## Best Practices

### Comprehensive Documentation

- **Thorough Records**:
  - Document all safety goals, requirements, design elements, safety measures, and verification activities.
  
- **Standardized Formats**:
  - Use consistent documentation formats to enhance clarity and facilitate easy reference.
  
- **Accessible Records**:
  - Ensure documentation is easily accessible to all relevant stakeholders for reference and auditing purposes.

### Early and Continuous Safety Integration

- **Incorporate Safety from the Outset**:
  - Integrate safety considerations during the initial design phases to identify and mitigate risks early.
  
- **Ongoing Safety Assessments**:
  - Continuously assess and update safety measures throughout the development lifecycle based on new insights and test results.

### Iterative Development and Refinement

- **Cycle of Design, Analysis, and Verification**:
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

Specifying and designing hardware and software in accordance with ISO 26262 is a meticulous process that demands a deep understanding of functional safety principles, rigorous adherence to standards, and the implementation of robust safety measures. By following best practices, leveraging advanced tools, and fostering cross-functional collaboration, automotive engineers can develop hardware and software components that not only fulfill functional requirements but also uphold the highest safety standards. Comprehensive documentation, traceability, and continuous safety assessments are integral to ensuring that modern vehicles are safe, reliable, and compliant with all regulatory requirements.

## Recommended Resource

To further enhance your understanding of the interplay between electronics, software, and safety, consider exploring **The Risks Digest**. This online forum, moderated by the esteemed Peter Neumann, focuses on the security and safety of computers, software, and technological systems, providing valuable insights and discussions relevant to functional safety in automotive systems.

## Next Steps

In our subsequent sessions, we will delve into the specifics of software development and hardware design, providing detailed methodologies and techniques to ensure that your systems are both functional and safe. Stay tuned for an in-depth exploration of software architectural design, hardware detail design, and the integration of safety mechanisms to achieve compliance with ISO 26262.