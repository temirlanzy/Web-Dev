def front_back(s):
    return s if len(s) <= 1 else s[-1] + s[1:-1] + s[0]