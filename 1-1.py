# 배열
# 1. Two Sum
# 브루트포스

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            for m in range(len(nums)):
                if n == m:
                    continue

                if nums[n] + nums[m] == target:
                    return [n, m]
                