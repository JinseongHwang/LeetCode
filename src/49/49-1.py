# 문자열 조작
# 49. Group Anagrams
# 정렬하여 딕셔너리에 추가

from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 존재하지 않는 key를 삽입해도 Error가 발생하지 않게 하려면 defaultdict로 선언해야 한다.
        anagrams = collections.defaultdict(list)
        for word in strs:
            # 정렬된 단어의 문자 배열을 ''로 join한 값을 key로 가지게 한다.
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()
