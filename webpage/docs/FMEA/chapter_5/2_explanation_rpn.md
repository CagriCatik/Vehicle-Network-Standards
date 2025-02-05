# Explanation of Risk Priority Number

## What Is a Risk Priority Number (RPN)?

The Risk Priority Number (RPN) is a quantitative metric used in Failure Modes and Effects Analysis  to assess and prioritize potential failure modes. It is calculated by multiplying three key factors:

- **Severity (S):**  
  - *Definition:* Measures the impact of a failure mode on the system, product, or process.  
  - *Scale:* Typically rated from 1 (least severe) to 10 (most severe).

- **Occurrence (O):**  
  - *Definition:* Represents the likelihood or frequency that a particular failure mode will occur.  
  - *Scale:* Typically rated from 1 (least likely) to 10 (most likely).

- **Detectability (D):**  
  - *Definition:* Evaluates the likelihood that the failure mode will be detected before it causes harm.  
  - *Scale:* Inversely rated on a scale from 1 (almost certain detection) to 10 (detection is almost impossible).

The RPN is calculated using the formula:
   - RPN = S x O x D

The resulting value provides a relative measure of the operational risk associated with each failure mode, with possible values ranging from 1 (lowest risk) to 1000 (highest risk).

---

## The Role of RPN in Risk Management

The RPN plays a central role in prioritizing failure modes and guiding corrective action. Its primary functions include:

- **Prioritization:**  
  High RPN values indicate failure modes that pose significant risks and require immediate attention. They help focus resources and efforts on mitigating the most critical issues.

- **Comprehensive Assessment:**  
  Although the RPN is useful for ranking risks, it is important to consider each of its components—Severity, Occurrence, and Detectability—individually. For example:
  - A failure mode with high severity should be closely examined, even if its overall RPN is low.
  - A low RPN should not lead to complacency; continuous improvement efforts are still necessary.

- **Decision Making:**  
  RPN values assist in making informed decisions about where to implement corrective actions. However, the context of each failure mode, including its potential impact on safety, regulatory compliance, and business objectives, should also be factored into any decisions.

---

## Practical Example of RPN Calculation

To illustrate how RPN is calculated, consider the following examples based on different failure modes:

1. **Failure Mode: No Calls**
   - **Severity (S):** 8  
   - **Occurrence (O):** 7  
   - **Detectability (D):** 3  
   - **RPN Calculation:** 8 x 7 x 3 = 168

2. **Failure Mode: Call Drops**
   - **Severity (S):** 4  
   - **Occurrence (O):** 4  
   - **Detectability (D):** 1  
   - **RPN Calculation:** 4 x 4 x 1 = 16

3. **Failure Mode: Bad Connection**
   - **Severity (S):** 5  
   - **Occurrence (O):** 4  
   - **Detectability (D):** 1  
   - **RPN Calculation:** 5 x 4 x 1 = 20

4. **Failure Mode: Lower Decibel in Voice Quality**
   - **Severity (S):** 3  
   - **Occurrence (O):** 4  
   - **Detectability (D):** 1  
   - **RPN Calculation:** 3 x 4 x 1 = 12

In this example, the failure mode "No Calls" has the highest RPN of 168, indicating that it represents the highest risk and should be prioritized for corrective action.

---

## Activity: Calculating RPN for Your FMEA

To apply these concepts in your own FMEA process:

1. **Identify Failure Modes:**  
   List the potential failure modes for your system or process.

2. **Assign Ratings:**  
   Evaluate and assign a rating (1–10) for Severity, Occurrence, and Detectability for each failure mode based on data, expert judgment, and historical information.

3. **Calculate the RPN:**  
   Use the formula  RPN = S x O x D  to compute the RPN for each failure mode.

4. **Prioritize Actions:**  
   Rank the failure modes by their RPN values and prioritize those with the highest numbers for corrective action.

5. **Review and Adjust:**  
   Continuously monitor the effectiveness of your corrective actions, and recalculate the RPN as needed to ensure that risks are kept within acceptable limits.

---

By understanding and accurately calculating the RPN, you can make informed decisions about where to focus your risk mitigation efforts, ultimately enhancing the quality and safety of your products and processes.