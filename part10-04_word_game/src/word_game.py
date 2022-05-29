# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        if len(player2_word) > len(player1_word):
            return 2
        return 3

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        count1 = 0
        count2 = 0
        for vowel in "aeiou":
            count1 += player1_word.count(vowel)
            count2 += player2_word.count(vowel)
        if count1 > count2:
            return 1
        if count2 > count1:
            return 2
        return 3

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_inputs = {"rock": 0, "paper": 1, "scissors": 2}

        if player1_word not in valid_inputs.keys() and player2_word not in valid_inputs.keys():
            return 3
        if player1_word not in valid_inputs.keys():
            return 2
        if player2_word not in valid_inputs.keys():
            return 1
        
        # big brain solution
        big_brain = valid_inputs[player1_word] - valid_inputs[player2_word]

        if big_brain == 0:
            return 3
        
        if big_brain == 1 or big_brain == -2:
            return 1
        
        return 2

        # smooth brain solution
        # if player1_word not in valid_inputs and player2_word not in valid_inputs:
        #     return 3
        # elif player1_word not in valid_inputs and player2_word in valid_inputs:
        #     return 2
        # elif player2_word not in valid_inputs and player1_word in valid_inputs:
        #     return 1
        # elif player1_word == player2_word:
        #     return 3
        # elif (player1_word == "rock" and player2_word == "scissors") or (player1_word == "paper" and player2_word == "rock") or (player1_word == "scissors" and player2_word == "paper"):
        #     return 1
        # return 2

