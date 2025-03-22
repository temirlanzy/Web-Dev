def sum13(nums):
    total = 0
    skip = False  # Flag to skip the number after 13

    for num in nums:
        if num == 13:
            skip = True  # Set flag to skip the next number
        elif skip:
            skip = False  # Reset flag after skipping one number
        else:
            total += num  # Add number to the total if not skipped

    return total