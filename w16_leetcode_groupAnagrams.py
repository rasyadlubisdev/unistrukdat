class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        keyToAnagrams = defaultdict(list)

        for str in strs:
            key = "".join(sorted(str))
            keyToAnagrams[key].append(str)

        for _, anagrams in keyToAnagrams.items():
            ans.append(anagrams)

        return ans
