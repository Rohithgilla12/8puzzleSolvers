from copy import deepcopy
import sys
from texttable import Texttable
import time

goalState=[[1,2,3],[4,5,6],[7,8,0]]
initalState=[[2,8,5],[1,0,4],[7,6,3]]
queue1=[]
queue2=[]
visited1=[]
visited2=[]
goalFound=False

def moveLeft(state):
    temp = deepcopy(state[0])
    path = deepcopy(state[1])
    path.append('L')
    x = y =sys.maxsize
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i][j]==0:
                x=i
                y=j
    if (y-1 >=0):
        temp[x][y],temp[x][y-1]=temp[x][y-1],temp[x][y]
        return [temp,path]
    else:
        return None

def moveRight(state):
    temp = deepcopy(state[0])
    path = deepcopy(state[1])
    path.append('R')
    x = y =sys.maxsize
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i][j]==0:
                x=i
                y=j
    if (y+1 < 3):
        temp[x][y],temp[x][y+1]=temp[x][y+1],temp[x][y]
        return [temp,path]
    else:
        return

def moveUp(state):
    temp = deepcopy(state[0])
    path = deepcopy(state[1])
    path.append('U')
    x = y =sys.maxsize
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i][j]==0:
                x=i
                y=j
    if (x-1 >=0):
        temp[x][y],temp[x-1][y]=temp[x-1][y],temp[x][y]
        return [temp,path]
    else:
        return

def moveDown(state):
    temp = deepcopy(state[0])
    path = deepcopy(state[1])
    path.append('D')
    x = y =sys.maxsize
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i][j]==0:
                x=i
                y=j
    if (x+1 <3):
        temp[x][y],temp[x+1][y]=temp[x+1][y],temp[x][y]
        return [temp,path]
    else:
        return

def checkDone(point1,point2):
    for i in point1:
        for j in point2:
            if i[0]==j[0]:
                return (point1.index(i),point2.index(j))
    return False


goalState=[[1,2,3],[4,5,6],[7,8,0]]
queue1.append([initalState,[]])
queue2.append([goalState,[]])

start = time.clock()
while True:
    temp=queue1.pop(0)
    visited1.append(temp[0])
    if moveDown(temp) is not None:
        if moveDown(temp)[0] not in visited1:
            queue1.append(moveDown(temp))
    if moveUp(temp) is not None:
        if moveUp(temp)[0] not in visited1:
            queue1.append(moveUp(temp))
    if moveLeft(temp) is not None:
        if moveLeft(temp)[0] not in visited1:
            queue1.append(moveLeft(temp))
    if moveRight(temp) is not None:
        if moveRight(temp)[0] not in visited1:
            queue1.append(moveRight(temp))
    
    temp=queue2.pop(0)
    visited2.append(temp[0])
    if moveDown(temp) is not None:
        if moveDown(temp)[0] not in visited2:
            queue2.append(moveDown(temp))
    if moveUp(temp) is not None:
        if moveUp(temp)[0] not in visited2:
            queue2.append(moveUp(temp))
    if moveLeft(temp) is not None:
        if moveLeft(temp)[0] not in visited2:
            queue2.append(moveLeft(temp))
    if moveRight(temp) is not None:
        if moveRight(temp)[0] not in visited2:
            queue2.append(moveRight(temp))
    
    if checkDone(queue1,queue2) is not False:
        op = open('output.txt','a+')
        op.write("Goal found with Bi Directional Search approach!\n For the example: \n")
        tt=Texttable()
        tt.add_rows(initalState)
        op.write(tt.draw())
        i,j=checkDone(queue1,queue2)
        path1=queue1[i][1]
        path2=queue2[j][1]
        for i in range(len(path2)):
            if path2[i]=='R':
                path2[i]='L'
            elif path2[i]=='L':
                path2[i]='R'
            elif path2[i]=='U':
                path2[i]='D'
            else:
                path2[i]='U'
        path=path1+path2[::-1]
        k=[initalState,[]]
        for j in path:
            t = Texttable()
            if j=='L':
                k=moveLeft(k)
                t.add_rows(k[0])
                print("Moving Left")
                print(t.draw())
                op.write("\nMoving Left \n")
                op.write(t.draw())
                
            if j=='R':
                k=moveRight(k)
                t.add_rows(k[0])
                print("Moving Right")
                print(t.draw())
                op.write("\nMoving Right \n")
                op.write(t.draw())
                
            if j=='U':
                k=moveUp(k)
                t.add_rows(k[0])
                print("Moving Up")
                print(t.draw())
                op.write("\nMoving Up \n")
                op.write(t.draw())
                
            if j=='D':
                k=moveDown(k)
                t.add_rows(k[0])
                print("Moving Down")
                print(t.draw())
                op.write("\nMoving Down \n")
                op.write(t.draw())
                
            print("_"*20+"\n")
        print("Path is "+'->'.join(path))
        print("Number of nodes visited: "+str(len(visited1)+len(visited2)))
        print ("time_taken=",time.clock()-start)
        op.write(("Path is "+'->'.join(path))+"\n")
        op.write("Number of nodes visited: "+str(len(visited1)+len(visited2))+"\n")
        op.write("time_taken="+str(time.clock()-start)+"\n") 
        op.close()
        break