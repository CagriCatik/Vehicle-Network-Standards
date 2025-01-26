# Sender/Receiver Communication: Buffered

This documentation details **Buffered Sender/Receiver (S/R) Communication** in AUTOSAR, a mechanism leveraging global buffers to preserve data consistency and ensure deterministic behavior. This approach also uses the **last-is-best semantic** for data transfer.

---

## **1. Key Features of Buffered Communication**

### **1.1 Last-Is-Best Semantic**
- **Definition:** 
  - Similar to direct communication, buffered communication prioritizes the most recent data.
  - Overwrites previous values in the buffer but guarantees consistency during a Runnable's execution.
  
### **1.2 Buffered Data Access**
- Before a Runnable executes, the RTE **copies the most recent value** into a local buffer specific to the Runnable.
- After the Runnable completes execution, the RTE **copies the modified value** (if any) back to the global buffer.

### **1.3 Immutable Data During Execution**
- Data values **cannot change mid-execution** of a Runnable.
- Guarantees a stable and deterministic input for the duration of the Runnable.

---

## **2. Communication Workflow**

### **2.1 Write Operation**
- The sender Runnable invokes the `Rte_IWrite` API to update the global buffer with a new value.
- The RTE ensures this value is consistent across Runnables reading from this buffer.

#### Code Example:
```c
void Rte_IWrite_<r>_<p>_<d>(<DataType> data);
```

### **2.2 Read Operation**
- The receiver Runnable retrieves the latest buffered value using the `Rte_IRead` API.
- The value read is guaranteed not to change during the Runnable's execution.

#### Code Example:
```c
<DataType> Rte_IRead_<r>_<p>_<d>(void);
```

---

## **3. Function Prototypes**

### **Rte_IRead**
```c
<DataType> Rte_IRead_<r>_<p>_<d>(void);
```
- **Returns:** 
  - The most recent value from the RTE buffer.
- **Usage:** 
  - Called within a Runnable to access consistent input data.

#### Example:
```c
int32 temperature = Rte_IRead_TemperatureModule_CurrentTemp();
```

### **Rte_IWrite**
```c
void Rte_IWrite_<r>_<p>_<d>(IN <DataType> data);
```
- **Parameters:**
  - `data`: The value to be written to the RTE buffer.
- **Usage:** 
  - Called within a Runnable to write output data.

#### Example:
```c
Rte_IWrite_ClimateControl_TargetTemp(25);
```

---

## **4. Data Flow**

| **Action**                 | **Component**          | **Description**                                    |
|----------------------------|------------------------|--------------------------------------------------|
| **Buffering Before Execution** | RTE                   | Copies global buffer values to a local buffer for the Runnable. |
| **Read Operation**          | Runnable              | Accesses buffered data during execution via `Rte_IRead`. |
| **Write Operation**         | Runnable              | Updates the local buffer via `Rte_IWrite`.        |
| **Buffering After Execution** | RTE                   | Updates the global buffer with values from the local buffer. |

---

## **5. Advantages of Buffered Communication**

1. **Deterministic Behavior:**
   - Prevents data inconsistencies during Runnable execution.
2. **Stability During Execution:**
   - Ensures input data remains constant, improving reliability.
3. **Data Synchronization:**
   - Buffered updates allow consistent data exchange across multiple Runnables.

---

## **6. Limitations**

1. **Increased Overhead:**
   - The RTE must manage additional copying operations between local and global buffers.
2. **Higher Memory Usage:**
   - Requires dedicated memory for both global and local buffers.

---

## **7. Use Cases**

1. **Control Systems:**
   - Scenarios where deterministic and stable input is essential, such as engine control.
2. **Time-Critical Applications:**
   - Buffered communication ensures predictable behavior during critical operations.

---

## **8. Summary**

Buffered Sender/Receiver Communication in AUTOSAR provides a reliable and deterministic method for exchanging data between SWCs. By leveraging **local and global buffers**, it ensures consistency and stability during Runnable execution.

### **Key Takeaways:**
- Buffered communication uses `Rte_IRead` and `Rte_IWrite` for data access.
- Ensures input data remains stable during execution.
- Best suited for deterministic and time-critical applications.
