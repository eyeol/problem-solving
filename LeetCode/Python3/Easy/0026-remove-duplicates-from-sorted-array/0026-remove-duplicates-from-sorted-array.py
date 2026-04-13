class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # index
        i = 0
        # 매번 nums 길이와 비교
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[j] == nums[i]:
                    nums.pop(j)
                else:
                    j += 1
            i += 1
        