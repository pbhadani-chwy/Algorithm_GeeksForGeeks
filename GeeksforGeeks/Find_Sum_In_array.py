# ***********************Tabular Approach **********************************#######
# def calculateMinCoin(z,sumout):
#     temp[0]=0
#     for i in range(len(temp)):
#         for key in z:
#             if int(key) <= i:
#                 j = i - int(key)
#                # print(j)
#                 if (temp[j] + 1 < temp[i]):
#                     #print('check')
#                     temp[i] = temp[j] + 1
#     print(temp)
#     print(temp[len(temp)-1])

# ******************Memoization Technique ************************#######
def calMinCoin(z,temp,sumout):
    if sumout == 0:
        return 0
    if (temp[sumout] != 9999):
        return temp[sumout]
    else:
        for key in z:
            if (int(key) <= sumout):
                print('sumout',sumout)
                j = sumout - int(key)
                #print('check')
                m = calMinCoin(z,temp,j)
                if (m+1 < temp[sumout]):
                    if (sumout == 0):
                        temp[sumout] = 0
                    else:
                        temp[sumout] = m+1
        print('m',temp[sumout])
        return temp[sumout]
    #calMinCoin(z,temp,sumout -1)



T = int(input())
while (T!= 0):
    size = input()
    sampleIn = input()
    sumout = int(input())
    z  = sampleIn.split()
    j = 0
    #print(z)
    temp = [9999]*(sumout + 1)
    temp[0] = 0
    #print(temp)
    #calculateMinCoin(z,temp,sumout)
    calMinCoin(z,temp,sumout)
    print(temp)

    #print((sampleIn))
    T -= 1






