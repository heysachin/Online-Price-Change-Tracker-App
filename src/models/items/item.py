

# Created by Sachin Dev on 01/06/18

class Item(object):
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def __repr__(self):
        return "<Item {} with url {}>".format(self.name,self.url)

    def load_item(self):
        #Amazon <span id="priceblock_ourprice" class="a-size-medium a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span> 57,990.00</span>

        pass