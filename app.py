print("=" *31 + "\n   Welcome to Coffee Machine \n" + "=" *31)
drink = {"coffee": 2.5, "cappuccino": 5, "mocha": 4.2, "latte": 3, "espresso": 4.3, "water": 1}
order = input("what do you want to drink? (coffee/cappuccino/mocha/latte/espresso/water): ").lower()
for i in drink:
    if order not in drink:
        print("Sorry, we don't have that drink.")
        break
    else:
        if order == i:
            print(f"The price of {order} is {drink[i]}$")
            payment = float(input("please enter the payment amount: "))
            if payment < drink[i]:
                print(f"Sorry, that is not enough money, take your money back: {payment}$")
            elif payment > drink[i]:
                change = payment - drink[i]
                print(f"Here is your {order} and your change {change :.2f}$")
                print("Enjoy your drink!")
            else:
                print(f"Here is your {order}")
                print("Enjoy your drink!")