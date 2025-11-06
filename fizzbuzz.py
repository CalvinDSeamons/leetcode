def fizzbuzz(num): # The most basic of basic programs.
    for i in range(1,num+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(28)
