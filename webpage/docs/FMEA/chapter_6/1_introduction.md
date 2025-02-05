# Stage 06: Reevaluating Risk and Visualizing FMEA Rankings

Stage 06 is the final, yet critical, phase in the FMEA process where you reassess the risks after corrective actions have been implemented and then visually present the updated risk rankings. This stage ensures that the FMEA remains a "living document" that accurately reflects the current state of the system or process and helps in ongoing decision-making.

---

## Reevaluating Risk

### Purpose of Reevaluation

After implementing corrective actions or mitigation strategies, it is essential to reevaluate the risk associated with each failure mode. This step confirms whether the actions taken have successfully reduced the likelihood or impact of potential failures.

### Calculating the Resulting Risk Priority Number (RPN)

The RPN remains the key metric for quantifying risk, calculated as:

    - RPN = Severity (S) x Occurrence (O) x Detection (D)

Where:

- **Severity (S):**  
  Reflects the impact of the failure mode on the system, product, or process. Typically remains unchanged unless the nature of the failure has been fundamentally altered.

- **Occurrence (O):**  
  Measures the likelihood that the failure mode will occur. Effective corrective actions should lower this rating.

- **Detection (D):**  
  Indicates the probability that the failure will be detected before it causes harm. Enhanced detection methods should result in a lower detection rating.

### Steps for Reevaluating Risk

1. **Reassess Severity (S):**  
   Determine if any mitigation has reduced the impact of the failure mode. Generally, severity may remain constant if the failure mode itself hasn’t changed.

2. **Reassess Occurrence (O):**  
   Evaluate if preventive measures have reduced the likelihood of the failure mode occurring. A decrease in the occurrence rating suggests effective risk mitigation.

3. **Reassess Detection (D):**  
   Review the effectiveness of any new or improved detection controls. An improved detection process will lower the detection rating.

4. **Compute the New RPN:**  
   Multiply the updated values:
   
    - `New_RPN = S_new × O_new × D_new`

   Compare the new RPN with the original value to gauge the effectiveness of the mitigation strategies.

5. **Decision-Making Based on RPN:**  
   - **If the new RPN is still high:** Additional corrective actions may be needed.
   - **If the new RPN is significantly reduced:** The current risk level is acceptable, but continue to monitor the situation.

---

## Visualizing FMEA Rankings

Visualization is crucial for communicating the results of your FMEA and prioritizing further actions. One effective method for this purpose is the **Spiral Chart**.

### Creating a Spiral Chart

A Spiral Chart is a visual tool that represents the distribution of RPN values and clearly highlights the most critical failure modes.

#### Steps to Create a Spiral Chart:

1. **Organize Failure Modes:**  
   List the failure modes in descending order based on their RPN values. The highest-risk failure mode should be considered first.

2. **Plot the Spiral:**  
   - Begin at the center of the spiral with the most critical failure mode.
   - Continue outward, placing subsequent failure modes in order of decreasing RPN.
   - The distance from the center corresponds to the RPN magnitude, with the highest values closest to the center.

3. **Mark Critical Thresholds:**  
   Use color coding or shading to indicate different risk levels (e.g., high, medium, and low risk). This visual differentiation helps stakeholders quickly identify areas that require immediate attention.

4. **Analyze the Chart:**  
   Look for clusters of high RPNs. Such clusters might indicate systemic issues that need further investigation.

### Advantages of a Spiral Chart

- **Intuitive Ranking:**  
  It provides an easy-to-understand, visual ranking of failure modes based on risk.
  
- **Emphasis on Critical Issues:**  
  The chart naturally highlights the most critical risks at the center, drawing attention to where mitigation efforts should be concentrated.

- **Compact and Effective:**  
  A spiral chart condenses complex information into a clear and engaging visual format, ideal for presentations or summary reports.

---

## Conclusion

Stage 06 is pivotal for ensuring the FMEA remains current and effective. By reevaluating risk and recalculating the RPN, you can verify whether the corrective actions have had the desired impact. The use of visualization tools such as Spiral Charts further enhances the ability to communicate risk levels clearly, facilitating better decision-making and prioritization.

Be sure to document all updates and reevaluations meticulously. If the new RPN suggests that further action is needed, revisit previous stages of the FMEA to implement additional improvements. This continuous cycle of evaluation and improvement is essential for maintaining system reliability and ensuring that risk management remains proactive and effective.

---