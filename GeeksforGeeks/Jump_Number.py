#code
T = int(input())
while (T!=0):
    size = input()
    #len_size = len(size)
    disc = {}
    for i in range(int(size)+1):
        if i <= 10:
            z = [str(d) for d in str(i)]
            disc[i] = z
        # elif (len(i)) == 1:
        #     dics[i] = 0
        else:
            k = 0
            flag = 0
            z = [str(d) for d in str(i)]
            #print(z)
            #z = m.split()
            #print(z)
            for j in range(len(z)):
                if j == 0:
                    continue
                if (int(z[j]) - int(z [j-1]) == 1) or (int(z[j]) - int(z [j-1]) == -1):
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                disc[i] = z
    #print(disc)
    fr = sorted(disc.items(), key = lambda x: x[1])
    final = []
    final_update= []
    for k,v in fr:
        final.append(v)
    #print(final)
    for i in final:
        p = (''.join(i))
        final_update.append(p)
    #print(final_update)

    print(' '.join(final_update))
    #print(final)
    T -= 1
