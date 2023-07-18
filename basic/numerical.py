def run():
    type1 = 3
    type2 = "a"
    type12 = 12
    print(f" type12 = {type12}")
    type12 *= 2
    print(f"type12 now = {type12}")
    type12 /= 4
    print(f"type12 now = {type12}")
    type12 -= 2
    print(f"type12 now = {type12}")
    type12 *= 2
    print(f"type12 now = {type12}")

    try:
        print(f"converting type2: {type2} - to integer")
        int(type2)
    except:
        print(f"type2 - value of: {type2} - cannot be an integer")

    try:
        float(type1)
        print(f"type1 - value of: {type1} - can be a float = {float(type1)}")
    except:
        print(f"type1 - value of: {type1} - cannot be a float")

    return
