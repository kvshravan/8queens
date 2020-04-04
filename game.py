import random
a = int(input("enter the box size\n"))
game = int(input("for ai vs ai enter 2 for ai vs human enter 1\n"))
print("select a number in between o,1 for toss")
toss = int(input("enter the number\n"))
if toss != 0 or 1:
    print("select eithe 0 or 1\n")
lis = [0,1]
lis = random.choice(lis) 
print(lis)
while(a!=0 and game == 1):
    if lis == toss:
        print(a)
        man = int(input("enter the number of sticks"))
       
        if man == 1 or 2 or 3:
            a = a - man
            print("the numof sticks",a)
            if a ==0:
                print("u have lost the game")
                break
        if(a%3 == 1 and a%2 != 1 and a > 3):
            a=a-3
            print("computer has selected",3)


        elif(a%3 != 1 and a%2 == 1 and a > 2):
            a=a-2
            print("computer has selected",2)
        elif(a%3 == 1 and a%2 == 1 and a > 3):
            a=a-2
            print("computer has selected",2)
        elif(a%3 != 1 and a%2 != 1):
            a=a-1
            if(a==0):
                print("user has won")
                break
            else:
                print("computer has selected",1)
        elif(a%3 == 1 and a%2 == 1 and a == 1):
            print("user has won")
            break
    if lis != toss:
        if(a%3 == 1 and a%2 != 1 and a > 3):
            a=a-3
            print("computer has selected",3)


        elif(a%3 != 1 and a%2 == 1 and a > 2):
            a=a-2
            print("computer has selected",2)
        elif(a%3 == 1 and a%2 == 1 and a > 3):
            a=a-2
            print("computer has selected",2)
        elif(a%3 != 1 and a%2 != 1):
            a=a-1
            if(a==0):
                print("user has won")
                break
            else:
                print("computer has selected",1)
        elif(a%3 == 1 and a%2 == 1 and a == 1):
            print("user has won")
            break
        print(a)
        man = int(input("enter the number of sticks"))
       
        if man == 1 or 2 or 3:
            a = a - man
            print("the numof sticks",a)
            if a ==0:
                print("u have lost the game")
                break
while(a!=0 and game == 2):
    if lis == toss:
        print(a)
        print("ai1 ha won the toss")
        if(a%3 == 1 and a%2 != 1 and a > 3):
            a=a-3
            print("computer1 has selected",3)


        elif(a%3 != 1 and a%2 == 1 and a > 2):
            a=a-2
            print("computer1 has selected",2)
        elif(a%3 == 1 and a%2 == 1 and a > 3):
            a=a-2
            print("computer1 has selected",2)
        elif(a%3 != 1 and a%2 != 1):
            a=a-1
            if(a==0):
                print("ai has won")
                break
            else:
                print("computer1 has selected",1)
        elif(a%3 == 1 and a%2 == 1 and a == 1):
            print("ai has won")
            break          
        if(a%3 == 1 and a%2 != 1 and a > 3):
            a=a-3
            print("computer2 has selected",3)


        elif(a%3 != 1 and a%2 == 1 and a > 2):
            a=a-2
            print("computer2 has selected",2)
        elif(a%3 == 1 and a%2 == 1 and a > 3):
            a=a-3
            print("computer2 has selected",3)
        elif(a%3 != 1 and a%2 != 1):
            a=a-1
            if(a==0):
                print("ai2 has won")
                break
            else:
                print("computer2 has selected",1)
        elif(a%3 == 1 and a%2 == 1 and a == 1):
            print("ai2 has won")
            break        
    if lis != toss:
        print(a)
        print("ai2 ha won the toss")
        if(a%3 == 1 and a%2 != 1 and a > 3):
            a=a-3
            print("computer2 has selected",3)


        elif(a%3 != 1 and a%2 == 1 and a > 2):
            a=a-2
            print("computer2 has selected",2)
        elif(a%3 == 1 and a%2 == 1 and a > 3):
            a=a-2
            print("computer2 has selected",3)
        elif(a%3 != 1 and a%2 != 1):
            a=a-1
            if(a==0):
                print("ai2 has won")
                break
            else:
                print("computer2 has selected",1)
        elif(a%3 == 1 and a%2 == 1 and a == 1):
            print("ai2 has won")
            break 
        if(a%3 == 1 and a%2 != 1 and a > 3):
            a=a-3
            print("computer1 has selected",3)


        elif(a%3 != 1 and a%2 == 1 and a > 2):
            a=a-2
            print("computer1 has selected",2)
        elif(a%3 == 1 and a%2 == 1 and a > 3):
            a=a-2
            print("computer1 has selected",2)
        elif(a%3 != 1 and a%2 != 1):
            a=a-1
            if(a==0):
                print("ai has won")
                break
            else:
                print("computer1 has selected",1)
        elif(a%3 == 1 and a%2 == 1 and a == 1):
            print("ai2 has won")
            break
