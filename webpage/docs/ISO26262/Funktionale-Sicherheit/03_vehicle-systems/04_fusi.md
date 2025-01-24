# Functional Safety Concept

The Functional Safety Concept is a fundamental component of the ISO 26262 standard, which governs the functional safety of electrical and electronic systems in road vehicles. It serves as a blueprint for defining how safety goals are achieved through specific functional safety requirements. This documentation provides an in-depth exploration of the Functional Safety Concept, encompassing clear explanations, practical examples, and best practices to ensure comprehensive understanding and effective implementation.

## Key Concepts

### Functional Safety Concept

- **Definition**: According to ISO 26262, the Functional Safety Concept is a specification of the functional safety requirements, along with associated information, their allocation to architectural elements, and their interactions necessary to achieve the safety goals.
  
- **Purpose**: It outlines how safety goals will be realized through specific requirements, ensuring that the system behaves safely under both normal and fault conditions.

- **Characteristics**:
  - **Work Product Specificity**: Contains information exclusively related to functional safety.
  - **Distinct from Item Definition**: Unlike the item definition, which provides a broad description of the item or system, the Functional Safety Concept focuses solely on safety-related aspects.

### Safety Goals and ASILs

- **Safety Goals**: High-level objectives that define the desired safety outcomes to prevent or mitigate hazards.
  
- **Automotive Safety Integrity Levels (ASILs)**:
  - **ASIL A**: Lowest level of hazard risk.
  - **ASIL D**: Highest level of hazard risk.
  - **QM (Quality Managed)**: Indicates that the safety goal is managed through quality processes and is not directly relevant to ISO 26262.

### Safe State

- **Definition**: An operating mode in which, in the event of a failure, the system remains safe without exposing individuals to unreasonable risk.
  
- **Characteristics**:
  - **Fault Tolerance**: The system can switch to a safe state to reduce or eliminate the effects of a fault.
  - **Timing Restrictions**: Transition to a safe state must occur within a predefined timeframe, known as the Fault Tolerant Time Interval (FTTI).

### Timing Intervals

- **Fault Tolerant Time Interval (FTTI)**:
  - **Definition**: The minimum time from the occurrence of a fault to the potential occurrence of a hazardous event if safety mechanisms are not activated.
  - **Typical Duration**: Measured in hundreds of milliseconds or seconds.
  
- **Additional Timing Intervals**:
  - **Fault Detection Time Interval (FDTI)**: Time required to detect a fault.
  - **Fault Reaction Time Interval (FRTI)**: Time available to react to a detected fault.
  - **Emergency Operation Time Interval (EOTI)**: Time allocated for the system to perform emergency operations after a fault is detected.

## Developing the Functional Safety Concept

### Deriving Functional and Nonfunctional Requirements

- **Process Overview**:
  1. **Output of HARA**: Utilize the results from Hazard Analysis and Risk Assessment (HARA) as the foundation.
  2. **Safety Analyses**: Conduct various safety analyses to bridge the gap between HARA outputs and the Functional Safety Concept.
  3. **Requirement Specification**: Define both functional and nonfunctional requirements that detail how the system will meet the safety goals.

- **Best Practices**:
  - **Clarity and Precision**: Requirements should be unambiguous and clearly state the intended safety behavior.
  - **Traceability**: Ensure that each requirement can be traced back to specific safety goals derived from HARA.
  - **Avoid Technological Solutions**: Focus on what needs to be achieved rather than how it will be implemented technologically.

- **Practical Example**:
  - **Safety Goal**: Prevent unintended locking of the steering wheel during driving.
  - **Functional Requirement**: The system shall disable the steering wheel lock mechanism when the vehicle is in motion.
  - **Nonfunctional Requirement**: The disabling action shall occur within 100 milliseconds of detecting vehicle movement.

### ASIL Decomposition

- **Definition**: ASIL decomposition involves dividing a high ASIL safety requirement into multiple redundant safety requirements allocated to independent elements, with the aim of reducing the overall ASIL of each individual requirement.

- **Objective**: To enhance safety by distributing safety functions across multiple components, thereby increasing system reliability and potentially lowering the ASIL of individual components.

- **Process**:
  1. **Identify Redundancies**: Determine which safety requirements can be duplicated across different elements.
  2. **Allocate Independently**: Assign these redundant requirements to separate, independent components to ensure that a single fault does not compromise all redundancies.
  3. **Assess ASIL Reduction**: Evaluate the impact of decomposition on the ASIL of each safety requirement.

- **Best Practices**:
  - **Ensure Independence**: Redundant elements must operate independently to prevent a single point of failure.
  - **Consistent Functionality**: Each decomposed part should be capable of fulfilling the original safety requirement independently.
  - **Adhere to Decomposition Schemas**: Follow the decomposition guidelines outlined in ISO 26262, Part 9, Clause 5.

- **Practical Example**:
  - **Initial Safety Requirement**: A sensor must detect driver movement with ASIL D.
  - **Decomposed Requirements**:
    - **Sensor A**: Detects driver movement with ASIL B.
    - **Sensor B**: Detects driver movement with ASIL B.
  - **Outcome**: The redundant sensors provide a combined safety integrity that satisfies the original ASIL D requirement.

### SEooCs and Functional Safety Concept

- **Safety Element Out of Context (SEooC)**:
  - **Definition**: A generic safety-related component not developed for a specific item, relying on assumptions that are validated upon integration.
  
