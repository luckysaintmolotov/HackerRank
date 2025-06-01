ef plusMinus(arr):
    n = len(arr)  # Get the size of the array
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # Count positive, negative, and zero elements
    for number in arr:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

    # Calculate ratios
    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n

    # Print results with 6 decimal places
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")
