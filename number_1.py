import random
import numpy as p
import time
import pandas as pd
import openpyxl

final_time_all = []
final_time = []
star_time_all = time.time()
column = [100, 200, 400, 1000, 2000, 4000, 10000]

for k in range(len(column)):
    star_time = time.time()
    matrixA = [[random.randint(1, 100) for j in range(column[k])] for i in range(column[k])]
    matrixB = [[random.randint(1, 100) for j in range(column[k])] for i in range(column[k])]

    print(p.dot(matrixA, matrixB))
    final_time.append(time.time() - star_time)
    final_time_all.append(time.time() - star_time_all)

result = pd.DataFrame({'Размер одной матрицы': column,
                       'Время выполнения': final_time,
                       'Общее время выполнения': final_time_all})
result.to_excel("./results1.xlsx")