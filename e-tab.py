greeting = input("Hello, welcome to the Rockysoul hotel, would you like to make an order yourself with this tablet or would you like a waiter to come over? (tablet / waiter): ").lower()

if greeting == "tablet":
    choice = input("Great, thank you for choosing me, now we have quite a selection of flavours for you today. Would you like to start with a drink, an appetizer or would you prefer jumping straight to the main meal? (appetizer / drink / main meal): ").lower()
    if choice == "appetizer":
        appetite = input("Let's see what appetizer you can have today, we have the following on our menu: Beef Carpaccio, ice cream, Tuna Tartare, Burrata Salad, Smoked Salmon Blinis, Mushroom Risotto, Duck spring rolls. Please select what you would like to have:  ").lower()
        print(f"Great choice, we will have your {appetite} coming right up, please let the waiter know what you will want after your appetizer")
    elif choice == "drink":
        drink = input("Would you like an alcoholic drink or a non-alcoholic drink? (alcoholic / non-alcoholic): ").lower()
        if drink == "alcoholic":
            alcohol = input("We have the following assortment of alcoholic drinks that you can enjoy today;")
        
    else: 
        main = input("Wow, you must be starving today, luckily we have just the right mouth savouring dishes, we have: ").lower()

else:
    if greeting == "waiter":
        print("Great, a waiter will attend to you in less than a minute")

 