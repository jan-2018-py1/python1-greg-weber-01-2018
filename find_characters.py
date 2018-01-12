# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.


#test cases
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
char2 = "m"
char3 = "n"
subStr1 = "ll"   #works for multi-character substrings, not just single characters 




def characterChecker(my_list, subString):
    new_list= []
    #loop through elements in list and compare with subString value to see if it's in each element
    for element in my_list:
        if subString in element:   
            new_list.append(element)   #if it is then append the element to the new list
    print new_list


characterChecker(word_list, char)
characterChecker(word_list, char2)
characterChecker(word_list, char3)
characterChecker(word_list, subStr1)




        
