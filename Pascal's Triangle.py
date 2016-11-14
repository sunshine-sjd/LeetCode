'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

def generate(numRows):
    pascal_triangle = [[1]]
    for row in range(1, numRows):
        pascal_triangle.append([1] + [pascal_triangle[row-1][i-1]+pascal_triangle[row-1][i] for i in range(1, row)] + [1])
    return pascal_triangle if numRows else []
