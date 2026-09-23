import random


def random_number():
    return random.randint(-10**9, 10**9)


def random_list(a, b, c):
    return [random.randint(a, b) for i in range(c)]


def random_pasword():
    import uuid
    random_password = str(uuid.uuid4())
    return random_password


def random_otp():
    return random.randint(1000, 10000000)


def main():

    print("1. Generate a random number")
    print("2. Generate a random list")
    print("3. Create a random password")
    print("4. Generate random OTP")
    print("5. Back to main menu")

    d = int(input("Enter your choice: "))

    if d == 1:
        a = random_number()
        return a

    elif d == 2:
        x = int(input("Enter the lower limit: "))
        y = int(input("Enter the upper limit: "))
        z = int(input("Enter the total number of elements in the list: "))

        f = random_list(x, y, z)
        return f

    elif d == 3:
        return random_pasword()

    elif d == 4:
        s = random_otp()
        return s

    elif d == 5:
        return "Exiting the random operations"

    else:
        return "Invalid choice"