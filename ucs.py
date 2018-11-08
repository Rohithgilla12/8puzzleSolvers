from copy import deepcopy
import sys

goalState=[[1,2,3],[4,5,6],[7,8,0]]
initalState=[[1,2,3],[7,8,0],[4,5,6]]
queue=[]
visited=[]
goalFound=False

class Node:
    def __init__(self,board,path):
        self.board=board
        self.path=path
    
    def moveLeft(self):
        temp = deepcopy(self.board)
        path = deepcopy(self.path)
        path.append('L')
        x = y = sys.maxsize
        for i in range(len(temp)):
            for j in range(len(temp)):
                if temp[i][j]==0:
                    x,y=i,j                    
        if (y-1>=0):
            temp[x][y],temp[x][y-1]=temp[x][y-1],temp[x][y]
            return Node(board=temp,path=path)
        else:
            return None            
    
    def moveRight(self):
        temp = deepcopy(self.board)
        path = deepcopy(self.path)
        path.append('R')
        x = y = sys.maxsize
        for i in range(len(temp)):
            for j in range(len(temp)):
                if temp[i][j]==0:
                    x,y=i,j                    
        if (y+1>=0):
            temp[x][y],temp[x][y+1]=temp[x][y+1],temp[x][y]
            return Node(board=temp,path=path)
        else:
            return None            
    
    def moveUp(self):
        temp = deepcopy(self.board)
        path = deepcopy(self.path)
        path.append('U')
        x = y = sys.maxsize
        for i in range(len(temp)):
            for j in range(len(temp)):
                if temp[i][j]==0:
                    x,y=i,j                    
        if (x-1 >=0):
            temp[x][y],temp[x-1][y]=temp[x-1][y],temp[x][y]
            return Node(board=temp,path=path)
        else:
            return None            
    
    def moveDown(self):
        temp = deepcopy(self.board)
        path = deepcopy(self.path)
        path.append('D')
        x = y = sys.maxsize
        for i in range(len(temp)):
            for j in range(len(temp)):
                if temp[i][j]==0:
                    x,y=i,j                    
        if (x+1>=0):
            temp[x][y],temp[x+1][y]=temp[x+1][y],temp[x][y]
            return Node(board=temp,path=path)
        else:
            return None
    
    def solve(self):
        queue.append(Node(self.board,[]))
        while len(queue)!=0:
            temp = queue.pop(0)
            visited.append(temp.board)
            if temp.moveDown() is not None:
                if temp.moveDown().board not in visited:
                    queue.append(temp.moveDown())
            if temp.moveUp() is not None:
                if temp.moveUp().board not in visited:
                    queue.append(temp.moveUp())
            if temp.moveLeft() is not None:
                if temp.moveLeft().board not in visited:
                    queue.append(temp.moveLeft())
            if temp.moveRight() is not None:
                if temp.moveRight().board not in visited:
                    queue.append(temp.moveRight())
            for i in range(len(queue)):
                if queue[i].board == goalState:
                    global goalFound
                    goalFound=True
                print("Path is "+'->'.join(queue[i][1]))
                print("Number of nodes visited"+str(len(visited)))
            if goalFound is True:
                break                    
