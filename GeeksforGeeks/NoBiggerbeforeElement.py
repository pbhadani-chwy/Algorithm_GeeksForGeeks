# # def noBiggerElement(arr):
# #     max = 0
# #     count = 0
# #     for i in range(len(arr)):
# #         if (arr[i] >= max):
# #             max = arr[i]
# #             count += 1
# #
# #     return(count)
# #
# # arr = [10, 40, 23, 35, 50, 7, 60]
# # arr1 = [1,2]
# #
# # z = noBiggerElement(arr1)
# # print(z)
#
# # str = '1 2 3 4 5'
# # list = str.split(",")
# # print(list)
#
# def maxDistance(arr, n):
#     # Code here
#     lookup = {}
#     count = 0
#     for i in range(len(arr)):
#         if (arr[i] in lookup):
#             count = i - lookup[arr[i]]
#         else:
#             lookup[arr[i]] = i
#
#     return(count)
#
# arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
# arr1 = [1, 1, 2, 2, 2, 1]
# z = maxDistance(arr1, 12)
# print(z)
#
# # 2
# # 5
# # 3 30 34 5 9
# # 4
# # 54 546 548 60


# Another code

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
        x = format(int(z[i]),'#010b')
        print(x)
        temp.append(x)

    p = (format((t),'#010b'))

    print(p)
    print('type',type(p))
    for i in range(len(p) - 1, 0, -1):
        index = 0
        if (p[i] == '1'):
            index = i
            break


    print("index", index)
    n= 0
    for i in range(len(temp)):
        q = temp[i]
        print(q)
        if q[index] == '1':
            n = n ^ int(z[i])
    result = []
    result.append(str(min(n, t ^ n)))
    result.append(str(max(n, t ^ n)))
    #a = min (n, t ^ n)
    #b = max (n, t ^ n)

    print (' '.join(result))
    T -= 1




