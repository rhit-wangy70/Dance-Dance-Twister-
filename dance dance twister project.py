# dance dance twister code
# made by Jack Wang, Carter Werkerma, Brian Yamada
# started on 3/27/2025

import time
import random


def gamestart(list):
    "What comes in: a list of 4 numbers; What goes out: none; Side effect: below"
    "All LED needs to blink in a circuilar pattern, then the first 2 of list tiles will start glowing"
    "in one color and the latter 2 will goes in another color"


def popping_up(emptytiles, t):
    "What goes in: a list containing 2 #s and 1 integer; what comes out: nothing; side effect: as shown below"
    "LED at 2 positions need to glow, with emptytiles[0] in one color and emptytiles[1] in another and brightness increase"
    "from 0 → 255, then decrease from 255 to 0, the number of looping is according to difficuity level t"


def going_off(going_off, t):
    "What goes in: a list with 2# and 1 integer; what comes out: nothing; side effect: as shown below"
    "LED in two lighted positions need to blink at 0.5Hz and have brightness reduced from 255 to 0 "
    "the time of changes is according to difficulty level t.  "


def messing_up(oops):
    "What comes in: a list of numbers; What goes out: nothing; side effect: as shown below"
    "LED that was going off and popping up turn red and blink for 3 times"


def active_or_not(tile):
    "What comes in: a list of numbers; what comes out: True or a list of location; Side effect: nothing"
    "for tiles at location if at least 2 of 4 sensors(might change as numbers of sensors changed)"
    "are activated, return True; else return position"
    count = 0
    position = []
    for i in range(len(tile) + 1):
        # if needed amount of sensors is activated at tile[i+1]
        count = count + 1
    # else: position = position + (i+1)
    if count == len(tile):
        return True

    return position


def main():
    "What comes in: nothing; What comes out: an integer(standing for rounds passed); Side effect: shown below"
    "generate 4 different random numbers, call gamestart() to start the game "
    "if all 4 tiles are active, start the loop"
    "loop content: an increasing #, if statement, popping_up and going_off, messing_up if the if statement is active"
    occupied = []
    empty = []
    off = []
    allnumbers = [1, 2, 3, 4, 5, 6]
    rounds = 0

    occupied = random.sample(range(1, 7), 4)
    empty = set(allnumbers) - set(occupied)  # removing occupied from allnumbers
    gamestart(occupied)
    # detent whether all four tiles are stepped. if yes, start game. If no, wait till they're all stepped.
    for i in range(100):
        off = random.sample(occupied, 2)
        popping_up(empty, i)
        going_off(off, i)
        messing_up = off + empty
        #if tiles in off is not removed or in empty is unpressed
            # messing_up(messing_up)
        #else:
            occupied = (set(occupied) - set(off)) | set(empty)
            rounds = rounds + 1

    print(rounds)
# second tile

# thrid tile and onward of random tile

# starting 3 blink sequence

# main code
main()
