# Understanding the Occurrence Rating in FMEA

The occurrence rating in Failure Modes and Effects Analysis  is a critical metric used to assess the likelihood that a specific failure mode will occur due to a particular cause. This rating is essential for prioritizing risks and determining where to focus mitigation efforts. The occurrence rating is typically expressed on a scale from 1 to 10, with 1 representing the least likely occurrence and 10 representing the highest likelihood.

## Defining the Occurrence Rating

The occurrence rating in FMEA quantifies the frequency or probability that a specific failure will happen due to a defined cause over a given period or number of operations. It serves as a critical metric in prioritizing risk and directing mitigation efforts. Typically, the occurrence rating is expressed on a numerical scale from 1 to 10, where:

- **1**: Extremely unlikely  
  *Probability example:* 1 in 1,000,000 instances.
- **2**: Very low likelihood  
  *Probability example:* 1 in 20,000 instances.
- **4**: Low likelihood  
  *Probability example:* Failure occurs once every 2,000 instances.
- **7**: Moderate likelihood  
  *Probability example:* Failure occurs once every 50 instances.
- **9**: High likelihood  
  *Probability example:* Failure occurs once every 10 instances.
- **10**: Very high likelihood  
  *Probability example:* Failure expected in 1 out of 2 instances.

The assigned rating must be supported by empirical data, historical records, or expert judgment. Precision in this assignment is essential because an inaccurate rating could either lead to the underestimation of risk—leaving critical failure modes unaddressed—or the overestimation of risk—resulting in misallocation of resources.

---

## Factors Influencing Occurrence Rating

Determining the occurrence rating involves integrating multiple sources of data and analysis:

1. **Empirical Data and Historical Records**  
   Past performance data, such as incident reports and quality control statistics, provide a quantitative basis for estimating the likelihood of failure. For example, if historical data indicates that a failure occurs once every 2,000 operations, this directly informs the occurrence rating.

2. **Statistical Analysis**  
   Tools like Weibull analysis are used to model failure probabilities over time. This statistical approach helps predict the trend of failure occurrences and can be particularly useful when data points are sparse.

3. **Expert Judgment**  
   In situations where data is limited, experienced engineers and domain experts use their insights to estimate the probability of occurrence based on similar past experiences and known industry trends.

4. **Simulation and Testing**  
   Controlled experiments, such as environmental or stress tests, provide additional verification of failure likelihood. These tests can simulate worst-case or real-world scenarios to help validate the occurrence rating.

---

## Conditions for Adjusting the Occurrence Rating

Adjustments to the occurrence rating must be made only when supported by direct, verifiable changes to the system. Such changes might include:

- **Process Improvements:**  
  Introducing a new quality control step that demonstrably reduces defect rates.

- **Design Modifications:**  
  Altering a component or system design to eliminate a known failure mode.

- **Operational Changes:**  
  Updating procedures or training protocols to minimize human error.

Speculative assumptions or unverified improvements should not influence the occurrence rating. Only tangible, documented changes can justify a reduction in the likelihood of occurrence, ensuring that the FMEA remains an objective and reliable risk management tool.

---

## Example Application: Call Center Case Study

To illustrate the application of occurrence ratings, consider a call center environment with several identified failure modes:

### Failure Mode: No Calls
- **Occurrence Rating:** 7  
- **Explanation:**  
  Data indicates that the failure occurs once in every 50 calls. This moderate frequency is significant enough to potentially impact operations if not mitigated.

### Failure Mode: Call Drops
- **Occurrence Rating:** 2  
- **Explanation:**  
  This failure is rare, with an occurrence rate of one in every 20,000 calls, suggesting that while the issue exists, it is not a critical risk under current operational conditions.

### Failure Mode: Bad Connection or Static
- **Occurrence Rating:** 4  
- **Explanation:**  
  Occurring once every 2,000 calls, this failure mode presents a low but noticeable risk, warranting monitoring and potential corrective measures.

### Failure Mode: Lower Decibel in Voice Quality
- **Occurrence Rating:** 4  
- **Explanation:**  
  Similar to bad connection issues, this failure mode is noted at a frequency of once every 2,000 calls, signifying a level of risk that requires attention.

In each case, the occurrence rating is determined by a combination of statistical data, historical performance, and expert judgment. These ratings guide the prioritization of risk mitigation efforts, ensuring that resources are directed toward the most impactful failure modes.

---

## Conclusion

The occurrence rating is a pivotal element of the FMEA process, providing a quantifiable measure of the likelihood that a failure mode will occur. By leveraging empirical data, statistical analyses, expert insights, and rigorous testing, engineers can accurately assign occurrence ratings on a scale of 1 to 10. This quantification not only facilitates the effective prioritization of risks but also ensures that any adjustments to the rating are made only when supported by verifiable changes in the process, design, or operational protocols. Ultimately, an accurate occurrence rating enhances the overall effectiveness of the FMEA, leading to better risk management and improved system reliability.

---