def zerooneknapsack(ind,W,w,prices):
    if W == 0:
        return 0
    if ind == 0:
        if w[ind]<=W:
            return prices[0]
        else:
            return 0
    nottake = zerooneknapsack(ind-1,W,w,prices)
    take = 0
    if(w[ind]<=W):
        take = prices[ind] + zerooneknapsack(ind-1,W-w[ind],w,prices)

    return max(take,nottake)

w = [1, 2, 3, 4]        # Item weights
prices = [10, 20, 30, 40]  # Corresponding values
W = 5                    # Knapsack capacity
n = len(w)               # Number of items

max_value = zerooneknapsack(n - 1, W, w, prices)
print(f"Maximum value in the knapsack: {max_value}")

