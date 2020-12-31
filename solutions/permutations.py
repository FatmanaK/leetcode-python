from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        permutations = []
        for i, num in enumerate(nums):
            child_permutations = self.permute(nums[:i]+nums[i+1:])
            for cp in child_permutations:
                permutations.append([num] + cp)

        return permutations


s = Solution()
print(s.permute([1, 2, 3]))
