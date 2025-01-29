# Vehicle State in Over-the-Air (OTA) Updates

## Importance of Vehicle Preconditions

In the context of OTA updates, vehicle preconditions play a crucial role in ensuring a seamless update process that does not compromise user experience or vehicle safety. While updates can be initiated remotely from the OEM backend, specific criteria must be met before an update can proceed. Failure conditions must also be predefined to prevent issues during the update process.

The update mechanism should prioritize the driver's convenience, ensuring minimal disruption. Based on their impact on vehicle operability, OTA updates can be categorized into two types:

1. **Drivable Updates**
2. **Non-Drivable Updates**

---

## Drivable Updates

Drivable updates refer to software updates that can be performed in the background without affecting the vehicle's functionality. These updates typically involve non-critical systems such as the infotainment system, where the vehicle remains operational throughout the process.

### Characteristics of Drivable Updates
- Updates occur seamlessly without interrupting vehicle functions.
- Notifications are provided to the driver, but they do not require immediate action.
- Examples include:
  - Bug fixes in the infotainment system.
  - Minor updates to UI/UX elements in vehicle displays.

### Execution Flow of Drivable Updates
1. **Automatic Update Enabled:** If the automatic update setting is enabled, the update can be pushed directly to the infotainment system and installed without user intervention. A notification is then displayed confirming the update.
2. **Automatic Update Disabled:** If automatic updates are disabled, the system prompts the driver via a message on the vehicle touchscreen or an app notification, requiring manual approval.
3. **Installation Process:** The update downloads in the background and installs either immediately or upon system restart.
4. **Failure Handling:** If the update fails, the system automatically rolls back to the previous software version to prevent functional issues.

---

## Non-Drivable Updates

Non-drivable updates involve critical software components where the vehicle must remain stationary during the update process. These updates typically target essential vehicle functions, such as the engine control unit (ECU) or battery management system (BMS), where an interruption could lead to severe malfunctions.

### Characteristics of Non-Drivable Updates
- The vehicle cannot be operated during the update process.
- Updates often involve firmware replacements that require system resets.
- Predefined conditions must be met before initiating the update to ensure vehicle safety.

### Examples of Non-Drivable Updates
- **Engine Management System (EMS) Updates:** Updating the engine ECU, requiring the vehicle to remain off to prevent operational conflicts.
- **Firmware Updates for ECUs:** These updates can take 15-30 minutes, making it necessary to prevent vehicle usage during the update.
- **Battery Management System (BMS) Updates:** Ensuring proper battery calibration and state-of-charge consistency, particularly in electric vehicles (EVs).

---

## Preconditions for Non-Drivable Updates

To maintain safety and prevent update failures, non-drivable updates require adherence to the following preconditions:

### 1. Vehicle Should Not Be in Operation
- The vehicle must remain stationary and switched off during the update.
- If the vehicle is inadvertently started during the update, the process is aborted based on the severity of the update.
- Some ECU updates may be irreversible, requiring driver confirmation before initiation.

### 2. Power Supply and Battery Health
- The vehicle must have sufficient battery charge to complete the update process.
- If the battery is low, the update is either postponed or prompts the user to charge the vehicle.
- In electric vehicles (EVs), updates should not be performed while charging.

### 3. No Active Fault Codes on ECUs
- The system should be in a fault-free state before initiating an update.
- If any active faults are detected, remote diagnostics may be required to assess update feasibility.

### 4. Unaltered Vehicle Configuration
- The vehicle should remain in its original manufacturing condition.
- Any user modifications, such as disconnected or altered wiring, could disrupt the OTA process and require diagnostics before proceeding.

### 5. Secure Communication with OEM Backend
- The vehicle must establish a stable connection with the OEM backend to verify update integrity and monitor progress.
- Update progress and failures should be logged and reported to the OEM backend for traceability and analysis.

---

## Failure Strategies in OTA Updates

To handle unexpected failures during OTA updates, robust failure management strategies must be implemented:

1. **Rollback Mechanism:**
   - If an update fails, the system automatically reverts to the previous stable version.
   - The rollback process ensures the vehicle remains functional even if an update is unsuccessful.

2. **Driver Notifications and Diagnostics:**
   - If an update fails due to precondition violations (e.g., low battery, active faults), a message is displayed to the driver.
   - The system may initiate a remote diagnostic session to determine the root cause of the failure.

3. **OEM Backend Monitoring:**
   - All update attempts and their statuses are logged in the OEM backend.
   - Failed updates trigger alerts for further analysis and corrective actions.

4. **User Confirmation for Critical Updates:**
   - For non-drivable updates, explicit user confirmation is required before proceeding.
   - The system may request scheduling to minimize user inconvenience.

---

## Conclusion

The effectiveness of OTA updates depends on stringent preconditions and robust failure management strategies. By classifying updates into **drivable** and **non-drivable** categories, OEMs can ensure that software updates enhance vehicle performance without compromising user experience. Careful scheduling, remote diagnostics, and rollback mechanisms contribute to a seamless and reliable update process, ensuring vehicle safety and operational integrity.