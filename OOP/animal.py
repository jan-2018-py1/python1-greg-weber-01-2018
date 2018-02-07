class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "{}'s health is {}".format(self.name, self.health)
        return self
        


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def display_health(self):
        print 'I am a dragon named the mighty {}'.format(self.name)
        return self
    def fly(self):
        self.health -= 10
        return self
    


x = Dog('Tanner')
print x.walk().walk().walk().display_health().run().run().pet().display_health()

y = Dragon('Puff')
print y.fly().run().fly().display_health().health