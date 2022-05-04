


def who_won(game_board: list):
    first = 0
    second = 0
    for row in game_board:
        first += row.count(1)
        second += row.count(2)
    if first > second:
        return 1
    elif second > first:
        return 2
    else: 
        return 0
