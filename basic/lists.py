
def run():
    list1 = ["item1", "item2", "item3", "item4", "item5"]
    print(f"list1 = {list1}")
    list2 = list("item4")
    print(f"list2 = {list2}")
    print(f"list last two elements = {list1[-3:-1]}")

    list3 = ["a", "b", "c", "d"]
    print(f"list3 = {list3}")
    list3[0] = "e"
    print(f"list3[0] changed to > {list3[0]} \nnow it is list3 {list3}")
    list3_removed_element = list3.pop(-1)
    print(
        f"popping last element of list3 > {list3_removed_element} \nNow it is > {list3}")
    list3_appended_element = list3.append("appended value")
    print(f"appending to list3 > {list3_appended_element} \nNow it is > {list3}")

    list3_insert_element = list3.insert(1, "inserted value")
    print(f"inserted to list3 > {list3_insert_element} \nNow it is > {list3}")

    return
