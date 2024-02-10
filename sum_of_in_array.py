# Q1) Given an array A[] of n numbers and another number x, the task is to check whether or not there exist two elements 
# in A[] whose sum is exactly x.

n=int(input())
x=int(input())
sample_list=[]
for i in range(n):
    ele=int(input())
    sample_list.append(ele)
    
for i in range(0,len(sample_list)-1):
    for j in range(i+1,len(sample_list)):
        if sample_list[i]+sample_list[j]==x:
            print("Yes")
        
        
# Input: arr[] = {0, -1, 2, -3, 1}, x= -2