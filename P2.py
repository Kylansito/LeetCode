class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i,v in enumerate(sorted(list(set(nums)))):
            nums[i]=v
        return i+1