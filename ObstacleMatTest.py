#Establish Obstacle Matrix   
import numpy as np 
import matplotlib.pyplot as plt
import cv2
from PIL import Image
#Create a C2C Matrix represntation of the map
ObstMatC2C = np.full((500,1200),np.inf)
#Create a C2G representation of the map
ObstMatC2G = np.full((500,1200),-1)

ObstMatR = np.full((500,1200),0)
ObstMatG = np.full((500,1200),0)
ObstMatB = np.full((500,1200),0)


# def normalize(im):
#    # Normalise image to range 0..1
#     min, max = im.min(), im.max()
#     return (im.astype(float)-min)/(max-min)
# ObstMatC2C[]
# print(ObstMatC2C[500][0])
print(ObstMatC2C.shape)
for i in range(94,180):
    for k in range(89,500):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 255
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 0
        
for i in range(99,175):
    for k in range(94,500):
        ObstMatC2C[k][i] = -1
        ObstMatB[k][i] = 255
        ObstMatR[k][i] = 0
        
# print(ObstMatC2C[150][300])
for i in range(269,354):
    for k in range(0,404):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 255
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 0
for i in range(274,349):
    for k in range(0,399):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 0
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 255        
        
#right obstacle

for i in range(1014,1104):
    for k in range(44,454):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 255
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 0
for i in range(1019,1099):
    for k in range(49,449):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 0
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 255
for i in range(894,1019):
    for k in range(369,454):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 255
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 0
for i in range(899,1019):
    for k in range(374,449):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 0
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 255
        
for i in range(894,1019):
    for k in range(45,124):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 255
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 0
for i in range(899,1019):
    for k in range(49,119):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 0
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 255        
        
#Hexagon

#MiddleRectangle:
for i in range(514,784):
    for k in range(174,324):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 255
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 0
        #Red Barrier Middle Rectangle
for i in range(519,779):
    for k in range(174,324):
        ObstMatC2C[k][i] = -1
        ObstMatR[k][i] = 0
        ObstMatG[k][i] = 0
        ObstMatB[k][i] = 255       
        
#TopLeftTriangle
GRat = 80/135
for i in range(514,649):
    for k in range(324,404):
        # ObstMatC2C[k][i] = -1
        XTemp = i-514
        YTemp = k-324
        if (XTemp*GRat)>YTemp:
            ObstMatC2C[k][i] = -1
            ObstMatR[k][i] = 255
            ObstMatG[k][i] = 0
            ObstMatB[k][i] = 0 
#Tope Left No Barrier
GRat = 75/130
for i in range(519,649):
    for k in range(324,399):
        # ObstMatC2C[k][i] = -1
        XTemp = i-519
        YTemp = k-324
        if (XTemp*GRat)>YTemp:
            ObstMatC2C[k][i] = -1
            ObstMatR[k][i] = 0
            ObstMatG[k][i] = 0
            ObstMatB[k][i] = 255            
            
            
#TopRight Triangle
GRat = -80/135          
for i in range(649,784):
    for k in range(324,404):
        # ObstMatC2C[k][i] = -1
        XTemp = i-649
        YTemp = k-324
        if (XTemp*GRat)+80>YTemp:
            ObstMatC2C[k][i] = -1
            ObstMatR[k][i] = 255
            ObstMatG[k][i] = 0
            ObstMatB[k][i] = 0 
            #TopRight No barrier
GRat = -75/130        
for i in range(649,779):
    for k in range(324,399):
        # ObstMatC2C[k][i] = -1
        XTemp = i-649
        YTemp = k-324
        if (XTemp*GRat)+75>YTemp:
            ObstMatC2C[k][i] = -1
            ObstMatR[k][i] = 0
            ObstMatG[k][i] = 0
            ObstMatB[k][i] = 255        #Need to fix  
#BotRightTriangle
GRat = 80/135
for i in range(649,784):
    for k in range(94,174):
        # ObstMatC2C[k][i] = -1
        XTemp = i-649
        YTemp = k-94
        if (XTemp*GRat)<YTemp:
            ObstMatC2C[k][i] = -1
            ObstMatR[k][i] = 255
            ObstMatG[k][i] = 0
            ObstMatB[k][i] = 0 
GRat = 75/130
for i in range(649,779):
    for k in range(99,174):
        # ObstMatC2C[k][i] = -1
        XTemp = i-649
        YTemp = k-99
        if (XTemp*GRat)<YTemp:
            ObstMatC2C[k][i] = -1
            ObstMatR[k][i] = 0
            ObstMatG[k][i] = 0
            ObstMatB[k][i] = 255 
#BotLeft Triangle
GRat = -80/135          
for i in range(514,649):
    for k in range(94,174):
        # ObstMatC2C[k][i] = -1
        XTemp = i-514
        YTemp = k-94
        if (XTemp*GRat)+80<YTemp:
            ObstMatC2C[k][i] = -1
            ObstMatR[k][i] = 255
            ObstMatG[k][i] = 0
            ObstMatB[k][i] = 0     
GRat = -75/130        
for i in range(519,649):
    for k in range(99,174):
        # ObstMatC2C[k][i] = -1
        XTemp = i-519
        YTemp = k-99
        if (XTemp*GRat)+75<YTemp:
            ObstMatC2C[k][i] = -1
            ObstMatR[k][i] = 0
            ObstMatG[k][i] = 0
            ObstMatB[k][i] = 255      
            

# print(ObstMatC2C[375][564])
#Using Euclidean distance for C2G
# print(len(ObstMatC2C[1]))
GoalPoint = [1150,300]

for i in range(0,1200):
    
    for k in range(0,500):
        # print(i,k)
        if ObstMatC2C[k][i] == np.inf:
            x1 = i
            y1 = k
            x2 = GoalPoint[0]
            y2 = GoalPoint[1]
            distance = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            distance=round(distance)
            # print(distance)
            ObstMatC2G[k][i] = distance
            # if distance==0:
            #     print(0)
            #     break


# x=np.linspace(0,1199)
# # y=np.linspace(0,499)
# n1 = normalize(ObstMatR) * 255.999
# n2 = normalize(ObstMatG) * 255.999
# n3 = normalize(ObstMatB) * 255.999
ObstMat3d = np.dstack((ObstMatR,ObstMatG,ObstMatB))

plt.matshow(ObstMatC2G)
plt.show()
# A = np.array(([0 ,1],[0,1]))
# cv2.imshow(ObstMatC2C)