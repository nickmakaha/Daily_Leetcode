#This problem was an interesting one for me since I'd never seen a path existing problem in an array format. It actually took me about an hour
#to figure out, as I was not sure how to setup the overall stack structure to perform DFS. After wrestling for a bit, I found
#that a hash map creates a simple way to keep track of all nodes and their adjancencies (Could probably use an adjacency list, but I'm not
#yet comfortable with those. Also, using a set/unordered map for the visited nodes is essential, as using a list would progressively get slower
#and up time complexity by a significant amount. O(n) insertions vs O(1) insertions.

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        dic = {}
        if(len(edges) == 0):
            return True
        for i in edges:

            if(i[0] not in dic):
                dic[i[0]] = []
                dic[i[0]].append(i[1])
            elif(i[0] in dic):
                dic[i[0]].append(i[1])
            if(i[1] not in dic):
                dic[i[1]] = []
                dic[i[1]].append(i[0])
            elif(i[1] in dic):
                dic[i[1]].append(i[0])
            
       # for k in dic:
       #     print("Key" + str(k))
       #     print("Value")
       #     print(dic[k])

        #start = dic[source]
        if source not in dic or destination not in dic: return False
        stack = [source]
        explored = {}
        while(len(stack) > 0):
            cur = stack.pop()
            explored[cur] = 0
            if(cur == destination):
                return True
            else:
                for k in dic[cur]:
                   # print(k)
                   if(k == destination):
                       return True
                   else:
                        if(k not in explored):
                            stack.append(k)
                    
        

