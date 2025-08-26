class Solution(object):
    def threeSum(self, nums):
       
        set_ans = set()
        nums.sort()

        for i in range(len(nums)-2):

            left = i+1
            right = len(nums) -1
            while left < right:
                temp = nums[i]+nums[left]+nums[right]
                if temp == 0:
                    set_ans.add((nums[i], nums[left],nums[right]))
                    right -= 1
                    left += 1
                    
                elif temp > 0:
                    right -=1
                else:
                    left +=1
        return list(set_ans)