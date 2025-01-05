---
sidebar_position: 1
---


# Reference Architecture

## **Introduction**
Service-Oriented Vehicle Diagnostics (SOVD) is a modern diagnostic paradigm designed to address the increasing complexity of automotive systems, particularly with the introduction of High-Performance Computers (HPCs) and software-driven functionalities. The SOVD standard is developed under the auspices of ASAM and emphasizes flexibility, scalability, and the integration of IT technologies like HTTP/REST and JSON. SOVD complements the Unified Diagnostic Services (UDS) while introducing capabilities to manage software-driven diagnostics dynamically.

---

## **Key Components of SOVD Reference Architecture**

1. **SOVD Gateway**
   - Serves as the central edge node for SOVD requests.
   - Routes requests to respective internal SOVD endpoints based on the URI entity.
   - Acts as an HTTP reverse proxy and supports both static configuration and dynamic discovery using multicast DNS (mDNS).
   - Configured via SOVDGatewayInstantiation in the TPS_Manifest.

2. **Diagnostic Manager**
   - Traditionally handled fault memory and ISO 14229-1 (UDS) diagnostic services.
   - Now acts as an SOVD server, supporting both native SOVD functionalities and translation to UDS where necessary.
   - Represents multiple Diagnostic Server Instances to maintain independence across software clusters.
   - Uses TPS_Manifest for configuration, enabling a seamless blend of UDS and SOVD operations.

3. **SOVD to UDS Translation**
   - Provides translation of SOVD commands to UDS requests and vice versa.
   - Relies on ODX (Open Diagnostic eXchange) definitions for mapping.
   - Acts as an onboard test client, ensuring backward compatibility with UDS-based systems.

4. **Backend Connectivity**
   - Facilitates remote diagnostics by routing SOVD requests through backend systems.
   - Backend connection abstracted as a functional block that integrates seamlessly with SOVD Gateway.
   - Discovery and routing are managed using mDNS and HTTP forwarding.

---

## **SOVD Use Cases**

### **General Use Cases**
SOVD supports a wide range of diagnostic operations across the vehicle lifecycle:
- **Proximity Diagnostics:** Workshop and manufacturing diagnostics, such as end-of-line testing and emission checks.
- **In-Vehicle Diagnostics:** Real-time health monitoring and predictive maintenance.
- **Remote Diagnostics:** Over-the-air software updates, fleet management, and remote assistance.

### **Specific Use Cases**
1. **Fault Management:**
   - Fault memory read and write operations.
   - Retrieval of fault details, including associated environmental data.

2. **Operational Control:**
   - Execution of internal software functions and actuator commands.
   - Monitoring, adjusting, or terminating ongoing operations.

3. **Data Handling:**
   - Access to categorized data such as identification data, system information, and stored records.
   - Support for data grouping and aggregated dataset creation.

4. **Software Updates:**
   - APIs for managing software updates, including preparation, execution, and status tracking.

5. **Logging:**
   - Aggregated log information retrieval.
   - Logging configuration and bulk data transport.

6. **Authorization and Proximity Challenges:**
   - OAuth-based role-specific authorization.
   - Proximity validation to ensure secure operations.

---

## **Technology Stack**

SOVD leverages modern IT standards to deliver its capabilities:
- **HTTP/REST:** Stateless communication protocol for seamless client-server interaction.
- **JSON:** Lightweight data-interchange format for structured diagnostic content.
- **OAuth2:** Secure access control for resource-specific operations.
- **OpenAPI:** Standardized API descriptions for easier implementation and tool integration.

---

## **Benefits of SOVD**

1. **Simplified Diagnostics:**
   - Self-describing APIs eliminate the need for external description files like ODX.
   - Native support for both traditional ECU-based diagnostics and software-driven HPC use cases.

2. **Flexibility and Scalability:**
   - Uniform API for proximity, in-vehicle, and remote diagnostics.
   - Dynamic discovery and configuration capabilities.

3. **Modernized Workflow:**
   - Integration of widely adopted IT standards ensures compatibility with existing development tools and platforms.
   - Support for multi-client access, enabling simultaneous diagnostics from different locations.

4. **Enhanced Use Cases:**
   - Advanced fault analysis with environmental context.
   - Logging and tracing for software-specific diagnostics.
   - OTA updates and dynamic software management.

---

## **Integration with Existing Standards**

SOVD does not aim to replace UDS but rather encapsulates and extends its functionality. The classic UDS protocol remains relevant for traditional ECUs, while SOVD introduces new capabilities for HPCs and software-centric diagnostics. The "Classic Diagnostic Adapter" ensures compatibility, translating SOVD requests for UDS-based systems when required.

---

## **Future Outlook**

As vehicle architectures evolve, SOVD is poised to become a cornerstone of automotive diagnostics. With its focus on modern IT technologies, it enables a seamless transition from hardware-centric to software-driven diagnostics. Upcoming releases will further enhance its capabilities, including support for periodic and event-triggered diagnostics, enriched authorization mechanisms, and extended logging functionalities.

---

## **Conclusion**
Service-Oriented Vehicle Diagnostics represents a significant leap in the evolution of automotive diagnostics. By integrating modern web technologies and supporting a wide array of use cases, SOVD ensures that diagnostics keep pace with the growing complexity of vehicle systems. Its compatibility with legacy protocols like UDS ensures a smooth transition for OEMs and suppliers while unlocking new possibilities for software-driven automotive ecosystems.

