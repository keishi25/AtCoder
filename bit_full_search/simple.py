ll = [2,9,0]

for i in range(8):
    lll = 0
    llll=[]
    for j in range(3):
        if (i >> j & 1):
            lll += ll[j]
            llll.append("+")
        else:
            lll -= ll[j]
            llll.append("-")
    if lll == 7:
        print(llll)
        print(lll)