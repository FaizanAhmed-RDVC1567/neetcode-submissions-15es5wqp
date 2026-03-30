from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        if len(strs) <= 1:
            result.append(strs)
            return result
        for string in strs:
            # Converting the return of sorted to tuple to give immutable key to dict.
            sorted_str = tuple(sorted(string))
            anagram_map[sorted_str].append(string)

        for value in anagram_map.values():
            result.append(value)

        return result
        # The answer is accepted because the question allows the output in any order.

