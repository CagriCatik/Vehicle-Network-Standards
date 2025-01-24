# Safety Analyses for concept, system, software

Functional safety is a cornerstone of modern automotive engineering, ensuring that vehicles operate reliably and safely under all conditions. A critical component of achieving functional safety is conducting thorough safety analyses. ISO 26262, the international standard for functional safety of electrical and electronic systems in road vehicles, provides a structured approach to identifying, assessing, and mitigating safety risks through various safety analysis methods. This documentation explores the essential aspects of safety analyses at the concept, system, and software levels, offering detailed explanations, practical examples, and best practices to guide automotive engineers in implementing effective safety strategies.

## Importance of Safety Analysis

Safety analysis serves as the foundation for identifying potential hazards and ensuring that safety goals are met. By systematically evaluating what can go wrong and determining whether sufficient measures have been taken to prevent such occurrences, safety analysis minimizes the risk of safety goal violations due to systematic or random faults.

## Key Objectives of Safety Analysis

1. **Identify Potential Hazards**:
   - Determine what can go wrong within the system.
   
2. **Assess Risk Mitigation**:
   - Evaluate whether existing safety measures adequately prevent identified hazards.

3. **Ensure Compliance**:
   - Verify that the risk of safety goal violations is sufficiently low.

## Perspectives of Safety Analysis

Safety analyses can be approached from different perspectives, categorized as follows:

### 1. Analytical Approach

- **Top-Down (Deductive) Analysis**:
  - Begins with known effects and works backward to identify potential causes.
  - **Example**: Fault Tree Analysis (FTA).
  
- **Bottom-Up (Inductive) Analysis**:
  - Starts with known causes and moves upward to identify potential effects.
  - **Example**: Failure Mode and Effects Analysis (FMEA).

### 2. Quantitative vs. Qualitative Analysis

- **Quantitative Analysis**:
  - Involves numerical evaluation of failure rates and probabilities.
  - **Uses**:
    - Validate hardware designs against predefined targets.
    - Assess hardware architectural metrics.
    - Determine likelihood of safety goal violations.
  - **Examples**: Quantitative FMEA, Quantitative FTA, Markov Models, FMEDA.
  
- **Qualitative Analysis**:
  - Focuses on identifying failures without quantifying their probabilities.
  - **Uses**:
    - Identify potential failures and their effects.
    - Applicable to software and other domains beyond hardware.
  - **Examples**: Qualitative FMEA, Qualitative FTA, Hazard and Operability Study (HAZOP), Event Tree Analysis (ETA).

## Safety Analysis Methods

ISO 26262 recommends several safety analysis methods, each suited to different aspects of system development. Below are four primary methods, along with their applications and best practices.

### 1. Failure Mode and Effects Analysis (FMEA)

- **Definition**: An inductive, bottom-up analysis method used to identify potential failure modes, their effects, and causes within a system.
  
- **Standards**:
  - **FMEA Handbook**: Released by VDA (Germany) and AIAG (USA), available online.
  
- **Types of FMEA**:
  - **Design FMEA (DFMEA)**: Focuses on technical designs.
  - **Process FMEA (PFMEA)**: Analyzes manufacturing and assembly processes.
  - **FMEA for Monitoring and System Response (FMEA-MSR)**: Evaluates failure causes under customer operating conditions.
  
- **Best Practices**:
  - **Use Dedicated Tools**: Employ tools like Isograph or APIS-IQ for structured analysis.
  - **Iterative Process**: Repeat the eight-step process to refine analysis outcomes.
  - **Comprehensive Coverage**: Ensure all functions and processes are analyzed for potential failures.
  
- **Practical Example**:
  - **Steer-by-Wire System**:
    - **Functions**: Steering input detection, actuator control.
    - **Failure Modes**: Sensor stuck-at, actuator malfunction.
    - **Effects**: Unintended steering maneuvers, loss of steering control.
    - **Causes**: Electrical faults, software bugs.

### 2. Fault Tree Analysis (FTA)

- **Definition**: A deductive, top-down analysis method that starts with an undesired event and systematically identifies its root causes through a logical tree structure.
  
- **Components**:
  - **Top Event**: The undesired event (e.g., violation of a safety goal).
  - **Intermediate Events**: Conditions that contribute to the top event.
  - **Basic Events**: Fundamental causes leading to intermediate events.
  
- **Best Practices**:
  - **Structured Approach**: Use standardized symbols and logical gates for clarity.
  - **Comprehensive Coverage**: Analyze all possible pathways leading to the top event.
  - **Tool Utilization**: Employ software tools like Isograph for efficient tree construction.
  
- **Practical Example**:
  - **Steer-by-Wire System**:
    - **Top Event**: Unintended steering maneuver.
    - **Intermediate Events**: Sensor failure, actuator failure.
    - **Basic Events**: Power supply disruption, software bug.

### 3. Hazard and Operability Study (HAZOP)

- **Definition**: A qualitative, inductive analysis method aimed at identifying potential hazards and operability issues by examining deviations from design intentions.
  
