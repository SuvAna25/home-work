def add_num(num, lst=None):
    lst = lst or []
    if not lst:
        lst = []
    lst.append(num)
    print(lst)


add_num(5)
add_num(10)
add_num(15)


def values(num, lst=[]):
    lst.append(num)
    print(lst)


add_num(5)
add_num(10)
add_num(15)
