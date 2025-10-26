from random import randint

def roll_two_d6() -> tuple[int, int]:
    roll_1 = randint(1, 6)
    roll_2 = randint(1, 6)

    return roll_1, roll_2


def is_bust(score: int) -> bool:
    return score > 100


def is_exact_100(score: int) -> bool:
    return score == 100


def turn_decision(input_fn) -> str:
    decision = ''

    while decision != 'p' and decision != 'r':
        decision = input_fn()
        print(decision)
    return decision



