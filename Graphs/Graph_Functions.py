#This is just a file I'll continually fill with random graph work I'd like to do in order to practice traversals/obtaining info


# Online Python - IDE, Editor, Compiler, Interpreter

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None 

root = Node(3)
leftchild = Node(4)
root.left = leftchild
rightchild = Node(5)
root.right = rightchild
leftchild.left = Node(20)
leftchild.right = Node(50)
rightchild.left = Node(2000)
rightchild.right = Node(20000000)
rightchild.right.right = Node(0)


def levels(root):
    current = []
    current.append(root)
    level = 1
    dic = {}
    while(len(current) > 0):
        cop = []
        for i in current:
         if(level not in dic):
             dic[level] = [i.val]
         else:
             dic[level].append(i.val)
         if(i.left is not None):
             cop.append(i.left)
         if(i.right is not None):
             cop.append(i.right)
        current = cop
        level += 1
    return dic
        
def numLeaves(root):
        if(root.left == None and root.right == None):
            return 1 
        else:
            if(root.left is not None and root.right is not None):
                return numLeaves(root.left) + numLeaves(root.right)
            elif(root.left is None):
                return numLeaves(root.right)
            else:
                return numLeaves(root.left)        
        
    
print(levels(root))
print(numLeaves(root))    


