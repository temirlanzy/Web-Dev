def end_other(a, b):
    a, b = a.lower(), b.lower()  # Convert both strings to lowercase
    return a.endswith(b) or b.endswith(a)