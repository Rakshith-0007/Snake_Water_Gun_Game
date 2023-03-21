import random
print("Welcome to Snake,Water,Gun game\nYou have 10 rounds All the Best:)")
game_content = ["Snake","Water","Gun"]
print("Round 1")
player_choice = int(input("Enter your choice code\n1.Snake\n2.Water\n3.Gun\n"))
i = j = k = l = 0
while True:
    comp_choice = random.choice(game_content)
    if l == 9:
        print(f"10 Rounds has been Completed\nYou won in {i} Rounds")
        print(f"Computer won in {j+1} Rounds")
        print(f"{k} times Draw")
        if i > j:
            print("You won the Game!")
        elif  i == j:
            print("Game result is Draw")
        else:print("Computer won the Game!")
        break
    elif (comp_choice == "Snake") and (player_choice == 2):
        l = l+1
        print("Computer Won!")
        print(f"{l+1} Round")
        player_choice = int(input("Enter your choice code\n1.Snake\n2.Water\n3.Gun\n"))
        j=j+1
        # continue
    elif (comp_choice == "Snake") and (player_choice == 3):
        l=l+1
        print("You Won!")
        print(f"{l+1} Round")
        player_choice = int(input("Enter your choice code\n1.Snake\n2.Water\n3.Gun\n"))
        i=i+1
        # continue
    elif (comp_choice == "Water") and (player_choice == 1):
        l=l+1
        print("You Won!")
        print(f"{l+1} Round")
        player_choice = int(input("Enter your choice code\n1.Snake\n2.Water\n3.Gun\n"))
        i=i+1
        # continue
    elif (comp_choice == "Water") and (player_choice == 3):
        l=l+1
        print("You Won!")
        print(f"{l+1} Round")
        player_choice = int(input("Enter your choice code\n1.Snake\n2.Water\n3.Gun\n"))
        i=i+1
        # continue
    elif (comp_choice == "Gun") and (player_choice == 1):
        l=l+1
        print("Computer Won!")
        print(f"{l+1} Round")
        player_choice = int(input("Enter your choice code\n1.Snake\n2.Water\n3.Gun\n"))
        j=j+1
        # continue
    elif (comp_choice == "Gun") and (player_choice == 2):
        l=l+1
        print("You Won!")
        print(f"{l+1} Round")
        player_choice = int(input("Enter your choice code\n1.Snake\n2.Water\n3.Gun\n"))
        i=i+1
        # continue
    elif (comp_choice == "Snake" and player_choice == 1) or (comp_choice == "Water" and player_choice == 2) or (comp_choice == "Gun" and player_choice == 3):
        l=l+1
        print("Draw!")
        print(f"{l+1} Round")
        player_choice = int(input("Enter your choice code\n1.Snake\n2.Water\n3.Gun\n"))
        k=k+1
        # continue
    else:
        print("Invalid Entry! Try again")
        l=l+1
        print(f"{l+1} Round")
        player_choice = int(input("Enter your choice code\n1.Snake\n2.Water\n3.Gun\n"))
