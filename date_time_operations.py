import datetime
import time


def display_current_date_time():
    current_time = datetime.datetime.now()
    return f"Current date and time: {current_time}"


def difference_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days


def format_date_custom(date, format_string):
    return date.strftime(format_string)


def stop_watch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()

    input("Press Enter to stop the stopwatch...")
    end_time = time.time()

    elapsed_time = end_time - start_time
    return f"Elapsed time: {elapsed_time:.2f} seconds"


def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds", end="\r")
        time.sleep(1)

    return "Time's up!"


def main():

    print("Date and Time Operations")
    print("1. Display current date and time")
    print("2. Calculate the difference between two dates")
    print("3. Format date into custom format")
    print("4. Stop watch")
    print("5. Countdown timer")
    print("6. Exit")

    a = input("Enter your choice (1-6): ")

    if a == '1':
        return display_current_date_time()

    elif a == '2':
        date1 = input("Enter the first date (YYYY-MM-DD): ")
        date2 = input("Enter the second date (YYYY-MM-DD): ")

        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

        days = difference_between_dates(date1, date2)
        return f"Difference: {abs(days)} days"

    elif a == '3':
        date = input("Enter the date (YYYY-MM-DD): ")
        format_string = input("Enter the custom format: ")

        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        formatted_date = format_date_custom(date, format_string)

        return f"Formatted date: {formatted_date}"

    elif a == '4':
        return stop_watch()

    elif a == '5':
        seconds = int(input("Enter the number of seconds: "))
        return countdown_timer(seconds)

    elif a == '6':
        return "Exiting program."
        exit()

    else:
        return "Invalid choice."