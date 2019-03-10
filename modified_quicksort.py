N = int(input("Введите размер массива "))
my_array = []
for i in range (0,N):
    my_array.append(int(input("Введите элемент массива ")))

def quicksort(nums):
    #выходим из рекурсии когда длина массив <= 1
    if len(nums) <= 1:
        return nums
    else:
    #выбираем опорный элемент
        q = nums[int(len(nums)/2)]
        bigger_array = []
        equal_array = []
        less_array = []
    for i in range(len(nums)):
        if nums[i] == q:
            equal_array.append(nums[i])
        if nums[i] < q:
            less_array.append(nums[i])
        if nums[i] > q:
            bigger_array.append(nums[i])
    # проверяем какой массив поступил на вход и возвращаем нужные массивы
    if nums[0] % 2 == 0:
        return quicksort(less_array) + equal_array + quicksort(bigger_array)
    else:
        return quicksort(bigger_array) + equal_array + quicksort(less_array)

def modified_quicksort(array):
    if len(array) <= 1:
        return array
    else:
        #создаем 2 массива: состоящие из четных и нечетных чисел
        odd_array = []
        even_array = []
        for number in array:
            if number % 2 == 0:
                even_array.append(number)
            else:
                odd_array.append(number)
    return quicksort(even_array) + quicksort(odd_array)

print(modified_quicksort(my_array))
