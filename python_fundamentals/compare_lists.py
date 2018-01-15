# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:


#test cases
a = [1,2,False,6,2]
b = [1,2,False,6,2]

x = [1,2,5,6,2]
y = [1,2,5,6,5,3]

l = [1,2,5,6,5,16]
m = [1,2,5,6,5]

a1 = ['this', 'is', 'a', 'list', 'of', 'strings', True]
b1 = ['this', 'is', 'a', 'list', 'of', 'strings', True]

x1 = ['celery','carrots','bread','milk']
y1 = ['celery','carrots','bread','cream']



def list_comparer(list_1, list_2):
    if list_1 == list_2:
        print 'The lists are the same'
    else:
        print 'The lists are not the same'


list_comparer(a,b)
list_comparer(x,y)
list_comparer(l,m)
list_comparer(a1,b1)
list_comparer(x1,y1)
