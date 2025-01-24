# Confirmation Measures in ISO 26262

## Introduction

In the realm of automotive functional safety, **confirmation measures** play a pivotal role in ensuring that safety objectives and requirements are meticulously met throughout the product lifecycle. According to **ISO 26262**, confirmation measures encompass **confirmation reviews**, **functional safety audits**, and **functional safety assessments**. This documentation delves into each of these components, providing clear explanations, practical examples, and best practices to facilitate a comprehensive understanding and effective implementation.

## Confirmation Reviews

### Definition

A **confirmation review** is a formal evaluation process that verifies whether a work product provides sufficient and convincing evidence contributing to the achievement of functional safety. This verification is conducted in alignment with the corresponding objectives and requirements outlined in ISO 26262.

### Purpose

- **Ensure Compliance:** Validate that work products meet functional safety requirements.
- **Identify Gaps:** Detect any deficiencies or inconsistencies in the work products.
- **Facilitate Improvement:** Provide actionable feedback to enhance the quality and safety of the product.

### Types of Work Products

Confirmation reviews can be applied to various work products, including but not limited to:

- **Documents:** Safety plans, requirements specifications, design documents.
- **Source Code:** Software modules, scripts, algorithms.
- **Artifacts:** Diagrams, models, test cases.

### Review Process

1. **Preparation:**
   - **Define Scope:** Identify the work product to be reviewed.
   - **Develop Checklist:** Utilize checklists based on ISO 26262 requirements to guide the review.
   - **Establish Criteria:** Set clear pass/fail criteria and relevant project-specific parameters.

2. **Execution:**
   - **Conduct Review:** Perform the formal evaluation using established checklists and guidelines.
   - **Document Findings:** Record observations, non-conformities, and areas for improvement.

3. **Evaluation:**
   - **Analyze Results:** Assess whether the work product meets the defined criteria.
   - **Determine Outcomes:** Decide on pass, conditional pass, or fail based on the findings.

4. **Follow-Up:**
   - **Address Issues:** Implement corrective actions for identified deficiencies.
   - **Re-Review if Necessary:** Conduct additional reviews to ensure issues are resolved.

### Independence

- **Objective Evaluation:** Reviewers must be independent from the team that created the work product to ensure unbiased assessment.
- **Levels of Independence:**
  - **I1:** Reviewers from the same team but different roles.
  - **I2:** Reviewers from different teams within the organization.
  - **I3:** Reviewers from external departments, divisions, or partner companies.

### Best Practices

- **Use External Partners:** Engage external experts to enhance independence and credibility.
- **Standardize Checklists:** Develop and maintain standardized checklists tailored to project needs.
- **Regular Reviews:** Schedule multiple confirmation reviews throughout the project lifecycle.
- **Training:** Ensure reviewers are adequately trained in ISO 26262 and the specific review process.

### Practical Example

**Scenario:** Reviewing the safety requirements specification for an autonomous braking system.

- **Preparation:** Develop a checklist focusing on completeness, correctness, and traceability of requirements.
- **Execution:** A cross-functional team conducts the review, identifying missing safety mechanisms.
- **Evaluation:** Determine that the specification partially meets ISO 26262 standards.
- **Follow-Up:** Update the requirements to include the identified safety mechanisms and schedule a re-review.

## Functional Safety Audits

### Definition

A **functional safety audit** is a systematic examination of implemented processes related to functional safety to determine their compliance with predefined process objectives.

### Purpose

- **Verify Process Implementation:** Ensure that safety-related processes are correctly implemented.
- **Assess Effectiveness:** Evaluate the effectiveness of processes in achieving safety objectives.
- **Identify Improvements:** Highlight areas for process enhancement and optimization.

### Differences Between Audit and Assessment

- **Audit:**
  - Focuses on **processes**.
  - Evaluates **compliance** with standards and procedures.
  - Conducted by individuals managing or overseeing processes.

- **Assessment:**
  - Focuses on **product safety**.
  - Evaluates the **achievement** of safety goals.
  - Conducted by specialized safety assessors.

### Types of Processes Audited

Functional safety audits typically cover a wide range of automotive engineering processes, including but not limited to:

