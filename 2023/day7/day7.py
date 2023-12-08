from collections import Counter
from enum import Enum
from functools import cmp_to_key
import os

class Hand:
  def __init__(self, cards, bid):
    self.cards = cards
    self.bid = bid

class HandCategory(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines
    
def handCompare(hand1, hand2):
    handCategory1 = categorizeHand(hand1.cards)
    handCategory2 = categorizeHand(hand2.cards)
    if handCategory1.value == handCategory2.value:
        # Compare cards one by one
        for i, c in enumerate(hand1.cards):
            if cardValue[c] < cardValue[hand2.cards[i]]:
                return -1
            if cardValue[c] > cardValue[hand2.cards[i]]:
                return 1
        return 1
    else:
        return handCategory1.value - handCategory2.value
    
def handCompareWithJokers(hand1, hand2):
    handCategory1 = categorizeHandWithJokers(hand1.cards)
    handCategory2 = categorizeHandWithJokers(hand2.cards)
    if handCategory1.value == handCategory2.value:
        # Compare cards one by one
        for i, c in enumerate(hand1.cards):
            if cardValueWithJokers[c] < cardValueWithJokers[hand2.cards[i]]:
                return -1
            if cardValueWithJokers[c] > cardValueWithJokers[hand2.cards[i]]:
                return 1
        return 1
    else:
        return handCategory1.value - handCategory2.value

def categorizeHand(cards):
    counter = Counter(cards)
    counts = counter.most_common(2)
    return getHandCategory(counts)
    
def categorizeHandWithJokers(cards):
    if cards == "JJJJJ":
        # Special case, treat it as five as a kind
        return HandCategory.FIVE_OF_A_KIND
    counter = Counter(cards)
    c = counter.most_common(5)
    counts = [count for count in c if count[0] != 'J']
    jokerCounts = [count[1] for count in c if count[0] == 'J']
    numJokers = jokerCounts[0] if len(jokerCounts) > 0 else 0
    # I think it's optimal to add the jokers to the most common non-joker card. I'm not 100% confident about this, but lets assume this for now.
    counts[0] = (counts[0][0], counts[0][1] + numJokers)
    return getHandCategory(counts)
    
def getHandCategory(counts):
    if counts[0][1] == 5:
        return HandCategory.FIVE_OF_A_KIND
    elif counts[0][1] == 4:
        return HandCategory.FOUR_OF_A_KIND
    elif counts[0][1] == 3 and counts[1][1] == 2:
        return HandCategory.FULL_HOUSE
    elif counts[0][1] == 3:
        return HandCategory.THREE_OF_A_KIND
    elif counts[0][1] == 2 and counts[1][1] == 2:
        return HandCategory.TWO_PAIR
    elif counts[0][1] == 2:
        return HandCategory.ONE_PAIR
    else:
        return HandCategory.HIGH_CARD

cardValue = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

cardValueWithJokers = {
    'J': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14
}

def solve(input, compareFn):
    hands = [Hand(line.split()[0], line.split()[1]) for line in input]
    hands.sort(key=cmp_to_key(compareFn))
    # print([hand.cards for hand in hands])
    sum = 0
    for i, hand in enumerate(hands):
        sum += int(hand.bid) * (i+1)
    print(sum)

def part1(input):
    print("Part 1: ")
    solve(input, handCompare)

def part2(input):
    print("\nPart 2: ")
    solve(input, handCompareWithJokers)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)