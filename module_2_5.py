def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
value = int(input('Введите значение: '))
result = get_matrix(n, m, value)










