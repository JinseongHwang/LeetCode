# 문자열 조작
# 819. Most Common Word
# 정규식과 Counter 객체를 활용 - 1

from typing import List
import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
sol = Solution()
print(sol.mostCommonWord(p, b))
