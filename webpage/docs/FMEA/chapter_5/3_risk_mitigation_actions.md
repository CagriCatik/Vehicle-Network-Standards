# Recommended Actions for Risk Mitigation

After assigning a Risk Priority Number (RPN) to each identified failure mode in the FMEA process, the next critical step is to determine and implement corrective actions aimed at mitigating these risks. The focus should be on addressing the failure modes with the highest RPN values, as well as those that have particularly high severity ratings, even if their overall RPN is lower.

## What Are Recommended Actions?

Recommended actions are specific steps that your team can take to reduce the risk associated with each failure mode. These actions are designed to lower one or more of the factors contributing to the RPN—namely severity, occurrence, or detectability. The ultimate goal is to reduce the RPN and, thereby, the risk to an acceptable level.

When developing recommended actions, the team should prioritize failure modes with the highest RPN and work through them in descending order. Additionally, failure modes with high severity should be considered with particular attention, even if their RPN is not the highest. This ensures that critical risks are not overlooked due to lower occurrence or detectability ratings.

## How Recommended Actions Influence RPN Components

Each recommended action targets a specific aspect of the RPN:

1. **Reducing Occurrence:**
   - **Objective:** Lower the probability of the failure mode occurring.
   - **Actions:** These may involve redesigning the process or product to eliminate or control the causes of the failure mode. Examples include improving component quality, enhancing process controls, or implementing preventive maintenance strategies.
   - **Impact:** Successful actions here will reduce the occurrence rating (O), directly lowering the RPN.

2. **Improving Detectability:**
   - **Objective:** Increase the likelihood of detecting the failure mode before it causes significant harm.
   - **Actions:** This can be achieved through enhanced process validation, better testing, or more stringent inspection protocols. The goal is to catch the failure mode earlier in the process, ideally before it reaches the customer.
   - **Impact:** Actions that improve detectability will lower the detectability rating (D), reducing the RPN.

3. **Mitigating Severity:**
   - **Objective:** Decrease the impact of the failure mode if it does occur.
   - **Actions:** Severity is typically the most challenging factor to reduce because it often requires a fundamental change in the design or function of the system. Process-level revisions or design changes may be necessary to lessen the consequences of a failure mode.
   - **Impact:** A successful reduction in severity (S) will have a significant impact on the RPN, though such opportunities are generally less common compared to those for occurrence and detectability.

In some cases, there may be no feasible actions available to reduce the RPN further. In such scenarios, it is important to document that no actions are possible, so that future users of the FMEA can see that the failure mode has been thoroughly considered.

## Practical Example: Recommended Actions

Let's consider the previously discussed failure modes and explore the recommended actions for each:

1. **Failure Mode: No Calls**
   - **Recommended Actions:**
     - Implement a voice disaster recovery infrastructure.
     - Add an appropriate notification procedure or escalation matrix.
     - Incorporate awareness training on the escalation matrix for frontline supervisors.
   - **Impact:** These actions primarily aim to reduce the occurrence and detectability ratings by improving system redundancy and response protocols.

2. **Failure Mode: Call Drops**
   - **Recommended Actions:**
     - Conduct a timely review of the escalation matrix.
     - Increase awareness among staff to follow the escalation matrix.
   - **Impact:** These actions focus on improving detectability by ensuring that response procedures are well understood and adhered to.

3. **Failure Mode: Bad Connections**
   - **Recommended Actions:**
     - Supervisors should replace faulty headsets immediately.
     - The voice and telecom team should incorporate network boosters to improve call connectivity.
   - **Impact:** These actions target both the occurrence and detectability ratings by addressing equipment reliability and enhancing network performance.

4. **Failure Mode: Lower Decibel in Voice Quality**
   - **Recommended Actions:**
     - The telephony team should collaborate with the vendor to identify and rectify the root cause of the problem.
     - Implement regular asset maintenance to prevent deterioration of voice quality.
   - **Impact:** These actions are geared towards reducing the occurrence of the issue by ensuring that equipment is well-maintained and that any underlying problems are resolved.

## Implementing and Documenting Actions

Once your team has identified suitable actions, it is essential to document them meticulously in your FMEA template. Each recommended action should include the following details:

- **Description of the Action:** Clearly outline what needs to be done.
- **Responsible Party:** Assign accountability to a specific individual or team.
- **Target Completion Date:** Set a deadline for when the action should be implemented.
- **Expected Outcome:** Specify the anticipated effect on the RPN, including which component(s) (S, O, D) are expected to decrease.

It is crucial to monitor the implementation of these actions and reassess the RPN after they have been completed. This will help ensure that the actions have effectively mitigated the risk and that the system's reliability has improved.

## Activity: Developing Recommended Actions for Your FMEA

Now, it's time to apply this process to your FMEA. Review the failure modes you have identified and calculate their RPNs. For each failure mode, develop and document recommended actions aimed at reducing the RPN. Pay special attention to failure modes with high severity, as mitigating these should be a priority. Remember that while actions affecting severity are rare, they are critical when applicable.

By systematically addressing each failure mode with appropriate actions, you can significantly reduce risks and enhance the overall reliability and safety of your systems.