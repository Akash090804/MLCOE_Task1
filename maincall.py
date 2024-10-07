from resource_1 import resource
from machine import machine

def main():
    #object instansiation of previously defined classes
    resources = resource()
    machine = machine(resources)
    while True:
        print("1.Espresso") 
        print("2.latte")
        print("3.Americano")
        print("4.mocha")
        print("5.cappuccino")
        print("6.Show machine status")
        print("7.Refill the machine")
        print("8.exit")
        
        choice=input("Enter your choice")
        if choice =="1":
            print(machine.make_coffee("Espresso"))
        elif choice =="2":
            print(machine.make_coffee("Latte"))
        elif choice =="3":
            print(machine.make_coffee("Americano"))
        elif choice =="4":
            print(machine.make_coffee("Moca"))
        elif choice =="5":
            print(machine.make_coffee("cappucino"))
        elif choice =="6":
            print(resources.current_Status())
        elif choice=="7":
            resources.refilling_machine()
        elif choice == "8":
            print("See you soon")
            break
        else:
            print("Try again later,please")        

            
            
            



