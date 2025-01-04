---
sidebar_position: 2
---


# Core Components of SOVD

## **SOVD Gateway**

The SOVD Gateway is a critical entry point for diagnostic communication in the vehicle's ecosystem. Acting as the edge node, it ensures that diagnostic requests from SOVD clients are routed to the appropriate endpoints within the vehicle system. This is achieved through URI-based routing, enabling precise forwarding of requests to specific SOVD components or subcomponents. The Gateway also operates as an HTTP reverse proxy, facilitating seamless communication between external diagnostic clients and internal vehicle systems. Its discovery mechanisms, which include static configuration and dynamic options like multicast DNS (mDNS), ensure flexibility and scalability in identifying internal endpoints​

The SOVD Gateway serves as the edge node of the system, responsible for routing diagnostic requests from SOVD clients to the appropriate internal endpoints. Key functionalities include:
- **Request Routing**: Based on URI patterns, the Gateway forwards requests to the correct SOVD component or subcomponent.
- **Reverse Proxy Functionality**: Operates at the application layer to facilitate communication between external SOVD clients and internal vehicle components.
- **Discovery Mechanisms**: Supports static configuration or dynamic discovery using multicast DNS (mDNS).

---

## **Diagnostic Manager**

The Diagnostic Manager serves as the central coordinator for diagnostic operations within SOVD. It functions as a native SOVD server while maintaining compatibility with traditional UDS standards (ISO 14229-1). By supporting multiple diagnostic server instances, it can independently manage different software clusters within the vehicle. Each server instance operates with a distinct diagnostic address, allowing isolation and targeted diagnostics. This modular design ensures that the Diagnostic Manager can support legacy UDS-based diagnostics while also enabling advanced SOVD-specific functionalities, such as fault management and real-time data access​

The Diagnostic Manager is the central orchestrator for diagnostic services in SOVD, managing both native SOVD functions and legacy UDS integration. Key roles include:
- **SOVD Server Functionality**: Acts as a server to handle diagnostic requests using modern protocols like HTTP/REST.
- **Multiple Server Instances**: Supports independent diagnostic server instances to address different software clusters within the vehicle.
- **UDS Compatibility**: Maintains backward compatibility with ISO 14229-1 services, enabling a smooth transition from UDS to SOVD.

---

## **SOVD to UDS Translation Layer**

The SOVD to UDS Translation Layer bridges the gap between modern SOVD diagnostics and traditional UDS-based systems. It translates high-level SOVD API calls into UDS-compliant requests using mappings defined in ODX files. This layer also interprets UDS responses, converting them into JSON format for SOVD clients. By managing UDS-specific features such as session controls, state management, and security protocols, this component ensures a seamless interaction between the two diagnostic paradigms

This component enables seamless interaction between SOVD clients and traditional UDS-based ECUs. Key features:
- **Request Translation**: Converts SOVD API calls into UDS requests based on predefined ODX mappings.
- **Response Translation**: Interprets UDS responses and converts them into the SOVD-compliant JSON format for client consumption.
- **State Management**: Handles UDS-specific stateful communication, including session controls and security protocols.

---

## **Data Resources**

Data management in SOVD is structured to provide clarity and efficiency. Data is categorized into semantic groups, including current data, identification data, stored data, and system information. This organization simplifies diagnostic queries and improves accessibility. Additionally, SOVD allows the creation of data lists, enabling grouped queries that streamline data retrieval processes. For dynamic needs, periodic and trigger-based data access modes are available, making the system adaptable to various diagnostic scenarios

SOVD organizes data into accessible and well-defined resources:
- **Categorized Data**: Supports categories such as `currentData`, `identData`, `storedData`, and `sysInfo` to streamline diagnostic queries.
- **Data Lists**: Allows for the creation of grouped data sets for batch processing, enhancing diagnostic efficiency.
- **Periodic and Triggered Access**: Enables configurable data access modes, including periodic and event-triggered updates.

---

## **Fault Management**

Fault handling in SOVD has been designed to be more intuitive and accessible than traditional methods. The system provides a standardized API for querying, analyzing, and clearing fault codes. Environmental data, which provides context for fault occurrences, is seamlessly integrated into fault responses. Filtering capabilities, based on severity and status, further enhance the diagnostic process by allowing targeted queries that focus on critical issues

Fault handling in SOVD is streamlined to provide symbolic fault information without the need for external interpretation:
- **Fault Resource**: A standardized API for querying, clearing, and analyzing fault codes.
- **Environmental Data Access**: Provides context for faults, such as environmental data or diagnostic logs.
- **Severity and Status Filters**: Allows filtering based on fault severity and aggregated status.

---

## **Operations Management**

SOVD facilitates the execution and monitoring of vehicle operations through a robust framework. Operations such as actuator control or software functions can be initiated, monitored, and terminated via the SOVD API. To prevent conflicts during critical operations, SOVD includes locking mechanisms, ensuring that resources remain exclusive to the executing client. Additionally, the system supports explicit mode management, allowing precise control over the state of entities within the vehicle

Operations represent executable functions or commands within the vehicle's software or hardware:
- **Execution Control**: Supports starting, monitoring, and terminating operations (e.g., actuator control).
- **Locking Mechanisms**: Ensures exclusive access to resources during critical operations to avoid conflicts between clients.
- **Mode Management**: Manages explicit control over entity states via predefined modes.

---

## **Logging and Traceability**

SOVD provides advanced logging capabilities to support diagnostics and debugging activities. Centralized log management enables the collection of data from various vehicle components, which can be configured for specific levels of detail. The system adheres to industry standards such as RFC 5424 and AUTOSAR diagnostic logs, ensuring compatibility and reliability. Logging configurations can be dynamically adjusted, and bulk data transport is supported for efficient analysis​

SOVD provides comprehensive logging capabilities to support diagnostics and debugging:
- **Centralized Logs**: Collects logs from various vehicle components, supporting bulk data transport.
- **Configuration**: Allows clients to configure logging levels and reset configurations as needed.
- **Standards Compliance**: Adheres to logging standards like RFC 5424 and AUTOSAR diagnostic logs.

---

## **Software Update Management**

The integration of software update management into the SOVD framework highlights its modern approach to diagnostics. A central vehicle component oversees the entire update process, with the SOVD API providing methods to prepare, execute, and monitor updates. This centralized model ensures consistency and control, simplifying the deployment of software patches and enhancements across the vehicle

SOVD integrates software update functionalities into its diagnostic framework:
- **Centralized Updates**: Relies on a central component to manage the update process.
- **Update Lifecycle Management**: Supports preparing, executing, and monitoring software updates.
- **API-Driven**: Provides a standardized API for managing update packages, ensuring consistency across systems.

These core components collectively enable SOVD to provide a unified, efficient, and scalable diagnostic framework for modern vehicles. Each component is designed to bridge traditional diagnostic methods with next-generation software-centric architectures.