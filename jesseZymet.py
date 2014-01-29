def RussianRoulette():

    selection = input("Hi! Let's play some Russian roulette. If you survive five rounds, you win and you get to hear a secret about the author of this program. Else, you lose. Pick an integer between 1 and 6. ")
    if selection < 1 or selection > 6:
        print "You fail to adhere to instructions. You lose!"
    else:
        from random import randint
        count = 1
        bullet = randint(1,6)
        while selection != bullet and count <= 5:
            print "You survived round ", count, "!"
            bullet = bullet%6 + 1
            count = count + 1
        if count <= 5:
            print "Sorry, you lose. Thanks for playing!"
        else:
            print "You win! The secret is: the author often sleeps with a nightlight on because, despite believing in science, he is afraid that a scary monster with large eyes will pop out in the middle of the night."
    ans = raw_input("Try again? Enter 'Y' or 'N': ")
    if ans == 'Y':
        return RussianRoulette()
    elif ans == 'N':
        print "Okay, bye."
    else:
        print "What? Never mind. Bye."
