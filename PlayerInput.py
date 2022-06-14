def playerinput():

    while True:
        try:
            playernumber = int(input("Which player is making an action?\n"))

            if playernumber in range(1, 9):
                break

            else:
                print("Oops, that's not a correct number, please enter a number between 1 and 8!")

        except ValueError:
            print("Oops, that's not a number!")

    while True:
        try:
            action = int(input(f"Player {playernumber}! What action would you like to make?\n1. Buy from the shop\n2. Reroll\n3. Sell a champ\n4. Buy XP\n5. Move a champ\n6. Use an Item\n7. Display Gamestate\n"))

            if action in range(1, 8):
                break

            else:
                print("Oops, that number doesn't correspond to an action, please enter a number between 1 and 6!")

        except ValueError:
            print("Oops, that's not a number!")

    return [playernumber, action]


