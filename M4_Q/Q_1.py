import csv

class Stock:
    def __init__(self,Name,Symbol,Exchange,Price):
        self.Name = Name
        self.Symbol = Symbol
        self.Exchange = Exchange
        self.Price = Price
    
    def __str__(self):
        print(f"{self.Name},{self.Symbol},{self.Exchange},{self.Price}")

def clean_init_get_stocks():
    stock_lst = []
    try:
        with open("Stock.csv","r") as f:
            data = csv.reader(f,delimiter=",")
            h = True
            for d in data:
                if h:
                    h = False
                    continue
                stock_lst.append(Stock(*d))
        for s in stock_lst:
            if "K" in s.Price:
                s.Price = float(s.Price.strip().replace("K",""))*1000
            else:
                s.Price = float(s.Price.strip())

        return stock_lst

    except Exception as err:
        print('{},value{!r}'.format(err.args[0],err))
    
def show_stock_by_price(price):
    st_lst = clean_init_get_stocks()
    f = filter(lambda x:x.Price <= price,st_lst)
    if f:
        show_stock_info(list(f))
    else:
        print("No stock found for the given price:{price}")
    
def show_stock_info(list_1):
    for data in list_1:
        print(data)

price = int(input("Enter the price:"))
show_stock_by_price(price)

'''def max_min_stock_price():
    st_lst = clean_init_get_stocks()'''





