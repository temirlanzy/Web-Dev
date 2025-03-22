def make_bricks(small, big, goal):
    max_big = min(big, goal // 5)  # Сколько больших кирпичей можно использовать
    remaining = goal - max_big * 5  # Сколько еще нужно добрать маленькими
    return remaining <= small  # Достаточно ли маленьких кирпичей