# O(N*N) time | O(1) space
def twoNumberSumLoop(array,targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum,secondNum]
    return []


# o(N) time | o(N) space
def twoNumberSumHashTable(array,targetSum):
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [targetSum - num,num]
        else:
            nums[num] = True
    return []

# o(nlog(n)) time | o(1) space
def twoNumberSumTwoPointer(array,targetSum):
    array.sort()
    left = 0
    right = len(array) -1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum ==  targetSum:
            return [array[left],array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1    
    return []

# print index:
def twoSum(nums, target):
    numToIndex = {}
    for i in range(len(nums)):
        if target - nums[i] in numToIndex:
            return [numToIndex[target - nums[i]], i]
        numToIndex[nums[i]] = i
    return []