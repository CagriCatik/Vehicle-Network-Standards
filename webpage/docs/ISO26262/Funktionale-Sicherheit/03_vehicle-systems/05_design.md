# Design Safer Systems

Advancements in automotive technology have significantly enhanced vehicle safety over the past few decades. Modern cars incorporate sophisticated electronic and electrical systems designed to protect occupants and minimize injury during crashes. This documentation explores the principles of designing safer systems in accordance with ISO 26262, emphasizing functional safety at the system level. Through detailed explanations, practical examples, and best practices, this guide aims to provide a comprehensive understanding of creating safer automotive systems.

## Evolution of Vehicle Safety

### Comparing Older and Newer Vehicles

- **Case Study: Ford Fiesta Crash Comparison**
  - **1998 Ford Fiesta**:
    - **Crash Outcome**: Body shell collapsed, occupant area caved in.
    - **Risk**: Extremely high risk of fatal and serious injury.
  - **Latest Ford Fiesta**:
    - **Crash Outcome**: Intact body shell, fully deployed airbags, minimal damage (cracked windscreen).
    - **Risk**: Entirely survivable crash with significantly reduced injury risk.

- **Conclusion**: Modern cars are generally safer than older models due to improved crash protection, advanced safety features, and better structural integrity.

## Functional Safety at the System Level

### Definition of Functional Safety

According to ISO 26262, **functional safety** is the absence of unreasonable risk due to hazards caused by malfunctioning behavior of electrical and electronic systems in vehicles. It focuses on ensuring that systems operate safely even in the presence of faults and failures.

### Types of Faults

1. **Systematic Faults**
   - **Definition**: Faults related to design, manufacturing, operational procedures, or documentation.
   - **Characteristics**:
     - Deterministic relationship with a specific cause.
     - Eliminated through changes in design or processes.
   - **Examples**:
     - Software bugs.
     - Design flaws in electronic circuits.
   
2. **Random Faults**
   - **Definition**: Unpredictable failures that follow a probability distribution.
   - **Characteristics**:
     - Occur without a specific cause.
     - Limited to hardware elements.
   - **Examples**:
     - Component wear-out.
     - Electrical shorts due to aging.

## Technical Safety Concept

### Overview

The **Technical Safety Concept** is a key work product in ISO 26262 Part 4, outlining the safety measures implemented to mitigate unreasonable risks associated with system failures. It bridges the gap between hazard analysis and the implementation of safety mechanisms.

### Development Phases

1. **Request for Quotation (RFQ) Phase**
   - **Objective**: Initiate the development of the Technical Safety Concept.
   - **Activities**:
     - Basic safety concept creation.
     - Preliminary safety analysis.
   - **Output**: Basic Technical Safety Concept.

2. **Successive Refinement**
   - **Objective**: Enhance the Technical Safety Concept through iterative analysis and design.
   - **Activities**:
     - Detailed safety analyses.
     - Integration of safety measures.
   - **Output**: Mature Technical Safety Concept.

3. **Integration into Software and Hardware Safety Concepts**
   - **Objective**: Develop detailed safety requirements for software and hardware components.
   - **Activities**:
     - Allocation of safety measures to specific elements.
     - Specification of safety mechanisms.
   - **Output**: Software and Hardware Safety Concepts.

### Components of the Technical Safety Concept

- **Safety Measures**:
  - **Definition**: Activities or technical solutions to avoid or control systematic failures, detect or control random hardware failures, or mitigate their harmful effects.
  - **Categories**:
    - **Technical Safety Measures**: Hardware and software solutions (e.g., CRC checks, timeout monitoring).
    - **Process Safety Measures**: Procedural activities (e.g., design reviews, testing protocols).

- **Safety Mechanisms**:
  - **Definition**: Technical solutions implemented by electronic functions or elements to detect and mitigate faults.
  - **Examples**:
    - **CRC (Cyclic Redundancy Check)**: Ensures data integrity.
    - **Timeout Monitoring**: Detects delays in system responses.
    - **Redundant Checks**: Multiple software or hardware components verifying the same function.

### Documentation and Tools

- **Modeling Techniques**:
  - **UML (Unified Modeling Language)**: Used for static and dynamic system descriptions.
    - **Structural Diagrams**: Class diagrams for static elements.
    - **Behavioral Diagrams**: State diagrams, use case diagrams, sequence diagrams for dynamic aspects.
  - **SysML (Systems Modeling Language)**: Alternative to UML for system-level modeling.

