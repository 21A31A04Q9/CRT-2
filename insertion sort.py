def performinsertionsort(nums):
    n=len(nums)
    lasteleinsortedarr=0
    for firstindex in range(1,n):
        temp=nums[firstindex]
        previous=lasteleinsortedarr

        while previous>=0 and nums[previous]>temp:
            nums[previous+1]=nums[previous]
            previous-=1
        nums[previous+1]=temp
        lasteleinsortedarr+=1
nums=[10,8,2,14,12,7]
print("before sorting:",nums)
performinsertionsort(nums)
print("after sorting:",nums)
