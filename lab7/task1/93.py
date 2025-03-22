def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0  # Нет
    if you >= 8 or date >= 8:
        return 2  # Да
    return 1  # Возможно