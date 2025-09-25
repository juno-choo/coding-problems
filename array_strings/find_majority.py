def maxConsecutiveOnes(nums):
    count = 0
    maxCount = 0

    for n in nums:
        if n == 1:
            count += 1
        else:
            count = 0
        maxCount = max(maxCount, count)

    return maxCount


arr1 = [1,0,0,1,1,1,0,1,1,1,1]
print(maxConsecutiveOnes(arr1))