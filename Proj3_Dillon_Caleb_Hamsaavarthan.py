"""Project 3, A* Algorithm implementation
    """
    
    
from ObstacleMatTest import ObstMatC2C,ObstMatC2G
import matplotlib.pyplot as plt
import time as time
from queue import PriorityQueue
import numpy as np
import random
import os
import cv2 as cv

    
def MoveUp(Node,C2C):
    NewNode = Node.copy()
    NewNode[1] = NewNode[1]+1
    NewCost = C2C+1
    return(NewNode,NewCost)
def MoveDown(Node,C2C):
    NewNode = Node.copy()
    NewNode[1] = NewNode[1]-1
    NewCost = C2C+1
    return(NewNode,NewCost)
def MoveLeft(Node,C2C):
    NewNode = Node.copy()
    NewNode[0] = NewNode[0]-1
    NewCost = C2C+1
    return(NewNode,NewCost)
def MoveRight(Node,C2C):
    NewNode = Node.copy()
    NewNode[0] = NewNode[0]+1
    NewCost = C2C+1
    return(NewNode,NewCost)
def MoveUL(Node,C2C):
    NewNode = Node.copy()
    NewNode[0] = NewNode[0]-1
    NewNode[1] = NewNode[1]+1
    NewCost = C2C+1.4
    return(NewNode,NewCost)
def MoveUR(Node,C2C):
    NewNode = Node.copy()
    NewNode[0] = NewNode[0]+1
    NewNode[1] = NewNode[1]+1
    NewCost = C2C+1.4
    return(NewNode,NewCost)
def MoveDL(Node,C2C):
    NewNode = Node.copy()
    NewNode[0] = NewNode[0]-1
    NewNode[1] = NewNode[1]-1
    NewCost = C2C+1.4
    return(NewNode,NewCost)
def MoveDR(Node,C2C):
    NewNode = Node.copy()
    NewNode[0] = NewNode[0]+1
    NewNode[1] = NewNode[1]-1
    NewCost = C2C+1.4
    return(NewNode,NewCost)
def CheckifGoal(Node,GoalNode):
    Stop = 0
    if Node ==GoalNode:
        Stop = 1
    return Stop
def CheckIfObstacle(Node, ObstMatC2C):
    InObstacle = 0
    if Node[1]>499:
        InObstacle = 1
    elif Node[1]<0:
        InObstacle = 1    
    elif Node[0]<0:
        InObstacle = 1 
    elif Node[0]>1199:
        InObstacle = 1
    elif ObstMatC2C[Node[1]][Node[0]] == -1:
        InObstacle = 1   
    return InObstacle
def CheckClosed(Node,Closed):
    InClosed = 0
    if Node in Closed:
        InClosed = 1
    return InClosed
def CheckAllClosed(Nodes,Closed):
    InClosedMat = [0,0,0,0,0,0,0,0]
    for ClosedMat in Closed:
        if Nodes[0]==ClosedMat:
            InClosedMat[0] = 1
        if Nodes[1]==ClosedMat:
            InClosedMat[1] = 1
        if Nodes[2]==ClosedMat:
            InClosedMat[2] = 1
        if Nodes[3]==ClosedMat:
            InClosedMat[3] = 1
        if Nodes[4]==ClosedMat:
            InClosedMat[4] = 1
        if Nodes[5]==ClosedMat:
            InClosedMat[5] = 1
        if Nodes[6]==ClosedMat:
            InClosedMat[6] = 1
        if Nodes[7]==ClosedMat:
            InClosedMat[7] = 1    
    
    return InClosedMat


startNode = [0,0]
endNode = [1150,300]
# startNode = [random.randint(0,50),random.randint(50,450)]
# endNode = [random.randint(1050,1149),random.randint(50,450)]
OriginalC2C = 0
WorkingC2C = 0

OpenQ = []
ClosedQ = []
ClosedC2C = []
VisitedQ = []
ClosedParent = []
Parent = []
C2C = []
OpenQ.append(startNode)
C2C.append(0)
TotalQ = PriorityQueue()
TotalQ.put((0, [startNode,'N/A']))
ClosedQPrio = PriorityQueue()

imgmat = []
Parent.append('N/A')
Go = 1



