class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
       
       
        if target not in nums:
            return([-1,-1])
        max = 0
        fmax = False
        if nums[-1] == target:
            max = len(nums) - 1
            fmax = True
        min = 0
        for c in range(len(nums)):
            if (nums[c] == target):
                min = c
                if fmax != True:
                    for x in range(c,len(nums)):
                        if nums[x] != target:
                            max = x-1
                            break
                break

        return([min,max])
