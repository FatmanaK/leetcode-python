from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        max_distance = 0
        for i in range(len(nums) - 1):
            first, second = nums[i], nums[i+1]
            diff = abs(first - second)
            max_distance = max(max_distance, diff)

        return max_distance


# Tests
s = Solution()
assert s.maximumGap([10]) == 0
assert s.maximumGap([3, 6, 9, 1]) == 3
