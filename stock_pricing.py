
def max_profit(prices):
    #if list is empty nothing can be returned
    if not prices:
        return 0
   
    #initialize both min to index 0 and max to 0 at start
    min_price, max_profit = prices[0], 0
    
    for price in prices:
        #price lower then min_price so update it 
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit


prices=[2, 10, 6, 5, 4]
print(max_profit(prices))  

