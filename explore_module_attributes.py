import mathematical_operations
import date_time_operations
import random_operations
import uuididentifier
import customfile


def main():

    print("Enter your choice to see all details using dir() function")

    print("1. mathematical_operations")
    print("2. date_time_operations")
    print("3. random_operations")
    print("4. uuididentifier")
    print("5. customfile")
    print("6. back to main menu")
    print("7. main file")

    y = int(input("Enter your choice: "))

    if y == 1:
        return dir(mathematical_operations)

    elif y == 2:
        return dir(date_time_operations)

    elif y == 3:
        return dir(random_operations)

    elif y == 4:
        return dir(uuididentifier)

    elif y == 5:
        return dir(customfile)

    elif y == 6:
        return "Exiting the module"

    elif y == 7:
        return dir()

    else:
        return "Invalid choice"