
class Car(object):
    def __init__(self, price, speed, fuel_level, fuel_economy):
        self.price = price
        self.speed = speed
        self.fuel_level = fuel_level
        self.fuel_economy = fuel_economy 
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    
    def display_all(self):
        print 'Price: ${}'.format(self.price)
        print 'Speed:', self.speed
        print 'Fuel level:', self.fuel_level
        print 'Fuel economy: {}mpg'.format(self.fuel_economy)
        print 'Tax:', self.tax
        print '*' * 50


my_car = Car(15000, '120mph', 'Running on empty', 30)
bobbys_car = Car(4900, '85mph', 'Full', 27)
kristins_car = Car(27000, '92mph', 'Half', 39)
moms_car = Car(50000, '85mph', 'Electric: Full charge', 60)
heidis_car = Car(24000, '110mph', 'Running on empty', 19)
michaels_car = Car(9000, '65mph', 'Quarter Tank Full', 32)


