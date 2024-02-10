# 1Given two strings X and Y (length(X)>=1, length(Y)<=10000), find out if Y is contained in X.
# Return “yes” if Y is contained in X, “no” if not.
# str1=input()
# str2=input()
# if str2 in str1:
#     print("yes")

# else:
#     print("no")


# 2)Fanny is given a string along with the string which contains a single character x. 
# She has to remove the character from the given string. Help her to remove all 
# occurrences of x character from the given string
# str1=input()
# str2=input()
# list1=str1.split()
# str3=str1.replace(str2,"")
# print(str3)


# 3)You are given two strings ‘X’ and ‘Y’, each containing at-most 10 characters.
# Write a program that can determine whether the characters in the string ‘X’ can be rearranged to 
# form the second string ‘Y’. The output be “yes” if this is possible and “no” if not.

str1=input()
str2=input()

if set(str1)==set(str2):
    print("yes")

else:
    print("no")