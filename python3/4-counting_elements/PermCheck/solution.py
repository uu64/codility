def solution(A):
    A.sort()
    N = len(A)

    for i in range(len(A)):
        if A[i] != i+1 or A[i] > N:
            return 0

    return 1


print(solution([4, 1, 1, 1]))
print(solution([99999, 100000]))
print(solution([100000]))