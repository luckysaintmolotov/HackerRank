def diagonalDifference(arr):
    primary_sum = 0
    secondary_sum = 0
    n = len(arr)  # Get the size of the square matrix

    for i in range(n):
        primary_sum += arr[i][i]  # Sum for primary diagonal
        secondary_sum += arr[i][n - 1 - i]  # Sum for secondary diagonal

    return abs(primary_sum - secondary_sum)  # Return the absolute difference