- **Requirements Management:** Processes for writing, tracing, and reviewing safety requirements.
- **Testing:** Development and execution of test plans, running tests, and analyzing results.
- **Static Code Analysis:** Evaluation of source code for compliance with safety standards.
- **Issue Management:** Processes for identifying, analyzing, and resolving safety-related issues.
- **Change Management:** Procedures for detecting and implementing changes to maintain safety integrity.

### Integration with Other Audits

- **ASPICE Audits:** Functional safety audits can be integrated with Automotive SPICE (ASPICE) audits to provide a comprehensive evaluation of both functional safety and process quality.
- **Combined Audits:** Conducting joint audits for multiple standards can streamline the audit process and reduce redundancy.

### Independence

- **Audit Team Composition:** Auditors should possess a degree of independence from the processes they audit to maintain objectivity.
- **External Auditors:** Utilizing external auditors can enhance independence and provide an unbiased perspective.

### Current Trends

- **Shift Towards Assessments:** There is a growing trend to emphasize functional safety assessments over explicit audits.
- **Integration with Quality Audits:** Functional safety processes are increasingly audited within broader quality management audits, such as ASPICE.

### Best Practices

- **Define Clear Objectives:** Establish specific goals for each audit to ensure focused and effective evaluations.
- **Regular Scheduling:** Conduct audits at regular intervals to maintain continuous compliance and improvement.
- **Comprehensive Documentation:** Maintain detailed records of audit findings, recommendations, and corrective actions.
- **Training Auditors:** Ensure auditors are well-versed in ISO 26262 and relevant process standards.

### Practical Example

**Scenario:** Auditing the testing process for an electronic stability control (ESC) system.

- **Preparation:** Develop an audit checklist focusing on test plan development, execution, and result analysis.
- **Execution:** An audit team examines the testing procedures, tools, and documentation.
- **Findings:** Identify gaps in test coverage for certain failure modes.
- **Follow-Up:** Implement additional test cases to cover the identified gaps and schedule a follow-up audit to verify compliance.

## Functional Safety Assessments

### Definition

A **functional safety assessment** evaluates whether a product achieves the desired level of functional safety and provides recommendations based on this evaluation.

### Purpose

- **Validate Safety Achievement:** Confirm that the product meets all functional safety requirements.
- **Provide Recommendations:** Offer insights on acceptance, conditional acceptance, or rejection based on safety compliance.
- **Support Safety Case Development:** Ensure all safety arguments are robust and well-documented.

### Execution Based on Safety Plan

- **Safety Plan Alignment:** Assessments are conducted in accordance with the project's safety plan, ensuring all planned safety activities are adequately evaluated.
- **Comprehensive Evaluation:** Review all aspects of functional safety, including work products, safety measures, processes, and quality aspects.

### Scope of Assessment

- **Work Products:** Documents, code, design artifacts, and other deliverables.
- **Safety Measures:** Techniques and methodologies employed to achieve safety goals.
- **Processes:** Safety-related processes and their effectiveness.
- **Quality Aspects:** Overall quality management and assurance practices.

### Sequence and Timing

- **Sequential Assessments:** Conduct assessments in a sequential manner aligned with project milestones.
- **Early Stage Involvement:** Initiate assessments early in the project lifecycle and continue as the project progresses.
- **ASIL-Based Assessments:** Perform assessments for all Automotive Safety Integrity Levels (ASIL), especially for projects with ASIL C or ASIL D safety goals.

### ASIL Considerations

- **ASIL Definition:** ASIL (Automotive Safety Integrity Level) categorizes the inherent risk in a system based on severity, exposure, and controllability.
- **Assessment Requirements:**
  - **ASIL C/D:** Mandatory assessments for projects with high safety integrity levels.
  - **Lower ASILs:** Recommended or optional assessments depending on project requirements.
  - **Quality Management (QM):** No specific assessment requirements under ISO 26262.

### Assessment Checklist

- **Develop Checklist:** Create a checklist based on ISO 26262 clauses relevant to the assessment.
- **Evaluate Requirements:** Assess each requirement using the checklist to determine compliance.
- **Clause Rating:** Assign ratings based on the fulfillment of objectives derived from each ISO 26262 clause.

### Rating and Evaluation

- **Rating Categories:**
  - **Acceptance:** Full compliance with functional safety requirements.
  - **Conditional Acceptance:** Partial compliance with identified conditions.
  - **Rejection:** Non-compliance with significant safety requirements.

