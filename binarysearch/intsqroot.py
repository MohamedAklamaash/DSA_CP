
def sqrt_integer(x):
    if x < 2:  # Handle 0 and 1 directly
        return x

    low, high = 0, x
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            ans = mid  # Store the floor value
            low = mid + 1
        else:
            high = mid - 1

    return ans  # Return the floor of the square root

# Example
print(sqrt_integer(16))  # Output: 4
print(sqrt_integer(20))  # Output: 4


