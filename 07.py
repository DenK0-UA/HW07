def decode(data):
    decoded_list = []

    if not data:
        return decoded_list

    value = data[0]
    count = data[1]

    if isinstance(value, list):
        # Рекурсивно декодуємо вкладений список
        decoded_value = decode(value)
    else:
        decoded_value = [value]

    decoded_list.extend(decoded_value * count)

    # Рекурсивно викликаємо функцію для обробки решти списку
    decoded_list.extend(decode(data[2:]))

    return decoded_list

# Приклад використання:
decoded_list = decode(["X", 5, "Z", 2, "X", 2, "Y", 3, "Z", 2])
print(decoded_list)
