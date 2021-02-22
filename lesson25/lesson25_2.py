def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)

def FibonacciSearch(arr, x):
    m = 0
    while FibonacciGenerator(m) < len(arr):
        m = m + 1
    offset = -1
    while (FibonacciGenerator(m) > 1):
        i = min( offset + FibonacciGenerator(m - 2) , len(arr) - 1)
        if (x > arr[i]):
            m = m - 1
            offset = i
        elif (x < arr[i]):
            m = m - 2
        else:
            return i
    if(FibonacciGenerator(m - 1) and arr[offset + 1] == x):
        return offset + 1
    return -1

if __name__ == '__main__':
    print(FibonacciSearch([1,2,3,4],3))