class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[0]
        for char in s:
            if char=="(":
                stack.append(0)
            else:
                curr=stack.pop()
                score=max(2*curr,1)
                stack[-1]+=score
        return stack[0]
        
        