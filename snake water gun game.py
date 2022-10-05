import random

def game(comp, you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
        

randNo=random.randint(1,3)
# print(randNo)
if randNo ==1:
    comp='s'
elif randNo ==2:
    comp='w'
elif randNo ==3:
    comp='g'
# print("comp turn: Sanke(s) Water(w) or Gun(g)?")
you=input("player turn: Snake(s) Water(w) or Gun(g)?")
a= game(comp,you)

if a==None:
    print("geme is a tie!")
elif a==True:
    print("you win!")
else:
    print("you loose!")