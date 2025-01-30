# OTA Architecture and Update Processes in Vehicles

Over-the-Air (OTA) updates have revolutionized the automotive industry by enabling remote software enhancements, reducing the need for physical recalls, and ensuring vehicles remain up-to-date with the latest features and security patches. A robust OTA architecture is essential for managing these updates efficiently, securely, and reliably across diverse vehicle fleets. This chapter provides an in-depth exploration of OTA architecture, detailing the key components, update mechanisms, infrastructure challenges, and technical implementations critical for advanced users and industry stakeholders.

## High-Level Overview

The OTA architecture in automotive systems is a multifaceted framework designed to facilitate seamless software and firmware updates across vehicles. At its core, the architecture integrates cloud-based management systems with in-vehicle embedded devices, ensuring that updates are distributed securely and efficiently. The primary components of this architecture include:

- **Cloud Management System:** Handles data management, update distribution, and cybersecurity.
- **Device Management System:** Oversees programmable variables, update variants, and regional configurations.
- **Telematics Control Unit (TCU):** Acts as the communication bridge between the cloud and vehicle's Electronic Control Units (ECUs).
- **Electronic Control Units (ECUs):** Manage specific vehicle functions and receive updates from the TCU.
- **Security Infrastructure:** Ensures the integrity and authenticity of updates through encryption and secure boot mechanisms.
- **Dashboard Interface:** Provides fleet managers and users with real-time status updates and management controls.

The interplay between these components ensures that each vehicle can receive and apply updates without compromising functionality or security.

## Key Components of OTA Architecture

### Cloud Management System

The Cloud Management System serves as the central hub for all OTA activities. It is responsible for storing, managing, and distributing update packages to vehicles. Key functionalities include:

- **Data Management:** Organizes and stores update packages, vehicle configurations, and user data.
- **Update Distribution:** Manages the rollout of updates, ensuring that they are delivered to the appropriate vehicles based on their configurations and regions.
- **Cybersecurity Management:** Implements security protocols to protect update data during transmission and storage.

*Example: Cloud-Based Update Distribution*

```python
import boto3
from botocore.exceptions import NoCredentialsError

def upload_update_to_s3(file_path, bucket_name, object_name=None):
    s3 = boto3.client('s3')
    try:
        response = s3.upload_file(file_path, bucket_name, object_name or file_path)
        print(f"Upload Successful: {object_name or file_path}")
        return True
    except FileNotFoundError:
        print("The file was not found.")
        return False
    except NoCredentialsError:
        print("Credentials not available.")
        return False

# Example usage
upload_update_to_s3('update_patch.bsdiff', 'ota-updates-bucket', 'firmware/2025/01/update_patch.bsdiff')
```

### Device Management System

The Device Management System is tasked with handling the diverse configurations and variants of vehicles. It ensures that each vehicle receives the correct update tailored to its specific hardware and regional requirements. Key responsibilities include:

- **Programmable Variables Management:** Controls the parameters that can be updated or configured remotely.
- **Variant and Regional Configuration:** Maintains a database of vehicle models, their configurations, and regional compliance requirements.
- **Update Validation:** Ensures that updates are compatible with the vehicle's current software and hardware setup to prevent misconfigurations.

*Example: Vehicle Configuration Database Schema*

```sql
CREATE TABLE VehicleConfigurations (
    VehicleID INT PRIMARY KEY,
    Model VARCHAR(50),
    Year INT,
    ECU_Count INT,
    SoftwareVersion VARCHAR(20),
    Region VARCHAR(10)
);

CREATE TABLE Updates (
    UpdateID INT PRIMARY KEY,
    TargetModel VARCHAR(50),
    TargetYear INT,
    TargetRegion VARCHAR(10),
    UpdateType VARCHAR(20),
    RequiredVersion VARCHAR(20),
    UpdatePackageURL VARCHAR(255)
);
```

### Telematics Control Unit (TCU)

