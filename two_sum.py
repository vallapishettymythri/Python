class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in dict:
                return [dict[needed], i]

            dict[nums[i]] = i
obj = Solution()
answer = obj.twoSum([2, 7, 11, 15], 9)