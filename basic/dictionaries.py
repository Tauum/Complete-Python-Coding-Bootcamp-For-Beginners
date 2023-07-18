
def run():
    dictionary1 = {"item5": 6, "item6": "shoes"}
    print(f"dictionary1 - {dictionary1}")
    print(f"dictionary1 - key 'item6' {dictionary1['item6']}")
    print(f"dictionary1 - only keys {dictionary1.keys()}")
    print(f"dictionary1 - only values {dictionary1.values()}")
    print(f"dictionary1 - as tuples {dictionary1.items()}")
    dictionary1["item5"] = 15
    print(f"dictionary1 - updating item5 to 15 > {dictionary1}")
    return