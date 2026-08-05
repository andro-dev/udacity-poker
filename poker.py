# #!/usr/bin/env python3.14

import sys, random
from pprint import pp

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    allmax = []
    max_rank = max(hand_rank(hand) for hand in iterable)
    [allmax.append(hand) for hand in iterable if hand_rank(hand) == max_rank]
    return allmax

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC'] ):
    random.shuffle(deck)
    return [deck[n*i : n*(i+1)] for i in range(numhands)]

def hand_rank(hand):
    """Return a value indicating how high the hand ranks.
       counts:  count of each rank; ranks:   lists corresponding ranks 
       E.g. ['7', 'T', '7', '9', '7'] => counts = (3, 1, 1); ranks = (7, 10, 9)
    """
    # print("hand:", hand)
    groups = group(['--23456789TJQKA'.index(r) for r, _ in hand])
    counts, ranks = zip(*groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5,4,3,2,1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flash = len({s for _, s in hand}) == 1
    return (9 if (5,) == counts else
            8 if straight and flash else
            7 if (4,1) == counts else
            6 if (3,2) == counts else
            5 if flash else
            4 if straight else
            3 if (3,1,1) == counts else
            2 if (2,2,1) == counts else
            1 if (2,1,1,1) == counts else
            0), ranks

def group(items):
    groups = [(items.count(x), int(x)) for x in set(items)]
    # print('groups:', groups)
    sorted_groups = sorted(groups, key=lambda x: (-x[0], -x[1]))
    # print("sorted_groups:", sorted_groups)
    return sorted_groups

def card_ranks(cards):
# "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse = True)
    # account for straight with high 5 (Ace rank is 1)
    return [1,2,3,4,5] if ranks == [14,5,4,3,2] else ranks

def test():
    #"Test cases for the functions in poker program."
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2] 
    return 'tests pass'

def main():
  print(test())
#   pp(deal(8,5)) # print 8 hands - 5 cards each

if __name__ == "__main__":
    main()