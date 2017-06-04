sampleIn = input()
sampleIn_data = []
sampleIn_operation = []
j = 0
while (sampleIn[j] != '/'):
    sampleIn_data.append(sampleIn[j])
    j += 1
n = len(sampleIn)
j = 0
while (sampleIn[n-1-j]!= '/'):
    sampleIn_operation.append(sampleIn[n-1-j])
    j += 1
simple_in = []

# while (simple_in != sampleIn_operation):
#     #print('check')
#     if len(simple_in) != 0:
#         #print('check2')
#         #print('simple_in',simple_in)
#         sampleIn_operation = simple_in
#         print('sample_oper',sampleIn_operation)
#     i = 0
#     simple_in = []
#     while (i < (len(sampleIn_operation))- 1):
#         #print('check1')
#         #if sampleIn_operation[i] == sampleIn_operation[i+1]:
#
#         if sampleIn_operation[i] == 'S':
#             if sampleIn_operation[i+1] == 'S':
#                 simple_in.append('S')
#                 i += 2
#             else:
#                 simple_in.append('S')
#                 i += 1
#         else:
#             if sampleIn_operation[i+1] == 'R':
#                 i += 2
#             else:
#                 simple_in.append('R')
#                 i += 1
#         #print('sampl',simple_in)
# print('SAMPLE_IN',simple_in)

samplestack = []
samplestack.append(sampleIn_operation[0])
for i in range(len(sampleIn_operation)-1,0,-1):
    if (sampleIn_operation[i] == 'S'):
        if (samplestack.pop() == 'S'):
            samplestack.append('S')
        else:
            samplestack.append('R')
            samplestack.append('S')
    else:
        if (samplestack.pop() == 'R'):
            continue
        else:
            samplestack.append('S')
            samplestack.append('R')
#print(samplestack)









    #     sampleIn_operation[i+1] = 0
    # if (sampleIn_operation[i] == sampleIn_operation[i+1] == 'S'):
    #     sampleIn_operation[i] = 0






def reverse_op (sampleIn_data):
    stack1 = []
    finres = []
    for i in range(len(sampleIn_data)):
        stack1.append(sampleIn_data[i])

    for i in range(len(sampleIn_data)):
        k = stack1.pop()
        if (k == '('):
            finres.append(')')
        if (k == ')'):
            finres.append('(')
        if (k != '(' and k != ')'):

            finres.append(k)
    return (finres)
    print("".join(finres))

# j += 1
# while (j < len(sampleIn)):
#
#     j += 1



# sampleIn_operation = sampleIn.lstrip("/")
#print(sampleIn_data)
#print(sampleIn_operation)
# z = []
# for i in sampleIn:
#     if i != " ":
#         z.append(i)
def simple_exp(sampleIn_data):
    #print(sampleIn_data)
    stack = []
    templist = []
    for i in range(len(sampleIn_data)):
        if (sampleIn_data[i] == '('):
            if (len(stack) != 0):
                stklst,val = stack.pop()
                stack.append(['(',val])

            #if (stklst == '('):
                val += 1
                stack.append(['(', val])
                templist.append(val)
                # print(templist)
                # print('stack',stack)
                #print(stack)
            else:
                stack.append(['(',1])
                templist.append(1)
                # print(templist)
                # print('stack',stack)

        if (sampleIn_data[i] == ')'):
            #print('stack',stack)
            stklst,val = stack.pop()
            templist.append(-val)
            # print(templist)
            # print('stack',stack)
        if (sampleIn_data[i] != ')' and sampleIn_data[i] != '('):
            templist.append(0)

    #print(templist)

    for i in range(len(templist)):
        if templist[0] == 1:
            templist[0] = 99
            for j in range(1,len(templist)):
                if templist[j] == -1:
                    templist[j] = 99
                    break
        else:
            if (templist[i] == templist[i-1] + 1 and templist[i] > 1):

                for j in range(i+1,len(templist)):
                    if templist[j] == -(templist[i]):
                        templist[j] = 99
                templist[i] = 99

    res = []
    for i in range(len(sampleIn_data)):
        if templist[i] != 99:
            res.append(sampleIn_data[i])

    return (res)
    print("".join(res))
    #print(templist)
revout = []
simout = []
for i in range(len(samplestack)-1,0,-1):
    if i == len(samplestack)-1:
        #print(samplestack[i])
        if (samplestack[i] == 'R'):
            revout = reverse_op(sampleIn_data)
        else:
            simout = simple_exp(sampleIn_data)
    else:
        if (samplestack[i] == 'R'):
            revout = reverse_op(simout)
        else:
            simout = simple_exp(revout)

if(samplestack[0] == 'S'):
    print("".join(simout))
else:
    print("".join(revout))







# reverse_op(sampleIn_data)
# simple_exp(sampleIn_data)



#stack.append(sampleIn_data[i])




#print(z)



