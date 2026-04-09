import secrets as s  # Cryptographically secure random generation
import os
import string  # For ASCII letters and digits
import pyperclip #To put password into clipboard

# =============================
# Global Configuration Variables
# =============================
ALLOW_SYMBOLS = True
SAVE_TO_FILE = False
LENGTH = 16
COPY_TO_CLIPBOARD = True  # default True


def clear_screen() -> None:
    """
    Clear the terminal screen.

    Uses OS-specific command:
        - Windows: 'cls'
        - Unix/Linux/macOS: 'clear'

    Big O Analysis:
        - Python: O(1)
        - Terminal operation: O(R * C), proportional to terminal rows (R) × columns (C)
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_password() -> str:
    """
    Generate a cryptographically secure password.

    Guarantees at least:
        - one lowercase letter
        - one uppercase letter
        - one digit
        - one symbol (if enabled)

    Fills remaining length with random characters from the allowed pool.
    Shuffles the result to remove predictable patterns.

    Saves to 'passwords.txt' if SAVE_TO_FILE is True.

    Returns:
        str: The generated password.

    Big O Analysis:
        - Adding guaranteed characters: O(1)
        - Filling remaining length: O(LENGTH)
        - Shuffling password: O(LENGTH)
    Overall: O(LENGTH)
    """
    password = [
        s.choice(string.ascii_lowercase),
        s.choice(string.ascii_uppercase),
        s.choice(string.digits)
    ]

    if ALLOW_SYMBOLS:
        password.append(s.choice("!@#$%^&*()-_=+[]{};:,.<>?"))
    #Above makes sure the password contains at least one lower, upper and number, and if symbols are allowed one of those too
    
    pool = string.ascii_letters + string.digits
    if ALLOW_SYMBOLS:
        pool += "!@#$%^&*()-_=+[]{};:,.<>?"
    
    for _ in range(LENGTH - len(password)):
        password += s.choice(pool)

    s.SystemRandom().shuffle(password)
    password = "".join(password)
    #above fills in the rest of the password, shuffles it and turns it into a string

    if SAVE_TO_FILE:
        with open("passwords.txt", "a") as f:
            f.write(password + "\n")
        print("Password saved to passwords.txt")
    #Saves to file if the user requested it

    if COPY_TO_CLIPBOARD:
        try:
            pyperclip.copy(password)
            print("\nPassword copied to clipboard!")
        except Exception as e:
            print("\nCould not copy to clipboard:", e)
    #Saves to clipboard if the user requested it
        
    return password
    #No matter what returns the password as a string

def config() -> None:
    """
    Configure password generation settings.

    Prompts user to:
        - Enable/disable symbols
        - Set password length
        - Enable/disable saving passwords to a file
        - Copy to clipboard

    Validates minimum length:
        - 4 if symbols are enabled
        - 3 if symbols are disabled

    Big O Analysis: O(1) per input interaction
    """
    global ALLOW_SYMBOLS, LENGTH, SAVE_TO_FILE, COPY_TO_CLIPBOARD

    # Symbol configuration
    symbol = input(
        "Would you like to use symbols? (Some sites may not allow specific symbols in passwords)\nT/F: "
    )
    ALLOW_SYMBOLS = symbol.lower().strip().startswith("t")
    clear_screen()

    # Length configuration
    try:
        length = int(input("How long would you like your password to be? The longer the more secure it is\n"))
        LENGTH = length
    except ValueError as e:
        print(f"Error setting length: {e}. Setting length to default of 16.")
        LENGTH = 16

    # Ensure minimum length
    if ALLOW_SYMBOLS:
        min_length = 4
    else:
        min_length = 3
    if LENGTH < min_length:
        print(f"Length too short for chosen settings. Setting to minimum of {min_length}.")
        LENGTH = min_length

    clear_screen()

    # File saving configuration
    file = input("Would you like to save generated passwords to a file? \nT/F: ")
    SAVE_TO_FILE = file.lower().strip().startswith("t")
    clear_screen()

    copy = input("Automatically copy generated passwords to clipboard? \nT/F: ")
    COPY_TO_CLIPBOARD = copy.lower().strip().startswith("t")


def menu() -> None:
    """
    Main interactive menu for the password generator.

    Allows user to:
        1. Generate a password
        2. Change configuration settings
        3. Exit the program

    Big O Analysis:
        - Per iteration: O(1)
        - Calls to generate_password(): O(LENGTH)
    """
    while True:
        print("Simple Password Generator:\nMade by Caleb Peters:\n\nChoose an option")
        choice = input("1: Make Password\n2: Change Config Settings\n3: Exit\n")

        #Make password
        if choice == "1":
            clear_screen()
            password = generate_password()
            print("Your password is:\n\n" + password)
            input("\nPress enter to continue")
            clear_screen()
        #Config
        elif choice == "2":
            clear_screen()
            config()
            clear_screen()
        #Exit
        elif choice == "3":
            clear_screen()
            print("Goodbye")
            break
        #Invalid choice
        else:
            clear_screen()
            print("Invalid Choice, please input just the number value")


if __name__ == "__main__":
    clear_screen()
    menu()