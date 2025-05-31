"""Description:

Write a function that takes an integer as input, and returns the number of bits that are equal to one 
in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case"""

def count_bits(n):
    """Сегодня я узнал, что в пайтон есть функция bin которая перводит обычное число в двоичное"""
    bin_n = str(bin(n))
    """А тут просто возвращается поиск числа 1 в строке bin_n"""
    return bin_n.count(str(1))
