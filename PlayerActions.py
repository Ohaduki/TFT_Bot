#select a champ
from Champions import Champion
from player import Player


#This function selects a specific location from the board or the bench. Very useful for many actions.
def champselect(player):
    while True:
        benchorboard = input("Would you like to select from the bench or the board?\n").lower()
        if benchorboard in ["bench", "board", "cancel"]:
            break
        else:
            print("You must choose bench, board or cancel")

    if benchorboard == "bench":
        print(f"Your bench is: {player.benchstatus()}")
        while True:
            try:
                whichone = int(input("Which number champion would you like to select?\n"))

                if whichone in range(1, 10):
                    break
                else:
                    print("Oops, please select a number between 1 and 9")
            except ValueError:
                print("Oops, please type in a number between 1 and 9")
        return [benchorboard, whichone-1]

    if benchorboard == "board":
        print(f"Your board is:")
        print(f"{player.boardstatus()[0]}\n{player.boardstatus()[1]}\n{player.boardstatus()[2]}\n{player.boardstatus()[3]}")
        while True:
            try:
                whichrow = int(input("What row would you like to select?\n"))

                if whichrow in range(1, 5):
                    break
                else:
                    print("Oops, please select a number between 1 and 4")
            except ValueError:
                print("Oops, please type in a number between 1 and 4")

        while True:
            try:
                whichcol = int(input("What column would you like to select?\n"))

                if whichcol in range(1, 7):
                    break
                else:
                    print("Oops, please select a number between 1 and 7")
            except ValueError:
                print("Oops, please type in a number between 1 and 7")

        return [benchorboard, [whichrow-1, whichcol-1]]

    elif benchorboard == "cancel":
        return "cancel"


#This function adds xp to a player, giving them an extra level if required
def buyxp(player):
    if player.level < 9:
        player.xp = player.xp + 4
        player.gold = player.gold - 4

    if player.level == 2:
        player.level = 3
        player.xp = 2
        print(f"{player.name} has reached Level {player.level}. He now has {player.xp} xp")

    if player.level == 3:
        if player.xp > 5:
            player.level += 1
            player.xp = player.xp - 6
            print(f"{player.name} has reached Level {player.level}. He now has {player.xp} xp")
        else:
            print(f"{player.name} now has {player.xp} xp")

    if player.level == 4:
        if player.xp > 9:
            player.level += 1
            player.xp = player.xp - 10
            print(f"{player.name} has reached Level {player.level}. He now has {player.xp} xp")
        else:
            print(f"{player.name} now has {player.xp} xp")

    if player.level == 5:
        if player.xp > 19:
            player.level += 1
            player.xp = player.xp - 20
            print(f"{player.name} has reached Level {player.level}. He now has {player.xp} xp")
        else:
            print(f"{player.name} now has {player.xp} xp")

    if player.level == 6:
        if player.xp > 35:
            player.level += 1
            player.xp = player.xp - 36
            print(f"{player.name} has reached Level {player.level}. He now has {player.xp} xp")
        else:
            print(f"{player.name} now has {player.xp} xp")

    if player.level == 7:
        if player.xp > 55:
            player.level += 1
            player.xp = player.xp - 56
            print(f"{player.name} has reached Level {player.level}. He now has {player.xp} xp")
        else:
            print(f"{player.name} now has {player.xp} xp")

    if player.level == 8:
        if player.xp > 79:
            player.level += 1
            player.xp = player.xp - 80
            print(f"{player.name} has reached Level {player.level}. He now has {player.xp} xp")
        else:
            print(f"{player.name} now has {player.xp} xp")

    if player.level == 9:
        print(f"{player.name} is at Max Level, no more xp can be bought.")

#checks if adding a champ will level them up, and if so returns the location of the other two instances
def level_check(player, champion, level):

    locations = []

    for row in range(4):
        for column in range(7):
            if type(player.board[row][column]) == type(champion) and player.board[row][column].level == level:
                locations.append(("board", row, column))
                if len(locations) == 2:
                    return locations


    for i in range(9):
        if type(player.bench[i]) == type(champion) and player.bench[i].level == level:
            locations.append(("bench", i))
            if len(locations) == 2:
                return locations

    return False


