import random
import os

# draw grid
# pick random location for exit door
# pick random location for player
# pick radom location for monster
# draw player in the grid
# take input for movement
# move player, unless invalid movement
# check for win/loss
# clear screen redraw grid

CELLS = [(0, 0), (1, 0), (2, 0), (3 , 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3 , 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3 , 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3 , 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3 , 4), (4, 4)
]

def print_map(player):
    print("_"*5)
    tile = "|{}"
    for cell in CELLS:
        player_x, player_y = cell
        if player_x < 4:
            line_ending = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_ending = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end = line_ending)


def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    # get the players location
    player_x, player_y = player
        # if move == LEFT, x-1
    if move == 'LEFT' and player_x > 0:
        player_x -= 1
        return (player_x, player_y)
        # if move == RIGHT x + 1
    elif move == 'RIGHT' and player_x < 4:
        player_x += 1
        return (player_x, player_y)
        # if move == DOWN y - 1
    elif move == 'UP' and player_y > 0:
        player_y -= 1
        return (player_x, player_y)
        # if move == UP y + 1
    elif move == 'DOWN' and player_y < 4:
        player_y += 1
        return (player_x, player_y)
    else:
        print("Invalid player move")
        return (player_x, player_y)


def clear_Screen():
    os.system('cls' if os.name == 'nt' else "clear")

def get_moves(player):
    moves = ["LEFT", "UP", "RIGHT", "DOWN"]
    player_x, player_y = player
    if player_y == 4:
        moves.remove("UP")
    elif player_y == 0:
        moves.remove("DOWN")
    elif player_x == 0:
        moves.remove("LEFT")
    elif player_x == 4:
        moves.remove("RIGHT")
    else:
        return moves
    return (", ").join(moves)

player, monster, door = get_locations()

print("Welcome to the Dungeon!")
start = input("Press enter to start or 'Q' to quit.")
if start.upper() == 'Q':
    print("Okay see you next time!")
elif start == "":
    clear_Screen()
    while True:
        print("You're currently in room {}".format(player)) #fill with player position
        print("You can move {}".format(get_moves(player))) # fill with available moves

        print_map(player)
        move = input("> ")
        move = move.upper()

        if move == 'QUIT' or move == 'Q':
            break
        # good move? change player position
        else:
            clear_Screen()
            player = move_player(player, move)
            #print(move_player(player, move))


        # hit door? They win
        if player == door:
            print("You made it to the door!  You Win!")
            break
        elif player == monster:
            print("You hit the monster! Sorry you lose!:(")
            break;
        # hit monster? they lose
