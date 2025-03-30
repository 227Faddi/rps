import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0


    def game():
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input('\nEnter ...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n')

        if player_choice not in ['1', '2', '3']:
            print('You must enter 1, 2, or 3.')
            return game()

        computer_choice = random.choice('123')

        player = int(player_choice)

        computer = int(computer_choice)

        print('\nYou chose ' + str(RPS(player)).replace('RPS.', '') + '.')
        print('Computer chose ' + str(RPS(computer)).replace('RPS.', '') + '.\n')

        def game_result(player, computer):
            if player == 1 and computer == 3:
                return '🥰 You win!'
            elif player == 2 and computer == 1:
                return '🥰 You win!'
            elif player == 3 and computer == 2:
                return '🥰 You win!'
            elif player == computer:
                return '🫡 Tie Game!'
            else:
                return '🐍 Computer wins!'
            
        print(game_result(player, computer))

        global game_count
        game_count += 1

        print('\nGame count:' + str(game_count))
        
        print()
        while True:
            replay = input('\nWould you like to play another game? (y/n):\n\n')
            if replay.lower() not in ['y', 'n']:
                print('\nInvalid input\nChoose between\ny(Yes) and (No)\n')
                continue
            else:
                break

        if replay.lower() == 'y':
            return game()
        else:
            print('\nThanks for playing!!\n\n🎉🎉🎉\n')
            sys.exit('Bye 👋, see you soon!')


rps()