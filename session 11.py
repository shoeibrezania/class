import random
f = ["sang" , "kaghaz" , "gheychi"]
PC = random.choice(f)
you = input("choose from : sang , kaghaz , gheychi : ")
if you in f :
    if PC == you :
        print('DRAW')
    else : 
        if you=="sang"  and PC=="kaghaz" :
            print("YOU LOOSE")
        else :
            if you=="ghechi" and PC=="sang" :
                print("YOU LOOSE")
            else:
                if you=="kaghaz" and PC=="gheychi" :
                    print("YOU LOOSE")
                else :
                    print("YOU WIN")
else:
    print("WRONG!!")

