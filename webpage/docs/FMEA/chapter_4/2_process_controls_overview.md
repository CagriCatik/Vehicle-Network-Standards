# Current Process Controls Overview

Current process controls are essential to mitigating the risks associated with failure modes. They work by either preventing failures from occurring or detecting them promptly when they do occur. These controls encompass a broad range of activities, including prevention measures, process validation, and verification efforts—all of which contribute to ensuring the reliability and safety of a system.

---

## Categories of Process Controls

Process controls can be divided into three primary types:

### 1. Prevention Controls
- **Purpose:**  
  Prevent the cause or failure mode from occurring, or reduce its rate of occurrence.
- **Significance:**  
  - Directly address the root cause of a failure.
  - Are the preferred approach in risk mitigation.
  - Can lead to a reassessment of the occurrence ranking in FMEA if deeply and reliably embedded within the process.

### 2. Detection and Corrective Action Controls
- **Purpose:**  
  Detect the cause of a failure and enable corrective actions before the failure escalates.
- **Significance:**  
  - Help catch failures early.
  - Minimize the impact of a failure.
  - Do not improve the occurrence ranking in the same way as prevention controls because they address the issue only after it has started.

### 3. Failure Detection Controls
- **Purpose:**  
  Identify the failure mode itself after it has occurred.
- **Significance:**  
  - Crucial for alerting teams to issues that have already manifested.
  - The least preferable option for risk mitigation since they do not prevent the failure.
  - Do not contribute to improving the occurrence ranking.

---

## Application of Process Controls in FMEA

When applying these controls within the FMEA process, the preferred approach is:

- **Use Prevention Controls Whenever Possible:**  
  Integrating effective prevention measures can lower the likelihood of a failure and may warrant a reassessment of the occurrence ranking—provided that the control is deeply embedded and proven to reduce failure likelihood.

- **Employ Detection and Corrective Action Controls When Prevention Is Not Feasible:**  
  These controls offer the benefit of early detection and timely intervention but do not alter the occurrence ranking.

- **Rely on Failure Detection Controls as a Last Resort:**  
  While useful for identifying failures after the fact, they do not help in reducing the initial probability of occurrence.

---

## Example: Process Controls in a Telephony System

Below are examples of failure modes along with their corresponding current process controls:

- **Failure Mode: No Calls**
  - **Process Controls:**
    - Continuous monitoring of the Call Management System (CMS).
    - Link monitoring of sessions running on the CMS for the peripheral gateway.
    - Escalation protocol: Any issues with the peripheral gateway are immediately escalated by the technology team to the telephony team.

- **Failure Mode: Call Drops**
  - **Process Controls:**
    - Monitoring of trunk statuses and alarms on the Private Branch Exchange (PBX).
    - Prompt detection of anomalies allows for timely intervention by relevant teams.

- **Failure Mode: Bad Connection or Static**
  - **Process Controls:**
    - Supervisors are responsible for replacing faulty headsets.
    - If issues persist, the voice team and telecom team are contacted to verify trunk lines and service provider connections.

- **Failure Mode: Lower Decibel in Voice Quality**
  - **Process Controls:**
    - An escalation process directs the issue to the telephony team.
    - The telephony team then takes action to restore proper voice quality.

Each example demonstrates controls tailored to the specific failure mode, either preventing the issue from occurring or ensuring it is detected promptly for corrective action.

---

## Documenting Current Process Controls

For the FMEA process to be effective, meticulous documentation of current process controls is essential. This documentation should include:

- **Clear Descriptions:**  
  Detail each control, its operational mechanism, and its role in either preventing failures or detecting them early.

- **Purpose and Contribution:**  
  Explain how each control contributes to risk mitigation and its impact on the overall occurrence ranking.

- **Stakeholder Clarity:**  
  Ensure that all stakeholders, including subject matter experts (SMEs), understand the controls in place. This shared understanding facilitates effective collaboration during the FMEA process.

- **Foundation for Continuous Improvement:**  
  Regularly update documentation to reflect new controls or enhancements to existing ones, ensuring that the FMEA remains an up-to-date tool for managing risk and improving system reliability.
