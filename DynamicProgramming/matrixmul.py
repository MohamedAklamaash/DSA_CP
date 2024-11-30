
def matrixmul(arr,i,j):
    if i == j:
        return 0
    min_mul = float("inf")
    for k in range(i,j):
        count = matrixmul(arr,i,k) + matrixmul(arr,k+1,j) + arr[i-1]*arr[k]*arr[j]
        min_mul = min(count,min_mul)
    return min_mul

# Example usage
arr = [1, 2, 3, 4]  # Dimensions of matrices: A(1x2), B(2x3), C(3x4)
n = len(arr)

# Call matrixmul to find the minimum number of multiplications
result = matrixmul(arr, 1, n - 1)
print(f"Minimum number of multiplications: {result}")

