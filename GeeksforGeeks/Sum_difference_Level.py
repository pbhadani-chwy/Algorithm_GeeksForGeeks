# Your task is to complete this function
# Function should return an integer
class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
def getLevelDiff(root):
    # Code here
    z = getHeight(root)
    print(z)
    sumeven = 0
    sumodd = 0
    for i in range(z):
        res = []
        getLevelSum(root,i,res)
        if (i%2 == 0):
            sumeven += sum(res)
        else:
            sumodd += sum(res)

    final = sumeven - sumodd
    print(final)
        #print(res)


def getLevelSum(root,h,res):
    if root == None:
        return
    if (h == 0):
        return res.append(root.data)
    #elif (root.left == None
    elif (root.left != None) and (root.right == None):
        return getLevelSum(root.left,h-1,res)
    elif (root.right != None) and (root.left == None):
        return getLevelSum(root.right, h-1,res)
    else:

        return (getLevelSum(root.left,h-1,res),getLevelSum(root.right,h-1,res))



def getHeight(root):
    if (root == None):
        return 0
    else:
        leftHeight = 1 + getHeight(root.left)
        rightHeight = 1 + getHeight(root.right)
        return max(leftHeight, rightHeight)

rootT = Node(50)
rootT.left = Node(26)
#root.right = Node(3)
rootT.left.left = Node(10)
rootT.left.left.right = Node(30)
rootT.left.left.left = Node(20)
rootT.left.left.left.left = Node(40)
rootT.left.left.left.right = Node(60)
rootT.right = Node(60)
rootT.right.left = Node(25)
rootT.right.right = Node(30)


getLevelDiff(rootT)




# char = 'A'
# integer = int(char)
# print(integer)


#code


def FindsubsetSum(soFar,rest,sumB,res):
    if (sum(map(int,soFar)) == sumB):
        return res.append(soFar)

    if (len(rest) == 0):
        return


    else:
        FindsubsetSum(soFar + [rest[0]], rest[1:],sumB,res) #First Char included
        FindsubsetSum(soFar,rest[1:],sumB,res) #First char not included

T = input()
while (T != 0):
    size = input()
    sampleIn = raw_input()
    z = sampleIn.split()
    sumB = input()
    soFar = []
    res = []
    FindsubsetSum(soFar,z,sumB,res)
    print(res)
    if (len(res) == 0):
        print("Empty")
    else:
        # res1 = []
        # res1 = res.sort()
        # print(res1)
        for i in range(len(res)-1):
            print('i',i)
            for j in range(i+1, len(res)):
                print('j',j)
                if (set(res[i]) == set(res[j])):
                    del(res[i])
        print(res)

    T -= 1


