def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    rigth = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left
    if rigth < n and array[largest] < array[rigth]:
        largest = rigth
    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array, n, largest)

def heapSort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

array = [4, 2, 5, 8, 1, 9, 2, 3, 6, 8, 5]
heapSort(array)
print(array)