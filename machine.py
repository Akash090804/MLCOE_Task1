class machine:
    def __init__(user,resources):
        user.resources=resources
    def make_coffee(user,type):
        print("preparing "+ type)

        used_water = int(input("Enter the amount of water (ml): "))
        used_coffee = int(input("Enter the amount of coffee beans (g): "))
        milk_used = int(input("Enter the amount of milk (ml): "))
        cup = int(input("Enter the number of cups: "))
        if user.resources.using(used_water,used_coffee,milk_used,cup):
            return f"coffee {type} is ready!!"
        else:
            return "You dont have enough resources for this {type}"
        