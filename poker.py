# #!/usr/bin/env python3.14

# cards = ['TH', '2S', 'KC', 'AD', '5C']
# # update list values: map T to 10, J to 11, Q to 12, K to 13, A to 14
# rank_map = {"T": "10", "J": "11", "Q": "12", "K": "13","A": "14"}

# cards = [rank_map.get(card[0], card[0] + card[1]) for card in cards]
    
# print(cards)

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
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(cards):
# "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse = True)
    # account for straight with high 5 (Ace rank is 1)
    return [1,2,3,4,5] if ranks == [14,5,4,3,2] else ranks


# -----------
# User Instructions
# 
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    ranks.sort(reverse=True)
    return max(ranks) -  min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n-of-a-kind of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    "If there are two pair here, return the two ranks of the two pairs, else None."
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

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
  pp(deal(8,5)) # print 8 hands - 5 cards each


if __name__ == "__main__":
    main()