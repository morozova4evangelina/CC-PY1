list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = list_numbers[0]  # начнем с первого
len_ = len(list_numbers)      # количество чисел
index_max = 0                 # вводим индекс числа

for current_index, current_number in enumerate(list_numbers):
    if current_number >= max_number:
        max_number = current_number
        index_max = current_index    # индекс максимального числа

list_numbers[index_max], list_numbers[len_ - 1] = list_numbers[len_ - 1], list_numbers[index_max]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
