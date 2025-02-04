# Current Process Controls Overview

Current process controls play a pivotal role in mitigating the risks associated with failure modes by either preventing them from occurring or detecting them promptly if they do occur. These controls encompass a broad range of activities, including but not limited to prevention measures, process validation, and verification efforts.

Process controls are critical in ensuring the reliability and safety of a system, and they can be categorized into three primary types:

1. **Prevention Controls**: These controls are designed to prevent the cause or failure mode from occurring or to reduce the rate of occurrence. Prevention is always the preferred approach, as it directly addresses the root cause of the failure mode, thereby reducing the likelihood of the issue arising.

2. **Detection and Corrective Action Controls**: These controls are focused on detecting the cause of a failure and enabling corrective actions to be taken. While not as ideal as prevention, this type of control is effective in minimizing the impact of a failure by addressing it before it can escalate.

3. **Failure Detection Controls**: The third type of control is designed to detect the failure mode itself. Although this control does not prevent the occurrence of the failure, it is crucial for identifying issues that have already manifested, allowing for timely responses to mitigate any adverse effects.

When applying these controls within the FMEA process, the preferred approach is to utilize prevention controls whenever possible. If a prevention control is effectively integrated into the process, it may warrant a reassessment of the occurrence ranking in subsequent iterations of the FMEA document. However, this reassessment should only be made if the prevention control is deeply embedded within the process and reliably reduces the likelihood of the failure mode occurring.

In situations where prevention is not feasible, the next best option is to employ detection and corrective action controls. These controls provide a valuable opportunity to catch failures early and implement corrective measures before they result in significant consequences. It is important to note, however, that while these controls are beneficial, they do not influence the occurrence ranking as prevention controls do.

Finally, failure detection controls, although useful, are the least preferable among the three types. These controls do not contribute to improving the occurrence ranking because they do not prevent the failure from happening; they merely identify it after the fact.

#### Example: Application of Process Controls

To illustrate the application of these process controls, consider the following examples of failure modes and their corresponding current process controls:

- **Failure Mode: No Calls**
  - **Current Process Controls**: Continuous monitoring of the Call Management System (CMS) and link monitoring of sessions running on CMS for the peripheral gateway. If any issue arises with the peripheral gateway, the technology team escalates the problem to the telephony team for resolution.

- **Failure Mode: Call Drops**
  - **Current Process Controls**: Monitoring the status of the trunks and alarms on the Private Branch Exchange (PBX). This ensures that any anomalies in the telephony system are detected promptly, enabling timely intervention by the relevant teams.

- **Failure Mode: Bad Connection or Static**
  - **Current Process Controls**: Supervisors are responsible for replacing faulty headsets. Additionally, if the issue persists, the voice team and telecom team are contacted to ensure that the trunk lines and service provider connections are functioning correctly.

- **Failure Mode: Lower Decibel in Voice Quality**
  - **Current Process Controls**: Escalation to the telephony team is initiated, and the telephony team is tasked with providing a solution to rectify the issue.

In each of these examples, the current process controls are specific to the nature of the failure mode and are designed to either prevent the issue from occurring or to detect it promptly for corrective action.

### 3. Documenting Current Process Controls

As you proceed with the FMEA, it is essential to meticulously document the current process controls for each identified failure mode. This documentation should include a clear description of the control, its purpose, and how it contributes to either preventing the failure or detecting it. Accurate documentation is critical for ensuring that all stakeholders, including subject matter experts (SMEs), understand the controls in place and can contribute effectively to the FMEA process.

Furthermore, by thoroughly documenting the current process controls, you create a foundation for continuous improvement. As new controls are implemented or existing ones are enhanced, this documentation can be updated to reflect these changes, ensuring that the FMEA remains an up-to-date and valuable tool in managing risk and improving reliability.