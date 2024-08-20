import random as r

b=eval(input("Enter your number (between 1-9):"))

a=r.randint(1,9)

if a==b:
    print("WOW ! You guess exact number, congratulations")

elif a>b:
    print("Your choice is smaller than computer's choice")

elif a<b:
    print("Your choice is greater than computer's choice")