- **Specialized Tools**:
  - **CodeBeamer ALM**: Application Lifecycle Management tool for managing safety concepts.
  - **IBM Suite**: Integrated tools for developing and managing safety concepts.

### Best Practices

- **Early Integration of Safety**: Incorporate safety considerations from the initial design phases to identify and mitigate risks effectively.
- **Comprehensive Documentation**: Maintain thorough records of safety goals, requirements, and architectural allocations.
- **Iterative Development**: Adopt an iterative approach to refine safety concepts through continuous analysis and verification.
- **Cross-Functional Collaboration**: Engage stakeholders from various disciplines to ensure a holistic approach to functional safety.

## Hardware Software Interface (HSI) Specification

### Definition and Purpose

The **Hardware Software Interface (HSI)** specifies the interactions between hardware components and software controls. It ensures that both hardware and software elements work together seamlessly to achieve safety goals.

### Key Elements of HSI Specification

- **Components Controlled by Software**: Identifies hardware parts managed by software functions.
- **Hardware Resources Supporting Software Execution**: Details the hardware resources required for software operations.
- **Characteristics of Hardware Elements**: Describes physical and functional properties of hardware components.
- **Interfaces**: Defines communication protocols and data exchange mechanisms between hardware and software.
- **Operational Conditions**: Specifies the conditions under which the hardware and software operate safely.

### Integration with Technical Safety Concept

- **Combined Work Products**: In some cases, HSI specifications are integrated into the Technical Safety Concept to streamline verification and validation processes.
- **Verification Concept**: Derive a common verification approach for both HSI and Technical Safety Concept to ensure consistency and completeness.

## Safety Analysis and Mechanism Allocation

### Safety Analysis

Safety analysis identifies potential hazards and determines the necessary safety measures to mitigate them. It is a critical step in developing the Technical Safety Concept.

### Allocation of Safety Measures and Mechanisms

1. **Identify Safety Measures**: Determine activities and technical solutions needed to address identified hazards.
2. **Allocate Safety Measures**:
   - **To Safety Mechanisms**: Assign specific technical solutions to hardware and software elements.
   - **To Processes**: Assign procedural activities to ensure systematic control of risks.
3. **Define Performance Requirements**: Specify the performance criteria for each safety mechanism to ensure effective fault detection and mitigation.

### Practical Example: Steering System Safety

1. **Safety Goal**: Prevent unintended steering maneuvers.
2. **Safety Measures**:
   - **Technical**: Implement redundant steering sensors.
   - **Process**: Conduct regular steering system diagnostics.
3. **Safety Mechanisms**:
   - **CRC Checks**: Verify sensor data integrity.
   - **Redundant Sensors**: Provide backup data in case of sensor failure.
4. **HSI Specification**: Define communication protocols between steering sensors and control units to ensure timely detection and response to faults.

## ASIL Decomposition

### Definition

**ASIL Decomposition** is the process of breaking down high Automotive Safety Integrity Levels (ASILs) into lower ASILs through the allocation of redundant safety requirements to independent elements.

### Objective

- **Reduce Overall ASIL**: By distributing safety functions across multiple components, the overall ASIL can be lowered, reducing the complexity and cost of safety measures.
- **Enhance Reliability**: Independent redundancies ensure that a single failure does not compromise the entire safety function.

### Process of ASIL Decomposition

1. **Identify High ASIL Requirements**: Determine which safety goals have high ASIL ratings (e.g., ASIL D).
2. **Introduce Redundancies**: Allocate redundant safety requirements to separate, independent elements.
3. **Assign Lower ASILs**: Each redundant element is assigned a lower ASIL (e.g., ASIL B) based on the decomposition schema.
4. **Verify Combined ASIL**: Ensure that the combined lower ASILs meet the original high ASIL requirement through redundancy.

### Best Practices

- **Ensure Independence**: Redundant elements must operate independently to prevent a single fault from affecting all redundancies.
- **Consistent Functionality**: Each decomposed element should independently fulfill the safety function.
- **Adhere to Decomposition Schemas**: Follow ISO 26262 Part 9, Clause 5 guidelines for effective decomposition.

### Practical Example: Driver Movement Detection

1. **Initial ASIL**: ASIL D for detecting driver movement.
2. **Decomposed Requirements**:
   - **Sensor A**: Detects driver movement with ASIL B.
   - **Sensor B**: Detects driver movement with ASIL B.
