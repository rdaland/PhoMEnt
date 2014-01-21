# MichaelLefkowitz.py plays a simple number game with users. Specifically, it asks them to input numbers, becomes increasingly angry at the user's choices, insults the user, and then terminates.

print ("Hello, user! Let's play a game.")
for x in range(0, 3):
    num = input("\nPlease enter a number: ")
    print ("I don't like the number ", num, ("!" * (x+1)), sep='')
print ("\nYou suck at this game. Goodbye.")
