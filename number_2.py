import random
import time
import pandas as pd
import xlsxwriter

def quick_sort_normal(array):
    if len(array) <= 1:
        return array

    support_element = array[0]

    left = list(filter(lambda x: x < support_element, array))
    center = [i for i in array if i == support_element]
    right = list(filter(lambda x: x > support_element, array))

    return quick_sort_normal(left) + center + quick_sort_normal(right)

def shell_sort(data):
    data = data.copy()
    last_index = len(data) - 1
    step = len(data)//2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data

def randomNumbers(lenght):
    return [random.randint(1, lenght) for i in range(lenght)]

def growingNumbers(lenght):
    return [i for i in range(lenght)]

def fallingNumbers(lenght):
    return [i for i in range(lenght, 0, -1)]

def growingAndFallingNumbers(lenght):
    return [i for i in range(lenght)] + [i for i in range(lenght, 0, -1)]

if __name__ == '__main__':
    time_qs_random = []
    time_qs_growing = []
    time_qs_falling = []
    time_qs_gf = []
    time_shell_random = []
    time_shell_growing = []
    time_shell_falling = []
    time_shell_gf = []
    time_sort_random = []
    time_sort_growing = []
    time_sort_falling = []
    time_sort_gf = []

    lenght_random = [i for i in range(10000, 100000, 10000)]
    lenght = [i for i in range(100, 1000, 100)]

    for i in range(len(lenght_random)):
        start_time_sort_random = time.time()
        rMassive = randomNumbers(lenght_random[i])
        sorted(rMassive)
        time_sort_random.append(time.time() - start_time_sort_random)

        start_time_qs_random = time.time()
        rMassive = randomNumbers(lenght_random[i])
        quick_sort_normal(rMassive)
        time_qs_random.append(time.time() - start_time_qs_random)

        start_time_shell_random = time.time()
        rMassive = randomNumbers(lenght_random[i])
        shell_sort(rMassive)
        time_shell_random.append(time.time() - start_time_shell_random)

    for i in range(len(lenght)):
        start_time_qs_growing = time.time()
        gMassive = growingNumbers(lenght[i])
        quick_sort_normal(gMassive)
        time_qs_growing.append(time.time() - start_time_qs_growing)

        start_time_qs_falling = time.time()
        fMassive = fallingNumbers(lenght[i])
        quick_sort_normal(fMassive)
        time_qs_falling.append(time.time() - start_time_qs_falling)

        start_time_qs_gf = time.time()
        gfMassive = growingAndFallingNumbers(lenght[i])
        quick_sort_normal(gfMassive)
        time_qs_gf.append(time.time() - start_time_qs_gf)

        start_time_shell_growing = time.time()
        gMassive = growingNumbers(lenght[i])
        shell_sort(gMassive)
        time_shell_growing.append(time.time() - start_time_shell_growing)

        start_time_shell_falling = time.time()
        fMassive = fallingNumbers(lenght[i])
        shell_sort(fMassive)
        time_shell_falling.append(time.time() - start_time_shell_falling)

        start_time_shell_gf = time.time()
        gfMassive = growingAndFallingNumbers(lenght[i])
        shell_sort(gfMassive)
        time_shell_gf.append(time.time() - start_time_shell_gf)

        start_time_sort_falling = time.time()
        fMassive = fallingNumbers(lenght[i])
        sorted(fMassive)
        time_sort_falling.append(time.time() - start_time_sort_falling)

        start_time_sort_growing = time.time()
        gMassive = growingNumbers(lenght[i])
        sorted(gMassive)
        time_sort_growing.append(time.time() - start_time_sort_growing)

        start_time_sort_gf = time.time()
        gfMassive = growingAndFallingNumbers(lenght[i])
        sorted(gfMassive)
        time_sort_gf.append(time.time() - start_time_sort_gf)

    result_random = pd.DataFrame({'lenght': lenght_random,
                                  'sorted': time_sort_random,
                                    'Qs random': time_qs_random,
                                    'Shell random': time_shell_random})

    result_other = pd.DataFrame({'lenght': lenght,
                                 'sorted growing': time_sort_growing,
                                 'sorted falling': time_sort_falling,
                                 'sorted growing-falling': time_shell_gf,
                                  'Qs growing': time_qs_growing,
                                  'Qs falling': time_qs_falling,
                                  'Qs growing-falling': time_qs_gf,
                                  'Shell growing': time_shell_growing,
                                  'Shell falling': time_shell_falling,
                                  'Shell growing-falling': time_shell_gf})

    sheet = {'random': result_random, 'other': result_other}
    writer = pd.ExcelWriter('./results2.xlsx', engine='xlsxwriter')

    for sheet_name in sheet.keys():
        sheet[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()