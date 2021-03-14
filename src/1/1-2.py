# 배열
# 1. Two Sum
# in을 이용한 탐색

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target에서 첫 값을 뺀 값이 존재하는지 in으로 판단하는 방법이다.
        # in으로 존재 확인을 진행하는 범위를 점차 좁혀나간다.
        for i, num in enumerate(nums):
            complement = target - num

            if complement in nums[i + 1:]:
                return nums.index(num), nums[i + 1:].index(complement) + (i + 1)
