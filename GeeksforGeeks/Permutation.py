def FindPerm(soFar, rest):
    res = "".join(soFar)
    #print(soFar)
    #print(rest)
    if (len(rest)== 0):
        #print ("check")
        print (res)
        if (res == '513'):
            return res
        else:
            return ""
    else:
        for i in range(len(rest)):
            remaining = rest[0:i] + rest[i+1:]
            found= FindPerm(soFar + [rest[i]],remaining)

            if (found != ""):
                return found
            #else:
               #return ""
        #print("yaha kitne baar aya hai flow")
        # return ""

soFar = []
rest = ['1','3','5']
finres = FindPerm(soFar,rest)
if(finres != ""):
    print("found",finres)
else:
    print('Not Found')




