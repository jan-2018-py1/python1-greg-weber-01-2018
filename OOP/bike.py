
# create a Bike class with a fmax speed, price and a miles ridden attribute, then create some methods to display info, 
# ride forward and reverse the distance ridden. Use the self argument in the methods parameters so that the methods can be chained


class Bike(object):
    def __init__(self, price, max_speed):
        self.max_speed = max_speed
        self.price = price
        self.miles = 0

    def display_info(self):
        print "Max Speed:", self.max_speed
        print "Price ${}".format(self.price)
        print "Total forward progress:", self.miles, 'miles'
        return self


    def ride(self):
        miles_ridden = self.miles = self.miles + 10
        print "Riding"
        print 'Total Mileage:', miles_ridden
        return self

    def reverse(self):
        if self.miles <= 5:
            print "you're not allowed to have negative mileage - try riding forward!!"
            return self
        miles_ridden = self.miles = self.miles - 5
        print "Reversing"
        print 'Total Mileage:', miles_ridden
        return self

# instances of Bike class
gregs_bike = Bike(4500, '40mph')
bobbys_bike = Bike(2750, '33mph')
kristins_bike = Bike(900, '11mph')

# chaining methods of bike class to instances
print "Greg's Bike:"
gregs_bike.ride().ride().ride().reverse().display_info()
print '*'*50
print "Bobby's Bike:"
bobbys_bike.ride().ride().reverse().reverse().display_info()
print '*'*50
print "Kristin's Bike:" 
kristins_bike.reverse().reverse().reverse().display_info()






    