'''Instructions
The goal of this kata is two-fold:

1.) You must produce a fibonacci sequence in the form of an array, containing a number of items equal to the input provided.

2.) You must replace all numbers in the sequence divisible by 3 with Fizz, those divisible by 5 with Buzz, and those divisible by both 3 and 5 with FizzBuzz.

For the sake of this kata, you can assume all input will be a positive integer.'''

def fibs_fizz_buzz(n):
    fib = fibonacci_generator(n)
    
    i = 0
    while i < len(fib):
        val = fib[i]
        result = ""
        if(val % 3 == 0):
            result += "Fizz"
            
        if(val % 5 == 0):
            result += "Buzz"
        
        if(result != ""):
            fib[i] = result
        
        i += 1
    
    return fib

def fibonacci_generator(fibsToGenerate):
    i = 0
    arr = []
    while i < fibsToGenerate:
        if(i <= 1):
            arr.append(1)
        else:
            arr.append((arr[len(arr)-1]) + (arr[len(arr)-2]))
        i += 1
    return arr