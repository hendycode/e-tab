greeting = input("Hello, welcome to the Rockysoul hotel, would you like to make an order yourself with this tablet or would you like a waiter to come over? (tablet / waiter): ").lower()

if greeting == "tablet":
    choice = input("Great, thank you for choosing me, now we have quite a selection of flavours for you today. Would you like to start with a drink, an appetizer or would you prefer jumping straight to the main meal? (appetizer / drink / main meal): ").lower()
    if choice == "appetizer":
        appetite = input("Let's see what appetizer you can have today, we have the following on our menu: Beef Carpaccio, ice cream, Tuna Tartare, Burrata Salad, Smoked Salmon Blinis, Mushroom Risotto, Duck spring rolls. Please select what you would like to have:  ").lower()
        print(f"Great choice, we will have your {appetite} coming right up, please let the waiter know what you will want after your appetizer")
    elif choice == "drink":
        drink = input("Would you like an alcoholic drink or a non-alcoholic drink? (alcoholic / non-alcoholic): ").lower()
        if drink == "alcoholic":
            alcohol = input("We have the following assortment of alcoholic drinks that you can enjoy today; Wine, Champagne, Cocktails, Spirits, Gin. Choose the one you would like: ").lower()
            if alcohol == "wine":
                whichwine = input("Please choose the type of wine you would like to enjoy today, we have White wine, red wine, barolo ").lower()
                print(f"Your {whichwine} will be served in a flash")
            elif alcohol == "champagne":
                whatchampe = input("We have a variety of champagnes you can choose from, take a look: Dom Pérignon, Krug Grande Cuvée,  chateau maragaux, brut nature, extra brut, moet & chandon, bollinger, ruinart, taittinger  ").lower()
                print(f"Your {whatchampe} will be served in a flash")
            elif alcohol == "cocktails":
                whatcocktail = input("We have a variety of cocktails you can choose from, take a look: Negroni, Old Fashioned, Espresso Martini, French 75 ").lower()
                print(f"Your {whatcocktail} will be served in a flash")
            elif alcohol == "spirits":
                whatspirit = input("We have a variety of spirits you can choose from, take a look: Macallan 18-Year-Old Scotch, Hennessy XO Cognac, Patrón Silver Tequila ").lower()
                print(f"Your {whatspirit} will be served in a flash")
            else:
                whatgin = input("We have a variety of Gins that you can have today, please make a pick: London dry gin, Old tom gin, plymouth gin, navy strength gin, genever, sloe gin").lower()
                print(f"Your {whatgin} will be served in a short while")

        elif drink == "non-alcoholic":
            noalcohol = input("We have the following assortment of non-alcoholic drinks you can enjoy today: Mocktails, Fresh juices, Tea, Coffee.Please make your selection: ").lower()
            if noalcohol == "mocktails":
                mock = input("Here are the different types of mocktails we have today: Virgin Mojito, Nojito, Cucumber Cooler, Tropical Sunrise. Please choose the one you would like to have: ").lower()
                print(f"Nice taste, your {mock} will be served in a flash")
            elif noalcohol == "fresh juices":
                juice = input("On our assortment of juices we have the following available:  Cold-pressed orange, green apple, beetroot-carrot-ginger blend, passion and mango blend. Please choose one you would like: ").lower()
            elif noalcohol == "tea":
                typetea = input("We have a variety of teas today, please select the one you would like to have today: Darjeeling, Jasmine Pearl, Matcha Latte, Herbal infusions").lower()
                sugar = input("How many teaspoons of sugar would you like in your tea? ").lower()
                print(f"Your {typetea} tea with {sugar} teaspoons of sugar will be served shortly")
            else:
                types = input("We have different types of coffees, please choose which one you would like to have today: Single-origin espresso, Nitro cold brew, Affogato ").lower()
                sugarr = input("How many teaspoons of sugar would you like in your coffee? ").lower()
                temp = input("Would you prefer your coffee hot or cold? ").lower()
                print(f"Your {temp} {types} coffee with {sugarr} teaspoons of sugar will be served shortly")
        else:
            print("We do not have that as of now, kindy pick a drink from the listed types")


    else: 
        main = input("Wow, you must be starving today, luckily we have just the right mouth savouring dishes for you to choose from, please select the one you like: Pan-seared Salmon, Lobster thermidor, oxtail, filet mignon, mushroom stroganoff ").lower()
        print(f"Your {main} will be served shortly, in the meanntime, enjoy the good music and spectacular ambience")

else:
    if greeting == "waiter":
        print("Great, a waiter will attend to you in less than a minute")

 