Stop = 0
start = time.time()
while(Stop==0):
    # plt.show(block=False)
    try:
        Go=Go+1
        # print(Go)
    
        
        QPop = TotalQ.get()
        WorkingC2C = QPop[0]
        WorkingNode = QPop[1][0]
        WorkingParent = QPop[1][1]
        Stop = CheckifGoal(WorkingNode,endNode)
        if Stop ==1:
            FinalNode = WorkingNode
            FinalParent = WorkingParent
            FinalC2C = WorkingC2C
            break
        # print(WorkingNode)
        # ClosedQPrio.put(())
        # ClosedQ.append(WorkingNode)
        # ClosedParent.append(WorkingParent)
        # ClosedC2C.append(WorkingC2C)

        Up,UpC2C = MoveUp(WorkingNode,WorkingC2C)
        A = CheckIfObstacle(Up,ObstMatC2C)
        if A ==0:
            B = CheckClosed(Up,ClosedQ)
            if B ==0:
                if UpC2C<ObstMatC2C[Up[1]][Up[0]]:
                    ObstMatC2C[Up[1]][Up[0]] = UpC2C
                    # ObstMatG[Up[1]][Up[0]] = 255
                    OpenQ.append(Up)
                    Parent.append(WorkingNode)
                    C2C.append(UpC2C)
                    TotalQ.put((UpC2C,[Up,WorkingNode]))   

            
        Down,DownC2C =MoveDown(WorkingNode,WorkingC2C)
        A = CheckIfObstacle(Down,ObstMatC2C)
        if A ==0:
            B = CheckClosed(Down,ClosedQ)
            if B ==0:
                if DownC2C<ObstMatC2C[Down[1]][Down[0]]:
                    ObstMatC2C[Down[1]][Down[0]] = DownC2C
                    # ObstMatG[Down[1]][Down[0]] = 255
                    OpenQ.append(Down)
                    Parent.append(WorkingNode)
                    C2C.append(DownC2C)
                    TotalQ.put((DownC2C,[Down,WorkingNode])) 
                    
        Left,LeftC2C =MoveLeft(WorkingNode,WorkingC2C)
        A = CheckIfObstacle(Left,ObstMatC2C)
        if A ==0:
            B = CheckClosed(Left,ClosedQ)
            if B ==0:
                if LeftC2C<ObstMatC2C[Left[1]][Left[0]]:
                    ObstMatC2C[Left[1]][Left[0]] = LeftC2C
                    # ObstMatG[Left[1]][Left[0]] = 255
                    OpenQ.append(Left)
                    Parent.append(WorkingNode)
                    C2C.append(LeftC2C)
                    TotalQ.put((LeftC2C,[Left,WorkingNode])) 
                    
        Right,RightC2C =MoveRight(WorkingNode,WorkingC2C)
        A = CheckIfObstacle(Right,ObstMatC2C)
        if A ==0:
            B = CheckClosed(Right,ClosedQ)
            if B ==0:
                if RightC2C<ObstMatC2C[Right[1]][Right[0]]:
                    ObstMatC2C[Right[1]][Right[0]] = RightC2C
                    # ObstMatG[Right[1]][Right[0]] = 255
                    OpenQ.append(Right)
                    Parent.append(WorkingNode)
                    C2C.append(RightC2C)
                    TotalQ.put((RightC2C,[Right,WorkingNode])) 
                    
        UL,ULC2C =MoveUL(WorkingNode,WorkingC2C)
        A = CheckIfObstacle(UL,ObstMatC2C)
        if A ==0:
            B = CheckClosed(UL,ClosedQ)
            if B ==0:
                if ULC2C<ObstMatC2C[UL[1]][UL[0]]:
                    ObstMatC2C[UL[1]][UL[0]] = ULC2C
                    # ObstMatG[UL[1]][UL[0]] = 255
                    OpenQ.append(UL)
                    Parent.append(WorkingNode)
                    C2C.append(ULC2C)
                    TotalQ.put((ULC2C,[UL,WorkingNode])) 
                    
        UR,URC2C =MoveUR(WorkingNode,WorkingC2C)
        A = CheckIfObstacle(UR,ObstMatC2C)
        if A ==0:
            B = CheckClosed(UR,ClosedQ)
            if B ==0:
                if URC2C<ObstMatC2C[UR[1]][UR[0]]:
                    ObstMatC2C[UR[1]][UR[0]] = URC2C
                    # ObstMatG[UR[1]][UR[0]] = 255
                    OpenQ.append(UR)
                    Parent.append(WorkingNode)
                    C2C.append(URC2C)
                    TotalQ.put((URC2C,[UR,WorkingNode])) 
                    
        DL,DLC2C =MoveDL(WorkingNode,WorkingC2C)
        A = CheckIfObstacle(DL,ObstMatC2C)
        if A ==0:
            B = CheckClosed(DL,ClosedQ)
            if B ==0:
                if DLC2C<ObstMatC2C[DL[1]][DL[0]]:
                    ObstMatC2C[DL[1]][DL[0]] = DLC2C
                    # ObstMatG[DL[1]][DL[0]] = 255
                    OpenQ.append(DL)
                    Parent.append(WorkingNode)
                    C2C.append(DLC2C)
                    TotalQ.put((DLC2C,[DL,WorkingNode])) 
                    
        DR,DRC2C =MoveDR(WorkingNode,WorkingC2C)
        A = CheckIfObstacle(DR,ObstMatC2C)
        if A ==0:
            B = CheckClosed(DR,ClosedQ)
            if B ==0:
                if DRC2C<ObstMatC2C[DR[1]][DR[0]]:
                    ObstMatC2C[DR[1]][DR[0]] = DRC2C
                    # ObstMatG[DR[1]][DR[0]] = 255
                    OpenQ.append(DR)
                    Parent.append(WorkingNode)
                    C2C.append(DRC2C)
                    TotalQ.put((DRC2C,[DR,WorkingNode])) 
        if Go%1500 ==0:
            print(Go)
            # ObstMat3d = np.dstack((ObstMatR,ObstMatG,ObstMatB))
            # imgname = "Temp"+str(Go)+".png"
            # cv.imwrite(imgname, ObstMat3d)
            # img = cv.imread(imgname)
            # imgmat.append(img)
            # os.remove(imgname) 
            # video.write(img)
            # os.remove("Tempimg.png") 
            
        
    except:
        break
