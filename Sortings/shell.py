'''Сортировка Шелла является несколько измененным вариантом сортировки вставками.
Сортировка вставками является медленной из-за того, что совершает перемещения только с соседними элементами, 
в отличии от сортировки Шелла, которая позволяет быстро сделать обмен между элементами, которые находятся далеко друг от друга.

Идея заключается в том, чтобы просматривать элементы беря каждый i тый элементы(начало откуда угодно).
В результате мы получаем массив где каждый i-тый элемент отсортирован. Повторяя такую операцию с использованием меньших i, 
заканчивая 1 результатом будет отсортированный массив.

'''


def Shell(A):
    t = int(len(A)/2)
    while t > 0:
        for i in range(len(A)-t):
            j = i
            while j >= 0 and A[j] > A[j+t]:
                A[j], A[j+t] = A[j+t], A[j]
                j -= 1
        t = int(t/2)