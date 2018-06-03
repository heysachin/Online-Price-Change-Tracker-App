

# Created by Sachin Dev on 01/06/18

class Alert(object):
    def __init__(self, user, price_limit, item):
        self.user = user
        self.price_limit = price_limit
        self.item = item

    def __repr__(self):
        return "<Alert for {} on item {} with price {}>".format(self.use.emailr,self.item.name,self.price_limit)
