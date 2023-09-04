class Solution:
    @staticmethod
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

nums = [3, 2, 3]
target = 6

if 2 <= len(nums) <= 104:
    result = Solution.twoSum(nums, target)
    if result:
        print(result)
    else:
        print("No solution found.")
else:
    print("Length is invalid.")
