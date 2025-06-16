"""
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.
"""


def sockMerchant(n, ar):
    counts = {}
    for i in ar:
        counts[i] = counts.get(i, 0) + 1
        pairs = 0
    for count in counts.values():
        pairs += count // 2
    print(pairs)
    return pairs

n = 7
ar = [1,2,1,2,1,3,2]
sockMerchant(n,ar)