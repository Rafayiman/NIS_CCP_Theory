# Hybrid Cipher System

A Python implementation of a hybrid classical cipher combining Playfair and Vigenere encryption methods with attack simulation capabilities.

## Project Structure

```
hybrid_cipher/
├── __init__.py              # Package initialization
├── constants.py             # Configuration and constants
├── playfair.py              # Playfair cipher implementation
├── vigenere.py              # Vigenere cipher implementation
├── attack_simulator.py      # Cryptanalysis tools
├── reports.py               # Display functions for reports
├── menu.py                  # User interface and menu system
├── main.py                  # Entry point (run from within folder)
└── README.md                # This file
```

## File Descriptions

### `constants.py`
- English letter frequency data
- Playfair alphabet configuration

### `playfair.py`
- **PlayfairCipher** class
- 5x5 matrix generation
- Digraph encryption/decryption

### `vigenere.py`
- **VigenereCipher** class
- Polyalphabetic encryption/decryption
- Key extension functionality

### `attack_simulator.py`
- **AttackSimulator** class
- Frequency analysis attack
- Known-plaintext attack
- Brute force complexity analysis

### `reports.py`
- Algorithm documentation display
- Security analysis report display

### `menu.py`
- **Menu** class
- Interactive user interface
- Command routing and state management

### `main.py` / `run_hybrid_cipher.py`
- Program entry points

## How to Run

### Option 1: Run from project root
```bash
python run_hybrid_cipher.py
```

### Option 2: Run from within the package
```bash
cd hybrid_cipher
python main.py
```

## Features

1. **Playfair Matrix Display** - View the 5x5 substitution matrix
2. **Message Encryption** - Two-layer hybrid encryption
3. **Message Decryption** - Two-layer hybrid decryption
4. **Algorithm Documentation** - Step-by-step algorithm details
5. **Security Analysis** - Comprehensive security report
6. **Frequency Analysis** - Simulate statistical attack
7. **Known-Plaintext Attack** - Simulate cryptanalysis
8. **Brute Force Analysis** - Keyspace complexity analysis

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Usage Example

```python
from hybrid_cipher.playfair import PlayfairCipher
from hybrid_cipher.vigenere import VigenereCipher

# Initialize ciphers
playfair = PlayfairCipher("SECRET")
vigenere = VigenereCipher("KEY")

# Encrypt
step1 = playfair.encrypt("Hello World")
ciphertext = vigenere.encrypt(step1)

# Decrypt
step1_decrypt = vigenere.decrypt(ciphertext)
plaintext = playfair.decrypt(step1_decrypt)
```

## Security Notice

This is an educational implementation of classical ciphers. **Do NOT use for real security purposes.**
Use modern encryption standards (AES, RSA) for actual cryptographic needs.
