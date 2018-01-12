# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'



def listTypeChecker(a_list):
    #set a few variables
    newString = ""  #new empty string that we will add strings in list to if there are any.
    stringType = False  #we will change this to true if we find a string in our list.
    Sum = 0    #initialize the sum of the intigers to 0 because we don't know yet if there are any ints in the list.  
    #loop through list, check type, and do something based on type
    for element in a_list:
        if isinstance(element, str):
            newString += element + " "  #add string elemts to a new string if there are any
            stringType = True #set to true since there are strings in the list
        elif isinstance(element, int):
            Sum += element  #add up all the intigers if there are any
        elif isinstance(element, float):
            Sum += element  #add any floats to the sum of numbers
        else:
            continue  #we haven't set our function to deal with any data types besides ints, floats and strings, so if incountered we will simply skip over for now.

    #now depending on info gathered above we will print a response to the data type contained in the list
    if Sum > 0 and stringType == False:
        print 'The list in question only contained numbers. Their sum is:', Sum
    elif Sum == 0 and stringType == True:
        print "This list in question only contained strings. Their content is:", newString
    else:
            print 'The list is of mixed type of values.' 
            print 'The numbers in the list sum to:', Sum
            print "The string content is:", newString




listTypeChecker([-25, 'all', 'about', 30.5, 'that', 15, 'bass', 100])
listTypeChecker([1.25,2,3,4,5, -15, 20, 0, -5.07])
listTypeChecker(['hello','world,','this', 'is', 'a', 'string.'])