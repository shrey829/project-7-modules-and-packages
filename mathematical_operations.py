import math


def factorial(n):
    assert n >= 0, "Factorial is not defined for negative numbers"

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def compound_intrest(principal, time_period, rate_intrest):
    amount = principal * math.pow((100 + rate_intrest) / 100, time_period)
    ci = amount - principal
    return ci, amount


def trignometric_operations(angle_degrees):
    print("1. to calculate sin")
    print("2. to calculate cos")
    print("3. to calculate tan")
    print("4. to calculate cosec")
    print("5. to calculate sec")
    print("6. to calculate cot")

    c = int(input("Enter your choice: "))

    if c == 1:
        return math.sin(math.radians(angle_degrees))

    elif c == 2:
        return math.cos(math.radians(angle_degrees))

    elif c == 3:
        return math.tan(math.radians(angle_degrees))

    elif c == 4:
        return 1 / math.sin(math.radians(angle_degrees))

    elif c == 5:
        return 1 / math.cos(math.radians(angle_degrees))

    elif c == 6:
        return 1 / math.tan(math.radians(angle_degrees))

    else:
        return "Invalid choice"


def circle():
    radius = float(input("Enter radius: "))
    area = math.pi * radius ** 2
    return f"Area of circle = {area:.2f}"


def rectangle():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    return f"Area of rectangle = {area:.2f}"


def square():
    side = float(input("Enter side: "))
    area = side ** 2
    return f"Area of square = {area:.2f}"


def triangle():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    return f"Area of triangle = {area:.2f}"


def parallelogram():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = base * height
    return f"Area of parallelogram = {area:.2f}"


def trapezium():
    a = float(input("Enter first parallel side: "))
    b = float(input("Enter second parallel side: "))
    height = float(input("Enter height: "))
    area = 0.5 * (a + b) * height
    return f"Area of trapezium = {area:.2f}"


def ellipse():
    a = float(input("Enter semi-major axis: "))
    b = float(input("Enter semi-minor axis: "))
    area = math.pi * a * b
    return f"Area of ellipse = {area:.2f}"


def area_geometric_shapes():
    print("Area Calculator")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")
    print("5. Parallelogram")
    print("6. Trapezium")
    print("7. Ellipse")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        return circle()

    elif choice == 2:
        return rectangle()

    elif choice == 3:
        return square()

    elif choice == 4:
        return triangle()

    elif choice == 5:
        return parallelogram()

    elif choice == 6:
        return trapezium()

    elif choice == 7:
        return ellipse()

    else:
        return "Invalid choice!"


def main():

    print("1. Calculate factorial of a number")
    print("2. Solve compound interest")
    print("3. Trigonometric operations")
    print("4. Area of geometric shapes")
    print("5. Back to main menu")

    b = input("Enter your choice (1-5): ")

    if b == '1':
        e = int(input("Enter number to find factorial of: "))
        return f"Factorial = {factorial(e)}"

    elif b == '2':
        p = int(input("Enter the principal: "))
        r = int(input("Enter the rate of interest: "))
        t = int(input("Enter the time period: "))

        ci, amount = compound_intrest(p, t, r)

        return f"Compound Interest = {ci:.2f}, Amount = {amount:.2f}"

    elif b == '3':
        angle = int(input("Enter the angle in degrees: "))
        return trignometric_operations(angle)

    elif b == '4':
        return area_geometric_shapes()

    elif b == '5':
        return "Exiting the module"
        exit()

    else:
        return "Invalid choice"