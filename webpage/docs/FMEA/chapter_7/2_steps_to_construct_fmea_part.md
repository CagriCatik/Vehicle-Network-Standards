# A Guide to Constructing a Failure Modes and Effects Analysis

## Introduction

Failure Modes and Effects Analysis (FMEA) is a structured and methodical approach used to identify potential failure modes within a system, process, or product. It assesses the impact of these failures, determines their causes, and prioritizes corrective actions. This guide provides a detailed, step-by-step process for constructing an FMEA, ensuring both novices and experienced professionals can apply this technique effectively in reliability engineering.

## Step-by-Step Process for Constructing an FMEA

### Step 1: Assemble a Cross-Functional Team

The success of an FMEA hinges on the collective expertise of a diverse, cross-functional team. This team should encompass individuals from various departments, each bringing unique insights into the product, process, or service under analysis.

- **Manufacturing Functions**: Include representatives from design, manufacturing, quality testing, reliability, maintenance, purchasing, sales, marketing, and customer service.
- **Service Industry Functions**: For service-oriented FMEAs, involve members from operations, training, finance, management information systems (MIS), quality assurance, transition, and customer support.

The diversity of the team ensures a comprehensive identification and assessment of potential failure modes from multiple perspectives.

### Step 2: Define the Scope of the FMEA

Clearly defining the scope is crucial to focus the FMEA on the relevant aspects of the system, process, or service.

- **Type of FMEA**: Determine whether the FMEA will focus on a concept, system, design, process, or service.
- **Boundaries**: Define the limits of the analysis, specifying what is included and excluded.
- **Level of Detail**: Decide how detailed the analysis should be, whether it will cover the entire system or specific subsystems or components.

Visual tools like flowcharts, block diagrams, or process maps can help clarify the scope and ensure all team members have a shared understanding.

### Step 3: Document Identifying Information on the FMEA Form

Before diving into the analysis, complete the essential identifying information at the top of the FMEA form:

- **Project Title**: The name of the project or the specific system/process being analyzed.
- **Date**: The date when the FMEA is initiated.
- **Team Members**: Names and roles of the individuals involved in the FMEA.
- **Additional Details**: Include any other relevant information, such as version number, approval signatures, or a brief project description.

Accurate documentation at this stage ensures traceability and accountability throughout the FMEA process.

### Step 4: Identify the Functions and Process Steps

Identify the primary functions of the system or process within the defined scope and document the associated process steps.

- **Functional Departments**: Specify the departments or areas for which the FMEA is being created.
- **Process Steps**: Detail the individual steps involved in the process, ensuring all critical operations are covered.

This step provides a foundation for identifying potential failure modes in the subsequent stages.

### Step 5: Identify Potential Failure Modes

For each function and process step identified, brainstorm potential failure modes—ways in which the component, subsystem, or process step might fail to perform its intended function.

- **Failure Mode Identification**: Conduct a thorough brainstorming session with the cross-functional team to list all conceivable failure modes.
- **Documentation**: Clearly and precisely record each identified failure mode on the FMEA form.

This step is critical as it lays the groundwork for analyzing the effects and risks associated with each failure mode.

### Step 6: Determine the Potential Effects of Each Failure Mode

Assess the potential effects of each identified failure mode on the system, related systems, processes, products, services, customers, or regulatory compliance.

- **Effect Analysis**: Ask key questions such as: What will the customer experience if this failure occurs? What are the potential downstream impacts on the system or process?
- **Customer Perspective**: Consider the impact from the customer’s point of view, as this is crucial in assessing the severity of the failure.

Document the effects of each failure mode on the FMEA form, ensuring all possible consequences are considered.

### Step 7: Assign a Severity Rating to Each Effect

The severity of each potential effect must be assessed to understand the criticality of the failure mode. Severity is typically rated on a scale from 1 to 10.

- **Rating Scale**:
  - **1**: Represents an insignificant effect with no impact on the system, process, or customer.
  - **10**: Indicates a catastrophic effect that could lead to system failure, significant process disruption, or serious harm to the customer or regulatory breach.

The severity rating helps prioritize which failure modes require the most attention in terms of risk mitigation.

### Step 8: Identify the Potential Root Causes for Each Failure Mode

Identify all potential root causes for each failure mode to address the underlying issues that lead to failure.

