class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i,nums in enumerate(nums):
            if target-nums in hash_table:
                if i != hash_table[target-nums]:
                    return [i,hash_table[target-nums]]
            hash_table[nums] = i
            