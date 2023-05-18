def solution(arr):
    answer = []
    a = min(arr)
    arr.remove(a)
    if arr:
        return arr
    elif not arr or len(arr) == 1:
        return [-1] 