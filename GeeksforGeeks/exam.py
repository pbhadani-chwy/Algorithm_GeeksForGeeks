# def findIndex(arr,s,e,k):
#     mid = int((s + e)/2)
#     if (arr[mid] == k):
#         print (type(mid), mid)
#         return mid
#     else:
#         if(arr[mid] > k):
#             return findIndex(arr,s,mid-1,k)
#         else:
#             return findIndex(arr,mid+1, e,k)
#
#
# global mid
# def subarray_median(arr, k):
#     z = 0
#     z = findIndex(arr,0,len(arr)-1,k)
#     print(z)
#
#     if(z%2 !=0):
#         p = int((0 + z)/2)
#         result = (arr[p] + arr[p+1])/2
#         return result
#     else:
#         p = int((0+z)/2)
#         result = (arr[p])
#         return result
#
# arr = [1,3, 5, 7, 8, 12, 14, 16, 18]
# final= subarray_median(arr, 14)
# print(final)
# def matrix():
#     grid_width = 4
#     grid_height = 5
#     z = [][]
#     for i in grid_width:
#         for j in grid_height:
#             z[i][j] = 1
# matrix = 5*[5*[0]]
# print(matrix

      # Complete the function below.

def findnear (matrix,grid_width, grid_height,conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y ):
    x1_conn = start_x - conn_x1
    y1_conn = start_y - conn_y1
    x2_conn = start_x - conn_x2
    y2_conn = start_y - conn_x2

    if (x1_conn > grid_width or x1_conn < grid_width or y1_conn > grid_height or y1_conn < grid_height) or (x2_conn > grid_width or x2_conn < grid_width or y2_conn > grid_height or y2_conn < grid_height):
        return matrix
    else:
        matrix[x1_conn][x1_conn] = 0
        matrix[x1_conn][x1_conn] = 0
        return findnear (matrix,grid_width, grid_height,conn_x1, conn_y1, conn_x2, conn_y2,x1_conn, y1_conn)
        return findnear (matrix,grid_width, grid_height,conn_x1, conn_y1, conn_x2, conn_y2,x2_conn, y2_conn)






def  num_illuminated(grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y):

    """
    grid_width - the width of the room grid
    grid_height - the height of the room grid
    conn_x1 - the x-coordinate of the first lamp connection
    conn_y1 - the y-coordinate of the first lamp connection
    conn_x2 - the x-coordinate of the second lamp connection
    conn_y2 - the y-coordinate of the second lamp connection
    start_x - the x-coordinate of the first lamp turned off
    start_y - the y-coordinate of the first lamp turned off
    """
    matrix = grid_height*[grid_width*[1]]
    grid_width = 10
    grid_height = 5
    conn_x1 = -1
    conn_y1 = 0
    conn_x2 = -1
    conn_y2 = -1
    matrix = findnear (matrix, grid_width, grid_height,conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y )
    count = 0
    for i in range(grid_height):
       for j in range(grid_width):
           print(matrix[i][j])
               #count += 1
    for i in range(grid_height):
       for j in range(grid_width):
           if(matrix[i][j] == 1):
               count += 1
    print(count)


grid_width = 10
grid_height = 5
conn_x1 = -1
conn_y1 = 0
conn_x2 = -1
conn_y2 = -1
start_x = 6
start_y = 4
num_illuminated(grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y)


