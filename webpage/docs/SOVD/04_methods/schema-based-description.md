---
sidebar_position: 3
---


# Schema-Based Description

## Overview of Schema-Based Architecture

The schema-based design of SOVD introduces a unified, self-describing API architecture that transforms vehicle diagnostics into a dynamic, scalable, and user-friendly system. The central premise of schema-based SOVD is the decoupling of static configurations like ODX files and enabling diagnostics that dynamically adapt to vehicle changes. Using standardized technologies such as HTTP, REST, and JSON, the schema-based approach offers flexibility, interoperability, and ease of implementation across diverse diagnostic scenarios.

---

## Key Concepts of Schema-Based Design

### 1. **Self-Describing API**
The SOVD schema-based system employs a self-describing API that dynamically reveals diagnostic capabilities. This eliminates dependency on external descriptive files like ODX, as each component and its resources provide introspective descriptions.

- **Discovery Process:** Clients can query the system to discover:
  - Entities and their sub-entities.
  - Associated resources such as fault codes, diagnostic data, and operations.
  - Capabilities and operational states.

  Example Request for Entity Discovery:
  ```http
  GET {base_uri}/components
  ```
  Response:
  ```json
  {
      "items": [
          {"id": "engine", "name": "Engine Control Unit", "href": "{base_uri}/components/engine"}
      ]
  }
  ```
  This structure allows a diagnostic client to interact dynamically with components.

---

### 2. **Resource-Based Architecture**
SOVD organizes its operations around **resources** represented as hierarchical and logical entities. Each resource can be queried or manipulated using RESTful principles. Resources include:
- **Data Resources:** Provide access to real-time (`currentData`), stored (`storedData`), and system information (`sysInfo`).
- **Fault Resources:** Enable fault memory operations such as reading, querying details, and clearing faults.
- **Operation Resources:** Represent software or hardware functions (e.g., actuator controls).

#### Categorization of Resources
SOVD categorizes resources into:
- **Data Categories:**
  - `identData`: Identification information (e.g., VIN, software version).
  - `currentData`: Live system data (e.g., sensor readings).
  - `storedData`: Historical or log-based information.
- **Fault Resources:**
  - Aggregated status (e.g., active faults).
  - Severity-based filters (e.g., critical errors only).

  Example Query for Identification Data:
  ```http
  GET {base_uri}/components/engine/data?categories=identData
  ```
  Response:
  ```json
  {
      "items": [
          {"id": "vin", "name": "Vehicle Identification Number", "category": "identData", "data": "V3CT0RV3H1CL3123"}
      ]
  }
  ```
.

---

### 3. **Dynamic Capability Descriptions**
SOVD provides dynamic descriptions of component capabilities through its schema. These descriptions allow clients to:
- Retrieve a component's operational capabilities.
- Access schema-based metadata that defines resource structure and semantics.
- Integrate offline and online capability descriptions seamlessly using OpenAPI and JSON Schema standards.

#### Example of Capability Discovery
Capability descriptions define available operations, locking mechanisms, and associated modes:
```http
GET {base_uri}/components/docs?include-schema=true
```
Response:
```json
{
    "paths": {
        "/components/engine/faults": {
            "get": {
                "operationId": "getEngineFaults",
                "description": "Retrieve active faults for the engine",
                "parameters": [
                    {"name": "status", "in": "query", "type": "string"}
                ],
                "responses": {
                    "200": {"description": "List of active faults"}
                }
            }
        }
    }
}
```
---

### 4. **Aggregated and Grouped Data Sets**
SOVD enhances efficiency through support for aggregated and grouped data access. For instance:
- **Data Lists:** Predefined collections of diagnostic data (e.g., grouped sensor readings).
- **Fault Groups:** Aggregated faults categorized by severity or functional domains.

Request to Create a Data List:
```http
POST {base_uri}/components/data-lists
{
    "items": [
        { "id": "sensor1", "name": "Temperature Sensor", "data": "30°C" },
        { "id": "sensor2", "name": "Pressure Sensor", "data": "100 kPa" }
    ]
}
```
Response:
```json
{
    "id": "460AB8A5-5971-4693-8626-6287960050AF",
    "status": "Created"
}
```
.

---

## Fault Memory and Control Operations

### Fault Memory Handling
Faults in SOVD are accessible via resource collections. Key operations include:
- Reading active or historical faults.
- Querying environment data tied to specific fault codes.
- Clearing specific or all faults.

Example Request to Retrieve Faults:
```http
GET {base_uri}/components/engine/faults?status[aggregatedStatus]=active
```
Response:
```json
{
    "items": [
        {
            "code": "P123401",
            "fault_name": "O2 Sensor Circuit Open",
            "severity": 2,
            "environment": {"temperature": "70°C", "pressure": "101 kPa"}
        }
    ]
}
```
.

---

### Locking and Operational Control
SOVD includes locking mechanisms to ensure exclusive access to resources during operations. Locks are tied to client tokens and have configurable expiration times.

#### Example Lock Request
```http
POST {base_uri}/components/engine/locks
{
    "lock_expiration": 3600
}
```
Response:
```json
{
    "id": "1234-5678-9012",
    "status": "Locked"
}
```
.

---

## Security and Extensibility

### Authorization
SOVD employs OAuth-based authorization to control access. The API dynamically adjusts its response based on user roles and access permissions.

#### Example of OAuth Token Authorization
Request:
```http
GET {base_uri}/components/engine/data
Authorization: Bearer <OAuth-Token>
```
.

### Extensible Schema Design
SOVD’s schema supports future extensions, allowing:
- Addition of new resources (e.g., HPC-specific diagnostics).
- Integration with advanced IT systems like cloud diagnostics or AI-driven analysis tools.

---

## Benefits of Schema-Based SOVD

1. **Interoperability:** Supports diverse clients without specialized stacks.
2. **Scalability:** Easily integrates new components and operations.
3. **Dynamic Diagnostics:** Adapts to software updates and real-time changes.
4. **Ease of Use:** Intuitive structure leveraging REST and JSON standards.
