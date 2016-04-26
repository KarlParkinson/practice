def calc(hand, sothe):
    hand.sort(reverse=True)
    score = 0
    for card in sothe:
        choice = greedyChoice(hand, card)
        print card,
        print choice
        if (choice > card):
            score += 1
        else:
            score -= 1
    print score


def greedyChoice(hand, card):
    choice = None
    if (card > max(hand)):
        choice = min(hand)
    else:
        for i in xrange(len(hand)-1):
            if (hand[i] > card and hand[i+1] < card):
                choice = hand[i]
                break
        if (choice == None):
            choice = hand[-1]
    hand.pop(hand.index(choice))
    return choice


calc([1,3,6], [2,4,5])
