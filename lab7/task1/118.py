def sum67(nums):
    total = 0
    in_section = False  # Flag to track if we're in the section to ignore

    for num in nums:
        if num == 6:
            in_section = True  # Start ignoring numbers after 6
        elif num == 7 and in_section:
            in_section = False  # End ignoring when we encounter 7
        elif not in_section:
            total += num  # Add number to the total if not in the 6-7 section

    return total