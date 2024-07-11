import random 
print("Welcome to the world of Gun,Water and Snake")
print('Enter "s" for snake\n "g" for Gun \n "w" for Water')
computer =random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]
print(f"You have choosen {reverseDict[you]}\nComputer has choosen {reverseDict[computer]}")
if(computer==you):
    print("It's a draw")
else:
    if(computer==-1 and you==1):
        print("You WIN!!")
    elif(computer==-1 and you==0):
        print("You LOSE!!")
    elif(computer==1 and you==-1):
        print("You LOSE!!")
    elif(computer==1 and you==0):
        print("You WIN!!")
    elif(computer==0 and you==1):
        print("You LOSE!!")
    elif(computer==0 and you==-1):
        print("You WIN!!")
    else:
        print("Something is wrong")