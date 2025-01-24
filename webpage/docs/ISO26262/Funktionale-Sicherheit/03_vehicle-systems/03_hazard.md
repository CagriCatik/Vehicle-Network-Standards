# Hazard Analysis and Risk Assessment

Hazard Analysis and Risk Assessment (HARA) is a pivotal activity within the ISO 26262 standard, serving as the cornerstone for ensuring functional safety in automotive systems. HARA systematically identifies potential hazards, evaluates associated risks, and establishes safety goals to mitigate or eliminate unreasonable risks. This documentation provides a comprehensive guide to understanding and implementing HARA, complete with clear explanations, practical examples, and best practices.

## Key Concepts

Before delving into HARA, it is essential to understand several foundational concepts as defined by ISO 26262:

- **Harm**: Physical injury or damage to the health of persons.
- **Hazard**: A potential source of harm resulting from the malfunctioning behavior of an item or system.
- **Hazardous Event**: A combination of a hazard and an operational situation.
- **Operational Situation**: A scenario that can occur during a vehicle's lifecycle.

*Note*: These definitions are specific to ISO 26262 and may vary under different standards.

## Overview of Hazard Analysis and Risk Assessment (HARA)

HARA is a structured method to identify and categorize hazardous events, subsequently specifying safety goals and Automotive Safety Integrity Levels (ASILs) to prevent or mitigate associated hazards. The primary objective is to avoid unreasonable risks by implementing appropriate safety measures.

### Components of HARA

1. **Hazard Analysis**: Identifies potential hazards by examining the relationships between system malfunctions and operational scenarios.
2. **Risk Assessment**: Evaluates the severity, exposure, and controllability of each hazardous event to determine its ASIL.

### Inputs to HARA

- **Item Definition**: Detailed description of the item or system under analysis.
- **Vehicle Information**: Data about the vehicle's characteristics and operational parameters.
- **Standards**: Relevant guidelines and requirements, primarily ISO 26262.
- **Previous HARA Studies**: Historical data and findings from earlier risk assessments.

### Outputs of HARA

- **Safety Goals**: High-level requirements to ensure the safety of the system.
- **ASIL Assignments**: Classification of hazards based on their risk levels.
- **Timing Restrictions**: Deadlines for achieving safety goals.

## Conducting Hazard Analysis and Risk Assessment

Implementing HARA involves a systematic approach divided into several steps. Adhering to best practices ensures thoroughness and compliance with ISO 26262.

### Methodology and Best Practices

- **Familiarize with E-GAS Concept**: The E-GAS concept provides practical steps and examples for applying ISO 26262 to systems like gasoline injection. It is a valuable resource for understanding the application of HARA.
- **Collaborative Approach**: Engage cross-functional teams with expertise in system design, safety engineering, and risk management.
- **Documentation**: Maintain detailed records of all findings, decisions, and rationale to facilitate reviews and audits.

## HARA for Items and Safety Elements Out of Context (SEooC)

### Understanding SEooC

A Safety Element Out of Context (SEooC) refers to a generic safety-related component not developed for a specific item. SEooCs rely on assumptions and are later integrated into various items with tailored safety requirements.

**Examples of SEooC**:
- A generic wiper system designed to be integrated into different OEM vehicles.
- Software components that perform specific safety functions across multiple systems.

### Conducting HARA for Items and SEooCs

1. **Gather Information**:
   - For items: Collect detailed item definitions, vehicle specifications, previous accident data, and relevant studies.
   - For SEooCs: Assemble assumptions, generic safety requirements, and potential integration scenarios.

2. **Analyze Data**:
   - Utilize the collected information to identify potential hazards and assess risks specific to the item or SEooC.

## Steps in Hazard Analysis

Effective hazard analysis involves identifying system functions, potential malfunctions, and operational scenarios, then combining these elements to uncover hazardous events.

### Defining Functions

- **Identify System Functions**: Determine what the system is intended to do, focusing on functional behavior rather than implementation details.
  
  **Examples**:
  - Warn the driver in case of failures.
  - Electrically adjust the steering wheel.
  - Sense the position of the steering wheel.
  - Perform onboard diagnostics.
  - Adapt steering wheel parameters based on selected driving modes.

- **Function Description**: Keep descriptions concise, typically a single sentence, suitable for inclusion in HARA tools.

### Developing a List of Malfunctions

- **Function-Specific Malfunctions**: Enumerate potential failures related to each function.
  
  **Examples**:
  - Loss of stability.
  - Loss of torque.
  - Excessive torque.
  - Insufficient torque.
  - Unintended changes in system behavior.

- **Parameter Considerations**: Malfunctions may involve temporal aspects, forces, accelerations, or other relevant parameters.

### Defining Operational Situations

- **Scenario Identification**: Outline various scenarios in which the system operates during the vehicle's lifecycle.
  
  **Examples**:
  - Parking in an underground garage.
  - Driving on a highway at speeds up to 120 km/h without road separation.
  - Navigating intersections with bicycle lanes.

- **Combining Factors**: Merge different road types, weather conditions, speeds, vehicle conditions, and other factors to create comprehensive operational scenarios.

### Combining Functions, Malfunctions, and Operational Situations

