# given some values test for type.  
# 1.if value is an intiger greater than or equal to 100 print 'that's a big number'
# else print 'that's a small number
# 2. If string is greater than or equal to 50 characters print 'Long scentence' else print 'Short scentence"
# 3. If list has grater than or equal to 10 values print "Big list" - else print "short list"


#set some vars for test cases:

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

this_dict = {'name': 'Greg'}


#function that passes in a value to be checked for type and length 
def typeChecker(value):
    if isinstance(value, int) and value >= 100:  #check if intiger and size >= 100
        print "That's a big number"
    elif isinstance(value, int):  #intiger type check, we know it true it is also less than 100
        print "That's a small number"
    elif isinstance(value, str) and len(value) >= 50: #check if string and character length >= 50
       print "Long scentence"
    elif isinstance(value,str):  #check if string we know length less than 50 if it is a string at this point
        print 'Short scentence'
    elif isinstance(value, list) and len(value) >= 10: #check type for list and length for less than or = to 10
        print 'Big list'
    elif isinstance(value,list):  #check for list type, we know if true it is shorter than 10
        print 'Short list'  
    else:                           #if we haven't determined type by this point in our function let us know
        print "Can't determine type"



#call our function to check the variables for type and length and then print apropriate response
typeChecker(sI)
typeChecker(mI)
typeChecker(bI)
typeChecker(eI)
typeChecker(spI)
typeChecker(sS)
typeChecker(mS)
typeChecker(bS)
typeChecker(eS)
typeChecker(aL)
typeChecker(mL)
typeChecker(lL)
typeChecker(eL)
typeChecker(spL)

#throw in a dict to see what happens
typeChecker(this_dict)

