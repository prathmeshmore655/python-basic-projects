import random as r

c_score=0
u_score=0

l=["rock","paper","scissor"]

print("\n")

z=eval(input("Enter no. of rounds you want to play :"))

for n in range(z+1,1,-1):

    a=(r.choice(l))
    
    print("\n")

    print('''Rounds Remaining :''',n-1,"\n",'''
           Choices : 1.rock
                     2.paper
                     3.scissor''')

               
    
    b=eval(input("\nEnter your choice :"))
    

    if a=="scissor" and b==2:
            print("You loose !,scissor cuts paper\n")
            c_score=c_score+1
            print("PLayers Score :",u_score)
            print("Computers Score:",c_score)

    elif a=="rock" and b==2:
            print("You win !, paper beats scissor\n")
            u_score=u_score+1
            print("PLayers Score :",u_score)
            print("Computers Score:",c_score)
    elif a=="paper" and b==3:
        print("You win !,rock beats paper\n")
        u_score=u_score+1
        print("PLayers Score :",u_score)
        print("Computers Score:",c_score)

    elif a=="rock" and b==3:
        print("You loose !,rock beats scissor\n")
        c_score=c_score+1
        print("PLayers Score :",u_score)
        print("Computers Score:",c_score)

    elif a=="paper" and b==1:
        print("You win !,rock beats paper\n")
        u_score=u_score+1   
        print("PLayers Score :",u_score)
        print("Computers Score:",c_score)

    elif a=="scissor" and b==1:
        print("You win !,rock beats scissor\n")
        u_score=u_score+1
        print("PLayers Score :",u_score)    
        print("Computers Score:",c_score)
    




if u_score>c_score:
    print("You Win ! Congratulations\n")
else :
    print("You Loose !Better Luck Next Time\n")
 