
def max_game_duration(binary_string):
    n = len(binary_string)
    total_duration = 0
    empty_spaces = binary_string.count('0')  # Total number of empty spaces

    for char in binary_string:
        if char == '1':
            # Each '1' takes 1 second to select and moves `empty_spaces` steps to the right
            total_duration += 1 + empty_spaces
        else:
            # For '0', reduce the available empty spaces
            empty_spaces -= 1
    
    return total_duration

# Example usage
binary_string = "1001001"
max_duration = max_game_duration(binary_string)
print(f"Maximum Duration: {max_duration}")
