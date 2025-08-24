class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=nums1+nums2
        nums3.sort()
        l=len(nums3)
        m=float()
        if l%2==0:
            m=(nums3[int(l/2)]+nums3[int(l/2)-1])/2.0
        else:
            m=nums3[int(l/2)]
        return m      