The TCU is the pivotal component that bridges the cloud and the vehicle's internal systems. It manages the reception, validation, and application of OTA updates. Key functions include:

- **Wireless Connectivity:** Supports multiple communication protocols such as 4G/5G, Wi-Fi, Bluetooth, and V2X for data transmission.
- **Update Management:** Handles the download, installation, and potential rollback of updates.
- **Data Encryption:** Ensures that all data transmitted between the cloud and the ECUs is encrypted to prevent unauthorized access.

*Example: TCU Firmware Update Process*

```c
#include "tcu.h"
#include "network.h"
#include "crypto.h"

// Function to initiate TCU firmware update
bool update_tcu_firmware(const char *update_url, const char *public_key_path) {
    uint8_t update_package[MAX_PACKAGE_SIZE];
    size_t package_size;

    // Download update package
    if (!network_download(update_url, update_package, &package_size)) {
        log_error("Failed to download TCU firmware update.");
        return false;
    }

    // Verify update package signature
    if (!verify_signature(update_package, package_size, public_key_path)) {
        log_error("TCU firmware update signature verification failed.");
        return false;
    }

    // Apply firmware update
    if (!apply_firmware(update_package, package_size)) {
        log_error("Failed to apply TCU firmware update.");
        return false;
    }

    log_info("TCU firmware updated successfully.");
    return true;
}
```

### Electronic Control Units (ECUs)

ECUs are specialized modules within the vehicle responsible for managing specific functions such as engine control, braking systems, infotainment, and advanced driver-assistance systems (ADAS). Each ECU operates independently but can be centrally managed through the TCU for OTA updates. Key aspects include:

- **Firmware Management:** Each ECU maintains its own firmware, which can be updated independently to enhance functionality or address security vulnerabilities.
- **Function-Specific Updates:** Allows targeted updates to specific vehicle systems without affecting unrelated components.

*Example: ECU Firmware Update Handler*

```c
#include "ecu.h"
#include "crypto.h"
#include "storage.h"

// Apply firmware update to ECU
bool apply_ecu_firmware_update(uint8_t *firmware_data, size_t firmware_size) {
    // Verify firmware signature
    if (!verify_signature(firmware_data, firmware_size, PUBLIC_KEY)) {
        log_error("Firmware signature verification failed.");
        return false;
    }

    // Write firmware to temporary storage
    if (!storage_write("temp_firmware.bin", firmware_data, firmware_size)) {
        log_error("Failed to write firmware to storage.");
        return false;
    }

    // Validate firmware integrity
    if (!validate_firmware("temp_firmware.bin")) {
        log_error("Firmware validation failed.");
        return false;
    }

    // Replace old firmware with new firmware
    if (!storage_replace("current_firmware.bin", "temp_firmware.bin")) {
        log_error("Failed to replace firmware.");
        return false;
    }

    // Reboot ECU to apply new firmware
    reboot_ecu();

    log_info("ECU firmware updated successfully.");
    return true;
}
```

### Security Infrastructure

Securing OTA updates is paramount to prevent unauthorized access, data breaches, and malicious modifications. The security infrastructure encompasses multiple layers of protection, including:

- **End-to-End Encryption:** Ensures that data transmitted between the cloud and the vehicle remains confidential and tamper-proof.
- **Secure Boot Mechanisms:** Validates the integrity and authenticity of the software before execution to prevent the installation of malicious code.
- **Digital Signatures and Hashes:** Utilizes cryptographic techniques to verify the authenticity and integrity of update packages.

*Example: Encrypted Data Transmission Using AES-256*

