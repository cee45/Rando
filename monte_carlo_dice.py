import random

def rollDice():
    roll = random.randint(0,100)

    if roll == 100:
        print(roll,"Roll was 100 you lose. What are the odds?! Play Again")
        return False
    elif roll <= 50:
        print(roll,"Roll was 1-50, you lose.")
        return False
    elif roll > 100 >= 50:
        print(roll, "Roll was 51-99, you Win!")
        return True

def simple_bettor(funds, inital_wager, wager_count):
    value = funds
    wager = inital_wager


    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        currentWager += 1
        print('Funds', value)

simple_bettor (10000, 100, 100)
