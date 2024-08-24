def buy_icecream(budget, prices):
    pairs = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] + prices[j] == budget :
                pairs.append([i,j])
    return pairs

print(buy_icecream(4,[1,2,3,4,2]))

def find_ice_cream_indices(m, prices):
    price_map = {}
    
    for i, price in enumerate(prices):
        complement = m - price
        if complement in price_map:
            return price_map[complement], i
        price_map[price] = i

m = 4
prices = [1, 4, 5, 3, 2, 2]
result = find_ice_cream_indices(m, prices)
print(result)  # Output: (0, 3)
