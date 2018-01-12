#write a function that takes in a dict and outputs a list of tuples wher the first item of each tuple is a key and 
#the second item is the value

#test case
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function  should output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]


def tupleizer(info):
    print info.items()


tupleizer(my_dict)

