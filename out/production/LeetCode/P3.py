class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in nums:
            if val in nums:
                nums.remove(val)
        if val in nums:
            nums.remove(val)
        return len(nums)