- **Standards**:
  - **IEC 61882**: Provides guidelines for conducting HAZOP.
  
- **Best Practices**:
  - **Use Guide Words**: Apply systematic guide words to explore deviations (e.g., No, More, Less, As well as).
  - **Team-Based Approach**: Involve cross-functional teams to enhance analysis comprehensiveness.
  - **Documentation**: Maintain detailed records of identified hazards and proposed mitigations.
  
- **Practical Example**:
  - **Steer-by-Wire System**:
    - **Deviation**: "No" steering input detected.
    - **Hazard**: Loss of steering control.
    - **Mitigation**: Implement redundant sensors and fail-safe mechanisms.

### 4. Failure Modes, Effects, and Diagnostic Analysis (FMEDA)

- **Definition**: An extension of FMEA that incorporates quantitative aspects, such as failure rates and diagnostic coverage, to assess the reliability of safety mechanisms.
  
- **Developed By**: Exida, a global leader in functional safety.
  
- **Best Practices**:
  - **Integrate with FMEA**: Combine FMEDA with FMEA to enhance depth of analysis.
  - **Use Reliable Data Sources**: Refer to standards like IEC 61709 for accurate failure rates.
  - **Focus on Random Failures**: Specifically analyze random hardware failures and their detection.
  
- **Practical Example**:
  - **Steer-by-Wire System**:
    - **Failure Rate**: Calculate failure rates for steering sensors.
    - **Diagnostic Coverage**: Assess how effectively CRC checks detect sensor faults.
    - **Residual FIT**: Determine the remaining failure rate after safety mechanisms are applied.

## Safety Analysis at Different Levels

Safety analyses are conducted at various stages of the system development lifecycle, each with specific objectives and methodologies.

### 1. Concept Level

- **Primary Analysis**: Hazard Analysis and Risk Assessment (HARA).
  
- **Additional Analyses**:
  - **Fault Tree Analysis (FTA)**:
    - Identify common cause faults across different systems.
    - Partition hardware metrics among system components.
  - **Failure Mode and Effects Analysis (FMEA)**:
    - Derive functional safety requirements.
    - Incorporate emission criteria and other non-functional aspects.
  
- **Best Practices**:
  - **Early Identification**: Conduct analyses early to influence design decisions.
  - **Comprehensive Coverage**: Include all relevant systems and functions in the analysis.
  - **Integration with Safety Concepts**: Ensure analyses inform the functional and technical safety concepts.

### 2. System Level

- **Primary Analyses**: FMEA and FTA (both qualitative and quantitative).
  
- **Objectives**:
  - Assist in system design by identifying and mitigating potential failures.
  - Analyze both systematic and random failures.
  
- **Methodology**:
  - **Design Without Safety Mechanisms**: Begin analysis without considering safety measures to identify inherent risks.
  - **Identify Safety Goal Violations**: Use FMEA to list potential effects leading to safety goal violations and analyze them with FTA.
  
- **Best Practices**:
  - **Use Both Deductive and Inductive Methods**: Combine FMEA and FTA to cover all failure pathways.
  - **Focus on Critical Interfaces**: Analyze failure impacts on system interfaces.
  - **Determine Testing Criteria**: Use safety analyses to define testing time and acceptance criteria.

### 3. Software Level

- **Primary Analyses**: Software FMEA, Software FTA, Design Failure Analysis (DFA), Critical Path Analysis (CPA), and HAZOP.
  
- **Challenges**:
  - **Applicability of FMEA**: Traditional FMEA is designed for hardware and processes, making it less straightforward for software.
  
- **Methodology**:
  - **Software FMEA**:
    - Identify software failure modes and their effects.
    - Link failures to safety requirements.
  - **Software FTA**:
    - Use Boolean logic to identify root causes of software failures.
  - **Software Dependent Failure Analysis (S-DFA)**:
    - Identify coupling factors that lead to multiple software component failures.
  
- **Best Practices**:
  - **Use Alternative Methods When Necessary**: Consider using DFA or CPA for more effective software safety analysis.
  - **Integrate with Architectural Design**: Ensure software safety analyses inform and are informed by software architectural design.
  - **Develop Comprehensive Test Cases**: Derive test cases from safety analyses to validate software behavior under fault conditions.

## Practical Example: Steer-by-Wire System

### System Overview

A steer-by-wire system replaces traditional mechanical steering connections with electronic controls, enhancing precision and enabling advanced driver assistance features.

### Safety Analysis Steps

1. **Concept Level**:
   - **HARA**: Identify hazards related to steering control loss.
   - **FMEA**:
     - **Functions**: Steering input detection, actuator control.
     - **Failure Modes**: Sensor stuck-at, actuator malfunction.
     - **Effects**: Unintended steering maneuvers, loss of steering control.
   - **FTA**:
     - **Top Event**: Unintended steering maneuver.
     - **Intermediate Events**: Sensor failure, actuator failure.
     - **Basic Events**: Power supply disruption, software bug.
   
