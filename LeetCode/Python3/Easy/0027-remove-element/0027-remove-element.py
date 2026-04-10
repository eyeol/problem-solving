class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        index = N - 1
        while index >= 0:
            if nums[index] == val:
                nums.pop(index)
            index -= 1
        return len(nums)