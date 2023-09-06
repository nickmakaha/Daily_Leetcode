#This problem is a bit odd, as my solution feels very "brute-force-esque," as I'm simply checking all possible 10 string combinations, but I suppose
#that's a necessity to actually solve this problem. Utilization of sets creates a huge speedup as insertion and lookup are O(1). 
#One interesting thing is that originally I appended to my string one character at a time in a for loop of range(pos, pos+10), but this slowed down
#my code an exorbitant amount. The reason for this is that a string can be treated as an array, so rather than just accessing a subset in O(1) time,
#I was adding each character in an O(n) time operation.
#Time complexity: O(n) - We are simply iterating through the list, but we do recheck multiple elements but it's still linear time. 
#Space complexity: O(n) - Worst case, every element is a unique substr so we'd have to store the entire string in different pieces in our set.

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        found = set()
        retList = set()
        pos = 0
        while(pos < len(s)-9):
            st = s[pos:pos+10]
            if((st) not in found):
                found.add((st))
            elif((st) in found and (st) not in retList):
                retList.add((st))
            pos += 1
            
        return retList
