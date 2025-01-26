# Client/Server Communication in AUTOSAR

Client/Server communication is one of the key paradigms in AUTOSAR used to facilitate interaction between Software Components (SWCs). It enables the execution of server-side operations invoked by clients.

## **Overview**

- **Communication**: Follows an n:1 relationship.
- **Server Call**:
  - A client invokes an operation on the server.
  - Operations are implemented as Runnables of the Server SWC.
  - Supports both **synchronous** and **asynchronous** operation calls.
- **Server Runnable Execution**:
  - Executes within:
    - The task context defined by the AUTOSAR Operating System.
    - The client’s task context in the case of direct function calls.

---

## **Synchronous Communication**

In synchronous communication:
- The client is blocked until the server completes execution.
- The server’s response is passed via the `OUT` parameter of the RTE function.

### **Key Features**
1. **Blocking Mechanism**:
   - The client application halts execution until the server completes the requested operation.
2. **RTE API**:
   - Example:
     ```c
     Std_ReturnType Rte_Call_<p>_<o>(
         [IN | IN/OUT | OUT <param_1>], ...);
     ```

### **Example**:
1. **Server Runnable**:
   ```c
   Std_ReturnType GetTime(uint32 *hour, uint32 *minute, uint32 *second);
   ```
2. **RTE Client API**:
   ```c
   Std_ReturnType Rte_Call_<Port>_GetTime(
       uint32 *hour, uint32 *minute, uint32 *second);
   ```

### **Sequence Diagram**:
- The sequence involves:
  - Client Application invoking the server operation.
  - The RTE layer forwarding the request to the server SWC.
  - The server SWC processing the request and sending a response.

---

## **Asynchronous Communication**

In asynchronous communication:
- The client continues execution without waiting for the server's response.
- The server provides results later, which can be fetched by polling or waiting.

### **Key Features**
1. **Non-blocking**:
   - The client is not halted.
2. **Result Retrieval**:
   - Client can retrieve server results using `Rte_Result...` APIs.
3. **Timeout Handling**:
   - Mechanisms to handle delayed or unresponsive servers.

### **RTE API**:
- Result Retrieval:
  ```c
  Std_ReturnType Rte_Result_<p>_<o>(
      [IN/OUT | OUT <param_1>], ...);
  ```

### **Alternative Approach**:
- RTE activates the client Runnable automatically when results are available.

---

## **Practical Use-Cases**

1. **Time Query**:
   - A client SWC queries the current time from a server SWC in a real-time clock module.
   - Synchronous for immediate results, asynchronous if the client needs to perform other tasks.

2. **Sensor-Actuator Coordination**:
   - Asynchronous communication between a client sensor SWC and an actuator SWC ensures non-blocking operation for critical tasks.

---

## **Comparison**

| **Feature**         | **Synchronous**                | **Asynchronous**                     |
|----------------------|---------------------------------|---------------------------------------|
| **Blocking**         | Client waits for server        | Client does not wait for server       |
| **Response Handling**| Immediate                      | Polling or callback-based             |
| **Use Case**         | Critical operations requiring immediate results | Background tasks with less critical timing |

---

### **Conclusion**

Client/Server communication is an integral aspect of AUTOSAR architecture, allowing modular, flexible, and efficient design of automotive software. Whether synchronous or asynchronous, the mechanism ensures robust inter-component interaction tailored to the specific requirements of embedded systems in vehicles.
