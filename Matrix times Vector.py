def solve(a: list[list[int | float]], b: list[int | float]) -> int:
    if len(a) == 0 or len(b) == 0 or len(a[0]) != len(b):
        return -1
    x = len(b)
    o = [0]*x
    for i in range(len(a)):
        if len(a[i]) != len(b):
            return -1
        else:
            for j in range(len(b)):
                o[i] += (a[i][j]*b[j])
    return o

a = [[1,2,3],[2,4,5],[6,8,9]]
b = [1,2,3]
print(solve(a, b))
