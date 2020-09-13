x = input()
l = [2,4,5,7,9]
i = [0,1,6,8]
if int(x[-1]) in l:
    print("hon")
elif int(x[-1]) in i:
    print("pon")
elif x[-1] == "3":
    print("bon")