- **Functional Safety Concept for SEooCs**:
  - **Item Definition**: Define the SEooC, including its intended safety functions and assumptions.
  - **HARA and Risk Assessment**: Perform hazard analysis and risk assessment considering the assumptions.
  - **Safety Requirements**: Specify functional and nonfunctional requirements tailored to the SEooC's intended use.
  
- **Best Practices**:
  - **Assumption Management**: Clearly document and validate all assumptions when integrating SEooCs into specific items.
  - **Integration Validation**: Ensure that the SEooC meets the safety requirements within the context of the target system.

## Writing Functional and Nonfunctional Requirements

- **Functional Requirements**:
  - **Definition**: Describe the specific behaviors or functions the system must perform to achieve safety goals.
  - **Example**: "The braking system shall activate automatic braking within 50 milliseconds upon detecting an obstacle."

- **Nonfunctional Requirements**:
  - **Definition**: Specify criteria that can be used to judge the operation of a system, rather than specific behaviors.
  - **Example**: "The automatic braking system shall achieve activation within 50 milliseconds under all operating conditions."

- **Best Practices**:
  - **Specificity**: Clearly define the scope and limits of each requirement.
  - **Measurability**: Ensure that requirements can be tested and verified.
  - **Avoid Ambiguity**: Use precise language to prevent misinterpretation.

## ASIL Composition

- **Definition**: ASIL composition refers to the process of determining the overall ASIL of a system by considering the combined ASILs of its individual components.
  
- **Perspective**: Always approached from the function's viewpoint, not based on hardware metrics or source code.

- **Best Practices**:
  - **Function-Centric Analysis**: Focus on how functions interact rather than the specific implementation details.
  - **Maintain Capability**: Ensure that decomposed or composed parts can independently fulfill the required safety functions.

## Verification and Validation of the Functional Safety Concept

- **Verification**:
  - **Objective**: Ensure that the Functional Safety Concept correctly implements the safety goals and requirements.
  - **Methods**:
    - **Checklist Reviews**: Use comprehensive checklists to verify that all safety aspects are covered.
    - **Consistency Checks**: Ensure alignment between safety goals, requirements, and architectural allocations.

- **Validation**:
  - **Objective**: Confirm that the Functional Safety Concept effectively achieves the intended safety goals in real-world scenarios.
  - **Methods**:
    - **Functional Safety Assessment**: Conduct assessments involving relevant stakeholders to validate the concept.
    - **Simulation and Testing**: Utilize simulations and real-world testing to validate safety mechanisms and timing intervals.

- **Best Practices**:
  - **Regular Reviews**: Schedule periodic reviews to assess the Functional Safety Concept's effectiveness and relevance.
  - **Stakeholder Involvement**: Engage cross-functional teams in the verification and validation processes to ensure comprehensive coverage.
  - **Documentation**: Maintain detailed records of all verification and validation activities for audit and compliance purposes.

## Practical Examples and Best Practices

### Example: Steer-by-Wire System

1. **Safety Goals**:
   - Prevent unintended steering maneuvers.
   - Ensure reliable steering feedback to the driver.

2. **Functional Safety Requirements**:
   - The system shall detect steering input within 10 milliseconds.
   - The system shall maintain steering control integrity under all operating conditions.

3. **Safe State**:
   - **Definition**: Upon detecting a fault, the system shall enter a mode where manual steering control is enabled.
   - **FTTI**: The transition to manual mode shall occur within 50 milliseconds of fault detection.

4. **ASIL Decomposition**:
   - **Initial ASIL**: ASIL D for preventing unintended steering maneuvers.
   - **Decomposed Requirements**:
     - **Redundant Sensor A**: Detects steering input with ASIL B.
     - **Redundant Sensor B**: Detects steering input with ASIL B.
   - **Outcome**: Combined, the redundant sensors satisfy the original ASIL D requirement.

5. **Verification and Validation**:
   - **Checklist Review**: Verify that all safety goals are addressed by functional requirements.
   - **Functional Safety Assessment**: Engage safety engineers and system designers to validate the steer-by-wire safety mechanisms.
   - **Testing**: Perform simulations to ensure that the system transitions to a safe state within the FTTI during fault conditions.

## Best Practices

- **Comprehensive Documentation**: Maintain thorough records of all aspects of the Functional Safety Concept, including safety goals, requirements, and architectural allocations.
  
- **Early Integration of Safety**: Incorporate functional safety considerations early in the design process to identify and mitigate risks effectively.
  
- **Iterative Review and Refinement**: Regularly review and update the Functional Safety Concept to reflect changes in system design, operational conditions, or new safety information.
  
- **Cross-Functional Collaboration**: Engage stakeholders from various disciplines, including system engineering, software development, and safety engineering, to ensure a holistic approach to functional safety.

- **Utilize Standards and Guidelines**: Adhere to ISO 26262 guidelines and leverage industry best practices to guide the development and implementation of the Functional Safety Concept.

## Conclusion

The Functional Safety Concept is a critical element of ISO 26262, providing a structured approach to defining and achieving safety goals within automotive systems. By meticulously specifying functional safety requirements, allocating them within the system architecture, and ensuring their effective interaction, organizations can significantly enhance the safety and reliability of their products. Adhering to best practices, leveraging practical examples, and conducting rigorous verification and validation are essential for the successful implementation of the Functional Safety Concept.

For further guidance, refer to ISO 26262 documentation and consider consulting the E-GAS concept for applied examples in systems such as gasoline injection.