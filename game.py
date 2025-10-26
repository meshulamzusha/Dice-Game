import utils

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


def input_function() -> str:
    return input(f'Choose whether you want to roll the dice or pass your turn (r/p). ')


def play_round(player: int, scores: dict):
    print(f"===Player {player}'s turn===\n"
          f"your score is: {scores[player]}\n"
          f"The opponent's score: {scores[1] if player == 2 else scores[2]}")

    decision = utils.turn_decision(input_function)

    if decision == 'r':
        roll_1, roll_2 = utils.roll_two_d6()
        new_score = roll_1 + roll_2 + scores[player]
        print(f'the result is: {roll_1} and {roll_2} the sum: {roll_1 + roll_2}'
              f' your score now is: {new_score}')

        scores[player] = new_score

    return decision


def play_game():
    scores = {1: 0, 2: 0}
    is_winer = False
    player = 1
    two_pass = ''

    while not is_winer:
        decision = play_round(player, scores)
        if decision == 'p':
            two_pass += 'p'

        if two_pass == 'pp':
            closer = closer_to_target(scores[1], scores[2], 100)
            if closer:
                winer = closer
                print(f'The winer is: player {winer}\n his score is {scores[winer]} Its closer to 100 after two pass decisions')
            else:
                winer = tie_breaker(utils.roll_two_d6)
                print(f'The winer is: player {winer}\n his score is {scores[winer]} He got more points in the decider after a draw')
            is_winer = True

        if utils.is_exact_100(scores[player]):
            winer = player
            print(f'The winer is: player {winer}\n his score is {scores[winer]} exactly')
            is_winer = True

        if utils.is_bust(scores[player]):
            winer = 2 if player == 1 else 1
            print(f'The winer is: player {winer}\n his score is {scores[winer]} He won because his opponent achieved more than the target')
            is_winer = True

        player = 2 if player == 1 else 1