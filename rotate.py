# Given an array arr[] of size N, the task is to rotate the array by d position to the left.

# Examples: 

# Input:  arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3, 4, 5, 6, 7, 1, 2
# Explanation: If the array is rotated by 1 position to the left, 
# it becomes {2, 3, 4, 5, 6, 7, 1}.
# When it is rotated further by 1 position,
# it becomes: {3, 4, 5, 6, 7, 1, 2}

# Input: arr[] = {1, 6, 7, 8}, d = 3
# Output: 8, 1, 6, 7

arr=[1,6,7,8]
d=int(input())
for i in range(len(arr)):
    for j in range(i+d,len(arr)):
        arr[i]=arr[j]
    j+=1

print(arr)