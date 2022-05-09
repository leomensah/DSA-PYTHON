def TwoSum(nums, target):
    hashmap = {}
    for index, num in enumerate(nums):
        remainder = target - num
        if remainder in hashmap:
            return [hashmap[remainder], index]
        hashmap[num] = index
    return

nums = [2,7,11,15]
target = 9
print(TwoSum(nums, target))