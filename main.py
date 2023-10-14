from random import shuffle
import copy


shuffle_list = (list(range(500)))
shuffle(shuffle_list)


def buble_sort(num_list: list):

    operations = len(num_list) ** 2
    index_num = len(num_list) - 1

    while operations != 0:
        if index_num == 0:
            index_num = len(num_list) - 1
        if num_list[index_num] > num_list[index_num - 1]:
            num_list[index_num], num_list[index_num - 1] = num_list[index_num - 1], num_list[index_num]
        operations -= 1
        index_num -= 1

    else:
        return num_list


def insertion_sort(num_list: list):
    sort_num_list = [num_list[0]]
    index_num_list = len(num_list) - 1

    while index_num_list:
        if sort_num_list[0] > num_list[index_num_list]:
            sort_num_list.insert(0, num_list[index_num_list])
        elif sort_num_list[-1] < num_list[index_num_list]:
            sort_num_list.append(num_list[index_num_list])
        else:
            for i in range(len(sort_num_list)):
                if (num_list[index_num_list] < sort_num_list[i]) and (sort_num_list[i - 1] < num_list[index_num_list]):
                    sort_num_list.insert(i, num_list[index_num_list])
                    break

        index_num_list -= 1

    return sort_num_list







list_number = (list(range(500)))


def binary_search(numm):
    list_numbers = list_number
    while len(list_numbers) != 1:
        len_half_num = len(list_numbers) // 2
        if list_numbers[:len_half_num][-1] >= numm:
            list_numbers = list_numbers[:len_half_num]
        else:
            list_numbers = list_numbers[len_half_num:]
    return list_numbers






print(f' Buble sorted:\n {buble_sort(shuffle_list)}\n{"=" * 150}')
print(f' Insertion sorted:\n {insertion_sort(shuffle_list)}\n{"=" * 150}')
print(f' Binary_search: {binary_search(30)}\n{"=" * 150}')

