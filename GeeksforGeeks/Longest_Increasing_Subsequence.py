T = int(input())

while T != 0:
    size = input()
    sampleIn = input()
    z = sampleIn.split()
    a = [1] * int(size)

    for i in range(1,int(size)):
        j = 0
        while (j < i):
            if (int(z[j])<= int(z[i])):
                if (a[i] < a[j]+1):
                    a[i] = a[j]+1
            j += 1

    print(a)
    print(max(a))
    T -= 1






