# Data Categorization in SOVD

Data categorization is a foundational aspect of Service-Oriented Vehicle Diagnostics (SOVD), enabling the organization, retrieval, and management of diagnostic information across modern vehicle systems. With the evolution of vehicle architectures and the introduction of High-Performance Computers (HPCs), categorization strategies are essential to maintain diagnostic consistency and efficiency.

---

## 1. **Overview of SOVD Data Categorization**

Data categorization in SOVD revolves around grouping diagnostic information based on its semantic context and operational needs. It ensures that diagnostics adapt dynamically to diverse scenarios, from in-vehicle assessments to remote troubleshooting. Key categories of data include:

### 1.1 **Identification Data (identData)**
   - **Purpose**: Provides metadata and unique identifiers for components.
   - **Examples**: Vehicle Identification Number (VIN), software versions, and hardware identifiers.
   - **Access**:
     - Query for available identifiers:
       ```http
       GET {base_uri}/components/{component_id}/data?categories=identData
       ```
     - Example Response:
       ```json
       {
         "items": [
           {
             "id": "vin",
             "name": "Vehicle Identification Number",
             "category": "identData",
             "data": "V3CT0RV3H1CL3123"
           }
         ]
       }
       ```

### 1.2 **Current Data (currentData)**
   - **Purpose**: Represents real-time measurements or states.
   - **Examples**: Sensor readings, actuator states.
   - **Use Case**: Monitoring ongoing system performance.

### 1.3 **Stored Data (storedData)**
   - **Purpose**: Encapsulates historical or static data.
   - **Examples**: Fault memory, logs, and configuration parameters.
   - **Usage**: Helps in diagnosing recurring issues or understanding past events.

### 1.4 **System Information (sysInfo)**
   - **Purpose**: Represents data about the overall system health and operational parameters.
   - **Examples**: System uptime, memory utilization, and processing load.

### 1.5 **Aggregated Data**
   - **Purpose**: Combines multiple related data points for holistic analysis.
   - **Examples**: Comprehensive fault summaries or diagnostic snapshots.
   - **Implementation**:
     - Example query to create a data group:
       ```http
       POST {base_uri}/components/engine/data-groups
       {
         "items": ["vin", "swversion"]
       }
       ```

---

## 2. **Methodologies in Data Access and Categorization**

### 2.1 **RESTful API Framework**
SOVD leverages REST principles for uniform access to categorized data:
- **HTTP Methods**: CRUD operations (GET, POST, PUT, DELETE).
- **Data Representation**: JSON format for simplicity and compatibility.
- **Query Parameters**: Key-value pairs for data filtering (e.g., severity levels, status).

### 2.2 **Capability Descriptions**
   - Provides metadata for all supported data categories and operations.
   - Self-descriptive, enabling discovery without external files like ODX.
   - Example query for capabilities:
     ```http
     GET {base_uri}/components/docs?include-schema=true
     ```

### 2.3 **Dynamic and Static Data Handling**
   - **Dynamic Data**: Adapted in real-time based on system state.
   - **Static Data**: Predefined and referenced as needed.

---

## 3. **Practical Applications of Data Categorization**

### 3.1 **Fault Memory Management**
   - Faults are categorized by severity, aggregated status, and associated environmental data.
   - Example query for active faults:
     ```http
     GET {base_uri}/components/engine/faults?status[aggregatedStatus]=active
     ```
   - Example Response:
     ```json
     {
       "items": [
         {
           "code": "123401",
           "display_code": "P123401",
           "fault_name": "O2 Sensor – Circuit Open",
           "severity": 1,
           "status": {
             "aggregatedStatus": "active"
           }
         }
       ]
     }
     ```

### 3.2 **Component Identification**
   - Quick overview of installed components.
   - Example query:
     ```http
     GET {base_uri}/components
     ```
   - Response:
     ```json
     {
       "items": [
         {
           "id": "engine",
           "name": "Engine Controller Unit"
         },
         {
           "id": "door",
           "name": "Door Unit"
         }
       ]
     }
     ```

### 3.3 **Data-Driven Sequences**
   - Diagnostic processes can be automated by leveraging data categories and aggregations.
   - Example: Retrieve a batch of critical data points in a single request.

---

## 4. **Advantages of Data Categorization in SOVD**

1. **Simplified Diagnostics**:
   - Categorized data eliminates the need for external diagnostic descriptions.
   - Streamlines operations through symbolic and human-readable formats.

2. **Enhanced Flexibility**:
   - Adaptive to both static and dynamic system changes.
   - Facilitates use cases from software tracing to real-time monitoring.

3. **Interoperability**:
   - Compatible with modern IT technologies (e.g., JSON, HTTP).
   - Allows integration across platforms and devices, from smartphones to backend servers.

4. **Improved Resource Utilization**:
   - Reduces computational overhead by pre-categorizing and aggregating data.

5. **Future-Proofing**:
   - Supports emerging use cases such as HPC diagnostics and remote software updates.

---

This detailed overview of data categorization in SOVD illustrates its pivotal role in achieving efficient and scalable vehicle diagnostics, ensuring readiness for current and future challenges in automotive technology.