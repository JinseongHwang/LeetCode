# 문자열 조작
# 125. Valid Palindrome
# 문자열 슬라이싱

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 패턴에 걸리지 않는 값(^)들을 공백('')으로 바꾼다. 대상은 문자열 s이다.
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]  # 뒤집어도 같으면 펠린드롬이다.
