def minCostPath(cost, m, n):
    minMatrix = makeMatrix(m,n)
    minMatrix[0][0] = cost[0][0]
    for j in range(1,n+1):
        minMatrix[0][j] = minMatrix[0][j-1] + cost[0][j]
    for i in range(1,m+1):
        minMatrix[i][0] = minMatrix[i-1][0] + cost[i][0]

    for i in range(1,m+1):
        for j in range(1,n+1):
            minMatrix[i][j] = min(minMatrix[j-1][i], minMatrix[i-1][j], minMatrix[i-1][j-1]) + cost[i][j]

    print cost
    print minMatrix

    return minMatrix[m][n]


def makeMatrix(m,n):
    matr = []
    for i in range(m+1):
        matr.append([None]*(n+1))
    return matr



cost = [[1,2,3],[4,8,2],[1,5,3]]
print minCostPath(cost, 2, 2)
