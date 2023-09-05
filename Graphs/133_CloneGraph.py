"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if node == None:
            return None
        stack = []
        dic = {}
        stack.append(node)
        while(len(stack) != 0):
            cur = stack.pop()
            if cur not in dic:
                dic[cur] = Node(cur.val)
            for i in cur.neighbors:
                if i not in dic:
                    dic[i] = Node(i.val)
                    stack.append(i)



        for i in dic:
            for j in i.neighbors:
                dic[i].neighbors.append(dic[j])
        return dic[node]
            
               

        
