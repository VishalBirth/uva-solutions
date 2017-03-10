def intInput():
    return int(input())
def twoIntInput():
    i = input().split()
    return int(i[0]), int(i[1]);
no=intInput()
while (no!=0):
    tempi, tempj = twoIntInput();
    for num in range(0,no):
      #  print(num)
        i,j = twoIntInput()
        i -= tempi
        j -= tempj
        if (i==0) | (j==0):
            print("divisa")
        elif i>0:
            if j>0:
                print("NE")
            else:
                print("SE")
        else:
            if j>0:
                print("NO")
            else:
                print("SO")
    no=intInput()
