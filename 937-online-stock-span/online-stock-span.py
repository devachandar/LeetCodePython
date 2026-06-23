class StockSpanner:

    def __init__(self):
        self.stocks = []


    def next(self, price: int) -> int:
        self.stocks.append(price)
        count = 0
        # print("d",self.stocks)
        for stock in self.stocks[::-1]:
            # print(stock,price)
            if price >= stock:
                count+=1
            else:
                break
        print(count)
        return count




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

