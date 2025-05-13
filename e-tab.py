greeting = input("Hello, welcome to the Rockysoul hotel, would you like to make an order yourself with this tablet or would you like a waiter to come over? (tablet / waiter): ").lower()

if greeting == "tablet":
    choice = input("Great, thank you for choosing me, now we have quite a selection of flavours for you today. Would you like to start with a drink, an appetizer or would you prefer jumping straight to the main meal? (appetizer / main meal): ")
    #if choice == ""

else:
    if greeting == "waiter":
        print("Great, a waiter will attend to you in less than a minute")

 