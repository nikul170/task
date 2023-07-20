import numpy as np

def count_of_min(i, j):
    cmb = [[a_i, a_j] for a_i in range(i - 1, i + 2) for a_j in range(j - 1, j + 2)]
    if i == j == 0:
        cmb = [element for index, element in enumerate(cmb[3:]) if index % 3 != 0 and a[element[0]][element[1]] != a[i][j]]
    elif i == j == 9:
        cmb = [element for index, element in enumerate(cmb[:4]) if index % 2 != 0 or index == 0]
    elif i == 9 and j == 0:
        cmb = [element for index, element in enumerate(cmb[:6]) if index % 3 != 0 and a[element[0]][element[1]] != a[i][j]]
    elif i == 0 and j == 9:
        cmb = [element for index, element in enumerate(cmb[3:8]) if index != 2 and a[element[0]][element[1]] != a[i][j]]
    elif j == 0:
        cmb = [element for index, element in enumerate(cmb) if index % 3 != 0 and a[element[0]][element[1]] != a[i][j]]
    elif i == 0:
        cmb = [element for index, element in enumerate(cmb[3:]) if a[element[0]][element[1]] != a[i][j]]
    elif j == 9:
        cmb = [element for index, element in enumerate(cmb) if (index + 1) % 3 != 0 and a[element[0]][element[1]] != a[i][j]]
    elif i == 9:
        cmb = [element for index, element in enumerate(cmb[:6]) if a[element[0]][element[1]] != a[i][j]]
    return 1 if all(a[i][j] < a[element[0]][element[1]] for element in cmb) else 0


def summa_of_elements(i, j):
    return abs(a[i][j]) if j > i else 0


a = np.random.random((10, 10))
print(a)
summa = 0
count = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        summa += summa_of_elements(i, j)
        count += count_of_min(i, j)
print(summa, count)

