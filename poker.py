# #!/usr/bin/env python3.14

# cards = ['TH', '2S', 'KC', 'AD', '5C']
# # update list values: map T to 10, J to 11, Q to 12, K to 13, A to 14
# rank_map = {"T": "10", "J": "11", "Q": "12", "K": "13","A": "14"}

# cards = [rank_map.get(card[0], card[0] + card[1]) for card in cards]
    
# print(cards)

import sys


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
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()  # noqa: SIM905
    fk = "9D 9H 9S 9C 7D".split()  # noqa: SIM905
    fh = "TD TC TH 7C 7D".split()  # noqa: F841, SIM905
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    assert straight(card_ranks(al))
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'


def main():
#   print(card_ranks(['AC', '3D', '4S', 'KH', 'UH'])) #should output [14, 13, 4, 3]
  print(test())


if __name__ == "__main__":
    main()