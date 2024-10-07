from resource_1 import resource
from machine import machine

print("Modules imported successfully!")  # Debugging print statement

def main():
    # object instantiation of previously defined classes
    print("Instantiating resources and machine...")  # Debugging print statement
    resources = resource()
    coffee_machine = machine(resources)
    
    while True:
        print("1. Espresso") 
        print("2. Latte")
        print("3. Americano")
        print("4. Mocha")
        print("5. Cappuccino")
        print("6. Show machine status")
        print("7. Refill the machine")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(coffee_machine.make_coffee("Espresso"))
        elif choice == "2":
            print(coffee_machine.make_coffee("Latte"))
        elif choice == "3":
            print(coffee_machine.make_coffee("Americano"))
        elif choice == "4":
            print(coffee_machine.make_coffee("Mocha"))  # Correct spelling
        elif choice == "5":
            print(coffee_machine.make_coffee("Cappuccino"))  # Correct spelling
        elif choice == "6":
            print(resources.current_Status())
        elif choice == "7":
            resources.refilling_machine()
        elif choice == "8":
            print("See you soon!")
            break
        else:
            print("Invalid choice, please try again.")
    
# Ensure the main function is called correctly
if __name__ == "__main__":
    print("Running the main function...")  # Debugging print statement
    main()
