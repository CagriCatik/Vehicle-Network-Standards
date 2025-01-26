# Sender/Receiver Communication: Data Element Invalidation

This documentation provides a comprehensive understanding of **data element invalidation** in AUTOSAR Sender/Receiver communication. This mechanism ensures robust handling of invalid or erroneous data values, enhancing system reliability and safety.

---

## **1. Overview**

### **What is Data Element Invalidation?**
- A mechanism to mark data elements as **invalid** when the sender detects erroneous or unreliable data, such as when a sensor malfunctions or delivers invalid values.
- The receiver is notified of the invalidation and can react accordingly.

---

## **2. Use Case**

- Typical scenario: A **sensor module** delivers unreliable or incorrect values (e.g., due to a hardware fault or out-of-range conditions).
- Only applicable to **non-queued communication** (`isQueued=false`).

---

## **3. How Data Element Invalidation Works**

### **3.1 Sender-Side Invalidation**
- **Realized by setting an invalid value** for the data element.
- The invalidation is performed using the `Rte_Invalidate_<p>_<d>()` API.

#### Sender-Side API Example:
```c
void Rte_Invalidate_<p>_<d>(void);
```
- **Parameters:**
  - None.
- **Effect:**
  - Marks the specified data element as invalid.

#### Code Example:
```c
Rte_Invalidate_Sensor_Temperature();
```

---

### **3.2 Receiver-Side Reaction**
- **Evaluation of the Return Type:**
  - The receiver evaluates the return value of the corresponding read function to determine if the data is invalid.
  - For direct communication:
    - The return value of `Rte_Read_<p>_<d>()` will be `RTE_E_INVALID`.
  - For buffered communication:
    - The invalidation is checked via `Rte_IStatus_<re>_<p>_<d>()`.

#### Receiver-Side API Examples:
1. **Direct Communication:**
   ```c
   Std_ReturnType Rte_Read_<p>_<d>(OUT <DataType> *data);
   ```
   - Returns `RTE_E_INVALID` if the data is marked as invalid.

2. **Buffered Communication:**
   ```c
   Std_ReturnType Rte_IStatus_<re>_<p>_<d>(void);
   ```
   - Indicates the invalidation status of the data.

#### Code Example (Direct Communication):
```c
int32_t temperature;
Std_ReturnType status = Rte_Read_Sensor_Temperature(&temperature);

if (status == RTE_E_INVALID) {
    // Handle invalid data
}
```

#### Code Example (Buffered Communication):
```c
Std_ReturnType status = Rte_IStatus_SensorModule_Temperature();

if (status == RTE_E_INVALID) {
    // Handle invalid data
}
```

---

## **4. Additional Mechanisms**

### **Activation of Runnables**
- The receiver can activate a Runnable to handle invalid data using the **`DataReceiveErrorEvent`**.

---

## **5. Benefits of Data Element Invalidation**

1. **Error Handling:**
   - Enables detection and appropriate handling of invalid data.
2. **System Safety:**
   - Prevents the propagation of erroneous data values.
3. **Flexibility:**
   - Supports both direct and buffered communication models.

---

## **6. Summary**

Data element invalidation is a crucial feature in AUTOSAR Sender/Receiver communication, providing a structured mechanism to handle erroneous or unreliable data. By marking data as invalid and enabling specific reactions, this approach enhances system safety, reliability, and fault tolerance.

### **Key Takeaways:**
- Use `Rte_Invalidate` on the sender side to mark data as invalid.
- Handle invalid data on the receiver side using `Rte_Read` or `Rte_IStatus`.
- Activate error-handling Runnables with `DataReceiveErrorEvent`.

For detailed configuration and implementation guidelines, refer to the AUTOSAR specification or your system architect.