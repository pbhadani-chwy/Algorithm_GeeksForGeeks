def RecurSubset(soFar, rest,length):
    if (len(rest)== 0):
        if (len(soFar)== length):

            print("".join(soFar))

    else:
        RecurSubset(soFar + [rest[0]], rest[1:],length)
        RecurSubset(soFar,rest[1:],length)

soFar = []
length = 3
rest = ['a','b','c','d','e']
RecurSubset(soFar,rest,length)

