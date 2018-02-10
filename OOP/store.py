
class Store(object):
    def __init__(self, name, owner_name):
        self.name = name
        self.owner_name = owner_name
        self.products = []


    def add(self, info):  
        #info should be a dict containing product name, discript, quantity
        self.products.append(info)
        return self

    def remove(self, product_name):
        for idx, product in enumerate (self.products):
            if product['name'] == product_name:
                x = idx 
                print 'all sold out of', product['name']
                print '='*40
        self.products.pop(x)
        return self

    def inventory(self):
        print 'inventory at', self.name 
        for items in self.products:
           print items
        print '='*40
        return self


x = Store("Jay's Hardware", 'JayJay')

x.add({'name': 'drywall screws', 'descript': 'for drywall', 'quantity': 2000}).add({'name': 'decking screws', 'descript': ' for decking', 'quantity': 100})
x.add({'name': 'paint', 'descript': 'forexterior painting', 'quantity': 25}).add({'name': 'hammer', 'descript': ' for hamering', 'quantity': 55})
x.add({'name': 'ladder', 'descript': 'for getting to hard to reach places', 'quantity': 13}).add({'name': 'tape', 'descript': ' blue painters tape', 'quantity': 199})
x.inventory()

x.remove('hammer').remove('tape')

x.inventory()  #no hammer or tape in inventory now