# video.release()
# os.remove("Tempimg.png") 
end = time.time()    
print(end-start)    


# Least = TotalQ.get()
# print(Least)
LeastC2C = FinalC2C
LeastNode = FinalNode
LeastParent = FinalParent
print(WorkingC2C)
print(WorkingNode)
print(WorkingParent)

print(len(Parent))
print(len(OpenQ))
# B = TotalQ.get([LeastParent])
# print(B)
TrackBack = []
# B = OpenQ.index(LeastParent)
# print(B)
# C = OpenQ[B]
end=1
while (end==1):
    # print(startNode)
    B = OpenQ.index(LeastParent)
    # print(B)   
    C = OpenQ[B]
    TrackBack.append(C)
    # print(C)
    D = Parent[B]
    LeastParent = D
    if D == [0,0]:
        end = 0
    elif D == startNode:    
        end = 0
TrackBack.append(startNode)
print(TrackBack)
counttrack = 0
for pixel in TrackBack:
    try:
        ObstMatC2C[pixel[1]][pixel[0]] = -1
        ObstMatC2C[pixel[1]-1][pixel[0]] = -1
        ObstMatC2C[pixel[1]+1][pixel[0]] = -1
        ObstMatC2C[pixel[1]][pixel[0]-1] = -1
        ObstMatC2C[pixel[1]][pixel[0]+1] = -1
        # ObstMatR[pixel[1]][pixel[0]] = -1
        # ObstMatR[pixel[1]-1][pixel[0]] = 255
        # ObstMatR[pixel[1]+1][pixel[0]] = 255
        # ObstMatR[pixel[1]][pixel[0]-1] = 255
        # ObstMatR[pixel[1]][pixel[0]+1] = 255
        # ObstMatG[pixel[1]][pixel[0]] = 255
        # ObstMatG[pixel[1]-1][pixel[0]] = 255
        # ObstMatG[pixel[1]+1][pixel[0]] = 255
        # ObstMatG[pixel[1]][pixel[0]-1] = 255
        # ObstMatG[pixel[1]][pixel[0]+1] = 255
        # ObstMatB[pixel[1]][pixel[0]] = 255
        # ObstMatB[pixel[1]-1][pixel[0]] = 255
        # ObstMatB[pixel[1]+1][pixel[0]] = 255
        # ObstMatB[pixel[1]][pixel[0]-1] = 255
        # ObstMatB[pixel[1]][pixel[0]+1] = 255
        counttrack = counttrack+1
        #Append the trackback iamges to the 
        # if counttrack%20 ==0:
        #     print(counttrack)
        #     ObstMat3d = np.dstack((ObstMatR,ObstMatG,ObstMatB))
        #     imgname = "Temp"+str(Go)+".png"
        #     cv.imwrite(imgname, ObstMat3d)
        #     img = cv.imread(imgname)
        #     imgmat.append(img)
        #     os.remove(imgname) 
    except:
        break
    
 #Append 10 frames of the final path (1second)   
# for i in range (0,10):
#     ObstMat3d = np.dstack((ObstMatR,ObstMatG,ObstMatB))
#     imgname = "Temp"+str(Go)+".png"
#     cv.imwrite(imgname, ObstMat3d)
#     img = cv.imread(imgname)
#     imgmat.append(img)
#     os.remove(imgname)    
    
# print("len im mat",len(imgmat))       
# video=cv.VideoWriter('TestVideo.mp4',cv.VideoWriter_fourcc(*'MP4V'),10,(1200,500))
# for i in range(0,len(imgmat)):
#     video.write(imgmat[i])
# video.release()
# cv.destroyAllWindows()
print(len(ClosedQ))
print(len(ClosedC2C))
print(len(ClosedParent))
# ObstMat3d = np.dstack((ObstMatR,ObstMatG,ObstMatB))
# cv.imwrite("FinalMap.png", ObstMat3d)
# plt.matshow(ObstMatC2C)
# plt.show()


plt.matshow(ObstMatC2C,cmap = 'gray')
plt.show()