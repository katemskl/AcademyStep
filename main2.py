# x = [10, [3.141, 20, [30, 'qqz', 2.178]], 'foo']
# print(x[1][2][1][2])
#
# print(sorted((1, 2, 3)))
# print(False == True in [False])


def divisible_by_b(a, b):
    while a % b != 0:
        a += 1
    return a


# print(divisible_by_b(17000, 8000))
# print(divisible_by_b(980000, 30000))

def multiply(arr):
    ret_list = []
    for elem in arr:
        elem_list = []
        for _ in range(len(arr)):
            elem_list.append(elem)
        ret_list.append(elem_list)
    return ret_list


def multiply2(arr):
    return [[i]*len(arr) for i in arr]

#
# print(multiply2([4, 5]))
# print(multiply(["*", "%", "$"]))


def sum_missing_numbers(arr):
    first = min(arr)
    last = max(arr)
    sum_arr = []
    for i in range(first, last):
        if i not in arr:
            sum_arr.append(i)
    return sum(sum_arr)


# def sum_missing_numbers2(arr):
#     return sum(range(min(arr), max(arr))) - sum(arr)


# print(sum_missing_numbers([4, 3, 8, 1, 2]))
# print(sum_missing_numbers([17, 16, 15, 10, 11, 12]))
# print(sum_missing_numbers([1, 2, 3, 4, 5]))


def is_slidey(num):
    check = str(num)
    for n in range(len(check) - 1):
        check1 = int(check[n]) == int(check[n+1])+1
        check2 = int(check[n]) == int(check[n+1])-1
        if check1 or check2:
            continue
        else:
            return False
    return True


# print(is_slidey(123454321) is True)
# print(is_slidey(54345) is True)
# print(is_slidey(987654321) is True)
# print(is_slidey(1123) is False)
# print(is_slidey(1357) is False)
# print(is_slidey(1) is True)

list1 = [1, 2, 3]

for x in range(len(list1)):
    print(list1[x-1])