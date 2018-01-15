#find and replace: in the string words find the firts instance of the word 'day'. Then create a new instance of the string where the word 'day' is replaced bu 'month'.

words = "It's Thanksgiving day. It's my birthday, too!"
print words.find('day')  #prints 18 
print words.replace('day','month') ##prints "It's Thanksgiving month. It's my birthmonth too!"


#min and max:print the min and max values in a list

x = [2,54,-2,7,12,98]
print 'the min value is:', min(x)  #prints -2
print 'the max value is:', max(x)  #prints 98


#first and last - print first and last values in a list. 
#Then create a new list containing only the first and last values from the first list.

y = ['hello',2,54,-2,7,12,98,'world']
first = y[0]
last = y[len(y)-1]
print 'the first value is:', first, 'and the last value is:' ,last
z = [] #initalize a new list
z.append(first)
z.append(last)
print z

#new list - given a list of intigers, sort then split in half. Place the first half in position 0 of a new list created by the second half. So you would have something like : [[1,2,3],4,5,6]

my_list = [19,2,54,-2,7,12,98,32,10,-3,6]
my_list.sort()
print my_list #prints sorted list
listFirstHalf = my_list[:len(my_list)/2] #places values from first part of list into a new list
listSecondHalf = my_list[len(my_list)/2:] #places values from second half of list in new list
# print listFirstHalf
# print listSecondHalf
listSecondHalf = [listFirstHalf] + listSecondHalf
print listSecondHalf

#here is an alternate method for appending to the 0 index of a list -  listSecondHalf.insert(0,listFirstHalf)
#using the .insert() method and pass the index the index want to insert at, followed by the variable of what 
#you want to insert - I read on stack overflow that this is 5 times faster than the way I did it above, but the 
#assignment said to only use the method we had learned on the previous tabs in the platform material.


