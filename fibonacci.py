

def fibonacci(n):
    a,b = 0,1
    for _ in range(n+1):
        print(a)
        a,b = b, a+b

    # print(a) # Prints final digit if you just want 1 value. 


fibonacci(10) # Print the first 10 fibonacci values.
