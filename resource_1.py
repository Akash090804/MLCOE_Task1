class resource:
  def __init__(user,water=100,coffeeBean=50,milk=200,cups=20):
    user.water=water
    user.coffeeBean=coffeeBean
    user.milk=milk
    user.cups=cups
  def using(user,used_water,used_coffee,milk_used,cup):   
      if user.water>=used_water and user.coffeeBean>=used_coffee and user.milk>=milk_used and user.cups>=cup:
         user.water -=used_water
         user.coffeeBean-= used_coffee
         user.milk -= milk_used
         user.cups -= cup
         return True
      else:
         return False
  def refilling_machine(user):
     user.water=100
     user.coffeeBean=50
     user.milk = 200
     user.cups=20  
     print("MAchine Refilled successfully")

   