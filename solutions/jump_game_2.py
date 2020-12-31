import sys
from typing import List


class Solution:

    def __init__(self):
        pass

    def jump(self, nums: List[int]) -> int:

        if not nums or len(nums) < 2:
            return 0

        first = nums[0]
        if first == 0:
            return sys.maxsize

        if first >= len(nums) - 1:
            return 1

        candidates = []
        for j in range(1, first + 1):
            candidates.append(self.jump(nums[j:]))

        ans = 1 + (min(candidates) if candidates else 0)

        return ans


s = Solution()

assert s.jump([]) == 0
assert s.jump([1, 1]) == 1
assert s.jump([2, 3, 1, 1, 1]) == 2
assert s.jump([2, 3, 1, 1, 4]) == 2
assert s.jump([1, 2, 3]) == 2
assert s.jump([2, 0, 2, 4, 6, 0, 0, 3]) == 3
