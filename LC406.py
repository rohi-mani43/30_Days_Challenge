class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        
        result = []
        
        for person in people:
            height, k = person
            result.insert(k, person)
        
        return result
