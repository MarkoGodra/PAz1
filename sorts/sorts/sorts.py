import sys
import random
import time
import itertools
import numpy as np
import matplotlib.pyplot as plt

def CreatePlot(input_data, exec_time, algo_name, subplotIndex):
    # plt.subplot(3,1,subplotIndex)
    plt.plot(input_data, exec_time, label=algo_name)
    # plt.title(algo_name)
    plt.xlabel('Ulaz [n]')
    plt.ylabel('Vreme [S]')
    plt.legend()
    print(algo_name)
    for i in range(0, len(input_data)):
        print("input_data: ", input_data[i], ", exec_time: ", exec_time[i])

def analyzeAlgorithm(type, subplotIndex):
    stdLenths = [1, 10, 100, 1000, 10000]
    sortTimes = list()
    j = 0
    for i in stdLenths:
        x = random_list(0, 1000000 + 1, i)
        startTime = time.clock()
        type(x)
        endTime = time.clock()
        sortTimes.append(endTime - startTime)
        j += 1
    if(is_sorted(x)):
        CreatePlot(stdLenths, sortTimes, type.__name__, subplotIndex)

def analyzeAlgorithm_with_return_value(type, subplotIndex):
    stdLenths = [1, 10, 100, 1000, 10000]
    sortTimes = list()
    j = 0
    for i in stdLenths:
        x = random_list(0, 1000000 + 1, i)
        startTime = time.clock()
        z = type(x)
        endTime = time.clock()
        sortTimes.append(endTime - startTime)
        j += 1
    if(is_sorted(z)):
        CreatePlot(stdLenths, sortTimes, type.__name__, subplotIndex)

def is_sorted(A):
    testList = A[:]
    testList.sort()
    if testList == A:
        return True
    return False

def find_number_of_digits(A) :
    max = A[0]
    for i in range(0, len(A)) :
        if A[i] > max :
            max = A[i]
    return len(str(max))
        

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def radix_sort(A) : 
    
    k_digit = 0
    k = 0
    RADIX = 10
    #Empty buckets
    B = [[] for i in range(0, RADIX)]

    #Find max number of digits in a number of array A
    max_len = find_number_of_digits(A)

    while(k < max_len) :
        for i in range(0, len(A)):
            k_digit = int((A[i]/RADIX**k)%RADIX)
            B[k_digit].append(A[i])
        
        A = list(itertools.chain(*B))
        B = [[] for i in range(0, RADIX)]
        k += 1
    return A

def selection_sort(A) : 
    for j in range(0, len(A) - 1) :
        min = j
        for i in range(j + 1, len(A)) :
            if A[min] > A[i] :
                #Find index of smallest element
                min = i
        if min != j :
            #Swaping elements
            A[j], A[min] = A[min], A[j]

def parent(i) :
    return(i - 1) // 2

def left(i) :
    return(2 * i + 1)

def right(i) :
    return(2 * i + 2)
            
def heap_max(A) :
    return A[0]

def max_heapify(A, i) :
    global size
    l = left(i)
    r = right(i)
    if l < size and A[l] > A[i] :
        largest = l
    else :
        largest = i
    if r < size and A[r] > A[largest] :
        largest = r
    if largest != i :
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A) :
    global size
    size = len(A)
    j = len(A) // 2 - 1
    for i in range(j, -1, -1) :
        max_heapify(A, i)

def heap_sort(A):
    global size
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1) :
        A[0], A[i] = A[i], A[0]
        size -= 1
        max_heapify(A, 0)

#Selection sort
print("\t\t Selection sort")
A = random_list(0,20,10)
print("Unsorted list :\t ", A)
start_time = time.clock()
selection_sort(A)
end_time = time.clock() - start_time
print("Sorted list : \t", A)
print("\t Epleased time: ", end_time)
sorted = is_sorted(A)
print("List sorted : \t", sorted)
print("\n\n")

#Radix sort
print("\t\t Radix sort")    
A = random_list(0, 1000000, 10)
print("Unsorted list :\t ", A)
start_time = time.clock()
B = radix_sort(A)
end_time = time.clock() - start_time
print("Sorted list : \t", B)
print("\t Epleased time: ", end_time)
sorted = is_sorted(B)
print("List sorted : \t", sorted)
print("\n\n")

#Heap sort
print("\t\t Heap sort")    
A = random_list(0, 20, 10)
print("Unsorted list :\t ", A)
start_time = time.clock()
heap_sort(A)
end_time = time.clock() - start_time
print("Sorted list : \t", A)
print("\t Epleased time: ", end_time)
sorted = is_sorted(A)
print("List sorted : \t", sorted)

#plot
analyzeAlgorithm(selection_sort, 1)
analyzeAlgorithm(heap_sort, 2)
analyzeAlgorithm_with_return_value(radix_sort, 3)
plt.show()