class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def isSubtree(rootT, rootS):
    if (rootT != None) and (rootS == None):
        return 1
    elif (rootT == None) and  (rootS == None):
        return 0
    elif (rootT != None) and (rootS != None):
        z = []
        findInorder(rootS,z)

        p = []
        findInorder(rootT,p)
        print (z, p)
        if (set(z).issubset(set(p))):
            print( set(z) < set(p))
        else:
            print('0')
        # for i in range(len(p)):
        #     if (p[i] == z[i]):
        #         k = 0
        #         while(k != len(z)):
        #             if ()






def findInorder(root, m):
    if root == None:
        return
    else:
        #m.append(root.data)
        #if (root.left != None) and (root.right == None):
            #return findInorder(root.left, m)

        #if (root.right != None) and  (root.left == None):
            #return findInorder (root.right, m)
        #else:
        return (findInorder(root.left, m),m.append(root.data), findInorder(root.right, m))

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


rootS = Node(26)
rootS.left = Node(10)
#root.right = Node(3)
rootS.left.left = Node(20)
rootS.left.right = Node(30)
rootS.left.left.left = Node(40)
rootS.left.left.right = Node(60)

isSubtree(rootT,rootS)









