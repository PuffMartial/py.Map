store = [("shirt",20.00),("pank",25.00),("jacket",50.00),]


to_rands = lambda data: (data[0],data[1]*19.00)


store_rands = list(map(to_rands, store))


for i in store_rands:
    print(i)