# #!/usr/bin/env python3.14

# cards = ['TH', '2S', 'KC', 'AD', '5C']
# # update list values: map T to 10, J to 11, Q to 12, K to 13, A to 14
# rank_map = {"T": "10", "J": "11", "Q": "12", "K": "13","A": "14"}

# cards = [rank_map.get(card[0], card[0] + card[1]) for card in cards]
    
# print(cards)

from ast import main
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


def main():
  print(card_ranks(['AC', '3D', '4S', 'KH', 'UH'])) #should output [14, 13, 4, 3]


if __name__ == "__main__":
    main()