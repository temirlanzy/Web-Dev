def count_code(s):
    count = 0
    for i in range(len(s) - 3):
        if s[i:i+2] == 'co' and (s[i+2] == 'd' or s[i+2] != 'd'):
            count += 1
    return count