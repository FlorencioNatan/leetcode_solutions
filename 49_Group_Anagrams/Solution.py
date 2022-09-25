from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for st in strs:
            sorted_str = ''.join(sorted(st))
            if (sorted_str not in groups):
                groups[sorted_str] = []
            groups[sorted_str].append(st)

        groups_list = []
        for lis in groups.values():
            groups_list.append(lis)
        return groups_list
