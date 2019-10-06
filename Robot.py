# Importing required modules
import argparse

# Initializing variables
# Starting Position of the Robot is at 0,0
position = [0, 0]

# Move Commands
move_cmd = {
    "F": [0, 1],          # F - move forward 1 unit
    "B": [0, -1],         # B - move backward 1 unit
    "R": [1, 0],          # R - turn right 90 degrees
    "L": [-1, 0]          # L - turn left 90 degrees
}


# Creating a function to calculate the minimum distance a robot needs to traverse in order to reach the starting point
def min_distance(my_args):
    # Splitting the commands
    for i in my_args:
        parts = i.split(",")

    # Splitting each command into direction and units
    for cmd in parts:
        direction = cmd[0]
        unit = cmd[1]

        # Moving the current position according to the input commands
        if direction in move_cmd and unit.isnumeric():
            position[0] += move_cmd[direction][0] * int(unit)
            position[1] += move_cmd[direction][1] * int(unit)

    # Calculating Distance
    distance = abs(position[0]) + abs(position[1])
    print("The minimum amount of distance to get back to the starting point is:", distance)


def main():
    # creating a parser object
    myparser = argparse.ArgumentParser(description="Calculating Robot's Distance from Starting Point")

    # adding argument
    myparser.add_argument("commands", nargs='*', metavar="string", type=str,
                          help="All the commands separated by comma will be parsed to the output as the mimimum "
                               "distance to the origin point")

    # parsing the arguments from the standard input
    my_args = myparser.parse_args()

    # check if command argument has any input data.
    # If it has, then calculate the robot's distance from the starting point
    if len(my_args.commands) != 0:
        min_distance(my_args.commands)


if __name__ == '__main__':
    # Calling main function
    main()
