
import customfile
import uuididentifier

print("Welcome To Multi-Utility Toolkit")
print("Please select an option:")
print("1.date and time operations")
print("2.mathematical operations")
print("3.random operations")
print("4.unique id operations")
print("5.file operations(custom module)")
print("6.explore module attributes(dir())")
print("7.exit")
choice = 0
while choice != '0':
    choice = input("Enter your choice (1-7): ")
    if choice == '1':
        import date_time_operations
        result=date_time_operations.main()
        print(result)
        customfile.save_logs_output("date_time_operations",uuididentifier.dateandtime(),result)
    elif choice == '2':
        import mathematical_operations
        result=mathematical_operations.main()
        print(result)
        customfile.save_logs_output("mathematical_operations",uuididentifier.mathematical_operation(),result)
    elif choice == '3':
        import random_operations
        result=random_operations.main()
        print(result)
        customfile.save_logs_output("random_operations",uuididentifier.random_op(),result)
    elif choice == '4':
        import uuididentifier
        result=uuididentifier.main()
        print(result)
        customfile.save_logs_output("uuididentifier",uuididentifier.uuid_id(),result)

    elif choice == '5':
        import customfile
        result=customfile.main()
        print(result)
        customfile.save_logs_output("customfile",uuididentifier.customfile_unique(),result)
    elif choice == '6':
        import explore_module_attributes
        result=explore_module_attributes.main()
        print(result)
        customfile.save_logs_output("explore_module_attributes",uuididentifier.explore_modules(),result)
    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break
        exit()


    else:
        print("Invalid choice. Please try again.")
    print("\nPlease select an option:") 

if __name__ == "__main__":
    print("this is the main.py file")

