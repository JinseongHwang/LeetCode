# 배열
# 1. Two Sum
# 첫 번째 수를 뺀 결과 키 조회

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리에 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # target에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            # 뺀 값이 딕셔너리에 존재하고 && num의 index와 뺀 값의 index가 다르다면
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
