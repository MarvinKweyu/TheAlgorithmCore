class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums[:] = nums[-k:] + nums[:k]

        length = len(nums)
        print(f"Length of array: {length} and value of k: {k}")
        k = k % length
        print(f"New value of k: {k}")
        sp = length - k
        print(f"Start point: {sp}")
        nums[:] = nums[sp:] + nums[:sp]


# nums = [-1, -100, 3, 99]
nums = [1, 2, 3, 4, 5, 6, 7, 9]


Solution().rotate(nums, 3)

print(nums)