```c
#include "crypto.h"
#include "network.h"

#define AES_KEY_SIZE 32
#define AES_IV_SIZE 16

bool encrypt_data_aes256(uint8_t *plaintext, size_t plaintext_len, uint8_t *ciphertext, size_t *ciphertext_len, uint8_t *key, uint8_t *iv) {
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (!ctx) return false;

    if (EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    int len;
    if (EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    *ciphertext_len = len;

    if (EVP_EncryptFinal_ex(ctx, ciphertext + len, &len) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    *ciphertext_len += len;

    EVP_CIPHER_CTX_free(ctx);
    return true;
}

bool transmit_secure_data(uint8_t *data, size_t data_size, const char *destination, uint8_t *key, uint8_t *iv) {
    uint8_t encrypted_data[1024];
    size_t encrypted_size;

    if (!encrypt_data_aes256(data, data_size, encrypted_data, &encrypted_size, key, iv)) {
        log_error("Data encryption failed.");
        return false;
    }

    if (!network_send(encrypted_data, encrypted_size, destination)) {
        log_error("Failed to send encrypted data.");
        return false;
    }

    log_info("Secure data transmitted successfully.");
    return true;
}
```

## OTA Update Process Flow

The OTA update process in vehicles involves a series of coordinated steps that ensure updates are delivered securely and efficiently. The process encompasses initiation, distribution, application, and verification phases, each governed by stringent protocols to maintain vehicle integrity and performance.

### Update Initiation

Updates can be initiated by various triggers, including:

- **Cloud-Initiated Updates:** Scheduled or triggered by manufacturers based on update availability.
- **User-Initiated Updates:** Driven by user requests for specific features or security patches.
- **Automated Triggers:** Based on diagnostic data indicating the need for an update.

*Example: Update Trigger Mechanism*

```python
import requests
import json

def trigger_ota_update(vehicle_id, update_details):
    api_endpoint = "https://ota-automanufacturer.com/update"
    payload = {
        "vehicle_id": vehicle_id,
        "update_details": update_details,
        "trigger_event": "Scheduled_Update"
    }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(api_endpoint, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print(f"OTA update triggered successfully for Vehicle ID: {vehicle_id}")
        return True
    else:
        print(f"Failed to trigger OTA update for Vehicle ID: {vehicle_id}")
        return False

# Example usage
update_info = {
    "version": "3.0.1",
    "description": "Enhanced Autopilot and Security Patch"
}
trigger_ota_update("VIN1234567890", update_info)
```

### Update Package Distribution

Once an update is initiated, the Cloud Management System distributes the update package to the targeted vehicles through the Device Management System. This distribution is tailored based on vehicle configurations, regional requirements, and network availability.

*Example: Differential Update Package Generation*

```bash
# Generate a delta patch between old and new firmware versions
bsdiff old_firmware.bin new_firmware.bin update_patch.bsdiff

# Apply the delta patch to update firmware
bspatch old_firmware.bin updated_firmware.bin update_patch.bsdiff
```

### Encryption and Decryption

To maintain the confidentiality and integrity of update data, all transmissions are encrypted using robust algorithms. Vehicles decrypt the received update packages using secure keys to ensure authenticity.

*Example: Decryption Process on Vehicle Side*

```c
#include "crypto.h"
#include "storage.h"

// Function to decrypt update package
bool decrypt_update_package(uint8_t *encrypted_data, size_t encrypted_size, uint8_t *decrypted_data, size_t *decrypted_size, uint8_t *key, uint8_t *iv) {
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (!ctx) return false;

    if (EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    int len;
    if (EVP_DecryptUpdate(ctx, decrypted_data, &len, encrypted_data, encrypted_size) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    *decrypted_size = len;

    if (EVP_DecryptFinal_ex(ctx, decrypted_data + len, &len) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    *decrypted_size += len;

    EVP_CIPHER_CTX_free(ctx);
    return true;
}

// Example usage
bool process_received_update(uint8_t *received_data, size_t received_size, uint8_t *key, uint8_t *iv) {
    uint8_t decrypted_data[MAX_PACKAGE_SIZE];
    size_t decrypted_size;

    if (!decrypt_update_package(received_data, received_size, decrypted_data, &decrypted_size, key, iv)) {
        log_error("Failed to decrypt update package.");
        return false;
    }

    // Proceed with applying the decrypted update
    return apply_firmware_update(decrypted_data, decrypted_size);
}
```

