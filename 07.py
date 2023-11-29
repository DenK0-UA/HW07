def data_preparation(list_data):
    merged_list = []

    for sublist in list_data:
        if len(sublist) > 2:
            sublist = sorted(sublist)[1:-1]  # Видаляємо найбільше і найменше значення зі списку
        merged_list.extend(sublist)  # Додаємо елементи списку до загального списку

    merged_list.sort(reverse=True)  # Сортуємо загальний список у зворотньому порядку (за зменшенням)

    return merged_list


a = data_preparation([[1,2,3],[3,4], [5,6]])
print(a)