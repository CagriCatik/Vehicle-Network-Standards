# Stage 02: Specifying the Occurrence of Failure

In the process of Failure Modes and Effects Analysis , Stage 02 is dedicated to specifying the occurrence of failure. This stage builds upon the foundational understanding developed in Stage 01, where the identification of failure modes and the specification of their severity were discussed. Stage 02 is crucial, as it determines how often a particular failure mode is likely to occur, which directly impacts the prioritization of actions to mitigate risks.

## Overview

Stage 02 of FMEA focuses on the likelihood that each identified failure mode will occur. Building on the previous stage—which identifies failure modes and assigns a severity rating—this phase quantifies how often these failures might happen. By precisely determining the occurrence, engineers can calculate the Risk Priority Number (RPN) more accurately, ensuring that risk mitigation strategies are prioritized based on both the impact and frequency of failure.

---

## Identifying Potential Causes

A rigorous analysis begins by understanding the underlying causes that contribute to each failure mode. Recognizing these causes not only clarifies how a failure may manifest but also informs the subsequent assignment of an occurrence rating. The potential causes typically include:

- **Design Flaws:**  
  Inadequate or erroneous design decisions that can introduce vulnerabilities into the system.

- **Manufacturing Defects:**  
  Errors during the production process such as improper assembly, inconsistent application of materials, or issues with fabrication techniques.

- **Human Error:**  
  Mistakes in operation, maintenance, or assembly, which may stem from inadequate training or oversight.

- **Environmental Factors:**  
  External conditions—like extreme temperature, humidity variations, or chemical exposures—that could compromise system integrity.

- **Wear and Tear:**  
  Natural degradation over time due to usage, aging components, or cumulative stress on materials.

A multidisciplinary approach is recommended to ensure that all relevant factors are considered. Involvement from design engineers, quality assurance teams, manufacturing experts, and field service personnel is critical to comprehensively map out all potential contributing factors.

---

## Determining the Occurrence Rating

Once the potential causes are well understood, the next step is to determine the occurrence rating—a numerical measure representing the probability of failure under specified conditions or timeframes. The process typically follows these steps:

### Factors Influencing the Occurrence Rating

1. **Historical Data:**  
   Empirical evidence such as past incident reports and warranty claims can be invaluable. For example, if historical analysis shows that a specific failure mode occurs in 2% of products within the first year, this data helps anchor the occurrence estimate.

2. **Statistical Analysis:**  
   Reliability engineering tools like Weibull analysis can model the failure distribution over time. Such statistical methods provide insight into how the probability of failure evolves, for instance, indicating a gradual increase from 2% to 4% over a three-year period.

3. **Expert Judgment:**  
   In situations where empirical data is limited, the insights from experienced engineers become essential. Their practical knowledge and comparison to similar systems can help in assigning a rating that reflects realistic failure behavior.

4. **Simulation and Testing:**  
   Controlled tests under simulated environmental or operational conditions can offer a quantifiable failure rate. For instance, environmental testing under high humidity might reveal a 5% failure rate, thereby influencing the overall occurrence rating.

### Rating Scale

The occurrence rating is usually defined on a numerical scale, often ranging from 1 to 10:
- **1:** Failure is extremely unlikely to occur.
- **10:** Failure is almost certain to occur.

Calibrating this scale appropriately is critical. Overestimating the occurrence may lead to unnecessary resource allocation, while underestimating it can leave critical failures unaddressed.

---

## Practical Application: A Case Study

To illustrate these principles, consider a hypothetical case study involving a consumer electronics product—such as a smartphone—with a failure mode related to the touch screen interface.

### Step 1: Identifying Potential Causes

- **Design Flaw:**  
  A touch sensor that is poorly calibrated could lead to inaccurate or unresponsive inputs.

- **Manufacturing Defect:**  
  An inconsistent application of adhesive during assembly may result in the touch screen not being securely affixed to the display.

- **Environmental Factors:**  
  Exposure to high humidity can cause moisture ingress, which degrades the screen’s performance over time.

### Step 2: Determining the Occurrence Rating

In this scenario, multiple data sources contribute to the occurrence assessment:

- **Historical Data:**  
  Warranty claims indicate that approximately 2% of units experience touch screen issues within the first year.

- **Statistical Analysis:**  
  Weibull analysis suggests a gradual increase in failure probability by roughly 0.5% per year, culminating in an estimated 4% failure rate by the third year.

- **Expert Judgment:**  
  Based on previous similar products, engineers might assign a moderate occurrence rating of 3 on a scale of 10.

- **Simulation and Testing:**  
  Environmental tests under conditions of high humidity reveal a 5% failure rate.

After integrating these inputs, a consensus occurrence rating might be established at approximately 4/10. This rating reflects a moderate likelihood of the touch screen failure mode occurring under typical operating conditions.

---

## Conclusion

The process of specifying the occurrence of failure in FMEA is pivotal for developing an accurate risk profile. By thoroughly identifying potential causes and applying a systematic approach to determine the occurrence rating—using historical data, statistical tools, expert judgment, and testing—engineers can effectively prioritize which failure modes require immediate mitigation. This structured approach not only bolsters the scientific integrity of the FMEA process but also ensures that resources are directed toward addressing the most significant risks, thereby enhancing the overall reliability of systems and products.
