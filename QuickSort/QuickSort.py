import random
def quick_sort(A, p, r) :
    if p < r :
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def partition(A, p, r) :
    x = A[p]
    j = p
    for i in range (p + 1, r + 1) :
        if (A[i] < x) :
            j += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    A[p] = A[j]

    A[j] = x
    return j
algoList = []
for i in range(99) :
    algoList.append(random.randrange(1, 1000))

quick_sort(algoList, 0, len(algoList) - 1)
print(len(algoList), algoList[0 : 99])
