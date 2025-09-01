class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        key_to_index = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        index = key_to_index[ruleKey]
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
        
        return count