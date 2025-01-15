# Asymmetric Keypair Management

Asymmetric cryptography, supported by AUTOSAR SecOC with modifications, uses **public/private keypairs** to secure in-vehicle communication. Unlike symmetric approaches that rely on a single shared secret, each sender holds a private key to sign outgoing messages, while receivers use the corresponding public key to verify message authenticity. Although more computationally expensive, asymmetric schemes add flexibility and robust security—compromise of one ECU’s private key does not affect others. Below is a comprehensive overview of keypair generation, distribution, and revocation as typically managed in an automotive environment via a Key Management Server (KMS).

---

## Keypair Basics

1. **Public/Private Key Roles**  
   - **Private Key**: Held securely by the sending ECU. Used to generate digital signatures, analogous to a MAC in symmetric systems.  
   - **Public Key**: Distributed to and trusted by receiving ECUs. Used to verify signatures.

2. **SecOC Adaptations**  
   - While SecOC primarily focuses on MAC-based authentication (using symmetric keys), it can be modified to handle asymmetric signatures.  
   - **No Truncated Signatures**: Unlike truncated MACs for bandwidth efficiency, asymmetric signatures generally must be transmitted in full.

3. **Security and Efficiency Trade-Off**  
   - **Benefits**: High compromise isolation (one private key breach does not affect all ECUs) and easier revocation/rotation.  
   - **Drawbacks**: Higher processing overhead; might be unsuitable for high-frequency signals on bandwidth-limited buses.

---

## Generating Keypairs

1. **ECU-Based Key Generation**  
   - Each ECU generates its own keypair (e.g., ECC or RSA) using the Crypto Service Manager (CSM) and secure hardware modules.  
   - This approach prevents centralized storage of private keys, minimizing single points of failure.

2. **Key Management Server (KMS) as Certificate Authority**  
   - Once an ECU generates a public key, it sends it to the KMS for signing.  
   - The KMS acts like a local Certificate Authority (CA), issuing a signature that validates the authenticity of the ECU’s public key.

3. **Default Keypair**  
   - In production, ECUs may ship with a presigned default keypair. The system can later replace or update this default pair once the vehicle is operational.

 **Example (Pseudocode)**
 ```c
 // Example: Keypair Generation via CSM

 bool generateKeypair(uint16_t ecuId, KeyPair *kpOut) {
     // Request key generation from Crypto Service Manager
     bool success = CSM_GenerateAsymmetricKey(
         ALGO_ECC_SECP256R1,  // Example curve
         kpOut-privateKey,
         kpOut-publicKey
     );
     if(!success) {
         return false;
     }

     // (Optional) Submit the new public key to KMS for signing
     success = KMS_RequestPublicKeySigning(ecuId, kpOut-publicKey, kpOut-publicKeySignature);
     return success;
 }
 ```

In this snippet, the ECU calls the **CSM_GenerateAsymmetricKey** function to produce an ECC keypair. It then forwards the public key to the KMS, which returns a signature or certificate attesting to the key’s legitimacy.

---

## Distribution of Public Keys

1. **KMS Broadcast**  
   - After signing the ECU’s public key, the KMS broadcasts this certified key to all other ECUs.  
   - Each ECU maintains a “whitelist” or “trusted store” of known, signed public keys.

2. **Activation**  
   - Once an ECU’s public key is accepted and stored by others, the ECU can begin transmitting signed messages.  
   - Receivers verify signatures by referencing the stored public key in their local whitelist.

3. **Certificate or Key Storage**  
   - Public keys (and their signatures) are stored in non-volatile memory or dedicated secure storage, preventing loss of trust across reboots.  
   - If the system supports X.509 certificates, each ECU might hold a small certificate chain.

---

## Revoking and Updating Keypairs

1. **Revocation Broadcast**  
   - If a private key is compromised or an ECU is deemed rogue, the KMS issues a revocation message (or “blacklist”) for that ECU’s public key.  
   - All ECUs remove or mark the compromised key as invalid to prevent future verifications.

2. **Keypair Regeneration**  
   - The affected ECU generates a new keypair using the Crypto Service Manager.  
   - The KMS signs the new public key and broadcasts it, restoring secure communication for that ECU.

3. **Efficient Isolation**  
   - Only the compromised ECU needs a key refresh. Other ECUs remain unaffected, illustrating the compromise isolation advantage of asymmetric crypto.

 **Example (Pseudocode)**
 ```c
 // Example: Revocation Flow

 bool revokePublicKey(uint8_t *compromisedPublicKey, size_t keyLen) {
     // KMS compiles a blacklist or revocation list
     RevocationMsg revMsg;
     memcpy(revMsg.key, compromisedPublicKey, keyLen);

     // Broadcast to all ECUs
     broadcastRevocationMessage(&revMsg);

     // On each ECU:
     // if( memcmp(localKeyStore[i].publicKey, revMsg.key, keyLen) == 0 ) {
     //     localKeyStore[i].status = KEY_REVOKED;
     // }
     return true;
 }
 ```

In this scenario, each ECU compares the revoked key against its local store. If it finds a match, that key is immediately deactivated.

---

## Summary

**Asymmetric Keypair Management** in an automotive SecOC environment involves:

- **Key Generation**: Each ECU creating its own public/private keypair, typically via hardware-backed cryptographic modules and the CSM.  
- **Certification**: The KMS (acting as a local CA) signs the public key to verify authenticity.  
- **Distribution**: All ECUs receive the signed public keys, updating whitelists or trust stores to recognize valid peers.  
- **Revocation**: Compromised or outdated public keys can be instantly revoked by a KMS broadcast.  
- **Security vs. Performance**: While more secure and granular in key revocation, asymmetric methods incur higher computational costs and do not support truncated signatures.

By adopting these best practices, automotive systems benefit from robust authentication, granular compromise isolation, and clear upgrade paths, further enhancing the security posture of in-vehicle communication.