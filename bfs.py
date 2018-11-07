from copy import deepcopy
import sys

goalState=[[1,2,3],[4,5,6],[7,8,0]]
initalState=[[1,2,3],[4,0,5],[7,8,6]]
queue=[]
visited=[]
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


def main(state):
    queue.append(state)
    while len(queue)!=0:
        temp=queue.pop(0)
        visited.append(temp[0])
        if moveDown(temp) is not None:
            if moveDown(temp)[0] not in visited:
                queue.append(moveDown(temp))
        if moveUp(temp) is not None:
            if moveUp(temp)[0] not in visited:
                queue.append(moveUp(temp))
        if moveLeft(temp) is not None:
            if moveLeft(temp)[0] not in visited:
                queue.append(moveLeft(temp))
        if moveRight(temp) is not None:
            if moveRight(temp)[0] not in visited:
                queue.append(moveRight(temp))
        for i in range(len(queue)):
            if queue[i][0] == goalState:
                global goalFound
                goalFound=True
                print(queue[i][1])
        if goalFound is True:
            break
if __name__ == '__main__':
    main([initalState,[]])