3. **Outcome**: The redundant sensors provide combined safety integrity, satisfying the original ASIL D requirement.

## Verification, Validation, and Integration at System Level

### Verification and Validation (V&V)

- **Objective**: Ensure that the Technical Safety Concept meets all safety requirements and effectively mitigates identified risks.
- **Methods**:
  - **Checklist Reviews**: Use comprehensive checklists to verify coverage of safety aspects.
  - **Consistency Checks**: Ensure alignment between safety goals, requirements, and safety measures.
  - **Functional Safety Assessment**: Engage stakeholders to validate the safety mechanisms and concepts.
  - **Simulation and Testing**: Conduct simulations and real-world testing to validate system behavior under fault conditions.

### Integration Process

1. **Design Phase**: Develop hardware and software components based on the Technical Safety Concept.
2. **Analysis Phase**: Perform detailed safety analyses to identify potential hazards and mitigation strategies.
3. **Verification Phase**: Verify that all safety requirements are met through testing and analysis.
4. **Implementation Phase**: Integrate safety mechanisms into hardware and software components.
5. **Iterative Refinement**: Continuously refine and validate the safety concepts through iterative cycles of design, analysis, and verification.

### Best Practices

- **Regular Reviews**: Schedule periodic reviews to assess the effectiveness of safety measures and mechanisms.
- **Stakeholder Involvement**: Engage cross-functional teams in the V&V process to ensure comprehensive coverage.
- **Documentation**: Maintain detailed records of all V&V activities for audit and compliance purposes.
- **Use of Specialized Tools**: Leverage tools like CodeBeamer ALM or IBM Suite to manage and trace safety requirements and their verification.

## Practical Example: Steer-by-Wire System

1. **Safety Goals**:
   - Prevent unintended steering maneuvers.
   - Ensure reliable steering feedback to the driver.

2. **Functional Safety Requirements**:
   - **Functional Requirement**: The system shall detect steering input within 10 milliseconds.
   - **Nonfunctional Requirement**: The system shall maintain steering control integrity under all operating conditions.

3. **Safe State**:
   - **Definition**: Upon detecting a fault, the system shall switch to manual steering control.
   - **FTTI**: Transition to manual mode within 50 milliseconds of fault detection.

4. **ASIL Decomposition**:
   - **Initial ASIL**: ASIL D for preventing unintended steering maneuvers.
   - **Decomposed Requirements**:
     - **Redundant Sensor A**: Detects steering input with ASIL B.
     - **Redundant Sensor B**: Detects steering input with ASIL B.
   - **Outcome**: Combined, the redundant sensors satisfy the original ASIL D requirement.

5. **Verification and Validation**:
   - **Checklist Review**: Confirm all safety goals are addressed by functional requirements.
   - **Functional Safety Assessment**: Validate steer-by-wire safety mechanisms with safety engineers and system designers.
   - **Testing**: Conduct simulations to ensure system transitions to a safe state within the FTTI during fault conditions.

## Best Practices for Designing Safer Systems

- **Comprehensive Documentation**: Ensure all safety goals, requirements, and safety measures are thoroughly documented and traceable.
- **Early and Continuous Safety Integration**: Incorporate safety considerations from the earliest design phases and maintain ongoing safety assessments throughout the development lifecycle.
- **Iterative Development and Refinement**: Adopt an iterative approach to continuously improve safety concepts based on testing and analysis feedback.
- **Cross-Functional Collaboration**: Foster collaboration among system engineers, software developers, safety analysts, and other stakeholders to ensure a unified approach to functional safety.
- **Adherence to Standards**: Strictly follow ISO 26262 guidelines and leverage industry best practices to guide the development and implementation of safety concepts.
- **Utilize Advanced Tools**: Implement specialized tools for managing safety requirements, performing safety analyses, and documenting safety concepts to enhance accuracy and efficiency.

## Conclusion

Designing safer systems in the automotive industry is a multifaceted process that requires a thorough understanding of functional safety principles as outlined in ISO 26262. By systematically identifying hazards, implementing robust safety measures and mechanisms, and adhering to best practices in verification and validation, organizations can significantly enhance the safety and reliability of their vehicles. Embracing an iterative and collaborative development approach, supported by comprehensive documentation and advanced tools, ensures that safety remains a paramount consideration throughout the system lifecycle.

For further guidance, refer to ISO 26262 documentation and explore practical applications through resources like the E-GAS concept, which demonstrates the implementation of safety standards in real-world systems such as gasoline injection.