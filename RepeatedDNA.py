class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        res = set()

        for i in range(len(s) - 9):  # substrings of length 10
            sub = s[i:i+10]
            if sub in seen:
                res.add(sub)
            else:
                seen.add(sub)

        return list(res)
