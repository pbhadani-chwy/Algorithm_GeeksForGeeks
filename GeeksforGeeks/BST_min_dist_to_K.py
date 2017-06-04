# your task is to complete this function
# Function should return an integer
def maxDiff(root, k):
    min_1 = 9999
    min_node = None
    z = findMin(root,k,min_1, min_node)
    #print('z', z)
    return(z)

def findMin(root,k, min_1,min_node):
    # Code here
    #base case
    if (root == None):
        return min_1,min_node
    else:
        #print(root.data)
        diff = abs(root.data - k)
        if (diff < min_1):
            min_1 = diff
            min_node = root.data
        #if (root.left != None):
        return min(findMin(root.left,k,min_1,min_node),findMin(root.right,k,min_1,min_node))


    #return min_1
    # if (root.left!= None):
    #     return findMin(root.left,k,min_1)
    # elif (root.right!= None):
    #     return findMin(root.right,k,min_1)
    # else:
    #     findMin(root.left,k,min_1)
    #     findMin(root.right,k,min_1)

    # return min_1



