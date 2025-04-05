from rps import rock_paper_scissors
from guess_number import guess_number
import sys

def play_arcade(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_arcade(name)

        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors(name)
        elif playerchoice == "2":
            guess_number(name)
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    play_arcade(args.name)