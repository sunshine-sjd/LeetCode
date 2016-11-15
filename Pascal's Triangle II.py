'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1]. 
'''


def getRow(rowIndex):
    pascal_triangle = [[1]]
    for row in range(1,rowIndex+1):
        pascal_triangle.append([1]+[pascal_triangle[row-1][i-1]+pascal_triangle[row-1][i] for i in range(1,row)]+[1])
    return pascal_triangle[-1]
