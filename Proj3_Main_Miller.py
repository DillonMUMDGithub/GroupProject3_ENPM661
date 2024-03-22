


from ObstacleMatTest import ObstMatC2C,ObstMatC2G, ClosedMat,VisitedMat
import matplotlib.pyplot as plt
import time as time
from queue import PriorityQueue
import numpy as np
import random
import os
import cv2 as cv
import math

stepsize = 50
#Create Action Set
def Actions(state):
    ActionSet = []
    ActionRound = []
    x = state[0] 
    y = state[1]
    theta =state[2] 
    for degchange in [-60,-30,0,30,60]:
        NewTheta = math.radians(theta+degchange)
        xDist = stepsize*math.cos(NewTheta)
        # xRounded = round(stepsize*math.cos(NewTheta))
        yDist = stepsize*math.sin(NewTheta)
        # yRounded = round(stepsize*math.sin(NewTheta))
        NewAction = [x+xDist,y+yDist,theta+degchange]
        NewRound = [int(round(x+xDist)),int(round(y+yDist))]
        # NewRound = [int(x+xDist),int(y+yDist)]
        ActionRound.append(NewRound)
        ActionSet.append(NewAction)
        
        
        #ActionSet - -60, -30, 0 +30, +60
    return ActionSet,ActionRound
def CheckIfGoal(state,endNode):
    AtGoal = 0
    if (abs(state[0]-endNode[0])<10)and(abs(state[1]-endNode[1])<10)and(abs(state[2]-endNode[2])<30):
        AtGoal=1 
    return AtGoal
def CheckIfClosedOrObstacle(Roundedstate,ObstMatC2C,State):
    InObstacle = 0
    # if ClosedMat[Roundedstate[1]][Roundedstate[0]]==1:
    #     InObstacle=1
    # print(Roundedstate)
    # if State in ClosedList:
    #     InObstacle =1
    if Roundedstate[1]>499:
        InObstacle = 1
    elif Roundedstate[1]<0:
        InObstacle = 1    
    elif Roundedstate[0]<0:
        InObstacle = 1 
    elif Roundedstate[0]>1199:
        InObstacle = 1
    elif ObstMatC2C[Roundedstate[1]][Roundedstate[0]] == -1:
        InObstacle = 1   

    return InObstacle
def CheckIfVisited(Roundedstate,ClosedMat):
    Visited =0
    if ClosedMat[Roundedstate[1]][Roundedstate[0]]!=0:
        Visited=1
    
    
    return Visited

# Create two empty lists named OpenList and ClosedList
OpenList = []
ClosedList = []
ParentList = []
RoundedList = []
# Get the initial (Xi) and goal node (Xg) from the user
startNode = [0,0,0]
endNode = [350,800,0]

# OpenList.put(startNode)
StartC2C = 0
StartC2G = ObstMatC2G[startNode[0],startNode[1]]
StartTotalCost = StartC2G+StartC2C
startParent = 'N/A'

OpenQ = PriorityQueue()
OpenQ.put((StartTotalCost, [startNode,startParent,StartC2C,startNode]))

# ClosedMat[startNode[1]][startNode[0]] = 1

start = time.time()
count=0
# While (OpenList not EMPTY) and (Not reached the goal) do
# while not OpenQ.empty():
while count<1500000:
    count=count+1
    # x OpenList.get()
    # WorkingNode = OpenList.get()
    QPop = OpenQ.get()
    # Add x to ClosedList
    WorkingNode = QPop[1][0]
    WorkingRounded = QPop[1][3]
    WorkingC2C = QPop[1][2]
    TotalCost = QPop[0]
    
    # ClosedMat[WorkingRounded[1]][WorkingRounded[0]] = TotalCost
    ClosedList.append(WorkingNode)
    ParentList.append(WorkingRounded = QPop[1][2])
    IsGoal = CheckIfGoal(WorkingNode,endNode)
    # if x = Xg
    if IsGoal == 1:
        print("AtGoal)")
        # Run backtrack function
        # return SUCCESS
    # else
    else:
        ActionSet,ActionRound = Actions(WorkingNode)
        # forall u ∈ U(x)
        for i in range(0,len(ActionSet)):
            # x’ f(x,u) # Generating each valid action
            Obstacle = CheckIfClosedOrObstacle(ActionRound[i][0:2],ObstMatC2C,ActionSet[i])
            # if (x’ ∉ ClosedList) and (NOT in the obstacle space)
            if Obstacle ==0:
                
                Visited = CheckIfVisited(ActionRound[i],ClosedMat)
                # if (x’ ∉ OpenList) or (CostToCome(x’) = ∞)
                if Visited ==0 or ObstMatC2C[ActionRound[i][1]][ActionRound[i][0]]== np.inf:
                    # ParentList.append(WorkingNode)
                    NewC2C = WorkingC2C+stepsize
                    ObstMatC2C[ActionRound[i][1]][ActionRound[i][0]] = NewC2C
                    NewC2G = ObstMatC2G[ActionRound[i][1]][ActionRound[i][0]]
                    # print(ActionRound[i])
                    RoundedList.append([ActionRound[i][1],ActionRound[i][0],ActionSet[2]])
                    NewPut = (NewC2G+NewC2C,[[ActionSet[i][0],ActionSet[i][1],ActionSet[i][2]],WorkingNode,NewC2C,[ActionRound[i][1],ActionRound[i][0],ActionSet[2]]])
                    OpenQ.put(NewPut)
                    VisitedMat[ActionRound[i][1]][ActionRound[i][0]] = 1
                    ##
                    IsGoal = CheckIfGoal([ActionSet[i][0],ActionSet[i][1],ActionSet[i][2]],endNode)
    # if x = Xg
                    if IsGoal == 1:
                        print("AtGoal)")
                elif Visited ==1:
                    NewC2C = WorkingC2C+stepsize
                    NewC2G = ObstMatC2G[ActionRound[i][1]][ActionRound[i][0]]
                    OldCost = ClosedMat[ActionRound[i][1]][ActionRound[i][0]]
                    NewCost = NewC2C+NewC2G
                    if OldCost>NewCost:
                        NewPut = (NewC2G+NewC2C,[[ActionSet[i][0],ActionSet[i][1],ActionSet[i][2]],WorkingNode,NewC2C,[ActionRound[i][1],ActionRound[i][0],ActionSet[2]]])
                        OpenQ.put(NewPut)
                        VisitedMat[ActionRound[i][1]][ActionRound[i][0]] = 1
                    # print(NewPut)
                    # Parent(x’) x
                    # CostToCome(x’) CostToCome(x) + L(x,u) # L(x,u) is the cost of the action
                    # Cost(x’) CostToCome(x’) + CostToGo(x’)
                    # OpenList.put(x’)
            # else
                
                # If Cost(x’) > CostToCome(x) + L(x,u)
                    # Parent(x’) x
                    # CostToCome(x’) CostToCome(x) + L(x,u)
                    # Cost(x’) CostToCome(x’) + CostToGo(x’)
    if count%1000 ==0:
        print(count)
end = time.time()
print(end-start)      
#BackTRacking



        
plt.matshow(VisitedMat)
plt.show()