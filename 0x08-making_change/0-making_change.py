#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for amnt in range(1, total + 1):
        for coin in coins:
            if coin <= amnt:
                dp[amnt] = min(dp[amnt], dp[amnt - coin] + 1)
    
    return -1 if dp[total] == float('inf') else dp[total]


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
    
    print(makeChange([1, 5, 10, 25], 30))
    print(makeChange([2], 3))
    print(makeChange([1], 0))
    print(makeChange([1, 3, 4], 6))
