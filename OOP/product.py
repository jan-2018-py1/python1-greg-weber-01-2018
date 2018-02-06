
class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
  
    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, decimal):
        self.price += round(self.price * decimal, 2)
        return self

    def return_item(self, return_state):
        if return_state == 'defective':
            self.status = 'defective'
            self.price = 0
        if return_state  == 'new in box':
            self.status = 'for sale'
        if return_state == 'opened box':
            self.status = 'used'
            self.price = self.price * .8  #%20 discount
        return self.display_info()
    
    def display_info(self):
        print 'Price: ${}'.format(self.price)
        print 'Item_name: {}'.format(self.item_name)
        print 'Weight: {} lbs'.format(self.weight)
        print 'Brand: {}'.format(self.brand)
        print 'status: {}'.format(self.status)
        return self
       

x = Product(1500, 'computer', '2', 'Apple')
y = Product(7, 'Bannanas', '2', 'Dole')
z = Product(749, 'iphone', '.67', 'Apple')
x.add_tax(.08).display_info().sell().display_info().return_item('opened box')
print '*'*50
y.add_tax(.093).display_info().sell().display_info().return_item('new in box')
print '*'*50
z.add_tax(.093).display_info().sell().display_info().return_item('defective')
