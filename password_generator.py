import secrets as s #Better way of making random values
import os
import string #used for easier ascii and digits for password gen

ALLOW_SYMBOLS = True
SAVE_TO_FILE = False
LENGTH = 16


def clear_screen() -> None:
    #Basic clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_password()-> str:
    password = [
        s.choice(string.ascii_lowercase),
        s.choice(string.ascii_uppercase),
        s.choice(string.digits)
    ]
    #gurantees we have at least one lower, one upper, and one digit

    if ALLOW_SYMBOLS:
        password.append(s.choice("!@#$%^&*()-_=+[]{};:,.<>?"))
    #gurantees we have one symbol if allowed

    # Fill remaining length
    pool = string.ascii_letters + string.digits
    if ALLOW_SYMBOLS:
        pool += "!@#$%^&*()-_=+[]{};:,.<>?"

    while len(password) < LENGTH:
        password.append(s.choice(pool))

    s.SystemRandom().shuffle(password)
    #The above shuffles the password to avoid the guranteed values we put at the start

    password= "".join(password) #turns it into a string
    return password

def config() -> None:
    global ALLOW_SYMBOLS, LENGTH, SAVE_TO_FILE

    symbol = input("Would you like to use symbols? (Some sites may not allow specific symbols in passwords)\nT/F:\n")
    
    if symbol.lower().strip()[0] == "t" :
        ALLOW_SYMBOLS = True
    else:
        ALLOW_SYMBOLS = False


    try:
        length = int(input("How long would you like your password to be? The longer the more secure it is\n"))
        if length < 4 and ALLOW_SYMBOLS:
            print("Password length is too small for all valid characters, setting to minimum of 4\n\n")
            LENGTH=4
        elif length <3:
            print("Password length is to small for all valid characters, setting to minimum of 3\n\n")
            LENGTH=3
        else:
            LENGTH=length

    except Exception as e:
        print(f"Error setting length {e} setting length to default of 16\n\n")
        LENGTH = 16

    print("Warning: Passwords are stored in plain text.")
    file = input("Would you like to save generated passwords to file? \nT/F:")
    if file.lower().strip()[0] == "t" :
        SAVE_TO_FILE = True
    else:
        SAVE_TO_FILE = False
    clear_screen()




def menu():
    while True:
        print("Simple Password Generator:\nMade by Caleb Peters:\n\nChoose an option")
        choice = input("1: Make Password\n2: Change Config Settings\n3: Exit\n")

        if choice == "1":
            clear_screen()
            password = generate_password()
            print("Your password is:\n\n" + password)

            if SAVE_TO_FILE:
                with open("passwords.txt", "a") as f:
                    f.write(password+ "\n\n")
                print("Password saved to passwords.txt")

            input("\nPress enter to continue")
            clear_screen()

        elif choice == "2":
            clear_screen()
            config()
            clear_screen()

        elif choice == "3":
            clear_screen()
            print("Goodbye")
            break

        else:
            clear_screen()
            print("Invalid Choice, please input just the number value")

if __name__ == "__main__":
    clear_screen()
    menu()