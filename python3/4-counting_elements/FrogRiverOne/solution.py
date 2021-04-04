def solution(X, A):
    # 時間が足りない
    if X > len(A):
        return -1

    memo = set()
    for i in range(len(A)):
        memo.add(A[i])
        if len(memo) == X:
            return i

    return -1
