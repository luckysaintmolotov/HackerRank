def plusMinus(arr):
    is_positive = [i for i in arr if i >0]
    is_negative = [i for i in arr if i <0]
    is_zero = [i for i in arr if i == 0]
    positive_ratio = len(is_positive)/len(arr)
    negative_ratio = len(is_negative)/len(arr)
    zero_ratio = len(is_zero)/len(arr)
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))