"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
def ThreeSum(numbers):
    answer = []
    numbers.sort()
    for idx, num in enumerate(numbers):
        if idx > 0 and num == numbers[idx - 1]:
            continue
        left, right = idx + 1, len(numbers)-1
        while left < right:
            calThreeSum = num + numbers[left] + numbers[right]
            if calThreeSum > 0:
                right -= 1

            elif calThreeSum < 0:
                left += 1

            else:
                answer.append([num, numbers[left], numbers[right]])
                left += 1
                while numbers[left] == numbers[left - 1] and left < right:
                    left += 1
    return answer

nums = [-1,0,1,2,-1,-4]
print(ThreeSum(nums))
