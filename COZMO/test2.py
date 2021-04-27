import cozmo
from cozmo.util import degrees

def cozmo_program(robot: cozmo.robot.Robot):
	robot.turn_in_place(degrees(5000)).wait_for_completed()
	
	
	
	


cozmo.run_program(cozmo_program)