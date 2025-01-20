# Logical Link

**Logical Link** refers to the logical communication path established between a diagnostic tester (client) and an ECU (Electronic Control Unit) on a vehicle's network. It is part of the **ISO 14229 standard** and is essential for managing diagnostic sessions.

### Key Characteristics of a Logical Link:
1. **Logical Abstraction**:
   - A logical link is not a physical connection but an abstraction that allows the communication to operate at a higher layer (typically the application layer of the OSI model).

2. **Addressing**:
   - Communication via logical links uses specific addressing schemes:
     - **Physical addressing**: Communication is directed to a specific ECU.
     - **Functional addressing**: Communication is directed to a group of ECUs that may provide a similar function.

3. **Session Management**:
   - Logical links are used to manage **UDS diagnostic sessions**. For example:
     - Default session
     - Extended session
     - Programming session

4. **Routing and Network Layers**:
   - Logical links interact with underlying protocols such as **ISO 15765-2 (CAN Transport Protocol)** or TCP/IP in Ethernet-based networks (e.g., DoIP). These protocols ensure proper routing and segmentation of diagnostic messages.

5. **Multiplexing**:
   - Logical links allow multiple communication streams to coexist on the same physical network by differentiating communication through unique identifiers (e.g., CAN IDs or IP/port pairs).

6. **States and Control**:
   - Logical links have states that ensure proper operation:
     - Open: Communication is active.
     - Closed: Communication is terminated or unavailable.
   - UDS services like **Communication Control (0x28)** can control whether certain communication types are allowed or blocked on a logical link.

7. **Diagnostic Communication Flow**:
   - Logical links handle communication flows such as request/response pairs:
     - The tester sends a diagnostic request (e.g., Read DTCs, Clear Fault Memory).
     - The ECU processes and responds via the same logical link.

### Practical Use in Diagnostics:
- **Establishment**: The tester establishes a logical link by initiating communication and setting up a diagnostic session.
- **Isolation**: Logical links ensure that communication between the tester and a specific ECU is isolated from other network activities.
- **Termination**: Logical links are closed when the session ends, or a timeout occurs.

### Example:
In a CAN network using UDS:
- Tester sends a request with a specific CAN ID (e.g., 0x7E0 for physical addressing).
- The ECU responds using another specific CAN ID (e.g., 0x7E8).
- The communication over these CAN IDs represents a logical link.