### Firmware/Application Flashing

After successful decryption and verification, the vehicle's ECUs apply the firmware or application updates. This process involves writing the new software to non-volatile memory and ensuring that the vehicle can reboot with the updated software without issues.

*Example: Atomic Firmware Flashing Process*

```c
#include "bootloader.h"
#include "storage.h"

// Atomic firmware flashing
bool flash_firmware_atomic(uint8_t *firmware_data, size_t firmware_size) {
    // Write to inactive firmware slot
    if (!storage_write("firmware_slot_2.bin", firmware_data, firmware_size)) {
        log_error("Failed to write to inactive firmware slot.");
        return false;
    }

    // Verify firmware integrity
    if (!validate_firmware("firmware_slot_2.bin")) {
        log_error("Firmware integrity validation failed.");
        return false;
    }

    // Switch active firmware slot
    if (!bootloader_switch_slot(2)) {
        log_error("Failed to switch firmware slots.");
        return false;
    }

    // Reboot to apply new firmware
    reboot_system();

    log_info("Firmware flashed atomically and system rebooted successfully.");
    return true;
}
```

### Status Reporting and Dashboard Integration

Post-update, the vehicle communicates the status of the update back to the Cloud Management System. Fleet managers and users can monitor these updates through dashboard interfaces, which display real-time progress, success rates, and any issues encountered during the update process.

*Example: Status Reporting to Dashboard*

```javascript
// JavaScript example using WebSocket for real-time status updates

const socket = new WebSocket('wss://fleetmanager.automanufacturer.com/status');

socket.onopen = function(e) {
  console.log("[open] Connection established");
  socket.send(JSON.stringify({ action: "subscribe", fleet_id: "FLEET123" }));
};

socket.onmessage = function(event) {
  const data = JSON.parse(event.data);
  updateDashboard(data);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    console.log('[close] Connection died');
  }
};

socket.onerror = function(error) {
  console.log(`[error] ${error.message}`);
};

function updateDashboard(data) {
  // Update the fleet management dashboard with new data
  document.getElementById('vehicle-status').innerText = `Vehicle ${data.vehicle_id}: ${data.status}`;
  // Additional UI updates...
}
```

## Technical Challenges in OTA Architecture

Implementing a robust OTA architecture in automotive systems presents several technical challenges that manufacturers must address to ensure the reliability, security, and efficiency of updates. This section explores these challenges and provides technical solutions to mitigate them.

### Device and Data Management

**Challenge:** Managing diverse vehicle configurations and ensuring that each vehicle receives the correct update variant is complex. Misconfigurations or incorrect update deployments can lead to system malfunctions or vehicle inoperability.

**Solution:** Implement a comprehensive Device Management System that maintains an extensive database of vehicle configurations, supports robust version control, and employs automated validation mechanisms to ensure compatibility before deploying updates.

*Example: Automated Compatibility Check*

```python
def is_update_compatible(vehicle_config, update):
    if vehicle_config['Model'] != update['TargetModel']:
        return False
    if vehicle_config['Year'] < update['TargetYear']:
        return False
    if vehicle_config['Region'] != update['TargetRegion']:
        return False
    if vehicle_config['SoftwareVersion'] != update['RequiredVersion']:
        return False
    return True
```

### Update Integrity and Security

**Challenge:** Ensuring the integrity and authenticity of update packages is critical to prevent malicious code injection and unauthorized access.

**Solution:** Utilize multi-layered security protocols, including digital signatures, encryption, and secure boot mechanisms. Regular security audits and adherence to industry standards (e.g., UNECE R156) further strengthen the security posture.

*Example: Multi-Layer Authentication Using JWT*

