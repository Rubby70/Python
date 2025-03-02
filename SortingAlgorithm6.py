import random

length = 9
max = 10

RP_arr = random.choices(range(1, max), k = length)
NRP_arr = random.sample(range(1, max), length)

arr1 = NRP_arr.copy()
arr2 = NRP_arr.copy()
arr3 = NRP_arr.copy()
arr4 = NRP_arr.copy()
arr5 = NRP_arr.copy()

#print(f"可重複數列 = {RP_arr}")
#print(f"不重複數列 = {NRP_arr}")
print(f"Initial Aray: {arr1}")

#定義函式
def CountingSort(arr, length):
    max = 0
    for i in range(length):
        if(arr[i] > max):
            max = arr[i]
    
    length_CountingArray = max + 1
    CountingArray = [0] * length_CountingArray
    for i in range(length):
        CountingArray[arr[i]] += 1

    for i in range(1, length_CountingArray):
        CountingArray[i] += CountingArray[i - 1]

    OutputArr = [0] * length
    for i in range((length - 1), -1, -1):
        OutputArr[CountingArray[arr[i]] - 1] = arr[i]
        CountingArray[arr[i]] -= 1
    
    print(f"Counting Sort: {OutputArr}")

def BubbleSort(arr, length):

    for i in range(length):
        for j in range(i, length):
            if(arr[i] > arr[j]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    
    print(f"Bubble Sort: {arr}")

def InsertionSort(arr, length):

    for i in range(length):
        temp = arr[i]
        cnt = i
        while((cnt > 0) & (temp < arr[cnt - 1])):
            arr[cnt] = arr[cnt - 1]
            cnt -= 1

        arr[cnt] = temp

    print(f"Insertion Sort: {arr}")

def QuickSort(arr):

    arr.sort()
    print(f"python內建的排序: {arr}")

def Merge(arr, length, start, mid, end):
    
    left = mid - start
    right = end - mid
    
    arrL = [0] * left
    for i in range(left):
        arrL[i] = arr[start + i]
    
    arrR = [0] * right
    for i in range(right):
        arrR[i] = arr[mid + i]

    i = 0
    j = 0
    k = start

    while((i < left) & (j < right)):
        if(arrL[i] >= arrR[j]):
            arr[k] = arrR[j]
            j += 1
            k += 1
        
        else:
            arr[k] = arrL[i]
            i += 1
            k += 1

    while(i < left):
        arr[k] = arrL[i]
        i += 1
        k += 1
    
    while(j < right):
        arr[k] = arrR[j]
        j += 1
        k += 1

def MergeLoop(arr, length, start, end):
    
    if(start >= end - 1):
        return
    
    mid = start + (end - start) // 2
    MergeLoop(arr, length, start, mid)
    MergeLoop(arr, length, mid, end)
    Merge(arr, length, start, mid, end)

def MergeSort(arr, length):

    MergeLoop(arr, length, 0, length)
    print(f"Merge Sort: {arr}")

#呼叫函式
CountingSort(arr1, length)
BubbleSort(arr2, length)
InsertionSort(arr3, length)
QuickSort(arr4)
MergeSort(arr5, length)






