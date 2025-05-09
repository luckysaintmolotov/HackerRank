'''There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first

letters of the infinite string.

'''
s = 'aba'
n = 10
def repeatedString(s, n):
    a_in_s = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)
    total_a = a_in_s * full_repeats + s[:remainder].count('a')
    print(total_a)
    
    return total_a
    

repeatedString(s, n)
