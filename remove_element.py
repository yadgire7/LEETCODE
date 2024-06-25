class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        unique_list = []
        for i in range(len(nums)):
            if nums[i] != val:
                unique_list.append(nums[i])
            else:
                pass
        for i in range(len(unique_list)):
            nums[i] = unique_list[i]
        
        return len(unique_list)
        