2. **System Level**:
   - **FMEA**:
     - **Subsystems**: Steering sensors, actuators, control units.
     - **Failure Modes**: Communication faults, timing issues.
     - **Effects**: Delayed steering response, incorrect actuator signals.
   - **FTA**:
     - **Top Event**: Delayed steering response.
     - **Causes**: CAN bus communication failure, CPU overload.
   
3. **Software Level**:
   - **Software FMEA**:
     - **Modules**: Steering input processing, actuator control algorithms.
     - **Failure Modes**: Algorithm error, memory corruption.
     - **Effects**: Incorrect steering commands, system crash.
   - **Software FTA**:
     - **Top Event**: System crash during steering operation.
     - **Causes**: Unhandled exception, watchdog timer failure.

### Implementation of Safety Mechanisms

- **Redundant Steering Sensors**:
  - **Diagnostic Coverage**: 90% to detect sensor faults.
  - **Mitigation**: Switch to redundant sensor upon fault detection.
  
- **Watchdog Timers**:
  - **Diagnostic Coverage**: 60% to detect unresponsive control units.
  - **Mitigation**: Trigger system reset or transition to manual steering mode.

### Verification and Validation

- **Fault Injection Testing**:
  - **Objective**: Verify that safety mechanisms detect and respond to simulated faults.
  - **Procedure**: Introduce faults such as sensor stuck-at high voltage and observe system response.
  
- **Hardware-in-the-Loop (HIL) Simulation**:
  - **Objective**: Validate system behavior under various fault conditions without physical prototypes.
  
- **On-Road Testing**:
  - **Objective**: Ensure real-world functionality and safety compliance.
  
- **Validation Report**:
  - **Contents**: Test results, analysis of fault detection effectiveness, compliance with safety goals.

## Best Practices for Conducting Safety Analyses

### Comprehensive Documentation

- **Detailed Records**:
  - Document all safety goals, identified hazards, analysis methods, and mitigation strategies.
  
- **Traceability**:
  - Maintain clear linkage between safety goals, requirements, analysis findings, and implemented safety measures.
  
- **Standardized Formats**:
  - Use consistent documentation templates to enhance clarity and facilitate audits.

### Early and Continuous Safety Integration

- **Safety from the Outset**:
  - Incorporate safety considerations during initial design phases to identify and mitigate risks early.
  
- **Ongoing Assessments**:
  - Continuously update safety analyses based on new insights, design changes, and testing feedback.

### Iterative Development and Refinement

- **Design-Analyze-Verify Cycle**:
  - Adopt an iterative approach, refining designs based on continuous analysis and verification feedback.
  
- **Responsive to Feedback**:
  - Incorporate findings from testing and validation to enhance system safety and performance.

### Cross-Functional Collaboration

- **Unified Safety Approach**:
  - Foster collaboration among hardware engineers, software developers, safety analysts, and other stakeholders.
  
- **Joint Reviews**:
  - Conduct joint design and safety reviews to identify and address cross-domain risks effectively.

### Adherence to Standards

- **Strict Compliance**:
  - Follow ISO 26262 guidelines meticulously to ensure all safety requirements are met.
  
- **Leverage Best Practices**:
  - Incorporate industry best practices in safety analysis to enhance system reliability and safety.

### Utilize Advanced Tools

- **Application Lifecycle Management (ALM) Tools**:
  - Use tools like CodeBeamer ALM or IBM Suite to manage requirements, traceability, and safety analysis activities.
  
- **Modeling and Simulation Tools**:
  - Employ UML, SysML, or HIL simulation tools to visualize system architecture and validate behavior under fault conditions.
  
- **Automated Analysis Tools**:
  - Implement tools like Isograph for FMEA and FTA to streamline analysis processes and improve accuracy.

## Conclusion

Safety analysis is an integral part of achieving functional safety in automotive systems as outlined by ISO 26262. By systematically identifying potential faults and failures, assessing their impacts, and implementing robust safety mechanisms, automotive engineers can ensure that safety goals are met and that vehicles operate reliably and safely under all conditions. Adhering to best practices, leveraging advanced tools, and fostering cross-functional collaboration are essential for conducting effective safety analyses at the concept, system, and software levels. Comprehensive documentation and continuous safety assessments further reinforce the integrity and safety of automotive systems throughout their lifecycle.

## Recommended Resources

- **The Risks Digest**:
  - An online forum moderated by Peter Neumann, focused on the security and safety of computers, software, and technological systems.
  
- **Electropedia**:
  - The world's online electrotechnical vocabulary, as defined by IEC 60050, providing comprehensive definitions and explanations of technical terms related to electronics and safety.
  
- **IEC 61508**:
  - A broader functional safety standard applicable to various industries, offering principles that complement ISO 26262.

- **FMEA Handbook by VDA and AIAG**:
  - Comprehensive guide on conducting FMEA, available online for reference.

## Next Steps

In upcoming sessions, we will delve deeper into specific safety analysis methods for hardware and software, exploring detailed methodologies and techniques to enhance your ability to conduct thorough safety assessments. Topics will include advanced Fault Tree Analysis, Software FMEA nuances, and integrating safety analyses into the overall system development lifecycle to achieve full compliance with ISO 26262.