- **Identify Hazardous Events**: Each hazardous event results from the combination of a specific malfunction occurring within a particular operational situation.
  
  **Example**:
  - **Function**: Electrically adjust the steering wheel.
  - **Malfunction**: Loss of torque.
  - **Operational Situation**: Driving on a highway at high speed.
  - **Hazardous Event**: Steering wheel fails to adjust torque, leading to loss of vehicle control.

- **Assess Effects**: Determine the impact of each hazardous event on the vehicle and its occupants.

## Steps in Risk Assessment

Risk assessment evaluates each identified hazardous event to determine its potential impact and the necessary safety measures.

### Rating Hazardous Events

Each hazardous event is assessed based on three parameters:

1. **Controllability (C)**:
   - **Definition**: The ability of the driver or system to prevent harm through timely reactions.
   - **Scale**: C0 (Inherently Safe) to C3 (Not Controllable).

2. **Exposure (E)**:
   - **Definition**: The likelihood or duration of the vehicle being in an operational situation where the hazard could occur.
   - **Scale**: E0 (Incredible) to E4 (High Probability).

3. **Severity (S)**:
   - **Definition**: The potential extent of harm to individuals resulting from the hazardous event.
   - **Scale**: S0 (No Injury) to S3 (Life-Threatening Injury).

*Best Practice*: Use consistent standards such as the Abbreviated Injury Scale (AIS), Maximum AIS (MAIS), or Injury Severity Score (ISS) to accurately classify severities.

### Assigning Automotive Safety Integrity Levels (ASILs)

Based on the ratings of controllability, exposure, and severity, each hazardous event is assigned an ASIL using the mapping table provided in ISO 26262.

- **ASIL Categories**:
  - **ASIL A**: Lowest impact.
  - **ASIL B**: Moderate impact.
  - **ASIL C**: High impact.
  - **ASIL D**: Highest impact.
  - **QM**: Quality Managed (not relevant to ISO 26262).

*Note*: If all safety goals are assigned QM, ISO 26262 compliance is not required.

### Creating Safety Goals

For each hazardous event, establish safety goals that serve as high-level functional requirements to mitigate or eliminate risks.

**Characteristics of Safety Goals**:
- **Functional Objectives**: Should not specify technological solutions.
- **Clarity and Conciseness**: Clearly state what needs to be achieved to ensure safety.
- **Example Safety Goals**:
  - "Ensure sufficient illumination of the road while driving when a low beam is requested by the driver."
  - "Prevent unintended locking of the steering wheel during driving."
  - "Avoid unintended forward movement of the driver's seat during parking or traffic light stops."
  - "Prevent unintended self-steering."

*Best Practice*: Limit the number of safety goals to maintain manageability, typically up to 10 for regular items. Complex systems may have more, but they should remain within a practical range.

## Practical Examples and Best Practices

### Example: Steering Wheel Adjustment System

1. **Functions**:
   - Electrically adjust the steering wheel.
   - Sense the position of the steering wheel.
   - Adapt steering wheel parameters based on driving modes.

2. **Malfunctions**:
   - Loss of torque during adjustment.
   - Sensor failure leading to incorrect position sensing.
   - Unintended changes in steering parameters.

3. **Operational Situations**:
   - High-speed highway driving.
   - Urban driving with frequent stops.
   - Driving in adverse weather conditions.

4. **Hazardous Event**:
   - **Combination**: Loss of torque (malfunction) while adjusting the steering wheel during high-speed highway driving (operational situation).
   - **Effect**: Loss of vehicle control leading to potential collisions.

5. **Risk Assessment**:
   - **Severity (S)**: S3 (Life-Threatening Injury).
   - **Exposure (E)**: E3 (Probable).
   - **Controllability (C)**: C1 (Controllable with driver intervention).

6. **ASIL Assignment**: Based on the mapping table, this hazardous event may be assigned ASIL D.

7. **Safety Goal**: "Prevent loss of steering wheel torque during high-speed driving to maintain vehicle control."

## Validation and Confirmation of HARA

Ensuring the effectiveness and accuracy of HARA involves thorough reviews and validations.

- **Comprehensive Review**: Engage relevant stakeholders, including safety engineers, system designers, and management, to review and approve the HARA.
- **Consistency Checks**: Verify that all safety goals are appropriately mapped to ASILs and that ratings are consistent across similar hazardous events.
- **Update Protocols**: Implement procedures to re-evaluate and confirm HARA whenever modifications are made to the system or when new information becomes available.

*Best Practice*: Utilize confirmation measures as outlined in ISO 26262-4, ensuring that every change in HARA undergoes the necessary validation steps.

## Conclusion

Hazard Analysis and Risk Assessment (HARA) is a fundamental process within ISO 26262, critical for identifying and mitigating risks associated with automotive systems. By systematically analyzing hazards, assessing risks, and establishing safety goals, organizations can enhance the safety and reliability of their products. Adhering to the structured methodology, leveraging best practices, and ensuring thorough validation are key to successful HARA implementation.

For further assistance or inquiries, refer to the E-GAS concept documentation and engage with ISO 26262 resources to deepen your understanding and application of HARA.