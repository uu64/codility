def solution(X, Y, D):
    div, mod = divmod(Y-X, D)
    if mod == 0:
        return div
    return div + 1