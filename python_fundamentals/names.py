# given the list --
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#create a program that outputs -- 
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel


def dictReader(info):
    for values in info:
       print values['first_name'], values['last_name']

dictReader(students)



#given the following dict:

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# create a program that prints :
# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

def doubleDictReader(some_info):
    idNum = 1 #initialize variable
    for key in some_info:
        print key 
        for value in some_info[key]:
            print idNum, '-', value['first_name'], value['last_name'], '-', (len(value['first_name'])+len(value['last_name']))
            idNum += 1
        idNum = 1 #reset for next dectionary 
        
           
print  #empty line on purpose to more easily see the output from the two different functions

doubleDictReader(users)
