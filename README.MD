# Secure Password Generator

A simple Python tool for generating secure passwords using cryptographically strong randomness.

## Features

* Uses Python's `secrets` module for secure password generation
* Configurable password length
* Optional inclusion of symbols
* Guarantees at least one lowercase, uppercase, and numeric character
* Optional saving of generated passwords to a local file

## How It Works

The program builds a password by:

1. Ensuring required character types (lowercase, uppercase, digits, and optionally symbols)
2. Filling the remaining length with random characters from a defined pool
3. Shuffling the result to remove predictable patterns

## Usage

### Run the program

```bash
python main.py
```

### Menu Options

* Generate a new password
* Change configuration settings
* Exit the program

### Configuration Options

* Enable/disable symbols
* Set password length
* Enable/disable saving passwords to file

## Example Output

```
Your password is:

A9f$kL2pQ!x8Zr1T
```

## File Storage

If enabled, generated passwords are saved to:

```
passwords.txt
```

## Security Note

Passwords saved to file are stored in plain text and are intended for educational purposes only.
For real-world use, a dedicated password manager should be used.

## Requirements

* Python 3.x

## Author

Caleb Peters
