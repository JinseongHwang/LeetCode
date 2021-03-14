# 문자열 조작
# 819. Most Common Word
# 정규식과 딕셔너리 자료구조 활용

from typing import List
import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('[^\w]', ' ', paragraph).lower().split()
        words = filter(lambda x: x not in banned, words)
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1

        return max(counts, key=counts.get)


p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
sol = Solution()
print(sol.mostCommonWord(p, b))
