from copy import deepcopy
import sys
from texttable import Texttable
import time

goalState=[[1,2,3],[4,5,6],[7,8,0]]
initalState=[[2,8,5],[1,0,4],[7,6,3]]
limit=18
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
                op = open('output.txt','a+')
                op.write("Goal found with Depth Limit approach!\n For the example: \n")
                tt=Texttable()
                tt.add_rows(initalState)
                op.write(tt.draw())
                print(queue[i])
                global goalFound
                goalFound=True
                k=[initalState,[]]
                for j in queue[i][1]:
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
                print("Path is "+'->'.join(queue[i][1]))
                print("Number of nodes visited: "+str(len(visited)))
                op.write("\nPath is "+'->'.join(queue[i][1])+"\n")
                op.write("Number of nodes visited: "+str(len(visited))+"\n")
                op.close()
if __name__ == '__main__':
    start=time.clock()
    main([initalState,[]])
    print ("time_taken=",time.clock()-start)