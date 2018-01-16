"""
Runs an instance of the tiger game. Command line input has the following format:

python play.py [player] [max_time]

player: The options are "Human" or "AI". If playing with a human player, the
user will be prompted with "What action would you like to make? " The options
are "left", "right" or "listen". The options are case sensitive. If playing with
an AI player, the player will play according to the predetermined strategy.

max_time: The number of time steps over which the game is played.
"""

import sys
import numpy as np

from game import Game
from agent import Agent, AI_Agent, Human_Agent
#from agent import Human_Agent
# _state variable exists for testing only - do not initialize
def play(player, max_time, _state = None):
    time = 0
    game = Game()
    if player == "AI":
        player = AI_Agent()
    elif player == "Human":
        player = Human_Agent()
    print("ready for solving1")
    while time < max_time:
        print("Step " + str(time + 1) + ":")
        if isinstance(player, Human_Agent):
            if time == max_time - 1:
                print("> This is your last move! Pick wisely!")
            move = input("What action would you like to make? ")
            move = player.pick_action(move)
        else:
            move = player.pick_action()
        print("You chose to make the move: " + str(move))
        reward, observation = game.respond(move)
        if move not in ("listen", "left", "right"):
            print("> You have attempted to deceive the game. You automatically lose. Cheaters never win.")
            sys.exit()
        player.update_observation(observation)
        if move == "listen":
            print("> You chose to listen!")
            tiger_sound(observation)
        player.update_reward(reward)
        print("> You received a reward of " + str(reward) + "\n")
        time += 1
    print("Game over! Total Reward: " + str(player.get_reward()) + "\n")

def tiger_sound(observation):
    print("> The tiger sound came from the " + observation + " door")

if __name__ == "__main__":
    args = sys.argv
    # whether the player is human or AI
    print("ready for solving")

    player = args[1]
    # the number of time steps over which the game occurs
    max_time = int(args[2])

    play(player, max_time)
