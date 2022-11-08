str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
com = list(set(str1)&set(str2))
print("The common letters in both the strings are: ")
for i in com:
    print(i)
