# There are two sorted arrays. First one is of size m+n containing only m elements. Another one is of size n and contains n elements. 
# Merge these two arrays into the first array of size m+n such that the output is sorted. 
def merge(nums1, m, nums2, n):
    # Initialize two pointers, one for nums1 and one for nums2
    p1, p2 = m - 1, n - 1
    # Initialize the end of the merged array
    end = m + n - 1

    # Merge from the end of the arrays to the beginning
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[end] = nums1[p1]
            p1 -= 1
        else:
            nums1[end] = nums2[p2]
            p2 -= 1
        end -= 1

    # If there are remaining elements in nums2, copy them to nums1
    # while p2 >= 0:
    #     nums1[end] = nums2[p2]
    #     p2 -= 1
    #     end -= 1

# Example usage:
nums1 = [2,0,7,0,0,10,0,0]
m=0
for i in nums1:
    if i==0:
        m+=1
print(m)
nums2 = [5,8,12,14]
n=len(nums2)
print(n)

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

