def new_file(file_name):
    with open(file_name, "x") as file:
        pass

    return "File created successfully."


def uuid_file(file_name):
    import uuid

    file_unique_identifier = uuid.uuid3(
        uuid.NAMESPACE_DNS,
        file_name
    )

    return file_unique_identifier


def write_file(file_name, write_data):
    with open(file_name, "w") as file:
        a = file.write(write_data)

    return f"Number of characters written: {a}"


def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()


def append_file(file_name, write_data_append):
    with open(file_name, "a") as file:
        d = file.write(write_data_append)

    return f"Number of characters appended: {d}"


def save_logs_output(file_name, file_unique_identifier, output):

    with open("save_logs_outputs.txt", "a") as file:

        file.write("File name: " + str(file_name) + "\n")
        file.write("Output: " + str(output) + "\n")
        file.write("Unique ID: " + str(file_unique_identifier) + "\n")
        file.write("--------------------------------\n")


def main():

    print("1. Create a new file in text format only")
    print("2. Write to a file")
    print("3. Read a file")
    print("4. Append to a file")
    print("5. Exit")

    g = int(input("Enter your choice: "))

    if g == 1:

        r = input("Enter your file name: ")
        return new_file(r)

    elif g == 2:

        r = input("Enter your file name: ")
        write_data = input("Enter the data you want to write: ")

        return write_file(r, write_data)

    elif g == 3:

        r = input("Enter your file name: ")

        return read_file(r)

    elif g == 4:

        r = input("Enter your file name: ")
        write_data_append = input("Enter the data you want to append: ")

        return append_file(r, write_data_append)

    elif g == 5:

        return "Exiting the file operations"

    else:

        return "Invalid choice"