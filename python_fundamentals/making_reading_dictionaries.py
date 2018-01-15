
#create a dictionary about myself-

my_info = {
    'name': 'Greg Weber',
    'age': 43,
    'home town': 'Portland, Or',
    'hobby': 'guitars'
}

#create a function that takes in dictionary data and then prints out the keys and values from the dict
def dict_reader_printer(stuff):
    for key, value in stuff.iteritems():
        print 'My', key, 'is', value


#call function
dict_reader_printer(my_info)
