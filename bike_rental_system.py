a=0
stocks=100
rent=100

while a!=3:
    print('''
          1.Show Avaiable Stocks of Bikes 
          2.Buy Bike
          3.Exit\n
          Choice:
''')
    a=input("\n")
    if a=='1':
        print("Available Stock of Bike ",stocks)
        print("Every Bike is of 100 Rs. rent")

    elif a=='2':
        if stocks<0:
            print("Sorry, No stocks are available")
        else:
            requirement=eval(input("Enter Number of Bikes You Want:"))
            if requirement<=stocks:
                price=requirement*rent
                stocks=stocks-requirement
                print("Your rent is for",requirement,"Bikes is",price)

            else:
                print("Sorry,We have only",stocks,"Bikes")
    elif a=='3':
        a=3


            
        







