#This one was just a sliding window problem. I wanted to use a set originally, but it requires iterating from the beginning rather than
#initializing a window to begin from, so I instead went for a hash-map but it's not very space-efficient, even though it's time complexity is good. 
#I plan to come back to this one and do a set implementation.

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur = 0
        dic = {}
        mx = 0
        for i in range(0, k):
            if(nums[i] in dic):
                dic[nums[i]] = dic[nums[i]] + 1
                
            else:
                dic[nums[i]] = 1
            cur += nums[i]
        if(len(dic) == k):
            mx = cur

        l = 0
        r = k
        while(r < len(nums)):
            if(nums[l] in dic):
                dic[nums[l]] = dic[nums[l]]-1
            else:
                dic[nums[l]] = 1
            if(dic[nums[l]] == 0):
                dic.pop(nums[l])
            cur = cur - nums[l] + nums[r]
            if(nums[r] in dic):
                dic[nums[r]] = dic[nums[r]] + 1
            else:
                dic[nums[r]] = 1
            if(len(dic) == k):
                mx = max(cur, mx)
            l += 1
            r += 1
        return(mx)
       # return 0
