import time

n = int(input())
ms = int(input())

time.sleep(ms / 1000)
print(f'Квадратный корень из {n} после {ms} миллисекунд равен {n**0.5}')