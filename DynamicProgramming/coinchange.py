
def coinChange(i,amount,prices):
    if i < 0 or amount < 0:
        return float("inf")
    if amount == 0:
        return 0
    if i == 0:
        if amount%prices[i] == 0:
            return amount // prices[i]
        else:
            return float("inf")    
    nottake = coinChange(i-1,amount,prices)
    take = float("inf")
    if(prices[i] <= amount):
        take = 1 + coinChange(i,amount-prices[i],prices)
    return min(take,nottake)

