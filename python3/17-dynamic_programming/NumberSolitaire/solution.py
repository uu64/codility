def solution(A):
    N = len(A)
    memo = [None for i in range(N)]
    memo[0] = A[0]
    for i in range(N):
        maxScore = None
        for j in range(max(0, i - 6), i):
            if maxScore is None or maxScore < memo[j] + A[i]:
                maxScore = memo[j] + A[i]
            memo[i] = maxScore

    # print(memo)
    return memo[-1]

solution([1, -2, 0, 9, -1, -2])
