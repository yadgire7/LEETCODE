class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_dict = {}
        counter = 0
        for i in range(len(nums)):    
            if nums[i] in unique_dict.values():
                pass
            else:
                unique_dict[counter] = unique_dict.get(counter, nums[i])
                counter = counter + 1
        for i in range(len(unique_dict)):
            nums[i] = unique_dict[i]
        return len(unique_dict)
        
        return len(unique_dict.keys())
        
