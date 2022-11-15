import numpy as np

series_of_numbers = np.arange(1000000, dtype=float)
# 1
sum_series_of_numbers = np.sum(series_of_numbers)
print(f'Сумма всех элементов ряда:  {sum_series_of_numbers}')
# 2
average_series_of_numbers = np.mean(series_of_numbers)
print(f'Среднее ряда:  {average_series_of_numbers}')
# 3
random_series_of_numbers = np.random.randint(1, 10, size = 1000000)
median_series_of_numbers = np.median(random_series_of_numbers)
print(f'Медиана случайных 1000000 чисел:  {median_series_of_numbers}')
# 4
prod_series_of_numbers = np.prod(random_series_of_numbers, dtype=object)
print(f'Произведение случайных 1000000 чисел:  {prod_series_of_numbers}')