
# Find the majority element in the array. A majority element in an array A[] of size n is an element that appears more than n/2 
# times (and hence there is at most one such element). 


# Examples : 

# Input : A[]={3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4
# Explanation: The frequency of 4 is 5 which is greater than the half of the size of the array size. 

# Input : A[] = {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element
# Explanation: There is no element whose frequency is greater than the half of the size of the array size.arr=[1,1,2,3,1]


arr=[1,1,1,2,3]
count= 1
maxcount=0
index=-1
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            count+=1
            
    if count>maxcount:
        maxcount=count
        index=i
        
if maxcount>len(arr)//2:
    print(arr[index])