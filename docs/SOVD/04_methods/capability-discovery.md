---
sidebar_position: 1
---

# Capability Discovery

---

## Introduction

SOVD, standardized by ASAM (Association for Standardization of Automation and Measuring Systems), represents the evolution of vehicle diagnostics from static, hardware-focused processes (as seen in UDS) to a dynamic, software-driven paradigm. SOVD leverages modern IT technologies, including HTTP, REST, and JSON, to provide a uniform interface for vehicle diagnostics across development, production, and service phases.

### Objectives of Capability Discovery
Capability discovery in SOVD enables:
- Identifying available diagnostic functionalities of components or systems.
- Discovering resources dynamically and efficiently, minimizing the need for preloaded data descriptions.
- Supporting structured and scalable approaches to vehicle diagnostics by leveraging RESTful interactions and self-descriptive APIs.

---

## SOVD Architecture

### Core Components
1. **SOVD Gateway**: Acts as the edge node, routing client requests to corresponding internal endpoints based on URI.
2. **Diagnostic Manager**: Functions as the SOVD server, managing diagnostics for HPCs and classic ECUs, and translating between SOVD and UDS protocols where necessary.
3. **Backend Connectivity**: Facilitates remote access to diagnostic data, abstracting backend connections via HTTP/REST.

### Integration with Existing Standards
- Encapsulation of UDS (ISO 14229-1), enabling the reuse of established protocols for fault codes, routines, and data.
- Alignment with AUTOSAR Adaptive for seamless diagnostics in HPC environments.

---

## Capability Discovery: Implementation

### Overview
Capability discovery provides dynamic access to the vehicle’s diagnostic capabilities. It eliminates reliance on static descriptions like ODX by offering:
- Resource queries via RESTful APIs.
- Self-descriptive data and metadata about available services, components, and functions.

### Methods for Capability Discovery
1. **Resource Identification**:
   - Use the `/components` resource to enumerate all available entities (e.g., ECUs, HPCs, apps).
   - Example:
     ```
     GET {base_uri}/components
     Response:
     {
       "items": [
         { "id": "engine", "name": "Engine Control Unit", "href": "{base_uri}/components/engine" },
         { "id": "brakes", "name": "Brake Control Unit", "href": "{base_uri}/components/brakes" }
       ]
     }
     ```

2. **Data Categorization**:
   - Supports categories such as `currentData`, `identData`, and `storedData`.
   - Filters allow granular queries, e.g., identification data:
     ```
     GET {base_uri}/components/{component_id}/data?categories=identData
     ```

3. **Schema Queries**:
   - OpenAPI specifications facilitate querying capability descriptions online.
   - Developers can generate type-safe libraries for diagnostics, simplifying integration.

---

## Benefits of Capability Discovery

### For Developers
- Eliminates the need for preloaded external descriptions, accelerating diagnostics and updates.
- Enables the use of type-safe libraries generated via OpenAPI, streamlining development.

### For Diagnostic Applications
- Supports simultaneous multi-client access, useful for remote diagnostics and collaboration.
- Integrates seamlessly into modern development environments, such as web-based or cloud systems.

### For End-Users
- Simplifies diagnostic tool interfaces with readable and symbolic data outputs.
- Reduces downtime by enabling parallel in-workshop and remote diagnostics.

---

## Conclusion

Capability discovery in SOVD represents a transformative shift in vehicle diagnostics. By adopting modern IT standards, SOVD facilitates dynamic, scalable, and efficient diagnostic operations. As the automotive industry continues to adopt HPCs and software-centric architectures, the importance of SOVD will only grow, paving the way for innovative applications and seamless integration across diverse platforms.
