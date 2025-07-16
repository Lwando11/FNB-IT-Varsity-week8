#shopping cart 

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food or press Q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}:R"))
        foods.append(food)
        prices.append(price)
        
print("------Your cart------") 


for food in foods:  
    print(food, end=" ") 
    
for price in prices:
    total += price


print("\n")    
    
print(f'Your total is: R{total}')            
        
