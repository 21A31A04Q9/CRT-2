nums=[12,10,6,23,123]
target=23
flag=-1
n=len(nums)
for i in range(n):
    if nums[i]==target:
        flag=i
if flag==-1:
    print("not found")
else:
    print("target value:",flag)
