class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)  # For O(1) lookups
        n = len(s)
        
        # dp[i] = True if s[:i] can be segmented into words from wordDict
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always valid
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
