# 문자열 조작
# 937. Reorder Data in Log Files
# 람다식과 '+' 연산자를 사용

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        # 우선적으로 identifier를 제외한 단어들을 기준으로 정렬하고,
        # 동일한 경우에 identifier를 비교해서 정렬한다.
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + digit


sol = Solution()
input = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(sol.reorderLogFiles(input))
