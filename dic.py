import random

value=True

#loop which is continus so we will use a while loop
while value:
    print(random.randint(1,6))
    #random int value start from a loop 1 to 6 
    roll_the_dice_agian=input(" Want to roll the dice again ? (y/n): ")
    if roll_the_dice_agian.lower()=="y":
        continue
    else:
        break