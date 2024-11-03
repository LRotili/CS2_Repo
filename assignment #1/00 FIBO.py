def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        result = fibo(n-1) + fibo(n-2)
   
    return result



print(fibo(23))