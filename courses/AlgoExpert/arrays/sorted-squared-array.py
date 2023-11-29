from collections import deque

def sorted_squared_array(array):
    n = len(array)
    result = deque()
    start, end = 0, n - 1
    
    for _ in range(n):
        if abs(array[start]) > abs(array[end]):
            result.appendleft(array[start] ** 2)
            start += 1
        else:
            result.appendleft(array[end] ** 2)
            end -= 1
            
    return list(result)