- **Evaluation Process:**
  - **Objective Fulfillment:** Determine if each clause's objectives are met.
  - **Recommendation Formulation:** Provide a clear recommendation based on the evaluation results.

### Best Practices

- **Use Comprehensive Checklists:** Ensure checklists cover all relevant ISO 26262 clauses.
- **Early and Continuous Assessment:** Integrate assessments early and conduct them iteratively as the project evolves.
- **Document Thoroughly:** Maintain detailed records of assessment findings and recommendations.
- **Engage Experienced Assessors:** Utilize assessors with deep knowledge of ISO 26262 and functional safety principles.

### Practical Example

**Scenario:** Assessing the functional safety of a lane-keeping assist system.

- **Preparation:** Develop a checklist based on relevant ISO 26262 clauses.
- **Execution:** Evaluate safety requirements, design, implementation, and testing against the checklist.
- **Findings:** Identify that the sensor fusion algorithm meets ASIL B requirements but requires additional validation for ASIL C.
- **Recommendation:** Conditional acceptance pending additional validation for higher ASIL compliance.

## Best Practices for Confirmation Measures

### Integration into Project Lifecycle

- **Early Planning:** Incorporate confirmation measures into the project plan from the outset.
- **Continuous Monitoring:** Regularly monitor and review confirmation measures throughout the project.
- **Lifecycle Alignment:** Ensure that confirmation measures align with each phase of the product development lifecycle.

### Use of External Partners

- **Enhance Independence:** Engage external partners to provide unbiased reviews and audits.
- **Leverage Expertise:** Utilize external expertise to bolster internal capabilities and perspectives.
- **Facilitate Collaboration:** Foster collaboration between internal and external teams for comprehensive evaluations.

### Documentation and Safety Case

- **Comprehensive Documentation:** Maintain detailed records of all work products, reviews, audits, and assessments.
- **Safety Case Development:** Compile a safety case that integrates all safety arguments, evidence, and assessments.
- **Traceability:** Ensure traceability between safety requirements, work products, and confirmation measures.

### Communication of Results

- **Clear Reporting:** Provide clear and concise reports on review, audit, and assessment findings.
- **Stakeholder Engagement:** Share relevant results with customers, OEMs, and other stakeholders as appropriate.
- **Confidentiality Management:** Handle sensitive information in accordance with contractual and organizational policies.

## Practical Examples

### Example of a Confirmation Review

**Objective:** Verify the completeness and correctness of the hazard analysis document.

- **Preparation:** Create a checklist based on ISO 26262 hazard analysis requirements.
- **Execution:** A cross-functional team reviews the hazard analysis, checking for identified hazards, risk assessments, and mitigation strategies.
- **Findings:** Discover that certain low-severity hazards were not adequately addressed.
- **Outcome:** Request additional analysis and mitigation measures for the identified gaps before approving the document.

### Example of a Functional Safety Audit

**Objective:** Assess the effectiveness of the software development process for an advanced driver-assistance system (ADAS).

- **Preparation:** Develop an audit plan focusing on software development practices, including coding standards, testing procedures, and issue management.
- **Execution:** Conduct the audit by examining process documentation, interviewing team members, and reviewing evidence of process adherence.
- **Findings:** Identify that the static code analysis is performed inconsistently across modules.
- **Outcome:** Recommend standardizing static code analysis procedures and provide training to ensure consistent application.

### Example of a Functional Safety Assessment

**Objective:** Determine if the electronic control unit (ECU) meets ASIL B functional safety requirements.

- **Preparation:** Assemble an assessment team and develop a checklist aligned with ASIL B criteria.
- **Execution:** Evaluate the ECU's design, implementation, testing, and safety measures against the checklist.
- **Findings:** Confirm that most ASIL B requirements are met but highlight the need for improved redundancy in sensor data processing.
- **Outcome:** Provide a recommendation for conditional acceptance, pending the implementation of additional redundancy measures.

## Conclusion

**Confirmation measures** are integral to achieving and maintaining functional safety in automotive systems as per ISO 26262. By systematically conducting confirmation reviews, functional safety audits, and functional safety assessments, organizations can ensure that their products not only comply with safety standards but also embody the highest levels of safety integrity. Adopting best practices, leveraging external expertise, and maintaining thorough documentation are critical to the successful implementation of confirmation measures, ultimately leading to the production of safe and reliable automotive systems.