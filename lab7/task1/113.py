def xyz_there(s):
    # Check if "xyz" is in the string and is not preceded by a period
    return 'xyz' in s and (s.find('xyz') == 0 or s[s.find('xyz') - 1] != '.')