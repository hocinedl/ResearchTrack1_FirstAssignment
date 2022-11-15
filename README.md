RT1_Assignment #1
=================

This repository contains my solution for the first assignment of RT1 in which we were asked to make a robot grabs silver boxes and place them near golden boxer, making pairs of silver and golden boxes. So we should have at the end 6 pairs of Silver Golden Boxes.

### Global variables:

a_th : The threshold for controlling the linear distance
d_th : The threshold for controlling the orientation

silverList = [] : List contains the codes of silver boxes.
goldenList = [] : List contains the codes of golden boxes.

The code is composed of different functions that I created:

### Drive and Turn functions:

These two functions are the same of exercice 1, they're functions that make the robot drive forward with fixed speed or Turn with specific orientation.

### Find_silver_token & find_golden_token:
This function tries to find the nearest silver box, by updating the distance of nearest silver non paired (not in List) token..
<pre>
find_silver_token():
 	Initialize distance to 100
 	for token in R.see():
		 if token_distance less than distance and Type of token is Silver and Token is not in silverList:
			 distance=token_distance
			 rotation=token_rotation
			 code_of_token=token_code
	 if distance is equal 100
		 return -1, -1 ,-1
 	else:    
		 return distance, rotation, code_of_token
</pre>
Same principle for the function find_golden_token


### silver_grabber:

This function works using the distance and orientation returned by the function 'find_silver_token' and it tends to update the distatnce and the orientation of the silver token each time using the functions turn and drive to reach the token. and also it is used to grab the token and append the list of silver tokens.
we call the function by passing the 3 arguments returned by the function find_silver_token (dist and orientation and the code of the box).

<pre>
    while (Robot Not in the right orientation): 
        turn the robot
        return distance, orientation, code of the box
    while (Robot is Far from Box) :
        drive the robot forward
        return distance, orientation, code of the box
    Append silverList
    R.grab()
</pre>


### go_to_golden_and_release:

After the silver box has been grabbed, we need to find the closest golden box to release it. So we call the function find_golden_token which returns the distance and the orientation and the code of the nearest golden token, we use the function go_to_golden_and_release in order to drive the tobot to our target (golden box).
It is compsed of loops for which each loop update the distance or the orientation.

<pre>
   while(distance is less than 0):
        turn the robot
        return distance, orientation, code of the box
    while (Robot Not in correct orientation) :
        turn the robot
        return distance, orientation, code of the box
    while (Robot is Far from Box) :
        drive the robot forward
        return distance, orientation, code of the box
    R.release_Token()
    Append goldenList
</pre>


### main:

<pre>
while (Number_silver_box <6):
        find_silver_token & return dist, orientation;
        if (distance is 100):
            turn the robot
            continue (find_silver)
            
        silver_grabber(rot_y,dist,code_of_token)
       
        find_golden_token & return dist, orientation;        
        go_to_golden_and_release(rot_y,dist,code_of_token)
        		
 print("Mission done")
    
</pre>

### The link for the Flowchart:
[The First Assignment Flowchart](https://drive.google.com/file/d/14NtOxaicDS87whEtD8bkOSqdCr2F6GDI/view?usp=sharing).
