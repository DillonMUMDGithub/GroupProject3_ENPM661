


from ObstacleMatTest import ObstMatC2C,ObstMatC2G, VisitedMat
import matplotlib.pyplot as plt
import time as time
from queue import PriorityQueue
import numpy as np
import random
import os
import cv2 as cv
import math

stepsize = 10
#Create Action Set
def Actions(state):
    ActionSet = []
    x = state[0] 
    y = state[1]
    theta =state[2] 
    for degchange in [-60,-30,0,30,60]:
        NewTheta = math.radians(theta+degchange)
        xDist = stepsize*math.cos(NewTheta)
        yDist = stepsize*math.sin(NewTheta)
        NewAction = [x+xDist,y+yDist,theta+degchange]
        ActionSet.append(NewAction)
        
        
        #ActionSet - -60, -30, 0 +30, +60
    return ActionSet
def CheckIfGoal(state,endNode):
    AtGoal = 0
    if (state[0]-endNode[0]<1.5)and(state[1]-endNode[1]<1.5)and(state[2]-endNode[2]<30):
        AtGoal=1 
    return AtGoal
def CheckIfClosedOrObstacle(state,ObstMatC2C,VisitedMat):
    
    
    return


# Create two empty lists named OpenList and ClosedList
OpenList = []
ClosedList = []

# Get the initial (Xi) and goal node (Xg) from the user
startNode = [0,0,0]
endNode = [300,1150,0]

OpenList.put(startNode)
# VisitedMat[startNode[1]][startNode[0]] = 1



# While (OpenList not EMPTY) and (Not reached the goal) do
while(len(OpenList!=0)):
    # x OpenList.get()
    WorkingNode = OpenList.get()
    # Add x to ClosedList
    ClosedList.append(WorkingNode)
    IsGoal = CheckIfGoal(WorkingNode,endNode)
    # if x = Xg
    if IsGoal == 1:
        print("AtGoal)")
        # Run backtrack function
        # return SUCCESS
    # else
    else:
        ActionSet = Actions(WorkingNode)
        # forall u ∈ U(x)
        for Act in ActionSet:
            # x’ f(x,u) # Generating each valid action
            
            # if (x’ ∉ ClosedList) and (NOT in the obstacle space)
            
                # if (x’ ∉ OpenList) or (CostToCome(x’) = ∞)
                
                    # Parent(x’) x
                    # CostToCome(x’) CostToCome(x) + L(x,u) # L(x,u) is the cost of the action
                    # Cost(x’) CostToCome(x’) + CostToGo(x’)
                    # OpenList.put(x’)
            # else
                # If Cost(x’) > CostToCome(x) + L(x,u)
                    # Parent(x’) x
                    # CostToCome(x’) CostToCome(x) + L(x,u)
                    # Cost(x’) CostToCome(x’) + CostToGo(x’)