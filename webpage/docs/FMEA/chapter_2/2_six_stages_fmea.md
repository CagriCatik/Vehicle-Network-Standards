# The Six Stages of FMEA

## Overview of the FMEA Process

The FMEA process is typically divided into six distinct stages:

1. **Identifying Failure Modes and Specifying Severity**
2. **Specifying the Occurrence of Failures**
3. **Specifying the Detectability of Failures**
4. **Quantifying Risk**
5. **Correcting High-Risk Situations**
6. **Reevaluating Risk**

Each stage plays a crucial role in the overall effectiveness of the FMEA process. Below is a detailed exploration of what happens during each stage.

## Stage 1: Identifying Failure Modes and Specifying Severity

### Objective

The objective of this stage is to systematically identify potential failure modes in the process, product, or system being analyzed and to assess the severity of their effects on overall performance and safety.

### Process

1. **Step Identification**: Begin by mapping out the different steps and activities involved in the process, product, or system. This comprehensive mapping ensures that no potential failure mode is overlooked.

2. **Brainstorming Potential Failure Modes**: For each step and activity identified, brainstorm potential failure modes. A failure mode refers to any way in which a process, product, or system could fail to meet its intended function.

   - **Examples**:
     - A component may break (mechanical failure).
     - A software algorithm may produce incorrect results (software failure).
     - A process step may be skipped (procedural failure).

3. **Documenting Potential Effects**: For each identified failure mode, document the potential effects of the failure. The effects should consider the impact on the immediate process, as well as on the overall system or product performance.

   - **Examples**:
     - Mechanical failure may lead to complete system shutdown.
     - Software failure may result in incorrect data processing.
     - Procedural failure may cause delays in product delivery.

4. **Assigning Severity Rankings**: Once the effects of each failure mode have been documented, assign a severity ranking. This ranking should reflect the seriousness of the potential effect, often on a scale from 1 (least severe) to 10 (most severe). Severity rankings should be based on the potential impact on customer safety, regulatory compliance, and overall system integrity.

   - **Example**:
     - A failure mode that could lead to a life-threatening situation might be assigned a severity ranking of 10.
     - A failure mode resulting in minor inconvenience might be assigned a severity ranking of 2.

### Outcome

At the end of this stage, you will have a detailed list of potential failure modes, their effects, and their severity rankings. This information serves as the foundation for the subsequent stages of the FMEA process.

## Stage 2: Specifying the Occurrence of Failures

### Objective

The objective of this stage is to determine how frequently each identified failure mode is likely to occur.

### Process

1. **Identifying Potential Causes**: For each failure mode identified in Stage 1, investigate and document the potential causes. This step requires a deep understanding of the process, product, or system being analyzed.

   - **Examples**:
     - Mechanical failure may be caused by material fatigue.
     - Software failure might occur due to a coding error.
     - Procedural failure might happen due to insufficient training.

2. **Assigning Occurrence Ratings**: After identifying the potential causes, assign an occurrence rating to each failure mode. This rating typically ranges from 1 (rare occurrence) to 10 (frequent occurrence).

   - **Example**:
     - A failure mode with a well-documented history of frequent occurrence might be rated a 9 or 10.
     - A failure mode that occurs under rare, specific conditions might be rated a 1 or 2.

### Outcome

At the conclusion of this stage, you will have occurrence ratings assigned to each failure mode. These ratings provide a quantitative measure of the likelihood that each failure mode will occur, which is essential for the risk assessment in subsequent stages.

## Stage 3: Specifying the Detectability of Failures

### Objective

The objective of this stage is to assess how easily each failure mode can be detected before it causes an adverse effect.

### Process

1. **Identifying Current Process Controls**: Review the existing controls that are in place to detect or prevent each failure mode before it leads to a failure effect. These controls might include inspections, testing, monitoring systems, or procedural checks.

   - **Examples**:
     - Visual inspections of components.
     - Automated software testing.
     - Standard operating procedures (SOPs) for process steps.

2. **Assigning Detection Ratings**: Based on the effectiveness of the existing controls, assign a detection rating to each failure mode. The detection rating typically ranges from 1 (very high likelihood of detection) to 10 (very low likelihood of detection).

   - **Example**:
     - A failure mode with highly effective, automated detection systems might be rated a 1 or 2.
     - A failure mode that can only be detected after a failure has occurred might be rated a 9 or 10.

