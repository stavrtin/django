list_ss = [None, 2,4,3,6]
list_2 = [2, None, 4,3,6]
print(list_ss)

def res_next(list_res):

    # new_list = list(map(lambda x: x if x != None else next(x), list_res))
    for _ in list_res:
        print(list_res.index(_))
        now_index = list_res.index(_)
        if _ == None:
            list_res[now_index] = list_res[now_index + 1]
            print('---', list_res[now_index + 1])
    return list_res

def res_prev(list_res):

    # new_list = list(map(lambda x: x if x != None else next(x), list_res))
    for _ in list_res:
        print(list_res.index(_))
        now_index = list_res.index(_)
        if _ == None:
            list_res[now_index] = list_res[now_index - 1]
            # print('---', list_res[now_index + 1])
    return list_res

print(res_next(list_ss))
print(list_2, res_next(list_2))