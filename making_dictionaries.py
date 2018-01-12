#create a function that takes two lists of equal length and creates a single dictionary form them.
#the first list comtains the keys and the second list contains the values.


#the lists
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def dicterizor(list_1, list_2):
    #zip() makes the two lists into a list of tupels and then the dict() turns that into a dictionary
    newDict = dict(zip(list_1, list_2)) 
    return newDict

print dicterizor(name, favorite_animal)
