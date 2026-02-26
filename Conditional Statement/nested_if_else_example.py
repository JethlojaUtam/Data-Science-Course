print("1. Car\n2. Bike")
choice=int(input("Enter the choice:"))

if choice==1:
    print("You selected car choice now further select:")
    print("1. BMW\n2. Audi\n3. Virtus")

    choice1=int(input("Enter the choice for the car:"))
    if choice1==1:
        print("You are selected 'BMW' car")
    elif choice1==2:
        print("You are selected 'Audi' car")
    elif choice1==3:
        print("You are selected 'Virtus' car")
    else:
        print("Invalid choice for car")
elif choice==2:
    print("You selected bike choice now further select:")
    print("1. R15\n2. Spender\n3. Pulsar")

    choice1=int(input("Enter the choice for the bike:"))
    if choice1==1:
        print("You are selected 'R15' bike")
    elif choice1==2:
        print("You are selected 'Spender' bike")
    elif choice1==3:
        print("You are selected 'Pulsar' bike")
    else:
        print("Invalid choice for bike")
else:
    print("Invalid choice!!")