# Creating a class name RobotCLI
class RobotCLI
    
  # Constructor for initializing values
  def initialize(posX, posY)
    # Initializing the starting position of the Robot
    @posX = posX
    @posY = posY
    
    # Move Commands
    @move_cmd = Hash.new
    @move_cmd["F"] = [0,1]       # F - move forward 1 unit
    @move_cmd["B"] = [0,-1]      # B - move backward 1 unit
    @move_cmd["L"] = [-1,0]      # L - turn left 90 degrees
    @move_cmd["R"] = [1,0]       # R - turn right 90 degrees
  end

  # Creating a function to calculate the destination point of the robot    
  def destinationcoordinate(arguments)
    # Creating a list for unknown commands
    unknown_cmd = []
    
    # Splitting the commands
    arguments.each do |step|
      step = step.split(',')
      # Splitting each command into direction and units
      step.each do |cmd|
        # Checking if the length of one command is more than 2, if yes then ask user to input again
        if cmd.length > 2 or cmd.length <2
            print "Please input the commands properly."
            exit!
        else
            direction = cmd[0]
            unit = cmd[1].to_i
            
            # Moving the current position according to the input commands
            if @move_cmd.has_key? direction 
                @posX += @move_cmd[direction][0] * unit
                @posY += @move_cmd[direction][1] * unit
            else
                unknown_cmd.push cmd
            end
        end
     end
    end
    # Print any unknown commands
    if unknown_cmd.length > 0
        puts "These commands were unknown to the robot. Hence have been ignored:", unknown_cmd 
    end
  end
  
  # Creating a function to display the destination position
  def displayPosition
    print @posX, " ", @posY, "\n"
  end
    
  # Creating a function to calculate the minimum distance a robot needs to traverse in order to reach the starting point
  def min_distance
    (@posX).abs + (@posY).abs
  end
end

  # Reading command line arguments 
  arguments=ARGV
  
  # Initializing the class and calling the Constructor
  robot = RobotCLI.new(0, 0)
  
  # Calling function to compute the destination coordinates
  robot.destinationcoordinate(arguments)
  print "Destination point of the Robot is: "
  
  # Calling function to display the destination coordinates
  robot.displayPosition
  print "The minimum amount of distance to get back to the starting point is: "
  
  # Calling function to compute the minimum distance back to source
  puts robot.min_distance
