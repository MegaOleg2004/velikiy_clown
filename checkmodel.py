import numpy as np

# Загрузка данных из файлов
input_data = np.loadtxt("input_data_summary_last.txt")
output_data = np.loadtxt("output_data_summary_last.txt")

# Получение количества строк
N = input_data.shape[0]

# Создание новых массивов для данных
# Новый массив будет иметь 10 * N строк и 40 столбцов
extended_input_data = np.full((N * 10, 40), 15001)
extended_output_data = np.zeros((N * 10, 1))

# Заполнение данных в extended_input_data и extended_output_data
for i in range(N):
    for j in range(10):
        # Копируем первые 30 чисел из input_data
        extended_input_data[i * 10 + j, :30] = input_data[i, :]

        # Постепенно добавляем числа из output_data начиная со второй строки
        if j > 0:
            for k in range(j):
                extended_input_data[i * 10 + j, 30 + k] = output_data[i, k]

        # В extended_output_data записываем очередное число из output_data
        extended_output_data[i * 10 + j] = output_data[i, j]
    print(i)
# Сохранение новых данных в файлы
np.savetxt("extended_input_data1.txt", extended_input_data, fmt='%d')
np.savetxt("extended_output_data1.txt", extended_output_data, fmt='%d')