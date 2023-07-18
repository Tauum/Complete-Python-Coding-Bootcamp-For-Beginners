def run():
    tuple_example = ("key", "value")
    tuple_example_2 = ("apple", 5)
    print(f"tuple_example (key, value) = {tuple_example[0], tuple_example[1]}")
    print(f"tuple_example (key, value) = {tuple_example_2[0], tuple_example_2[1]}")

    tuple_example1 = ("val1", "val2")
    tuple_example2 = ("valA", "valB")
    print(f"{tuple_example1}")
    print(f"{tuple_example2}")
    tuples_combined = tuple_example1 + tuple_example2
    print(tuples_combined)
    del tuple_example1
    try:
        print(f"{tuple_example1}")
    except:
        print(
            f"touple 1 is no longer available but it is still in combined - {tuples_combined}")

    print(f"length of tuple_combined = {len(tuples_combined)}")
    print(f"min of tuple_combined = {min(tuples_combined)}")
    print(f"max of tuple_combined = {max(tuples_combined)}")

    return
