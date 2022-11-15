from __future__ import print_function

import time
from sr.robot import *

R = Robot()
a_th = 1.5 # The threshold for controlling the linear distance
d_th = 0.4 # The threshold for controlling the orientation


silverList = [] # a list to count the number of silver tokens grabbed and save their codes.
goldenList = [] # a list to count the number of golden tokens and save their codes.

def silver_grabber(rot_y,dist,code_of_token):

    """This function works using the distance and orientation returned by the 
    function 'find_silver_token' and it tends to update the distatnce and the orientation of the 
    silver token each time using the functions turn and drive to reach the box. and also it is used to grab
    the token and append the list of silver tokens"""

    while (rot_y >= a_th or rot_y<=-a_th) : 
        turn(sign(rot_y-a_th) * 10,0.001)
        dist, rot_y,code_of_token = find_silver_token()
    while (dist >= d_th) :
        drive(30,0.01)
        dist, rot_y, code_of_token = find_silver_token()
    silverList.append(code_of_token)
    print("Got you silver box number:",len(silverList))
    R.grab()
    turn(20,0.1)
    
    

def go_to_golden_and_release(rot_y,dist,code_of_token):
    """This function works with the same principle of the function silver grabber, except 
    that it search for the nearest golden box and release the silver box near it """
    while(dist<0):
        turn(-5,0.01)
        dist, rot_y, code_of_token = find_golden_token()
    while (rot_y >= a_th or rot_y<=-a_th) :
        turn(sign(rot_y-a_th) * 10,0.001)
        dist, rot_y, code_of_token= find_golden_token()
    while (dist >= 1.5*d_th) :
        drive(40,0.01)
        dist, rot_y, code_of_token= find_golden_token()
    R.release()
    goldenList.append(code_of_token)
    print("Found you golden box number:",len(goldenList))
    drive(-30,0.8)

def drive(speed, seconds):
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = speed
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0
def sign(a):
	if a < 0:
		return -1
	else:
		return 1
def turn(speed, seconds):
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = -speed
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0

def find_silver_token():
	dist=100
	for token in R.see():
		if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and token.info.code not in silverList:
			dist=token.dist
			rot_y=token.rot_y
			code_of_token=token.info.code
	if dist==100:
		return -1, -1 ,-1
	else:    
		return dist, rot_y, code_of_token

def find_golden_token():

	dist=100
	for token in R.see():
		if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and token.info.code not in goldenList:
			dist=token.dist
			rot_y=token.rot_y
			code_of_token=token.info.code
	if dist==100:
		return -1, -1, -1
	else:
		
		return dist, rot_y, code_of_token

def main():

    #drive(30,2)
    while (len(goldenList)<6):
        """Let's start our task by finding the silver box using the following function"""
        dist, rot_y, code_of_token = find_silver_token()
        """This if statement to make the robot turn until it found a silver box"""
        if dist==-1:
            turn(10,0.1)
            continue
        """Now we have the orientation and the distance of the closest silver box so we ask
        the robot to go and grab it"""
        silver_grabber(rot_y,dist,code_of_token)
        print("Lets pair you with one of the golden boxes arround")
        """Now let's find a golden box"""
        dist, rot_y, code_of_token = find_golden_token()
        """Now we have the orientation and the distance of the closest golden box so we ask
        the robot to go and release the silver box near to it"""
        go_to_golden_and_release(rot_y,dist,code_of_token)
        print("")		
    drive(-30,2)
    turn(20,0.5)
    print("Mission done")
            
            
main()          
            
   	
  
	

