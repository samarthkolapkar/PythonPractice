# Given an array of positive integers. All numbers occur an even number of times except one 
# number which occurs an odd number of times. Find the number in O(n) time & constant space.

# Examples : 

# Input : arr = {1, 2, 3, 2, 3, 1, 3}
# Output : 3

# Input : arr = {5, 7, 2, 7, 5, 2, 5}
# Output : 5

arr=[1,2,3,2,3,1,3]
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            count+=1
        
if count%2!=0:
    print(arr[i])

