import random
import numpy as p
import time
import pandas as pd
import openpyxl

final_time = []
star_time = time.time()
column = [10, 15, 20, 32, 45, 64, 100]
#column = [100, 200, 400, 1000, 2000, 4000, 1000]

for k in range(len(column)):
    matrixA = [[random.randint(1, 100) for j in range(column[k])] for i in range(column[k])]
    matrixB = [[random.randint(1, 100) for j in range(column[k])] for i in range(column[k])]

    print(p.dot(matrixA, matrixB))
    final_time.append(time.time() - star_time)

result = pd.DataFrame({'Размер одной матрицы': [100, 200, 400, 1000, 2000, 4000, 10000], 'Время выполнения': final_time})
result.to_excel("./results1.xlsx")