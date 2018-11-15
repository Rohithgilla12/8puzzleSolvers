import collections
import itertools
from copy import deepcopy
from texttable import Texttable
totalNodes=0
import time
op=open('output.txt','a+')
op.write("Goal found with A star Search approach!\n For the example: \n")
class Node:
    def __init__(self, puzzle, parent=None, nextMove=None):
        self.puzzle=puzzle
        self.parent=parent
        self.nextMove=nextMove
        if self.parent != None:
            self.g = parent.g+1
        else:
            self.g=0
    
    @property
    def score(self):
        return (self.g+self.h)
    
    @property
    def state(self):
        return str(self)
    
    @property
    def path(self):
        node, path=self, []
        while node:
            path.append(node)
            node = node.parent
        yield from reversed(path)
    
    @property
    def solved(self):
        return self.puzzle.solved
    
    @property
    def nextMoves(self):
        return self.puzzle.nextMoves

    @property
    def h(self):
        return self.puzzle.manhattan

    @property
    def f(self):
        return self.g+self.h

    
    def __str__(self):
        return str(self.puzzle)
    

class Solver:
    def __init__(self,start):
        self.start=start
    
    def solve(self):
        queue = collections.deque([Node(self.start)])
        visited = set()
        visited.add(queue[0].state)
        while queue:
            global totalNodes
            totalNodes=len(queue)
            queue = collections.deque(sorted(list(queue),key=lambda node : node.f))
            node = queue.popleft()
            if node.solved:
                return node.path
            for move,nextMove in node.nextMoves:
                child = Node(move(),node,nextMove)

                if child.state not in visited:
                    queue.appendleft(child)
                    visited.add(child.state)

class Puzzle:
    def __init__(self,board):
        self.width = len(board[0])
        self.board = board

    @property
    def solved(self):
        n = self.width**2
        return str(self) == ''.join(map(str, range(1,n))) + '0'

    @property
    def nextMoves(self):
        def create_move(at,to):
            return  lambda: self._move(at,to)
        
        moves=[]
        for i,j in itertools.product(range(self.width),range(self.width)):
            direcs = {
                'R':(i,j-1),
                'L':(i,j+1),
                'U':(i+1,j),
                'D':(i-1,j)
            }
            for nextMove, (r,c) in direcs.items():
                if r >= 0 and c >= 0 and self.width > r and self.width > c and self.board[r][c]==0:
                    move = create_move((i,j),(r,c)),nextMove
                    moves.append(move)
        return moves
    
    @property
    def manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j]!=0:
                    x, y = divmod(self.board[i][j]-1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance
    
    def copy(self):
        return Puzzle(deepcopy(self.board))

    def _move(self,at,to):
        copy = self.copy()
        i , j = at
        r , c = to
        copy.board[i][j], copy.board[r][c] = copy.board[r][c], copy.board[i][j]
        return copy
    
    def pprint(self):
        op=open('output.txt','a+')
        x=Texttable()
        for row in self.board:
            x.add_row(row)
        print(x.draw())
        op.write(x.draw())
        op.write('\n')
    
    def __str__(self):
        return ''.join(map(str, self))
    
    def __iter__(self):
        for row in self.board:
            yield from row


board = [[2,8,5],[1,0,4],[7,6,3]]

puzzle = Puzzle(board)
s = Solver(puzzle)
start=time.clock()
p = s.solve()


steps = 0
for node in p:
    print(node.nextMove)
    node.puzzle.pprint()
    steps += 1

op.write("Total number of steps: " + str(steps-1)+"\n")
op.write("Total Number of nodes explored: "+str(totalNodes-1)+"\n")
op.write("time_taken=" +str(time.clock()-start))
print("Total number of steps: " + str(steps-1))
print("Total Number of nodes explored: "+str(totalNodes-1))
print ("time_taken=",time.clock()-start)
op.close()