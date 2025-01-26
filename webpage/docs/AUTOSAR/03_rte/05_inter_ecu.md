# Sender/Receiver Communication: Inter-ECU

The **Sender/Receiver (S/R)** communication paradigm in AUTOSAR facilitates the asynchronous exchange of data between Software Components (SWCs). When operating across multiple ECUs, this mechanism is supported by the **Runtime Environment (RTE)** and the **Communication Stack (COM)** in the Basic Software (BSW). The provided diagram illustrates the interaction between two SWCs located on different ECUs via Inter-ECU communication.

---

## **1. Key Concepts**

### **Provider and Requestor:**
1. **Provider (P-Port):** The source of the data, responsible for writing the signal.
2. **Require (R-Port):** The consumer of the data, responsible for reading the signal.

### **Components in the Communication Flow:**
- **SWC1 (on ECU1):**
  - Contains the sender Runnable.
  - Writes data via the RTE.
- **SWC2 (on ECU2):**
  - Contains the receiver Runnable.
  - Reads data via the RTE.
- **RTE:** 
  - Handles intra-ECU routing of signals.
  - Integrates with BSW for inter-ECU communication.
- **COM Stack:**
  - Ensures transmission of data across the bus for inter-ECU communication.

---

## **2. Communication Workflow**

### **Step-by-Step Process:**
1. **Sender-Side Communication (ECU1):**
   - SWC1’s Runnable writes data to the P-Port.
   - The RTE processes the write operation and passes the data to the COM module in the BSW.
   - The COM module transmits the signal to the target ECU over the network bus.

   #### Example Sender Code:
   ```c
   Rte_Write_SWC1_Port_Data(signalValue);
   ```

2. **Receiver-Side Communication (ECU2):**
   - The COM module in ECU2 receives the signal and forwards it to the RTE.
   - The RTE routes the data to SWC2’s R-Port.
   - SWC2’s Runnable reads the data from the RTE.

   #### Example Receiver Code:
   ```c
   uint32 signalValue;
   Rte_Read_SWC2_Port_Data(&signalValue);
   ```

---

## **3. Interaction with Basic Software (COM)**

The **COM module** in the BSW is critical for handling inter-ECU communication. It provides functions for signal transmission and reception:
- **Sender Function:** `Com_SendSignal()`
- **Receiver Function:** `Com_ReceiveSignal()`

#### Code Snippets:
- **Sending a Signal (ECU1):**
   ```c
   Com_SendSignal(signalId, &signalValue);
   ```
- **Receiving a Signal (ECU2):**
   ```c
   Com_ReceiveSignal(signalId, &signalValue);
   ```

---

## **4. Data Flow**

| **Action**                     | **Component**          | **Description**                                      |
|--------------------------------|------------------------|------------------------------------------------------|
| **Write Operation**            | SWC1 (Runnable)        | Writes data to the P-Port.                          |
| **Intra-ECU Routing**          | RTE (ECU1)             | Routes data from P-Port to COM stack.               |
| **Signal Transmission**        | COM (BSW, ECU1)        | Transmits the signal over the network.              |
| **Signal Reception**           | COM (BSW, ECU2)        | Receives the signal and passes it to the RTE.       |
| **Intra-ECU Routing**          | RTE (ECU2)             | Routes data to the R-Port of SWC2.                  |
| **Read Operation**             | SWC2 (Runnable)        | Reads the data from the R-Port.                     |

---

## **5. Advantages of Inter-ECU S/R Communication**

1. **Decoupling of SWCs:**
   - SWCs are independent of the underlying network protocol and ECU-specific details.
2. **Scalability:**
   - Supports large-scale systems with multiple ECUs.
3. **Standardized Interfaces:**
   - Ensures compatibility across different AUTOSAR implementations.
4. **Flexibility:**
   - Handles both periodic and event-driven communication seamlessly.

---

## **6. Summary**

The Sender/Receiver communication paradigm in AUTOSAR ensures efficient and scalable data exchange between SWCs across ECUs. By leveraging the RTE and COM stack, AUTOSAR abstracts the complexities of inter-ECU communication, enabling developers to focus on SWC functionality rather than network implementation details.

### **Key Takeaways:**
- Sender (P-Port) writes data, and Receiver (R-Port) reads it.
- The RTE and COM stack facilitate intra- and inter-ECU communication.
- `Rte_Write` and `Rte_Read` functions abstract the complexity of data exchange.

For further elaboration or additional examples, feel free to reach out!