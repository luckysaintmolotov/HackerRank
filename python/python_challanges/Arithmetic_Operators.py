if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    
    def solution1(a, b):
        def sum_of(a, b):
            return a + b
        def diff(a, b):
            return a - b
        def prod(a, b):
            return a * b
        print(sum_of(a, b))
        print(diff(a, b))
        print(prod(a, b))

def solution2(a, b):
    def return_values(a, b):
        return [a + b, a - b, a * b]
    for val in return_values(a, b):
        print(val)


solution1(a, b)
solution2(a, b)