def solution(N, A):
    counter = [0 for i in range(N)]

    maxv = 0
    memo = (-1, maxv)
    modified = [-1 for i in range(N)]
    for i in range(len(A)):
        v = A[i]
        if v == N+1:
            memo = (i, maxv)
        else:
            if memo[0] > modified[v-1] and counter[v-1] != memo[1]:
                counter[v-1] = memo[1]
            modified[v-1] = i
            counter[v-1] += 1
            maxv = max(maxv, counter[v-1])

    if memo[0] == -1:
        return counter
    else:
        for i in range(N):
            if modified[i] < memo[0]:
                counter[i] = memo[1]
        return counter

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
print(solution(20, [21, 7, 14, 21, 14, 21, 18, 5, 5, 21, 14, 7, 6, 21, 6, 14, 18, 15, 4, 10, 19, 5, 10, 10, 12, 10, 17, 4, 16, 21]))
print(solution(1, [1]))
print(solution(1, [2]))