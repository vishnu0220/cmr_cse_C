n = int(input())
nums = []
for i in range(n):
    ele = int(input())
    nums.append(ele)
target = int(input("Enter target : "))
# Traversing
isFound = False
for i in nums:
    if i == target:
        isFound = True
        print("Found")
        break
if isFound == False:
    print("Not found")