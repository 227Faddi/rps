import sys
import random
from enum import Enum

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        player_choice = input(f'\n{name}, guess which number i\'m thinking of... 1, 2, or 3.\n\n')

        if player_choice not in ['1', '2', '3']:
            print('You must enter 1, 2, or 3.')
            return play_guess_number()

        computer_choice = random.choice('123')
        player_choice = int(player_choice)
        computer_choice = int(computer_choice)

        print(f'\n{name}, you chose {player_choice}.')
        print(f'I was thinking about the number {computer_choice}.\n')

        def game_result(player_choice, computer_choice):
            nonlocal name
            nonlocal player_wins

            if player_choice == computer_choice:
                player_wins += 1
                return f'🥰 {name}, You win!'
            else:
                return f'\nSorry, {name}... Better luck next time!'
            
        result = game_result(player_choice, computer_choice)
        print(result)

        nonlocal game_count
        game_count += 1
        winning_rate = player_wins / game_count

        print(f'\nGame count: {game_count}')
        print(f'\n{name}\'s wins: {player_wins}')
        print(f'\nWinning percentage: {winning_rate:.2%}')

        while True:
            replay = input(f'\nWould you like to play another game {name}? (y/n):\n\n')
            if replay.lower() not in ['y', 'n']:
                print('\nInvalid input\nChoose between\ny(Yes) and (No)\n')
                continue
            else:
                break

        if replay.lower() == 'y':
            return play_guess_number()
        else:
            print('\nThanks for playing!!\n\n🎉🎉🎉\n')
            if __name__ == "__main__":
                sys.exit(f'Bye, {name} 👋, see you soon!')
            else:
                return

    return play_guess_number()