### Outcome

By the end of this stage, you will have a detection rating for each failure mode, indicating how likely it is that the failure will be detected before it causes harm. This information is crucial for the risk prioritization that follows.

## Stage 4: Quantifying Risk

### Objective

The objective of this stage is to calculate the overall risk associated with each failure mode by combining the severity, occurrence, and detection ratings.

### Process

1. **Calculating the Risk Priority Number (RPN)**: For each failure mode, calculate the Risk Priority Number (RPN) by multiplying the severity, occurrence, and detection ratings:

   \[
   \text{RPN} = \text{Severity} \times \text{Occurrence} \times \text{Detection}
   \]

   The RPN is a numerical value that prioritizes the failure modes based on their associated risks.

   - **Example**:
     - A failure mode with a severity rating of 8, an occurrence rating of 6, and a detection rating of 5 would have an RPN of 240 (8 × 6 × 5).

2. **Ranking the Failure Modes**: Once the RPNs are calculated, rank the failure modes from highest to lowest RPN. The failure modes with the highest RPNs represent the most significant risks and should be prioritized for corrective action.

### Outcome

At the conclusion of this stage, you will have a ranked list of failure modes based on their RPNs, highlighting the areas of greatest concern and providing a clear focus for mitigation efforts.

## Stage 5: Correcting High-Risk Situations

### Objective

The objective of this stage is to develop and implement corrective actions for the failure modes with the highest RPNs.

### Process

1. **Documenting Recommended Actions**: For each high-risk failure mode, document the recommended actions that should be taken to reduce the associated risks. These actions might involve design changes, process modifications, additional controls, or enhanced detection methods.

   - **Examples**:
     - Implementing stronger materials to prevent mechanical failure.
     - Revising software algorithms to eliminate coding errors.
     - Providing additional training to prevent procedural errors.

2. **Assigning Responsibility and Target Dates**: Assign responsibility for implementing each recommended action and set target dates for completion. This ensures accountability and timely execution of the corrective measures.

   - **Example**:
     - Assigning the engineering team to develop a new material specification with a target date of completion within three months.

### Outcome

At the end of this stage, you will have a detailed action plan for mitigating the highest risks identified in the FMEA process. This plan should include clear responsibilities and timelines, ensuring that the necessary corrective actions are implemented effectively.

## Stage 6: Reevaluating Risk

### Objective

The objective of this final stage is to reassess the risks after the implementation of the corrective actions, ensuring that the desired risk reduction has been achieved.

### Process

1. **Documenting Specific Actions Taken**: After completing the recommended actions, document the specific actions that were implemented. This documentation should include any changes made to the process, product, or system, as well as any new controls introduced.

   - **Example**:
     - Documentation of a new material specification and the results of testing the new material under operational conditions.

2. **Revising Severity, Occurrence, and Detection Ratings**: Reevaluate the severity, occurrence, and detection ratings for each failure mode based on the implemented actions. If the actions were effective, these ratings should reflect a lower level of risk.

   - **Example**:
     - A failure mode that previously had a detection rating of 9 might now have a detection rating of 3 due to the implementation of an automated testing system.

3. **Calculating the New RPN**: Recalculate the RPN for each failure mode using the revised ratings. Compare the new RPNs to the original RPNs to determine the effectiveness of the corrective actions.

4. **Documenting and Communicating Results**: Document the final RPNs and communicate the results to all relevant stakeholders. This step ensures that everyone involved is aware of the risk levels and the effectiveness of the mitigation efforts.

### Outcome

Upon completing this stage, you

 will have an updated risk assessment that reflects the current state of the process, product, or system after corrective actions have been implemented. This re-evaluation provides assurance that the risks have been effectively managed and that the process is now more robust.

## Conclusion

Failure Modes and Effects Analysis (FMEA) is an essential tool in reliability engineering, providing a structured approach to identifying, assessing, and mitigating risks. By following the six stages outlined in this document—identifying failure modes, specifying occurrence, specifying detectability, quantifying risk, correcting high-risk situations, and reevaluating risk—you can systematically reduce the likelihood and impact of failures in your processes, products, or systems.
