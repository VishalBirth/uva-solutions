def getInput():
    return input()
def intInput():
    return int(getInput())
def twoIntInput():
    i = getInput().split()
    return int(i[0]), int(i[1]);
def twoFloatIntInput():
    i = getInput().split()
    return float(i[0]), int(i[1]);


i, j=twoIntInput()
rfp=0;
while (i!=0) & (j!=0):
    rfp+=1
    maxrequiremnt=0
    price=0.0
    name=""
    for num in range(0,i):
        req = getInput()
    for num in range(0,j):
        curname = getInput();
        cost, requiremnt = twoFloatIntInput()
        for k in range(0,requiremnt):
            waste = getInput();
        if requiremnt > maxrequiremnt:
            price= cost
            name= curname
            maxrequiremnt=requiremnt
        elif (requiremnt == maxrequiremnt) & (cost < price):
            price= cost
            name= curname
            maxrequiremnt=requiremnt
    print("RFP #"+str(rfp))
    print(name)
    print("");
    i,j = twoIntInput()

