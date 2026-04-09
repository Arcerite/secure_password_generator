# Secure Password Generator

A Python tool for generating cryptographically secure passwords with optional file saving and clipboard copying. This project demonstrates clean, professional coding practices, including docstrings, Big O analysis, and configurable behavior.

---

## Features

- Cryptographically secure passwords using Python’s `secrets` module
- Guarantees inclusion of:
  - At least one lowercase letter
  - At least one uppercase letter
  - At least one digit
  - At least one symbol (if enabled)
- Configurable password length
- Optional symbols
- Optional saving of passwords to a local file
- Optional automatic copying to clipboard
- Clean terminal menu interface
- Fully documented with docstrings and Big O analysis

---

## Installation

Clone the repository and install dependencies:

`git clone git@github.com:yourusername/secure-password-generator.git`  
`cd secure-password-generator`  
`pip install pyperclip`

---

## Usage

Run the program:

`python password_generator.py`

Menu options:

1. **Generate a password** – prints to console, optionally saves to file, optionally copies to clipboard  
2. **Change configuration settings** – enable/disable symbols, set length, toggle file saving and clipboard copy  
3. **Exit the program**

Example output:

`Your password is: A9f$kL2pQ!x8Zr1T`

If clipboard copy is enabled, the password is automatically available for pasting.

---

## Configuration

The `config()` menu allows you to:

- Enable/disable symbols  
- Set password length (minimum 3 without symbols, 4 with symbols)  
- Enable/disable saving passwords to `passwords.txt`  
- Enable/disable automatic clipboard copy  

---

## Security Note

- Passwords saved to file are **stored in plain text**.  
- Intended for educational purposes; for real-world usage, consider using a dedicated password manager.  

---

## Big O Analysis

- Generating a password: `O(LENGTH)`  
  - Guaranteed characters: `O(1)`  
  - Filling remaining characters: `O(LENGTH)`  
  - Shuffling: `O(LENGTH)`  
- Menu and configuration: `O(1)` per iteration  

---

## Requirements

- Python 3.x  
- `pyperclip` (for clipboard copy functionality)

---

## Author

Caleb Peters

---

## Future Improvements

- Encrypt saved passwords  
- Allow customizable symbol sets  
- Add password entropy estimation  
- Build a GUI interface