```python
import jwt
import datetime

# Function to generate JWT token
def generate_jwt(user_id, private_key_path):
    with open(private_key_path, "rb") as key_file:
        private_key = key_file.read()
    
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    
    token = jwt.encode(payload, private_key, algorithm='RS256')
    return token

# Function to verify JWT token
def verify_jwt(token, public_key_path):
    with open(public_key_path, "rb") as key_file:
        public_key = key_file.read()
    
    try:
        decoded = jwt.decode(token, public_key, algorithms=['RS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return None

# Example usage
token = generate_jwt('user123', 'private_key.pem')
decoded = verify_jwt(token, 'public_key.pem')
if decoded:
    print("Authentication successful:", decoded)
else:
    print("Authentication failed.")
```

### Handling Variants and Regional Requirements

**Challenge:** Vehicles across different regions may have varying hardware configurations and regulatory requirements, necessitating tailored updates.

**Solution:** Maintain a detailed registry of vehicle variants and regional regulations within the Device Management System. Utilize conditional logic to deploy region-specific updates and ensure compliance with local standards.

*Example: Conditional Update Deployment Based on Region*

```python
def deploy_update(vehicle, update):
    region = vehicle['Region']
    if region == 'EU':
        if not comply_with_r156(update):
            log_error("Update does not comply with UNECE R156.")
            return False
    elif region == 'USA':
        if not comply_with_nhtsa(update):
            log_error("Update does not comply with NHTSA guidelines.")
            return False
    # Proceed with deployment
    return perform_update(vehicle, update)
```

### Failure Management and Rollbacks

**Challenge:** Interruptions or failures during the update process can render vehicles inoperable or cause system instability.

**Solution:** Incorporate fail-safe mechanisms such as dual firmware partitions (A/B partitioning), automated rollback procedures, and integrity checks to ensure that updates can be safely reverted in case of failures.

*Example: Rollback Procedure Implementation*

```c
#include "storage.h"
#include "crypto.h"

// Rollback to previous firmware version
bool rollback_firmware() {
    uint8_t backup_firmware[MAX_FIRMWARE_SIZE];
    size_t backup_size;

    // Load backup firmware from secure storage
    if (!storage_read("backup_firmware.bin", backup_firmware, &backup_size)) {
        log_error("Failed to read backup firmware.");
        return false;
    }

    // Verify backup firmware integrity
    if (!verify_firmware_integrity(backup_firmware, backup_size)) {
        log_error("Backup firmware integrity check failed.");
        return false;
    }

    // Apply backup firmware
    if (!apply_ecu_firmware_update(backup_firmware, backup_size)) {
        log_error("Failed to apply backup firmware.");
        return false;
    }

    log_info("Firmware rollback successful.");
    return true;
}
```

## Technical Implementations

This section presents detailed technical implementations of key aspects of the OTA architecture, including secure data transmission, update package handling, device management, and status reporting.

### Secure Data Transmission

Ensuring that data transmitted between the cloud and the vehicle is secure is fundamental to the OTA process. This involves encrypting data during transmission and verifying its integrity upon receipt.

*Example: Encrypted Data Transmission Using AES-256*

```c
#include "crypto.h"
#include "network.h"

#define AES_KEY_SIZE 32
#define AES_IV_SIZE 16

bool encrypt_data_aes256(uint8_t *plaintext, size_t plaintext_len, uint8_t *ciphertext, size_t *ciphertext_len, uint8_t *key, uint8_t *iv) {
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (!ctx) return false;

    if (EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    int len;
    if (EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    *ciphertext_len = len;

    if (EVP_EncryptFinal_ex(ctx, ciphertext + len, &len) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    *ciphertext_len += len;

    EVP_CIPHER_CTX_free(ctx);
    return true;
}

bool transmit_secure_data(uint8_t *data, size_t data_size, const char *destination, uint8_t *key, uint8_t *iv) {
    uint8_t encrypted_data[1024];
    size_t encrypted_size;

    if (!encrypt_data_aes256(data, data_size, encrypted_data, &encrypted_size, key, iv)) {
        log_error("Data encryption failed.");
        return false;
    }

    if (!network_send(encrypted_data, encrypted_size, destination)) {
        log_error("Failed to send encrypted data.");
        return false;
    }

    log_info("Secure data transmitted successfully.");
    return true;
}
```

