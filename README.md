## What is Śārṅga ?
Śārṅga is a encryption and decryption tool. It implements a high-security cipher algorithm designed by Shaivarth, capable of converting plaintext into a secure encrypted binary form and back. Designed and implemented a custom cipher algorithm using fixed-length binary encoding with unique prefixes for lowercase, uppercase, digits, and symbols—aimed at reducing pattern recognition and resisting brute-force attempts.<br><br>
I developed Śārṅga to deepen my understanding of cryptography and security principles. By designing a custom cipher from scratch, I explored how encoding, prefixing, and binary representations can be used to resist common attacks such as brute force and frequency analysis. This hands-on project allowed me to combine theoretical cryptography with practical implementation. The project remains experimental and educational, and my goal is to continue improving it while also benchmarking it against established algorithms to sharpen my research and development skills in cybersecurity.

## Features :

- Encrypt and decrypt text using a proprietary high-security cipher, keeping sensitive information secure.
- Perfect for securing passwords, private messages, or confidential data in binary form.
- Output can be stored safely without worrying about unauthorized access.
- Minimalistic and responsive design for smooth user experience.

## Śārṅga Cipher Algorithm 
**This table represents the structure of my high-security Śārṅga Cipher Algorithm, which combines custom prefixes and binary encoding to encrypt text securely.**

| Prefix | Type            | Bits             | Example        |
|--------|-----------------|------------------|----------------|
| 00     | Lowercase a-z   | 5 bits           | c → 00 00011   |
| 11     | Uppercase A-Z   | 5 bits           | C → 11 00011   |
| 01     | Digits 0-9      | 4 bits           | 5 → 01 0101    |
| 10     | Symbols/Other   | 8 bits (ASCII)   | @ → 10 01000000|

## Why Śārṅga is Secure?

- **Custom Prefixes:** Different prefixes for lowercase letters, uppercase letters, digits, and symbols make pattern recognition extremely difficult.

- **Binary Encoding:** Converts characters into fixed-length binary sequences, making it resistant to guessing attacks.

- **All Character Support:** Encrypts lowercase, uppercase, numbers, and symbols securely.

- **Practical Security:** Encrypted outputs can be stored anywhere without risk of revealing passwords or confidential information.

- **Easy-to-Use:** Minimalistic web interface allows fast encryption/decryption while maintaining high security.

