# #!/usr/bin/env python3.14

# cards = ['TH', '2S', 'KC', 'AD', '5C']
# # update list values: map T to 10, J to 11, Q to 12, K to 13, A to 14
# rank_map = {"T": "10", "J": "11", "Q": "12", "K": "13","A": "14"}

# cards = [rank_map.get(card[0], card[0] + card[1]) for card in cards]
    
# print(cards)

import sys


def card_ranks(cards):
    rank_map = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        'T': 10, 'J': 11, 'Q': 12,
        'K': 13, 'A': 14
    }

    # ranks = [rank_map[card[0]] for card in cards if card[0] in rank_map]

    ranks = []
    for card in cards:
        rank = card[0]
        if rank not in rank_map:
            # raise ValueError(f"Invalid card rank: {rank!r} in {card!r}")
            print(f"Warning: invalid card {card!r} ignored.", file=sys.stderr)
            continue

        ranks.append(rank_map[rank])
        
    return sorted(ranks, reverse=True)


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
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'


def main():
  print(card_ranks(['AC', '3D', '4S', 'KH', 'UH'])) #should output [14, 13, 4, 3]
  print(test())


if __name__ == "__main__":
    main()