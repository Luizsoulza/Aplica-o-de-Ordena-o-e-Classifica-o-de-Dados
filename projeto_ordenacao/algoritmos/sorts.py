# ==================== ALGORITMOS ====================

def bubble_sort(arr):
    arr = arr[:]
    comparacoes = 0
    trocas = 0
    
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
    
    return arr, comparacoes, trocas


def selection_sort(arr):
    arr = arr[:]
    comparacoes = 0
    trocas = 0
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparacoes += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            trocas += 1
    
    return arr, comparacoes, trocas


def merge_sort(arr):
    arr = arr[:]
    comparacoes = 0
    trocas = 0
    
    def merge(left, right):
        nonlocal comparacoes, trocas
        res = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparacoes += 1
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
            trocas += 1
        
        while i < len(left):
            res.append(left[i])
            i += 1
            trocas += 1
        
        while j < len(right):
            res.append(right[j])
            j += 1
            trocas += 1
        
        return res
    
    step = 1
    n = len(arr)
    while step < n:
        for i in range(0, n, step * 2):
            left = arr[i:i+step]
            right = arr[i+step:i+2*step]
            merged = merge(left, right)
            for j, val in enumerate(merged):
                arr[i+j] = val
        step *= 2
    
    return arr, comparacoes, trocas


def quick_sort(arr):
    arr = arr[:]
    comparacoes = 0
    trocas = 0
    
    def partition(a, low, high):
        nonlocal comparacoes, trocas
        pivot = a[high]
        i = low - 1
        
        for j in range(low, high):
            comparacoes += 1
            if a[j] <= pivot:
                i += 1
                if i != j:
                    a[i], a[j] = a[j], a[i]
                    trocas += 1
        
        if i + 1 != high:
            a[i+1], a[high] = a[high], a[i+1]
            trocas += 1
        
        return i+1
    
    def qs(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            qs(a, low, pi-1)
            qs(a, pi+1, high)
    
    qs(arr, 0, len(arr)-1)
    return arr, comparacoes, trocas
