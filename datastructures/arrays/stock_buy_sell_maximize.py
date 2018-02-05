def  stock_buy_sell(array):
    n=len(array)
    if n==1:
        return
    count=0
    buy = []
    sell = []
    for i in range(n-1):
        if array[i]<array[i+1] and len(buy)==len(sell):
            buy.append(i)
        if array[i]>array[i+1] and len(buy)>len(sell):
            sell.append(i)
        if i==n-2 and len(buy)>len(sell):
            sell.append(i+1)
    for i in range(len(buy)):
        print("Buy on {},".format(buy[i]), end=' ')
        print("Sell on {}".format(sell[i]), end=' ')
        print()

stock_buy_sell([100, 180, 260, 310, 40, 535, 695])
