# Importing required modules
import argparse

# Initializing variables
# Starting Position of the Robot is at 0,0
position = [0, 0]

# Move Commands
move_cmd = {
    "F": [0, 1],  # F - move forward 1 unit
    "B": [0, -1],  # B - move backward 1 unit
    "R": [1, 0],  # R - turn right 90 degrees
    "L": [-1, 0]  # L - turn left 90 degrees
}


# Creating a function to calculate the destination point of the robot
def destinationcoordinate(my_args):
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

    # Destination Point of the Robot
    print("Destination point of the Robot is: ", position)
    return position


# Creating a function to calculate the minimum distance a robot needs to traverse in order to reach the starting point
def min_distance(coordinates):
    # Calculating Distance
    distance = abs(coordinates[0]) + abs(coordinates[1])
    print("The minimum amount of distance to get back to the starting point is:", distance)


def main():
    # creating a parser object
    myparser = argparse.ArgumentParser(description="Calculating minimum amount of units the robot will need to "
                                                   "traverse in order to get back to it's starting point")

    # adding argument
    myparser.add_argument("commands", nargs='*', metavar="string", type=str,
                          help="All the commands separated by comma will be parsed to the output as the minimum "
                               "distance to the origin point. "
                               "Example of providing inputs:"
                               " F1,R1,B2,L1,B3")

    # parsing the arguments from the standard input
    my_args = myparser.parse_args()

    # check if command argument has any input data.
    # If it has, then calculate the robot's distance from the starting point
    if len(my_args.commands) != 0:
        # Calling function to compute the destination coordinates
        coordinates = destinationcoordinate(my_args.commands)

        # Calling function to compute the minimum distance back to source
        min_distance(coordinates)
        quit()
    else:
        print("Please enter alteast one command. Use filename -h for more instructions.")
        quit()


if __name__ == '__main__':
    # Calling main function
    main()
