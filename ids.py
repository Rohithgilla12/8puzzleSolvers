from copy import deepcopy
import sys

goalState=[[1,2,3],[4,5,6],[7,8,0]]
initalState=[[1,3,0],[4,2,5],[7,8,6]]
limit=10
queue=[]
visited=[]
totalNodes=0
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


def main(state,limit):
    queue.append(state)
    while len(queue)!=0:
        temp=queue.pop()
        visited.append(temp[0])
        if moveDown(temp) is not None:
            if moveDown(temp)[0] not in visited and len(moveDown(temp)[1]) <=limit :
                queue.append(moveDown(temp))
        if moveUp(temp) is not None:
            if moveUp(temp)[0] not in visited and len(moveUp(temp)[1]) <=limit :
                queue.append(moveUp(temp))
        if moveLeft(temp) is not None:
            if moveLeft(temp)[0] not in visited and len(moveLeft(temp)[1]) <=limit :
                queue.append(moveLeft(temp))
        if moveRight(temp) is not None:
            if moveRight(temp)[0] not in visited and len(moveRight(temp)[1]) <=limit :
                queue.append(moveRight(temp))
        for i in range(len(queue)):
            if queue[i][0] == goalState:
                global goalFound
                goalFound=True
                print(queue[i][1])
        if goalFound is True:
            return True

i=1
while i < limit:
    totalNodes=totalNodes+len(visited)
    queue=[]
    visited=[] 
    if main([initalState,[]],i) is True:
        print("Minimum depth required is: "+str(i))
        print(totalNodes)
        i=limit+1
    i+=1


    
