def make_chocolate(small, big, goal):
    # Используем максимально возможное количество больших плиток
    max_big_bars = min(big, goal // 5)

    # Остаток, который нужно добрать маленькими плитками
    remaining = goal - (max_big_bars * 5)

    # Если хватает маленьких плиток, возвращаем их количество, иначе -1
    return remaining if remaining <= small else -1