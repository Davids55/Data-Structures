set_1 = {10, 15, 20, 40, 55}
set_2 = {30, 50, 15, 25}


set_3 = set_1.intersection(set_2)
if len(set_3) > 0:
    print(set_1.union(set_2))
else:
    print("no matching items were found")