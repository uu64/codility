def solution(A):
    if not A:
        return 1
    A.sort()
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1
    return len(A) + 1


print(solution([1]))