# O algoritmo Merge Sort utiliza a técnica de divisão e conquista. Ele divide a lista em duas metades, recursivamente ordena cada metade e, em seguida, combina as duas partes ordenadas para obter a lista final ordenada.

def merge_sort(arr):
    if len(arr) > 1:
        # Divide a lista ao meio
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursivamente ordena as duas metades
        merge_sort(left_half)
        merge_sort(right_half)

        # Combina as duas metades ordenadas
        merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
print("Array antes da ordenação:", arr)

merge_sort(arr)

print("Array após a ordenação:", arr)
