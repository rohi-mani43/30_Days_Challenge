class Solution(object):
    def lengthOfLastWord(self, s):
        
        b=[str(i) for i in s.split()]
        return len(b[-1])