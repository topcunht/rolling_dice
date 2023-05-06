import random

def roll_dice():
    dice_image = {
    1: (
        "---------",
        "         ",
        "    *    ",
        "         ",
        "---------"
    ),      
    2: (
        "---------",
        "*        ",
        "         ",
        "        *",
        "---------"
    ),
    3:(
        "---------",
        "*        ",
        "    *    ",
        "        *",
        "---------"
    ),
    4: (
        "---------",
        "*       *",
        "         ",
        "*       *",
        "---------"
    ),
    5: (
        "---------",
        "*       *",
        "    *    ",
        "*       *",
        "---------"
    ),
    6: (
        "---------",
        "*       *",
        "*       *",
        "*       *",
        "---------"
    )     
}
    roll = input("Do you want to dice? y/n: ")
    if roll != "y" and roll != "n":
        print("Invalid request!")
    if roll == "n":
        print("Dice will not be rolled! ")
    while roll.lower() == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print(f"Dice rolled {dice1} and {dice2} ")
        print("\n".join(dice_image[dice1]))
        print("\n")
        print("\n".join(dice_image[dice2]))
        
        roll = input("Roll Again ? y/n: ")
        if roll == "n":
            print("Dice will not be rolled! ")
        
roll_dice()