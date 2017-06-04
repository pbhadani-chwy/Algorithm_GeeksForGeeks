#code

def findMin(s, e, z):
    mid = int((s + e)/2)
    print('mid',mid)
    print(z[mid])
    if ((z[mid] < z[mid + 1] and z[mid] < z[mid - 1]) or z[mid] == z[e] or z[mid] == z[s]):
        print(z[mid])
    else:
        if (z[e] > z[s]):
            findMin(s, mid - 1, z)
        else:
            findMin(mid+1, e, z)


T = int(input())
while (T != 0):
    size = int(input())
    sampleIn = input()
    z = (sampleIn.split())
    final = findMin(0,size - 1, z)
    #print (final)
    T -= 1








