#I was surprised that this solution was in the 90th percentile for both speed and storage, as when writing it I felt as though there was something I was missing and
#an obvious better approach. I'm not a huge fan of utilizing a dictionary to list conversion, nor a fan of the wasted space in my 2nd dictionary, but my logic
#was to maintain two separate dictionaries, one to track frequencies of elements, and one to track elements at a given frequency. This made it possible
#for me to simply iterate through the frequency of elements dictionary in reverse K total times to obtain my result.

class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        dic2 = {}

        for i in nums:
            if(i in dic):
                dic[i] += 1
                if dic[i] in dic2:
                    dic2[dic[i]].append(i)
                else:
                    dic2[dic[i]] = [i]
            else:
                dic[i] = 1
                if(dic[i] in dic2):
                    dic2[dic[i]].append(i)
                else:
                  dic2[dic[i]] = [i]
        ret = set()
        num = 0
        ind = 0
        adds = 0
        for i in list(dic2)[::-1]:
            for j in (dic2[i]):
                print(j)
                if j not in ret: 

                    ret.add(j)
                    adds += 1
                    if(adds == k):
                        return ret
        return ret
