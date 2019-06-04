from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    # This problem uses a similiar technique as trapping rain water problem
    # by caching the max sale going forwards and then backwards
    max_sale = 0
    cur_min, max_sale_forward = float('inf'), [0] * len(prices)
    # first we check going forward and calculated the max first buy we can
    # get for the first buy, from each index.  We keep that value in case we
    # cannot sell two times in a value representing the max total sale
    for i, price in enumerate(prices):
        cur_min = min(price, cur_min)
        max_sale = max(max_sale, price - cur_min)
        max_sale_forward[i] = max_sale
    # then we go backwards, and calculate the max second buy.  By storing the 
    # Max price encountered so far and subtracting it from the current price
    # we can determine the best second sell price we could get from our current
    # location.  Add this to the max sale from one index before to see if it beats
    # the max total sale.  We add from the previous position because we must buy
    # on a position after the first sell
    max_price = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price = max(max_price, price)
        max_sale = max(max_sale,
                            max_price - price + max_sale_forward[i - 1])

    return max_sale


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
