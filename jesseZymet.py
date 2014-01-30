def RussianRoulette():

    print "Hi! Let's play some Russian roulette. If you survive five rounds, you win and you get to hear a secret about the author of this program. Else, you lose."
    marker = "Y"
    while marker == "Y":
        while True:
            try:
                choice = input("Pick an integer between 1 and 6. ")
                break
            except NameError:
                print "You fail to adhere to instructions. You lose!"
        if choice < 1 or choice > 6:
            print "You fail to adhere to instructions. You lose!"
        else:
            from random import randint
            count = 1
            bullet = randint(1,6)
            while choice != bullet and count <= 5:
                print "You survived round", count, "!"
                bullet = bullet%6 + 1
                print choice, bullet
                count = count + 1
            if count <= 5:
                print "Sorry, you lose. Thanks for playing!"
            else:
                print "You win! Now, you might have already known that it was the author's 7th and 8th grade experiences in the National Spelling Bee that led him to study linguistics. What you didn't know, however, is that he also tried to qualify in 6th grade, but was eliminated during his school spelling bee after misspeaking while spelling 'jiggle'."
        marker = raw_input("Try again? Enter 'Y' or 'N': ")
        if marker == "N":
            print "Okay, bye."
        elif marker != "Y":
            print "What? Never mind. Bye."
