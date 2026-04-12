class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        th = N / 2

        done = {}
        for num in nums:
            records = 0
            if num not in done:
                for i in range(N):
                    if nums[i] == num:
                        records += 1
                        if records > th:
                            return num
                done[num] = records
            