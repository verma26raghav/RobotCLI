# RobotCLI
CLI application to parse commands and display the result. Inputs can be either passed as a string or a filename which contains commands as contents. 

Note
I have created 2 branches for this repository. Develop branch is for Python code and Ruby/RoboCLI branch is for Ruby code.

Prerequisites
1.	Download python version 2.7 or above from https://www.python.org/downloads/
2.	Download any editor of your choice. I preferred PyCharm software which can be downloaded from https://www.jetbrains.com/pycharm/download/#section=windows
	You can download the community version for this.

Running the tests for Python
1.	This is a scenario, where Commands are passed a string input:
	C:\Users\user\Desktop\Woven\Robot\RobotCLI>Robot.py F1,R1,B2,L1,B3

	Output:
	Source point of the robot is: [0,0]
	Destination point of the Robot is: [0, -4]
	The minimum amount of distance to get back to the starting point is: 4

2.	This is a scenario, where filename is used as an input:
	C:\Users\user\Desktop\Woven\Robot\RobotCLI>Robot.py -r Command.txt

	Output:
	Source point of the robot is: [0,0]
	Destination point of the Robot is: [0, -4]
	The minimum amount of distance to get back to the starting point is: 4

3.	This is a scenario, where inputs are not passed properly:
	C:\Users\user\Desktop\Woven\Robot\RobotCLI>Robot.py F@,2F

	Output:
	These commands were unknown to the robot: ['F@', '2F'], please input the commands again.

4.	This is a scenario, where some inputs are correct, and some are not passed properly:
	C:\Users\user\Desktop\Woven\Robot\RobotCLI>Robot.py F1,B2,S5,D3

	Output:
	These commands were unknown to the robot: ['S5', 'D3'], hence they have been ignored.
	Source point of the robot is: [0,0]
	Destination point of the Robot is: [0, -1]
	The minimum amount of distance to get back to the starting point is: 1

5.	This is a scenario, where filename is not correct:
	C:\Users\user\Desktop\Woven\Robot\RobotCLI>Robot.py -r Command.pdf

	Output:
	Error: Invalid file path/name. Path Command.pdf does not exist.

6.	This is a scenario, where input is not passed properly:
	C:\Users\user\Desktop\Woven\Robot\RobotCLI>Robot.py F1,B2,S5,D

	Output:
	Please input the commands properly. For more help write Filename.py -h.


Running the Tests for Ruby
1.	This is a scenario, where Commands are passed a string input:
	$ruby RobotCLI.rb F1,R1,B2,L1,B3

	Output:
	Destination point of the Robot is: 0 -4                                                                                       
	The minimum amount of distance to get back to the starting point is: 4

2.	This is a scenario, where input is not passed properly:
	$ruby RobotCLI.rb F1,R1,B2,L1,B

	Output:
	Please input the commands properly. 

3.	This is a scenario, where some commands are not right:
	$ruby RobotCLI.rb F1,R1,B2,L1,D5

	Output:
	These commands were unknown to the robot. Hence have been ignored:                                                            
	D5                                                                                                                            
	Destination point of the Robot is: 0 -1                                                                                       
	The minimum amount of distance to get back to the starting point is: 1
