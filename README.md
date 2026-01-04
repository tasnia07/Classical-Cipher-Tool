# Classical Cipher Tool

A comprehensive encryption/decryption tool implementing four classical cryptographic ciphers with both a modern graphical user interface (GUI) and command-line interface (CLI). Includes a Hill Cipher cracker for known plaintext attacks.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [User Guide](#user-guide)
  - [GUI Application](#gui-application)
  - [Command Line Interface](#command-line-interface)
  - [Hill Cipher Cracker](#hill-cipher-cracker)
- [Cipher Reference](#cipher-reference)
- [Architecture](#architecture)
- [Development](#development)

---

## Features

### Supported Ciphers

| Cipher         | Type         | Key Format             | Security Level |
| -------------- | ------------ | ---------------------- | -------------- |
| **Caesar**     | Substitution | Single number (0-25)   | ★☆☆☆☆          |
| **Affine**     | Substitution | Two numbers (a,b)      | ★★☆☆☆          |
| **Playfair**   | Digraph      | Keyword                | ★★★☆☆          |
| **Hill (2×2)** | Matrix       | Four numbers (a,b,c,d) | ★★★★☆          |

### Application Features

- **Modern Dark Theme** - Easy on the eyes, professional appearance
- **Dual Interface** - GUI for ease of use, CLI for scripting
- **Real-time Validation** - Instant feedback on key validity
- **History Tracking** - Review past operations
- **Import/Export** - Load text from files, save results
- **Hill Cipher Cracker** - Recover keys using known plaintext attack
- **Keyboard Shortcuts** - Fast operation for power users

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download

```bash
git clone https://github.com/yourusername/cipher.git
cd cipher
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install numpy PyQt6
```

### Step 3: Verify Installation

```bash
python run_gui.py --help
```

---

## Quick Start

### Launch GUI (Recommended)

```bash
python run_gui.py
```

### Launch CLI

```bash
python main.py
```

### Crack a Hill Cipher Key

```bash
python cracker.py -p "hello" -c "hiozhn"
```

---

## User Guide

### GUI Application

#### Starting the Application

```bash
python run_gui.py          # Normal mode
python run_gui.py --crack  # Open directly to Cracker tab
```

#### Cipher Tab - Encrypt/Decrypt

1. **Select a Cipher** - Click on one of the four cipher cards on the right panel
2. **Choose Mode** - Click "Encrypt" or "Decrypt" button
3. **Enter Text** - Type or paste your text in the input area
4. **Enter Key** - Provide the encryption key (format shown below input)
5. **Execute** - Click "Encrypt Now" or "Decrypt Now"
6. **View Result** - Output appears in the result area

#### Crack Tab - Hill Cipher Cracker

1. **Enter Known Plaintext** - The original text you know
2. **Enter Ciphertext** - The encrypted version of that text
3. **Click "Crack Key"** - The tool will recover the 2×2 key matrix
4. **Use the Key** - Decrypt other messages encrypted with the same key

#### Keyboard Shortcuts

| Shortcut | Action                |
| -------- | --------------------- |
| `Ctrl+1` | Switch to Cipher tab  |
| `Ctrl+2` | Switch to Crack tab   |
| `Ctrl+H` | View history          |
| `Ctrl+L` | Clear all fields      |
| `Ctrl+W` | Swap input/output     |
| `Ctrl+O` | Import text from file |
| `Ctrl+S` | Export result to file |

---

### Command Line Interface

The CLI provides an interactive menu-driven interface:

```bash
python main.py
```

#### Menu Navigation

```
============================================================
               CLASSICAL CIPHER TOOL
============================================================

[SELECT CIPHER]
1. Caesar Cipher
2. Affine Cipher
3. Playfair Cipher
4. Hill Cipher (2x2)
5. Exit

Enter your choice (1-5):
```

---

### Hill Cipher Cracker

The standalone cracker tool recovers Hill cipher keys from known plaintext-ciphertext pairs.

#### Command Line Usage

```bash
# Basic crack
python cracker.py -p "plaintext" -c "ciphertext"

# Crack and decrypt additional text
python cracker.py -p "hello" -c "hiozhn" -d "moreciphertext"

# Analyze plaintext for invertibility
python cracker.py -a "hello"

# Interactive mode
python cracker.py -i
```

#### Example Session

```bash
$ python cracker.py -p "attack" -c "frfmkc"

============================================================
  HILL CIPHER KNOWN PLAINTEXT ATTACK (2x2)
============================================================

Plaintext:  attack
Ciphertext: frfmkc

==================================================
CRACKED KEY MATRIX (2x2):
==================================================
┌───────────────┐
│     3      3 │
│     2      5 │
└───────────────┘
Determinant (mod 26): 9
Key as flat array: [3,3,2,5]
==================================================

Verification - Decrypted: ATTACK
```

---

## Cipher Reference

### Caesar Cipher

Shifts each letter by a fixed amount.

| Parameter   | Description          |
| ----------- | -------------------- |
| **Key**     | Integer from 0 to 25 |
| **Example** | Key=3: A→D, B→E, C→F |

```
Plaintext:  HELLO
Key:        3
Ciphertext: KHOOR
```

### Affine Cipher

Applies the formula: `E(x) = (ax + b) mod 26`

| Parameter | Description                                                     |
| --------- | --------------------------------------------------------------- |
| **Key**   | Two integers: a,b                                               |
| **a**     | Must be coprime with 26 (valid: 1,3,5,7,9,11,15,17,19,21,23,25) |
| **b**     | Any integer 0-25                                                |

```
Plaintext:  HELLO
Key:        5,8
Ciphertext: RCLLA
```

### Playfair Cipher

Uses a 5×5 key matrix for digraph substitution.

| Parameter | Description           |
| --------- | --------------------- |
| **Key**   | Any keyword or phrase |
| **Note**  | J is treated as I     |

```
Plaintext:  HELLO
Key:        MONARCHY
Ciphertext: CFSUPM
```

### Hill Cipher (2×2)

Matrix multiplication cipher using a 2×2 key matrix.

| Parameter       | Description                                         |
| --------------- | --------------------------------------------------- |
| **Key**         | Four integers: a,b,c,d forming matrix [[a,b],[c,d]] |
| **Requirement** | det(K) mod 26 must be coprime with 26               |

```
Plaintext:  HELLO
Key:        3,3,2,5  →  [[3,3],[2,5]]
Ciphertext: HIOZHN
```

**Valid Key Examples:**

- `3,3,2,5` (det=9) ✓
- `5,8,17,3` (det=7) ✓
- `7,8,11,11` (det=1) ✓

**Invalid Key Examples:**

- `2,4,3,6` (det=0) ✗
- `2,3,4,5` (det=24, gcd(24,26)=2) ✗

---

## Architecture

### Project Structure

```
cipher/
├── main.py                  # CLI entry point
├── run_gui.py               # GUI entry point
├── cracker.py               # Hill cipher cracker (standalone)
├── requirements.txt         # Python dependencies
├── README.md                # This file
│
├── ciphers/                 # Cipher implementations
│   ├── __init__.py
│   ├── caesar_cipher.py     # Caesar cipher
│   ├── affine_cipher.py     # Affine cipher
│   ├── playfair_cipher.py   # Playfair cipher
│   └── hill_cipher.py       # Hill cipher
│
├── cipher_gui/              # GUI application package
│   ├── __init__.py          # Package init (version info)
│   ├── main.py              # GUI main module
│   │
│   ├── core/                # Application core
│   │   ├── application.py   # Main window class
│   │   └── settings.py      # Settings persistence
│   │
│   ├── ui/                  # UI layout components
│   │   ├── header.py        # Header widget
│   │   ├── left_panel.py    # Input/output panel
│   │   ├── right_panel.py   # Cipher selection panel
│   │   └── theme.py         # Stylesheet definitions
│   │
│   ├── widgets/             # Reusable UI widgets
│   │   ├── cracker_panel.py # Hill cipher cracker UI
│   │   ├── cipher_selector.py
│   │   ├── input_section.py
│   │   ├── output_section.py
│   │   └── ...
│   │
│   ├── dialogs/             # Dialog windows
│   │   ├── about_dialog.py
│   │   └── history_dialog.py
│   │
│   ├── actions/             # Action handlers
│   │   ├── cipher_actions.py
│   │   ├── file_actions.py
│   │   └── ui_actions.py
│   │
│   ├── models/              # Data models
│   │   ├── history.py       # History management
│   │   └── cipher_config.py # Cipher configurations
│   │
│   └── utils/               # Utilities
│       ├── validators.py    # Key validation
│       └── helpers.py       # Helper functions
│
└── task/                    # Project task documents
```

### Technology Stack

| Component             | Technology                  |
| --------------------- | --------------------------- |
| **Language**          | Python 3.8+                 |
| **GUI Framework**     | PyQt6                       |
| **Matrix Operations** | NumPy                       |
| **Architecture**      | MVC-inspired modular design |

### Libraries Used

| Library   | Purpose                           | Link                                     |
| --------- | --------------------------------- | ---------------------------------------- |
| **PyQt6** | Cross-platform GUI framework      | [PyQt6](https://pypi.org/project/PyQt6/) |
| **NumPy** | Matrix operations for Hill cipher | [NumPy](https://numpy.org/)              |

---

## Development

### Adding a New Cipher

1. Create `ciphers/new_cipher.py`:

```python
class NewCipher:
    def encrypt(self, plaintext: str, key: str) -> str:
        # Implementation
        pass

    def decrypt(self, ciphertext: str, key: str) -> str:
        # Implementation
        pass
```

2. Register in `cipher_gui/models/cipher_config.py`

3. Add to `cipher_map` in `cipher_gui/core/application.py`

### Running Tests

```bash
python -c "
from ciphers.caesar_cipher import CaesarCipher
c = CaesarCipher()
assert c.encrypt('HELLO', 3) == 'KHOOR'
print('Tests passed!')
"
```

### Development

- **Framework**: PyQt6 for cross-platform GUI
- **Algorithms**: Classical cryptography implementations
- **Design**: Dark theme inspired by modern IDEs

### References

- [Hill Cipher Cryptanalysis](https://book-of-gehn.github.io/articles/2019/01/02/Break-Hill-Cipher-with-a-Known-Plaintext-Attack.html)
- [Classical Cipher Algorithms](https://en.wikipedia.org/wiki/Classical_cipher)

---

**Version**: 1.0.0  
**Platform**: Windows, macOS, Linux  
**Python**: 3.8+
