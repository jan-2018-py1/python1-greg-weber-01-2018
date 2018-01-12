#Create a function called draw_stars() that takes a list of numbers and prints out *'s. If the list element is a string treat it as: Grab the first letter of string - make lower case - print it the number of times of the string length.


def starPrinter(list):
    for element in list:
        if isinstance(element, str):
            print element[0].lower() * len(element)  #takes first letter of a string, turns it lowercase and prints it the string length number of times.
        elif isinstance(element, int):
            print '\033[1;31m *\033[1;m' * element  #red formating with '*' - and * is used as a multiplier after the ''
        else:
            continue #if element is a type that we havn't dealt with yet

starPrinter([1,2,3])
starPrinter([4,5,'Hello',6,'World'])
starPrinter([6,5,'Biggest and longest yet',4,3,2,11,'eleven'])


