class machine:
    def resource_initialising(user,resources):
        user.resources=resources
    def make_coffee(user,type):
        print("preparing "+ type)

        used_water = int(input("Enter the amount of water (ml): "))
        used_coffee = int(input("Enter the amount of coffee beans (g): "))
        milk_used = int(input("Enter the amount of milk (ml): "))
        cup = int(input("Enter the number of cups: "))
        