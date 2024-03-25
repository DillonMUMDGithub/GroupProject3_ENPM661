# GroupProject3_ENPM661
Group Project, Project 3, ENPM661 Miller, Myers, Ravichandar


Libraries used in the code:
- cv2
- heapq
- math
- numpy
- time


Given below are the instructions to execute a code written for the implementation of
‘2D Optimal Path Planning’ for a mobile robot in a workspace space with obstacles,
using A* Algorithm.
- In the map (dimensions: 1200 * 500) shown below:
• The ‘Free Space’ for the point robot is depicted by ‘White’ pixels
• The ‘Obstacle Space’ are denoted by ‘Blue’ pixels
• A ‘Clearance Space’ of user-defined value from obstacles and walls are given by
‘Black’ pixels

Instructions to execute the code:
- The source code is a python file written using Visual Studio Code and I’ve
attached the (a_star_Caleb_Dillon_Hamsaavarthan.py) format for execution.
- Run ‘.py’ in the VS Code for execution.
- Enter the (x, y), where x in range [0,1200] and y in range [0,500], coordinates for
the ‘Start’ and ‘Goal’ respectively, one at a time node as requested by the code,
with the respect to the origin at the bottom-left corner of the map shown above.
- Followed by the orientation of mobile robot at the source and goal nodes
respectively, from the values [180, 150, 120, …, 30, 0, -30, -60, …, -150].
- If the given coordinates are not reachable (belongs to obstacle space), the code will
prompt with “The given coordinates are not reachable. Try again with different
coordinates”.
- Provided with valid ‘Start’ and ‘Goal’ coordinates, the code will display the
‘Optimal Path’, as example shown below, for 5 seconds. (Press any ‘key’ to quit).


- The output of an animated video ‘A*_output.avi’, will be created as a demonstration for node exploration and optimal path travelling for reference.
The ‘Start’ and ‘Goal’ nodes are denoted by ‘Yellow’ and ‘Purple’ circles
respectively.


Link to the GitHub Repository:
https://github.com/DillonMUMDGithub/GroupProject3_ENPM661/tree/main


Caleb Myers - cmyers17 - 120504440
Dillon Miller - Dmille19 - 121013316
Hamsaavarthan Ravichandar - rhamsaa - 120516979
