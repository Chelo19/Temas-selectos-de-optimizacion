data = []

def createArray():
    rows = int(input('Cantidad de filas: '))
    cols = int(input('Cantidad de columnas: '))
    fillArray(rows, cols)

def fillArray(filas, columnas):
    array = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            dato = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            fila.append(dato)
        array.append(fila)
    printArray(array)

def printArray(matriz):
    for fila in matriz:
        data.append(fila)
    print(data)

# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
data = [[16, 14, 2], [4, 1, 2], [21, 22, 16], [10, 9, 8]]
# data = [[20, 7, 13], [18, 10, 15], [21, 5, 22]]

def checkWhereToStart():
    shape = checkShape()
    col_diff_sum = 0
    col_diff_prom = 0
    row_diff_sum = 0
    row_diff_prom = 0
    cols = []
    rows = []
    for i in range(shape[1]):
        current_array = []
        current_sum = 0
        for j in range(shape[0]):
            current_array.append(data[j][i])
            current_sum += data[j][i]
        diff = max(current_array) - min(current_array)
        current_array.append(diff)
        current_array.append(current_sum / shape[0])
        cols.append(current_array)
        col_diff_sum += diff
    col_diff_prom = col_diff_sum / shape[1]

    for i in range(shape[0]):
        current_array = []
        current_sum = 0
        for j in range(shape[1]):
            current_array.append(data[i][j])
            current_sum += data[i][j]
        diff = max(current_array) - min(current_array)
        current_array.append(diff)
        current_array.append(current_sum / shape[1])
        rows.append(current_array)
        row_diff_sum += diff
    row_diff_prom = row_diff_sum / shape[0]

    # print(f'Promedio de la suma de las diferencias del max y min de filas: {row_diff_prom}')
    # print(f'Promedio de la suma de las diferencias del max y min de columnas: {col_diff_prom}')

    if(row_diff_prom >= col_diff_prom):
        # print('Vamos por rows')
        return rows
    else:
        # print('Vamos por cols')
        return cols

def mainAlgorithm():
    shape = checkShape()
    working_array = checkWhereToStart()
    banned_index = []
    grand_sum = 0
    index_max_min = getMaxMinArray(working_array, [], [])
    working_array = checkWhereToStart()
    print(shape)
    is_rows = False
    if(len(working_array) == shape[0]):
        print('rows')
        is_rows = True
        iter_num = shape[1]
    else:
        print('cols')
        iter_num = shape[0]

    for i in range(len(index_max_min)):
        # print(working_array[index_max_min[i]])
        options_taken = []
        min_value = 99999999
        min_index = 0
        for j in range(iter_num):
            # print(working_array[index_max_min[i]][j])
            if(working_array[index_max_min[i]][j] < min_value and j not in banned_index):
                min_value = working_array[index_max_min[i]][j]
                min_index = j
        grand_sum += min_value
        banned_index.append(min_index)
    for i in range(len(banned_index)):
        if(is_rows):
            print(f'Columna {banned_index[i] + 1}, Fila {index_max_min[i] + 1}')
        else:
            print(f'Columna {index_max_min[i] + 1}, Fila {banned_index[i] + 1}')

    print(f'Valor total: {grand_sum}')



def getMaxMinArray(working_array_max_min, index_max_min, banned_index):
    max_value = 0
    for i in range(len(working_array_max_min)):
        if(working_array_max_min[i][len(working_array_max_min[0])-1] > max_value and i not in banned_index):
            max_value = working_array_max_min[i][len(working_array_max_min[0])-1]
            max_index = i
    banned_index.append(max_index)
    index_max_min.append(max_index)
    # working_array_max_min.pop(max_index)
    if(len(working_array_max_min) != len(index_max_min)):
        getMaxMinArray(working_array_max_min, index_max_min, banned_index)
    return index_max_min


def checkShape():
    shape = []
    shape.append(len(data))
    shape.append(len(data[0]))
    return shape

if __name__ == "__main__":
    # createArray()
    mainAlgorithm()