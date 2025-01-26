# Sender/Receiver Communication: Queued

This documentation focuses on **Queued Sender/Receiver Communication** within AUTOSAR, which uses an **event-based semantic** mechanism (`isQueued=true`) for data exchange. This approach relies on receive queues for managing multiple data instances, providing flexibility in scenarios requiring event-based communication.

---

## **1. Key Features of Queued Communication**

### **1.1 Event Semantic**
- **Polling Receive:** 
  - The receiver actively checks the queue for new data.
- **Waiting Receive:** 
  - The receiver blocks and waits for data until a timeout occurs (if defined).
- **Queue Management:**
  - RTE reads data from a **dedicated receive queue**, ensuring ordered processing of events.

### **1.2 Data Consistency**
- Each data instance in the queue is handled as a separate event, ensuring no overwrites or loss of intermediate data values.
- Data remains available in the queue until consumed.

### **1.3 Timeout Handling**
- Waiting receive operations can be configured with a timeout to ensure system responsiveness.
- Enables robust handling of real-time systems where delays in data reception could occur.

---

## **2. Communication Workflow**

### **2.1 Send Operation**
- The sender Runnable uses the `Rte_Send` API to push data into the queue.
- The RTE appends the data to the tail of the queue.

#### Code Example:
```c
Std_ReturnType Rte_Send_<p>_<d>(IN <DataType> data);
```

### **2.2 Receive Operation**
- The receiver Runnable retrieves data from the queue using the `Rte_Receive` API.
- The RTE pops data from the head of the queue.

#### Code Example:
```c
Std_ReturnType Rte_Receive_<p>_<d>(OUT <DataType> *data);
```

---

## **3. Function Prototypes**

### **Rte_Send**
```c
Std_ReturnType Rte_Send_<p>_<d>(IN <DataType> data);
```
- **Parameters:**
  - `data`: The value to send into the queue.
- **Usage:**
  - Called by the sender Runnable to enqueue data for the receiver.
- **Return:**
  - `E_OK`: Successful operation.
  - `E_NOT_OK`: Queue is full, and data cannot be enqueued.

#### Example:
```c
Rte_Send_SensorModule_Temperature(25);
```

### **Rte_Receive**
```c
Std_ReturnType Rte_Receive_<p>_<d>(OUT <DataType> *data);
```
- **Parameters:**
  - `data`: Pointer to the variable where dequeued data will be stored.
- **Usage:**
  - Called by the receiver Runnable to retrieve the next queued data instance.
- **Return:**
  - `E_OK`: Successful operation.
  - `E_NOT_OK`: Queue is empty.

#### Example:
```c
int32_t receivedTemp;
Std_ReturnType status = Rte_Receive_SensorModule_Temperature(&receivedTemp);
```

---

## **4. Advantages of Queued Communication**

1. **Event-Based Communication:**
   - Ideal for systems requiring event-driven data handling.
2. **Lossless Data Transmission:**
   - Prevents overwrites and ensures every data instance is processed.
3. **Scalability:**
   - Multiple data instances can be stored and processed sequentially.

---

## **5. Limitations**

1. **Queue Management Overhead:**
   - Additional memory and processing overhead due to queue handling.
2. **Queue Size Constraints:**
   - Limited by the size of the receive queue; excessive data can cause overflow.

---

## **6. Use Cases**

1. **Sensor Data Streams:**
   - Applications where periodic sensor readings must be processed as discrete events.
2. **Interrupt-Driven Systems:**
   - Event-driven communication for scenarios like button presses or fault notifications.

---

## **7. Summary**

Queued Sender/Receiver Communication in AUTOSAR provides an efficient mechanism for handling **event-based data exchange**. By employing **dedicated queues** for data transmission, this approach ensures lossless communication and supports robust event handling.

### **Key Takeaways:**
- APIs include `Rte_Send` and `Rte_Receive` for enqueueing and dequeueing data.
- Ensures ordered, event-based communication.
- Suitable for scenarios requiring discrete event processing.

This mechanism is indispensable in real-time systems requiring robust and deterministic communication. For further details, refer to the AUTOSAR specification or consult your system architect.