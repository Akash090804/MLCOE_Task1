from resource_1 import resource
from machine import machine



def main():
    # object instantiation of previously defined classes
    resources = resource()
    coffee_machine = machine(resources)
    print("!---------------------------------------!")
    print("Welcome to the coffee shop")
    while True:
        print("1. Espresso") 
        print("2. Latte")
        print("3. Americano")
        print("4. Mocha")
        print("5. Cappuccino")
       
        print("6. Refill the machine")
        print("7. Exit")
        print("!-------------------------------------------!")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(coffee_machine.make_coffee("Espresso"))
        elif choice == "2":
            print(coffee_machine.make_coffee("Latte"))
        elif choice == "3":
            print(coffee_machine.make_coffee("Americano"))
        elif choice == "4":
            print(coffee_machine.make_coffee("Mocha")) 
        elif choice == "5":
            print(coffee_machine.make_coffee("Cappuccino"))  
        
        elif choice == "6":
            resources.refilling_machine()
        elif choice == "7":
            print("See you soon!")
            break
        else:
            print("Invalid choice, please try again.")
    

if __name__ == "__main__":
    main()
