def merge(nums1, m, nums2, n):
    # Initialize pointers
    i = m - 1  # Last element of nums1
    j = n - 1  # Last element of nums2
    k = m + n - 1  # Last position in merged array
    
    # Compare and place elements from end to start
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
