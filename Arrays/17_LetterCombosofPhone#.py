class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {}
        ch = 'a'
        if(len(digits) == 0):
          return None
        ret = set()
       # print(chr(ord('a') + 1))
        for i in range(2,10):
          for j in range(0, 3):
           # print(i)
           if(i not in dic):
              dic[i] = [ch]
           else:
             dic[i].append(ch)
           ch = chr(ord(ch) + 1)
           if(i == 7 and j == 2 or i == 9 and j == 2):
             dic[i].append(ch)
             ch = chr(ord(ch) + 1)
        if(len(digits) == 1):
          for k in dic[int(digits[0])]:
            ret.add(k)
          return ret
       # for ind, k in enumerate(digits):
        adder =  set(dic[int(digits[0])][:])
        num = 0
        ind = 1
        while(num != len(digits)-1):
          added = set()
          for i in adder:
            for j in (dic[int(digits[ind])]):
              added.add(i+j)
             # print(i)
          print(added)
          adder = added
          num += 1
          ind += 1
          
        return adder
          
               
 
               
        return ret
             
             

