import random


def heap_sort(A) :
    result = []
    build_maxHeap(A)
    for i in range (len(A) - 1, 1, -1) :
        result.insert(0, A[0])
        A[0] = A[i]
        A.pop()
        maxHeapify(A, 0)

    return result

def build_maxHeap(A) :
    for i in range(len(A) // 2, -1, -1) :
        maxHeapify(A, i)

def maxHeapify(A, i) :
    left = i * 2 + 1
    right = i * 2 + 2
    if right < len(A) and A[i] < A[right] :
        largest = right
    else :
        largest = i

    if left < len(A) and A[largest] < A[left] :
        largest = left
    if largest != i :
        temp = A[largest]
        A[largest] = A[i]
        A[i] = temp
        maxHeapify(A, largest)

algoList = []
for i in range(99) :
    algoList.append(random.randrange(1, 1000))

print(heap_sort(algoList))
