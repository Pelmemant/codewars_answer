"""The Fibonacci numbers are the numbers in the following integer sequence (Fn): 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such that:
F(0)=0F(1)=1F(n)=F(n−1)+F(n−2)F(0) = 0\\F(1) = 1\\F(n) = F(n-1) + F(n-2)F(0)=0F(1)=1F(n)=F(n−1)+F(n−2)

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying:
F(n)∗F(n+1)=prodF(n) * F(n+1) = prodF(n)∗F(n+1)=prod

Your function takes an integer (prod) and returns an array/tuple 
(check the function signature/sample tests for the return type in your language):"""

def product_fib(_prod):
    a = 0
    b = 1
    c = 0
    d = 0
    while d < _prod:
        c = a + b
        a = b
        b = c
        d = a*b
    if d == _prod:
        return [a, b, True]
    return [a, b, False]
