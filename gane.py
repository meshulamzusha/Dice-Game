from random import randint

def roll_two_d6() -> tuple[int, int]:
    roll_1 = randint(1, 6)
    roll_2 = randint(1, 6)

    return (roll_1, roll_2)


def is_bust(score: int) -> bool:
    return score > 100


def is_exact_100(score: int) -> bool:
    return score == 100 


def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    distance_1 = target - a
    distance_2 = target - b

    closer = None

    if distance_1 < distance_2:
        closer = 1
    if distance_2 < distance_1:
        closer = 2

    return closer


def tie_breaker(roller) -> int:
    roll_p1 = (0, 0)
    roll_p2 = (0, 0)

    winer = 0

    while sum(roll_p1) == sum(roll_p2):
        roll_p1 = roller()
        roll_p2 = roller()

    if sum(roll_p1) > sum(roll_p2):
        winer = 1
    if sum(roll_p2) > sum(roll_p1):
        winer = 2

    return winer

def turn_decision(input_fn) -> str:
    decision = ''

    while decision != 'p' or decision != 'r':
        decision = input_fn()

    return decision


def input_function() -> str:
    return input(f'Choose whether you want to roll the dice or pass your turn (r/p). ')


def play_game():
    score_1 = 0
    score_2 = 0
    is_winer = False

    while not is_winer:
        
# .רצופים, הכרעת שוויון, הודעות ניצחון Pass לולאת המשחק הראשית: ניהול ניקוד, תורות, שני
