#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'zork.json'
item_file = 'items.json'
current = ['BUNKER','BACKROOM','ZOMROOM','FRSTDEST']

def load_files():
    try:
        __location__= os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__,game_file)) as json_file: game = json.load(json_file)
        return game
    except:
        print("There was a problem reading either the game of item file.")
        os._exit(1)

def render(game,current):
    c = game[current]
    print("You are at the " + c["name"])
    print(c["desc"]

def get_input():
    response = input("What do you want to do?")
    response= response.upper().strip()
    return response

def update(game,current,choice):
    c = game[current]
    for e in c["exits"]:
        if choice == e["exit"]:
            return e["target"]
    return current

# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        with open(os.path.join(__location__, item_file)) as json_file: items = json.load(json_file)
        return (game,items)
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)

# The main function for the game
def main():
    current = 'START'  # The starting location
    end_game = ['END']  # Any of the end-game locations

    (game,items) = load_files()

    while True:
        render(game,current)
        for e in end_game:
            if current == e:
                print("GAME OVER")
                break

        response = get_input()

        if response == "QUIT" or response == "Q":
            break
        current = update(game,current,response)
    print("Thanks for playing")

# run the main function
if __name__ == '__main__':
	main()