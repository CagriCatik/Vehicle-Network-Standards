# Symmetric Secret Key Management

Effective **symmetric key management** under AUTOSAR SecOC involves generating cryptographically strong keys, distributing them securely to all relevant ECUs, protecting those keys in hardware, and cycling or revoking keys upon suspicion of compromise. Below is a comprehensive overview of the key processes—generation, distribution, storage, and compromise handling—derived from the provided material.

---

## Key Generation

1. **Random Bit Generators (RBG)**  
   - All keys must be generated using approved, high-quality Random Bit Generators.  
   - The randomness of the key is paramount for security; poor RNGs reduce the key space and leave systems vulnerable to brute-force attacks.

2. **Approved Cryptographic Modules (Hardware Security)**  
   - Key generation often occurs in secure hardware modules within ECUs (e.g., Hardware Security Modules or dedicated cryptographic engines).  
   - Software-only generation is discouraged, as it may expose private material to debugging ports or memory dumps.

3. **Compliance with International Standards**  
   - **Europe**: Adhere to ENISA guidelines and recommended key sizes from documents like “Algorithms – key size and parameters.”  
   - **USA**: Ensure compliance with NIST FIPS 140-2 (or latest) for cryptographic module standards.  
   - **AUTOSAR CryIF Module**: Must integrate with hardware that meets these national/international requirements, ensuring uniform compliance across the supply chain.

---

## Key Distribution

1. **Key Management Server (KMS)**  
   - A designated “primary ECU” often serves as the Key Management Server.  
   - This KMS is responsible for generating new keys (or receiving them from a secure backend) and distributing them to all ECUs in the vehicle.

2. **Network-Agnostic Distribution**  
   - Keys are packaged into secure PDUs (encrypted with an older or default key) and transmitted over in-vehicle networks (CAN, Ethernet, etc.).  
   - Distribution can happen during production (in secure environments), or in-field updates if the system design allows over-the-air (OTA) or service-tool-based rekeying.

3. **Default & Updated Keys**  
   - ECUs are shipped with a default “bootstrap” key.  
   - Once live in the vehicle, the KMS uses that bootstrap key to distribute the next operational key. Subsequent key updates can then be encrypted with the most recently activated key.

4. **Key Update Process**  
   - On receiving a key update PDU, each ECU decrypts it using the previously stored key.  
   - The newly extracted key is then stored in secure hardware and marked active.

 **Example (Pseudocode)**
 ```c
 // Simplified snippet showing how an ECU might handle a key update PDU.
 // Assumes the existingKey is used to decrypt the newKey data.

 bool processKeyUpdate(const uint8_t *encKeyData, size_t encKeyLen) {
     uint8_t newKey[KEY_LEN];
     
     // Decrypt with the existing key
     if (!Crypto_Decrypt(existingKey, encKeyData, encKeyLen, newKey)) {
         return false; // Decryption failed
     }

     // Store newKey in secure hardware
     if (!SecureHardware_StoreKey(newKey, KEY_LEN)) {
         return false; // Storing failed
     }

     // Overwrite existing key with new key
     memcpy(existingKey, newKey, KEY_LEN);

     return true;
 }
 ```

---

## Key Storage and Access

1. **Secure On-Chip Hardware**  
   - Keys reside in secure flash or registers inaccessible via debug ports or normal software routines.  
   - Examples of hardware-based security solutions:  
     - **Arm TrustZone®**  
     - **NXP Secure Kinetis®**

2. **Access Layers**  
   - **AUTOSAR SecOC Module** → **Crypto Service Manager (CSM)** → **CryIF Module** → **MCAL (hardware layer)**  
   - This layered architecture ensures cryptographic operations and key manipulations are not exposed to application-level software.

3. **No Software-Only Crypto**  
   - Performing symmetric encryption/decryption or MAC generation solely in unprotected software memory is a security risk; hardware-accelerated or protected operations are strongly preferred.

---

## Key Compromise Handling

Even with robust security measures, keys can become compromised. Common triggers include tampering attempts, unusual clock changes, or repeated false replays indicating malicious activity.

1. **Tamper Event Detection**  
   - Each ECU may run detection algorithms that watch for suspicious operational changes.  
   - Once a threshold of suspicion is reached, the ECU can halt secure communication and log a tamper event in non-volatile memory.

2. **Emergency Procedures**  
   - Vehicle may cease to function safely or remain parked with the engine off.  
   - The compromised key is extracted under authorized service conditions (OEM service shop).  
   - A new key is injected using proprietary, secured workflows.

3. **Per-ECU Isolation**  
   - If one ECU is compromised, it does not necessarily compromise all others (assuming group or per-ECU keys).  
   - That ECU’s bus traffic is distrusted until the cryptographic reset is complete.

---

## Key Lifecycles: Archiving, Destruction, and Recovery

1. **Archiving & Rotation**  
   - Keys often have a predefined lifespan (e.g., 30 days) before rotation.  
   - The Key Management Server distributes fresh keys before the old keys expire.  
   - Typically, a small number of older keys remain in secure storage to support fallback or recovery.

2. **Destroying Old Keys**  
   - Once a key surpasses its validity window, it is securely wiped.  
   - Only the current key and a limited set of previous generation keys are retained (e.g., the last two generations).

3. **Recovering Corrupted Keys**  
   - If an ECU’s flash is corrupted or a hardware fault invalidates a key, the ECU broadcasts a distress signal.  
   - The ECU can attempt to fall back to a previously archived key.  
   - If the fallback also fails, the key is deemed compromised, and the KMS issues a new, valid key to all ECUs.

 **Example (Pseudocode)**
 ```c
 // Example flow illustrating a fallback to a previous key.

 bool recoverCorruptedKey(uint8_t *currentKey, uint8_t *prevKey) {
     if (isKeyValid(prevKey)) {
         // Switch to the previous key
         memcpy(currentKey, prevKey, KEY_LEN);

         // Notify KMS of fallback
         sendDistressMessage("Key Corruption - Fallback");
         return true;
     } 
     return false;
 }
 ```

---

## Summary

Symmetric secret key management under AUTOSAR SecOC spans the entire lifecycle of cryptographic keys:

- **Generation** using standards-compliant random number sources and hardware security modules.  
- **Distribution** via a Key Management Server, leveraging bootstrap or previously active keys to encrypt updates.  
- **Storage & Access** restricted to secure hardware paths and protected software modules (CSM and CryIF).  
- **Compromise Handling** through tamper detection, halting communication, and secure rekeying by trusted parties.  
- **Lifecycle Management** ensuring timely key rotation, secure destruction of old keys, and recovery of corrupted keys.

These coordinated processes, built on robust cryptographic foundations and hardware protections, form the backbone of secure automotive communications—helping maintain vehicle integrity, passenger safety, and compliance with international security standards.