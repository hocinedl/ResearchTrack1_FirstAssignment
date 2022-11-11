from __future__ import print_function

import time
from sr.robot import *

"""rlength = R.info.length

def rotate(speed,angle):
	s = expresseion
	turn(speed,s)
	while(dist<0):
		turn(5,0.05)
		dist, rot_y, code_of_token = find_golden_token()
	rotate(speed,rot_y)
	goto(speed,dist)
"""

a_th = 1.5
d_th = 0.4
silver= True

R = Robot()

silverList = []

goldenList = []

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
		print("Silver token N': ", code_of_token)    
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
		print("Golden token N': ", code_of_token)
		return dist, rot_y, code_of_token

   	
   	
#turn(20,1)
drive(30,2)
while (len(silverList)<6):
	dist, rot_y, code_of_token = find_silver_token()
	
	if dist==-1:
		turn(10,0.1)
		continue
	while (rot_y >= a_th or rot_y<=-a_th) : #make it as a function that detects silver token orientation and update the angle rot_y. and same for other loops. make one loop that do all of this 
		turn(sign(rot_y-a_th) * 10,0.001)
		dist, rot_y,code_of_token = find_silver_token()
		
	while (dist >= d_th) :
		drive(30,0.01)
		dist, rot_y, code_of_token = find_silver_token()
	
	print("Trying to see u")	
	#if code_of token == 
	R.grab()
	print("Got you")
	silverList.append(code_of_token)
	#turn(30,1)
	print("Lets find your pair from golden boxes arround")
	dist, rot_y, code_of_token = find_golden_token()
	while(dist<0):
		turn(5,0.01)
		dist, rot_y, code_of_token = find_golden_token()
	while (rot_y >= a_th or rot_y<=-a_th) :
		turn(sign(rot_y-a_th) * 10,0.001)
		dist, rot_y, code_of_token= find_golden_token()
	while (dist >= 1.7*d_th) :
		drive(40,0.01)
		dist, rot_y, code_of_token= find_golden_token()
	R.release()
	drive(-30,0.1)
	goldenList.append(code_of_token)
	turn(20,2)		
turn(20,1)
drive(30,2)	
   	
   	
   	
   	
  
	

