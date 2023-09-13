def binary_search(array, element, left, right):
    if left > right:
            return False
    mid = (right + left) // 2
    if element == array[mid]:
        if element > array[mid - 1]  and element <= array[mid]:
            return mid
        elif element < array[mid]:
            return binary_search(array, element, left, mid - 1)
    elif element == array[mid - 1]:
            return binary_search(array, element, left, mid - 1)
    else:
            return binary_search(array, element, mid + 1, right)
array = list(map(int, input("Введите числа через пробел: ").split()))
element = int(input("Введите любое число из списка: "))

array.sort()
left = int(array[-1])
right = int(array[0])
print(array)

if element > left or element < right:
    print('Введенного вами числа нет в списке')
else:
    print(binary_search(array, element, 0, len(array) - 1))