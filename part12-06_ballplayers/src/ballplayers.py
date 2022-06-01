class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals(players: list):
    return max(players, key=lambda player: player.goals).name

def most_points(players: list):
    player = max(players, key=lambda player: player.goals + player.passes)
    return (player.name, player.number)

def least_minutes(players: list):
    return min(players, key=lambda player: player.minutes)


if __name__ == "__main__":
    a = BallPlayer("Pete",4,12,6,900) 
    b = BallPlayer("Arnold",6,14,11,885)
    c = BallPlayer("John",9,19,2,840)
    d = BallPlayer("Kim", 3,11,9,1034)

    list = [a, b, c, d]

    for player in list:
        print(player.name, player.goals)

    print(most_points(list))