### Update Package Handling

Efficient handling of update packages is essential to minimize bandwidth usage and ensure timely updates. This includes generating differential updates and applying them atomically to prevent partial installations.

*Example: Differential Update Process Using Bsdiff*

```bash
# Generate a delta patch between old and new firmware versions
bsdiff old_firmware.bin new_firmware.bin update_patch.bsdiff

# Apply the delta patch to update firmware
bspatch old_firmware.bin updated_firmware.bin update_patch.bsdiff
```

### Device Management Logic

Managing diverse vehicle configurations and ensuring compatibility of updates requires sophisticated device management logic. Automated systems can validate compatibility and streamline the update process.

*Example: Automated Compatibility Check*

```python
def is_update_compatible(vehicle_config, update):
    if vehicle_config['Model'] != update['TargetModel']:
        return False
    if vehicle_config['Year'] < update['TargetYear']:
        return False
    if vehicle_config['Region'] != update['TargetRegion']:
        return False
    if vehicle_config['SoftwareVersion'] != update['RequiredVersion']:
        return False
    return True
```

### Status Reporting Mechanisms

Real-time status reporting enables fleet managers and users to monitor the progress and success of OTA updates. Integrating status updates into dashboard interfaces provides transparency and control.

*Example: Status Reporting to Dashboard*

```javascript
// JavaScript example using WebSocket for real-time status updates

const socket = new WebSocket('wss://fleetmanager.automanufacturer.com/status');

socket.onopen = function(e) {
  console.log("[open] Connection established");
  socket.send(JSON.stringify({ action: "subscribe", fleet_id: "FLEET123" }));
};

socket.onmessage = function(event) {
  const data = JSON.parse(event.data);
  updateDashboard(data);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    console.log('[close] Connection died');
  }
};

socket.onerror = function(error) {
  console.log(`[error] ${error.message}`);
};

function updateDashboard(data) {
  // Update the fleet management dashboard with new data
  document.getElementById('vehicle-status').innerText = `Vehicle ${data.vehicle_id}: ${data.status}`;
  // Additional UI updates...
}
```

## Conclusion

The OTA architecture in automotive systems is a sophisticated framework that integrates cloud-based management with in-vehicle embedded devices to deliver secure, efficient, and reliable software updates. By leveraging key components such as the Cloud Management System, Device Management System, TCU, ECUs, and robust security infrastructures, manufacturers can ensure that vehicles remain up-to-date with the latest functionalities and security measures.

However, the implementation of OTA systems comes with significant technical challenges, including managing diverse vehicle configurations, ensuring update integrity, handling regional compliance, and mitigating failure risks. Addressing these challenges through advanced technical solutions, comprehensive device management, and stringent security protocols is essential for the successful deployment of OTA services.

As the automotive industry continues to evolve with increasing software complexity and connectivity, the importance of a robust OTA architecture cannot be overstated. Embracing these technologies not only enhances vehicle performance and safety but also significantly improves the overall user experience, driving the future of connected and autonomous vehicles.

# References

- **UNECE Regulation No. 156**: [UNECE R156 Documentation](https://unece.org/transport/documents/2021/03/standards/un-regulation-no-156-software-update-and-software-update)
- **ISO/SAE 21434**: Road Vehicles – Cybersecurity Engineering
- **GDPR**: General Data Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **Uptane Framework**: [Uptane Documentation](https://uptane.github.io/)
- **ISO 26262**: Road Vehicles – Functional Safety
- **OTA Market Reports**: Industry forecasts and market analysis reports (2020–2022)
