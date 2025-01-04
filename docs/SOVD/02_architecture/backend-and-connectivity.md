---
sidebar_position: 6
---


# Backend and Connectivity

## Introduction

Service-Oriented Vehicle Diagnostics (SOVD) represents a paradigm shift in automotive diagnostics, transitioning from static, hardware-centric protocols like Unified Diagnostic Services (UDS) to dynamic, software-driven architectures. Unlike UDS, which primarily relies on predefined diagnostic data structures and byte-level communications, SOVD leverages modern web technologies, including RESTful APIs, JSON, and HTTP. This transformation addresses the complexities of modern vehicles equipped with High-Performance Computers (HPCs) and interconnected electronic control units (ECUs).

Backend and connectivity play a pivotal role in this evolution. In a service-oriented architecture, the backend acts as the central node facilitating communication between diagnostic tools and the vehicle's internal components. Connectivity ensures seamless interaction across local, proximal, and remote diagnostics, extending the lifecycle capabilities of vehicles from development to after-sales support. This document delves into the architectural underpinnings, protocols, and practical applications of backend and connectivity in SOVD.

## SOVD Architecture and Connectivity

### Key Architectural Components

The SOVD architecture is built around several core components designed to abstract vehicle diagnostics into a unified API interface. These components ensure compatibility with both traditional and software-driven systems, enabling backward compatibility with UDS-based diagnostics while embracing future-ready technologies.

The **SOVD Gateway** serves as the primary edge node. It routes incoming diagnostic requests from clients to the appropriate internal SOVD endpoints within the vehicle. By functioning as an HTTP reverse proxy, the gateway abstracts the internal complexity of distributed systems, allowing diagnostic clients to interact with a single, centralized endpoint. Routing is configured using static or dynamic methods, such as multicast DNS (mDNS), to identify and connect with the appropriate subcomponents.

The **Diagnostic Manager** integrates native SOVD capabilities, acting as a central server for diagnostics and fault memory management. While originally developed for UDS, the Diagnostic Manager now facilitates seamless SOVD operations, managing both traditional diagnostics and newer capabilities such as data aggregation and dynamic resource discovery. Each diagnostic server instance, defined within the Diagnostic Manager, represents a distinct software cluster or ECU component.

Another critical component is the **SOVD to UDS Translation Layer**, which bridges the gap between SOVD’s API-driven approach and UDS’s byte-stream protocol. This layer dynamically maps SOVD requests into UDS commands based on predefined ODX definitions, enabling diagnostics across legacy ECUs without significant changes to existing infrastructures.

### Communication Protocols and Standards

SOVD’s reliance on modern IT technologies ensures its robustness and scalability. It employs RESTful APIs built on HTTP/2, offering stateless communication with high reliability and efficiency. JSON serves as the standard data format, enabling structured and human-readable diagnostic data representation.

Security is integral to SOVD’s design. OAuth2 authentication tokens safeguard data access, while Transport Layer Security (TLS) ensures encrypted communication channels. These mechanisms align SOVD with industry standards for secure web-based interactions, reducing vulnerabilities and ensuring compliance with regulatory requirements.

## Backend Functionality in SOVD

The backend in SOVD orchestrates a multitude of diagnostic functionalities, from managing faults to performing software updates. Its design emphasizes versatility, supporting various operational scenarios such as proximity, remote, and in-vehicle diagnostics.

Proximity diagnostics are conducted when direct access to the vehicle is available, such as during manufacturing or routine maintenance. In these scenarios, the backend manages local connections through Ethernet or other high-speed communication interfaces, ensuring rapid data retrieval and fault analysis.

Remote diagnostics extend this capability by integrating cloud-based services. Vehicles communicate diagnostic data to remote servers via wireless technologies such as 4G/5G or Wi-Fi. This setup enables real-time fault monitoring, over-the-air (OTA) software updates, and remote assistance, significantly reducing downtime for complex repair scenarios. In-vehicle diagnostics, meanwhile, rely on local HPCs to manage and process diagnostic data internally, allowing for predictive maintenance and real-time health monitoring without external connectivity.

