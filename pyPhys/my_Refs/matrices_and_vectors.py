
import numpy as np

arr1 = [[1,2,3],[11,22,33],[111,222,333]]
arr2 = [[4,5,6],[44,55,66],[444,555,666]]

result = [[0,0,0],
 [0,0,0],
 [0,0,0]]

for i in range(len(arr1)):
    for j in range(len(arr2[0])):
        for k in range(len(arr2)):
            result[i][j] += arr1[i][k] * arr2[k][j]

# for r in result:
#  print(r)

arr3 = np.array([[1,2,3],[11,22,33],[111,222,333]])
arr4 = np.array([[4,5,6],[44,55,66],[444,555,666]])

print(arr3*arr4)
print(arr3.dot(arr4))