- **Root Cause Analysis**: Use tools like the 5 Whys, Fishbone Diagram (Ishikawa), or Fault Tree Analysis to systematically explore the underlying causes of failures.
- **Documentation**: List all identified root causes for each failure mode on the FMEA form.

This step ensures that mitigation efforts target the actual sources of failure rather than just addressing the symptoms.

### Step 9: Determine the Occurrence Rating for Each Cause

The occurrence rating estimates the likelihood that each root cause will lead to the associated failure mode.

- **Rating Scale**:
  - **1**: Indicates that the cause is extremely unlikely to lead to failure.
  - **10**: Indicates that failure due to the cause is inevitable or highly probable.
- **Documentation**: Record the occurrence rating for each cause in the FMEA form.

Accurately assessing the occurrence rating is crucial for prioritizing risks and focusing mitigation efforts.

### Step 10: Identify Current Process Controls

For each root cause, document any existing process controls that are in place to prevent the failure mode from occurring or to detect it before it impacts the customer.

- **Types of Controls**:
  - **Preventive Controls**: Controls that reduce the likelihood of the failure mode occurring.
  - **Detective Controls**: Controls that detect the failure mode after it occurs but before it reaches the customer.
- **Documentation**: Clearly list all current controls for each cause in the FMEA form.

This step ensures that all existing safeguards are recognized and potential gaps in the control processes are identified.

### Step 11: Assign a Detection Rating for Each Control

Evaluate the effectiveness of current process controls in detecting the failure mode before it leads to an impact. The detection rating is typically on a scale from 1 to 10.

- **Rating Scale**:
  - **1**: Indicates that the failure mode is almost certain to be detected before causing any harm.
  - **10**: Indicates that the failure mode is very unlikely to be detected until it results in significant impact.
- **Documentation**: Record the detection rating for each cause in the FMEA form.

This rating highlights areas where detection mechanisms may need improvement.

### Step 12: Calculate the Risk Priority Number (RPN)

The Risk Priority Number (RPN) is a critical metric in FMEA, providing a numerical value that helps prioritize failure modes based on their risk.

- **Calculation**: Multiply the severity, occurrence, and detection ratings to calculate the RPN:
  \[
  \text{RPN} = \text{Severity (S)} \times \text{Occurrence (O)} \times \text{Detection (D)}
  \]
- **Purpose**: The RPN helps in ranking the failure modes, with higher RPNs indicating higher risks that should be addressed first.
- **Documentation**: Calculate and document the RPN for each failure mode on the FMEA form.

The RPN serves as a guide for prioritizing risk mitigation efforts.

### Step 13: Identify Recommended Actions

For failure modes with high RPNs, develop and recommend actions to reduce or eliminate the associated risks.

- **Types of Actions**:
  - **Design Changes**: Modify the design to eliminate the cause or reduce the severity of the effect.
  - **Process Improvements**: Enhance process controls to lower the occurrence or improve the detection of the failure mode.
  - **Additional Controls**: Implement new controls or strengthen existing ones to better manage the identified risks.
- **Responsibility and Timelines**: Assign responsibility for each action to specific team members and establish target completion dates.
- **Documentation**: Record the recommended actions, along with responsible persons and timelines, on the FMEA form.

Prompt and effective action on high-priority risks is essential for reducing the likelihood and impact of potential failures.

### Step 14: Re-evaluate Risks and Failures Continuously

FMEA is an iterative process that requires continuous monitoring and updating as changes are made to the system, process, or controls.

- **Re-evaluation**: After implementing recommended actions, reassess the risks by recalculating the RPN.
- **Documentation**: Update the FMEA form with the results of the re-evaluation, including any new ratings, the new RPN, and the dates of these changes.
- **Ongoing Review**: Establish a regular review process to ensure that the FMEA remains current and relevant.

This ongoing process ensures that the FMEA continues to be a valuable tool for managing risks and improving the reliability and safety of the system or process.

## Conclusion

This structured, 14-step process for constructing an FMEA provides a comprehensive approach to identifying, assessing, and mitigating risks within a system, product, or process. By following these steps, you can systematically reduce the likelihood of failures, enhance the effectiveness of controls, and ensure that potential risks are managed proactively. This methodology is essential for both beginners and experienced professionals in reliability engineering and serves as a critical tool for ensuring the quality, safety, and performance of any system or process.