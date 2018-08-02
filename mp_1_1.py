def pattern(num):
    for i in range(0,num):
        for j in range(0,i+1):
            print(" 1",end="")
        print("\n")
num=5
pattern(num)