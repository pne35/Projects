def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = []
        amount = 0
        for count in range(len(nums)):
            if nums[count] not in seen:
                seen.append(nums[count])
        amount = len(seen)
        for x in range(len(nums)-amount):
            seen.append("_")
        return amount 

print(removeDuplicates([1,1,3,3,4]))
