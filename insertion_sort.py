def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

#numbers = [5, 3, 8, 4, 2]
#print(f"Вхідний список: {numbers}")
#print(f"Результат виконання: {insertion_sort(numbers)}")