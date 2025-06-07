"""Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case."""

def find_missing_letter(chars):
    letters = [chr(i) for i in range(ord('A'), ord('z')+1)]
    letters = letters[letters.index(chars[0]):letters.index(chars[-1])]
    return "".join([i for i in letters if i not in chars])
