
#code
T = int(input())
while (T != 0):
    size = input()
    SampleIn = str(input())
    z = SampleIn.split()
    t = 0
    temp = []
    for i in range(len(z)):
        t = int(z[i]) ^ t
        x = format(int(z[i]),'#032b')
        #print(x)
        temp.append(x)

    p = (format((t),'#032b'))

    #print(p)
    #print('type',type(p))
    for i in range(len(p) - 1, 0, -1):
        index = 0
        if (p[i] == '1'):
            index = i
            break


    #print("index", index)
    n= 0
    for i in range(len(temp)):
        q = temp[i]
        #print(q)
        if q[index] == '1':
            n = n ^ int(z[i])
    result = []
    result.append(str(min(n, t ^ n)))
    result.append(str(max(n, t ^ n)))
    #a = min (n, t ^ n)
    #b = max (n, t ^ n)

    print (' '.join(result))
    T -= 1




