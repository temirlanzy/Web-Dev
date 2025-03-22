def has22(nums):
    for i in range(len(nums) - 1):  # Loop through the array up to the second-to-last element
        if nums[i] == 2 and nums[i + 1] == 2:  # Check if two consecutive 2's are found
            return True
    return False