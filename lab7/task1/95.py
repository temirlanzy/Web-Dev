def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5  # В день рождения лимиты выше на 5

    if speed <= 60:
        return 0  # Нет штрафа
    elif speed <= 80:
        return 1  # Маленький штраф
    else:
        return 2  # Большой штраф