## Dynamic and Static Data Management

SOVD introduces a revolutionary approach to data management through its self-descriptive API. Traditional UDS systems depend heavily on external diagnostic description files like ODX to interpret data. In contrast, SOVD’s API provides intrinsic descriptions of resources, eliminating the need for external files and reducing setup complexity.

Data within the SOVD framework is categorized into distinct groups based on semantics:
- **IdentData**: Identification information such as vehicle identification numbers (VINs) and software versions.
- **CurrentData**: Real-time operational parameters and measurements.
- **FaultData**: Details about faults, including severity levels and environmental conditions at the time of fault occurrence.

The API allows for dynamic queries, enabling users to retrieve, filter, and aggregate data efficiently. For instance, a technician can request all active fault codes with associated environmental data through a single API call, streamlining the diagnostic process.

## Backend Communication Mechanisms

SOVD’s communication mechanisms emphasize flexibility and efficiency. Multi-client capabilities allow simultaneous access from different users or systems. For example, a vehicle can be diagnosed in a workshop while a remote technical assistance center monitors the same data.

Fault handling is a core functionality of the backend. Users can read, delete, or aggregate fault codes, with the system automatically interpreting and presenting data in a human-readable format. This simplifies troubleshooting and ensures consistency in fault reporting.

Logging and tracing capabilities further enhance diagnostics. The backend can aggregate system logs, enabling comprehensive analyses of operational anomalies. These logs adhere to standardized formats like AUTOSAR’s Diagnostic Log and Trace (DLT) protocol, ensuring compatibility with industry tools.

## Security and Scalability

Security is a cornerstone of SOVD’s backend architecture. OAuth2 authentication tokens manage role-based access, ensuring that only authorized users can perform sensitive diagnostic operations. TLS encryption further secures communication, protecting data integrity and confidentiality during transmission.

Scalability is achieved through modular architecture and dynamic discovery protocols like mDNS. These features allow the backend to adapt to varying diagnostic workloads and support diverse vehicle configurations, from single-ECU systems to multi-HPC setups.

## Examples and Use Cases

Real-world applications of SOVD demonstrate its versatility and efficacy. A workshop technician using SOVD can perform a comprehensive vehicle quick check, retrieving installed ECUs, their software versions, and active faults in a single session. Meanwhile, a remote operator can initiate an OTA software update, monitor its progress, and verify the success of the installation.

The API’s simplicity is exemplified in its operations. For instance, querying the VIN of an engine control unit involves a straightforward HTTP GET request to the relevant endpoint. The response, formatted in JSON, provides the VIN in a human-readable format along with metadata for further analysis.

## Challenges and Future Developments

While SOVD addresses many limitations of traditional diagnostics, transitioning from UDS presents challenges. Compatibility with legacy systems requires robust translation layers, and the adoption of new technologies necessitates training and process changes for diagnostic teams.

Future developments aim to enhance SOVD’s capabilities further. Planned features include periodic data updates, event-based communication, and deeper integration with next-generation platforms like AUTOSAR Adaptive. These advancements will solidify SOVD’s position as the cornerstone of modern vehicle diagnostics.

## Summary and Conclusion

SOVD’s backend and connectivity innovations mark a significant milestone in automotive diagnostics. By integrating modern web technologies, SOVD simplifies data access, enhances security, and supports diverse diagnostic scenarios. Its unified API framework bridges traditional UDS systems with cutting-edge software architectures, ensuring compatibility and future-readiness.

The journey toward fully realized SOVD diagnostics is ongoing, but the foundation laid by its backend and connectivity components is robust and scalable. As vehicles become increasingly complex, SOVD will play an indispensable role in maintaining their functionality and reliability throughout their lifecycle.

