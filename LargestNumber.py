class Solution(object):
    def largestNumber(self, nums):
       
        str_nums = [str(num) for num in nums]
        
        from functools import cmp_to_key
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        str_nums.sort(key=cmp_to_key(compare))
        
        result = ''.join(str_nums)
        
        return '0' if result[0] == '0' else result
