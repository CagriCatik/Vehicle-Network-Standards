# Typical Communication Sequence

This section provides a comprehensive explanation of the Diagnostic over Internet Protocol (DoIP) communication sequence, as used in conjunction with Vector CANoe. The aim is to provide a structured understanding, practical insights, and best practices for implementing and analyzing DoIP sequences.

<img src="../image/ip-adress-assignment.png" alt="Image" style="max-width:75%; display: block; margin: 0 auto;" />

---

## Introduction

DoIP, or Diagnostic over Internet Protocol, is a standardized protocol that enables vehicle diagnostics using IP-based communication. This guide focuses on the theoretical steps involved in a typical DoIP communication sequence, ranging from the initial connection to the handling of diagnostic messages. While the examples are demonstrated using Vector CANoe, the principles and methodologies discussed here are broadly applicable across various DoIP implementations.

---

## Key Components in DoIP Communication

To implement a DoIP communication sequence effectively, certain hardware and software components are essential. The Vector Network Hardware Interface, specifically the VN5610A model, is required to connect the tester to the ECU. Additionally, Vector CANoe serves as the software tool that allows users to simulate, analyze, and test communication sequences in automotive networks. The two main network protocols used during the communication sequence are UDP (User Datagram Protocol) and TCP (Transmission Control Protocol). UDP is primarily used for the initial identification phase, while TCP ensures secure and reliable communication during diagnostic operations.

---

## DoIP Communication Sequence

### Initial Connection

The communication process begins with establishing a connection between the ECU and the tester. This is achieved using the VN5610A hardware interface. Once connected, ensure that the ECU is powered on. This setup forms the foundation for all subsequent communication steps.

### IP Address Assignment

A critical prerequisite for successful communication is the proper configuration of IP addresses. Both the tester and the ECU must have correctly assigned IP addresses. In Vector CANoe, this configuration is performed within the TCP/IP stack settings. For users unfamiliar with this process, detailed tutorials are available that explain the steps to configure the IP stack in CANoe.

### Vehicle Announcement

When the ECU is powered on, it broadcasts a Vehicle Announcement Message three times. The visibility of this message depends on the current status of the network. This announcement is an essential step as it signals the presence of the ECU to the network and prepares the tester for subsequent actions.

### Vehicle Identification Request and Response

Following the vehicle announcement, the tester sends a Vehicle Identification Request. This request can be sent with or without parameters. When sent without parameters, the request functions as a discovery query, essentially asking all devices on the network, "Who’s there?" In response, all ECUs that receive the request will transmit their Vehicle Identification Numbers (VINs) through a Vehicle Identification Response Message.

If the request is sent with specific parameters, such as a VIN or an Entity ID, only the ECU matching the specified criteria will respond, while all others will discard the request. In Vector CANoe, these parameters are configured in the Diagnostic Session settings. To send a parameter-less request, the address field should be left empty. For parameterized requests, the VIN or Entity ID must be explicitly defined.

### TCP Channel Establishment

After the identification phase, the communication transitions from UDP to TCP to ensure secure and reliable data transfer. The tester initiates a TCP handshake, which establishes a dedicated channel for subsequent communication. This step is crucial for maintaining data integrity and synchronization during the diagnostic operations.

### Routing Activation

Once the TCP channel is established, the tester sends a Routing Activation Request to the ECU. This request activates communication with ECUs located behind the gateway or with the gateway itself. For this step to succeed, logical addresses for both the tester and the ECU must be correctly configured. When the ECU receives the Routing Activation Request, it responds with a Routing Activation Response, confirming that the activation was successful. This step ensures seamless communication between all relevant components within the vehicle network.

### Diagnostic Message Exchange

With routing activated, the tester can now send DoIP Diagnostic Messages. Upon receiving these messages, the gateway acknowledges receipt by sending a Diagnostic Message Positive Acknowledgment. The gateway then routes the message to the appropriate ECU within the car’s internal network or processes it internally if required. Once the target ECU processes the diagnostic request, it sends a response back to the gateway, which in turn forwards it to the tester. These diagnostic exchanges can be monitored in real time using the Diagnostic Console in CANoe, providing a clear view of the communication flow and response behavior.

### Closing the TCP Channel

After completing all diagnostic operations, the TCP channel is closed through a process known as TCP Teardown. This step ensures that resources are freed, and the communication session is properly terminated.

---

## Practical Example: Using Vector CANoe for DoIP

To illustrate the process, consider a scenario where an engineer uses Vector CANoe to analyze DoIP communication. The process begins with setting up the hardware by connecting the ECU to the tester via the VN5610A interface and powering on the ECU. The IP addresses are then configured using the TCP/IP stack settings in CANoe. Once configured, the engineer observes the vehicle announcement messages in the Diagnostic Console. The tester sends vehicle identification requests, and the responses are verified for accuracy. Routing is activated by correctly setting logical addresses, after which diagnostic messages are exchanged and analyzed. Finally, the TCP channel is closed to complete the session.

---

## Best Practices

To ensure a successful DoIP implementation, it is vital to follow certain best practices. During the initial setup, verify that the IP addresses are correctly assigned and that the network configuration matches the requirements of the diagnostic tools. During communication, monitor vehicle announcement and diagnostic messages to ensure they align with expected behavior. Properly configure logical addresses for both the tester and ECU to facilitate seamless routing activation. Additionally, log all communication steps to identify and debug any issues that may arise. In scenarios where the ECU fails to respond, implement robust error-handling mechanisms to maintain system reliability.

