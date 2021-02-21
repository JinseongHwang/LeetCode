# 문자열 조작
# 125. Valid Palindrome
# Deque 자료형을 활용한 최적화

import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        dq = collections.deque()

        for c in s:
            if c.isalnum():
                dq.append(c.lower())

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False

        return True