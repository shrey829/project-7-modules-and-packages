import uuid
import customfile


def dateandtime():
    file_unique_identifier = uuid.uuid3(
        uuid.NAMESPACE_DNS,
        "date_time_operations"
    )
    return file_unique_identifier


def mathematical_operation():
    file_unique_identifier = uuid.uuid3(
        uuid.NAMESPACE_DNS,
        "mathematical_operations"
    )
    return file_unique_identifier


def random_op():
    file_unique_identifier = uuid.uuid3(
        uuid.NAMESPACE_DNS,
        "random_operations"
    )
    return file_unique_identifier


def customfile_unique():
    file_unique_identifier = uuid.uuid3(
        uuid.NAMESPACE_DNS,
        "customfile"
    )
    if customfile.g==1:
        re=customfile.uuid_file(customfile.r)
    return file_unique_identifier,"customfile",re,"file that has been created to handle files"


def explore_modules():
    file_unique_identifier = uuid.uuid3(
        uuid.NAMESPACE_DNS,
        "explore_module_attributes"
    )
    return file_unique_identifier


def uuid_id():
    file_unique_identifier = uuid.uuid3(
        uuid.NAMESPACE_DNS,
        "uuid"
    )
    return file_unique_identifier


def main():

    print("Enter your choice to create UUID for each file")
    print("1. Date and time operations")
    print("2. Mathematical operations")
    print("3. Random operations")
    print("4. Unique ID operations")
    print("5. File operations (custom module)")
    print("6. Explore module attributes (dir())")
    print("7. Back to main menu")

    r = int(input("Enter your choice: "))

    if r == 1:
        return dateandtime()

    elif r == 2:
        return mathematical_operation()

    elif r == 3:
        return random_op()

    elif r == 4:
        return uuid_id()

    elif r == 5:
        return customfile_unique()

    elif r == 6:
        return explore_modules()

    elif r == 7:
        return "Exiting towards main menu"

    else:
        return "Invalid choice"