import random

def merge_sort(A, p, r) :
    if p < r :
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r) :
    pre_list = A[p : q + 1]
    post_list = A[q + 1 : r + 1]
    j = 0
    k = 0
    pre_list.append(518289)
    post_list.append(591283)
    for i in range(p, r + 1) :
        if pre_list[j] < post_list[k] :
            A[i] = pre_list[j]
            j += 1
        else :
            A[i] = post_list[k]
            k += 1



algoList = []
for i in range(99) :
    algoList.append(random.randrange(1, 1000))

merge_sort(algoList, 0, len(algoList) - 1)
print(len(algoList), algoList[0 : 99])
