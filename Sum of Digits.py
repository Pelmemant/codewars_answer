"""Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer."""

def digital_root(n):
    while len(str(n)) > 1:
        a = 0
        while n > 0:
            i = n % 10
            a += i
            n //= 10
        n = a
    return n
