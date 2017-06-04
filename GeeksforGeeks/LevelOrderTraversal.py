class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printAll_level(root):
    h = height(root)
    for i in range(1, h+1):
        result = []
        printGivenLevel(root,i,result)
        if (i == 1 or i%2 == 0):
            print(result.pop(0))
        else:
            print(result.pop())

        #   startflag = 1
        #     endflag = 0
        # else:
        #     endflag = 1
        #     startflag = 0



def printGivenLevel(root,level,result):

    #countodd = 1
    if root == None:
        return
    if level == 1:
        result.append(root.data)
        #if startflag == 1 and endflag == 0:

        #print(root.data)
            #startflag = 0
            #countodd += 1
    elif level > 1:
        printGivenLevel(root.left, level-1,result)
        printGivenLevel(root.right, level-1,result)

    #if endflag == 1 and startflag == 0:
        #print (root.data)

def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
        #print('lheight', lheight)
        #print('rheight', lheight)


        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level order traversal of binary tree is -")
printAll_level(root)







