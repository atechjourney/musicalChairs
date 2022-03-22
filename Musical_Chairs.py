print("Welcome to Musical Chairs!,to begin the game ")
players = int (input("Please enter the amount of players: "))

chair = players

rounds = 0

while players > 1:
    rounds += 1 

    print ()
    print("** Round: ", rounds, "Has Started **")
    print ("Players remaining:",players)


    chairRemoved = 0


    if rounds % 5 == 0:
        chairRemoved = 3

    elif rounds % 2 == 0: 
        chairRemoved = 2

    else: 
        chairRemoved = 1

    if chair - chairRemoved <= 0:
        chair = 1
        print ("Removing remaining chairs except 1")
    else:
        chair -= chairRemoved
        print ("Remove", chairRemoved, "Chair(s)")

    players = chair
    print (players, "Player left")
    print()

print("Game is over. Winner declared after",rounds,"Rounds")
