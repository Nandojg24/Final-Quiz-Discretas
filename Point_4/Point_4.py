# Integrante 1: Juan Fernando Jimenez Garcia - 202459394
# Docente: Luis Germán Toro Pareja.
# Número de grupo:52
# Final Quiz
import re
import time


def validate_credentials(username, password):
    # This function is to make sure that the username and password
    # are valids according to the riules of the data base of the library
    # The username must start with a 2 digit number between 00 and 25,
    # and the password must start with 2 letters and then the username.
    # I use regular expresions to validate the credentials because
    # they are very useful to validate patterns in strings.
    validation = 0
    if len(username) == 7 and re.fullmatch(r"^([0-1]\d{6}|2[0-5]\d{5})",
                                           username):
        validation += 1
    if len(password) == 9 and re.match(r"^([a-zA-Z]{2})" +
                                       re.escape(username) +
                                       "$", password):
        validation += 1
    return validation == 2


def welcome_message():
    # This function is to print the welcome message of the library
    print("####"*6, " Welcome to the BuPen Univalle ", "####"*6, "\n")
    print(" This is the library of the University of Valle \n")

    # With the while loop, the user can choose
    # to turn on or off the BuPen system
    # and when the system is turned on,
    # the user will be able to enter their credentials
    while True:
        print("Do you want to turn on the system? \n"
              "If you want to turn on the system, please type 'yes' \n"
              "If you want to turn off the system, please type 'no'")
        starting_up = input(": ").strip().lower()
        if starting_up == "yes":
            print("The BuPen system is starting up...\n")
            time.sleep(2)
            print("The BuPen system is now ready to use!\n")
            start_up()
        elif starting_up == "no":
            print("The BuPen system is closing up...\n")
            time.sleep(2)
            print("The BuPen system is now shut down\n")
            time.sleep(2)
            exit()
        else:
            print("Invalid option, please try again\n")
            time.sleep(2)
            welcome_message()


def start_up():
    # This function is to enter to the BuPen system
    # and to validate the credentials of the user
    max_attempts = 4
    attempts = 0
    credentials_rules = ("To use the BuPen system,"
                         "you must enter your credentials.\n"
                         "1. The username must start with a 2 digit"
                         "number between 00 and 25.\n"
                         "2. The password must start with 2 letters"
                         " and then follow by the username.\n")
    print(credentials_rules)
    time.sleep(2)

    # I decide to use attempts to limit the number of tries,
    # and make the BuPen system more secure.
    while attempts < max_attempts:
        username = input("Please enter your username: ").strip()
        password = input("Please enter your password: ").strip()

        if validate_credentials(username, password):
            print("welcome to the BuPen system!\n"
                  "You now are able to use the system.")
            print("---"*30)
            exit()
        else:
            attempts += 1
            print("Invalid credentials.\n"
                  "Before you try again,"
                  "please make sure that your credentials are valid.\n"
                  f"You have {max_attempts - attempts} attempts left.\n")
            time.sleep(2)
            start_up()
    if attempts == max_attempts:
        print("You have reached the maximum number of attempts.\n"
              "The BuPen system is now shutting down...\n")
        time.sleep(2)
        exit()


if __name__ == "__main__":
    welcome_message()
