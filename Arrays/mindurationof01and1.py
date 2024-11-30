
def min_game_duration(binary_string):
    n = len(binary_string)
    total_duration = 0
    next_position = n - 1  # Next available position for a '1' (starting from the rightmost)

    # Traverse the string from right to left
    for i in range(n - 1, -1, -1):
        if binary_string[i] == '1':
            # Add selection time (1 second) and movement time
            total_duration += 1 + (next_position - i)
            next_position -= 1  # Update the next available position for the next '1'
    
    return total_duration

# Example usage
binary_string = "1001001"
min_duration = min_game_duration(binary_string)
print(f"Minimum Duration: {min_duration}")

