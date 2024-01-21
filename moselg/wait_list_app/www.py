import statistics
# import numpy
list_1 = [None, 5, 3,2,8, 4,5]
list_2 = [1, 5, 8,2,8, None]
list_3 = [None, 5, 9,2,8, 3,None]
list_4 = [None, None, 3, 7, None,2,8, None,None]
list_5 = [nan, 3.0, 3.0, nan]


def change_none_nex(list_num):
    res_list = list_num.copy()
    for _ in res_list:
        # print(res_list.index(_))
        if _ is None:
            res_list[res_list.index(_)] = res_list[res_list.index(_) + 1]
    return res_list

def change_none_prev(list_num):
    res_list = list_num.copy()
    for _ in res_list:
        if _ is None:
            res_list[res_list.index(_)] = res_list[res_list.index(_) - 1]
    return res_list

def change_none(list_num):
    res_list = list_num.copy()
    first_ = [value for value in list_num if value][0]
    if res_list[0] is None :
        res_list[0] = first_
    for _ in res_list:
        if _ is None :
            res_list[res_list.index(_)] = res_list[res_list.index(_) - 1]
    return res_list

print(f'list_1={list_1}')
print(change_none(list_1))
print(f'list_2={list_2}')
print(change_none(list_2))
print(f'list_3={list_3}')
print(change_none(list_3))
print(f'list_4={list_4}')
print(change_none(list_4))

