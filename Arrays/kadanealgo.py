
def maxSubArray(nums):
    # Initialize the variables
    current_max = global_max = nums[0]
    
    # Loop through the array
    for i in range(1, len(nums)):
        # Update current_max
        current_max = max(nums[i], current_max + nums[i])
        
        # Update global_max
        global_max = max(global_max, current_max)
    
    return global_max

