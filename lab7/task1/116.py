def centered_average(nums):
    # Sort the array first
    nums.sort()

    # Remove the smallest and largest values
    nums = nums[1:-1]

    # Return the mean of the remaining values using int division
    return sum(nums) // len(nums)