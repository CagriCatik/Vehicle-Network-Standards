# UDS Simulator

A Python-based simulator for the Unified Diagnostic Services (UDS) protocol. This simulator includes both a **Client (Tester)** and a **Server (ECU)** to mimic the interaction between a diagnostic tool and an Electronic Control Unit (ECU).

## Features
1. **Client (Tester):**
   - Simulates a diagnostic tool sending UDS requests.
   - Constructs and transmits UDS requests.
   - Decodes and handles responses from the server.

2. **Server (ECU):**
   - Simulates an ECU that processes UDS requests.
   - Parses incoming requests.
   - Generates appropriate responses, including both positive and negative responses.

## Supported UDS Services
The UDS Simulator supports the following key UDS services:
- **Diagnostic Session Control (0x10):** Start and control diagnostic sessions.
- **ECU Reset (0x11):** Reset the ECU.
- **Read Data by Identifier (0x22):** Retrieve specific data values from the ECU.
- **Write Data by Identifier (0x2E):** Write specific data values to the ECU.
- **Routine Control (0x31):** Start, stop, or request the results of specific routines.

## Implementation Details

### Server (ECU)
The server mimics an ECU by:
- **Listening for Requests:** A listener waits for incoming UDS requests.
- **Parsing Requests:** Decodes the request to identify the UDS service and its parameters.
- **Generating Responses:** Based on the request, the server sends back a response:
  - **Positive Response:** For example, a successful `Read Data by Identifier (0x22)` request:
    ```
    [0x62, DID, Data]
    ```
  - **Negative Response:** For instance, if the requested DID is invalid:
    ```
    [0x7F, 0x22, NRC]
    ```
    - **NRC (Negative Response Code):** Indicates the error type.
- **Sending Responses:** Responds to the client with the appropriate message.

### Client (Tester)
The client simulates a diagnostic tester by:
- **Constructing Requests:** Builds UDS-compliant requests with Service IDs (SIDs) and parameters.
- **Sending Requests:** Transmits requests to the server.
- **Handling Responses:** Decodes responses from the server to determine the outcome.

### Usage
1. Start the Server or ECU:
   ```bash
   python uds_server.py
   ```
2. Run the Client or Tester:
   ```bash
   python uds_client.py
   ```

## Project Structure
```
uds-simulator/
│
├── uds_client.py            # Implements the UDS client (tester)
├── uds_server.py            # Implements the UDS server (ECU)
└── requirements.txt     # Project dependencies
```