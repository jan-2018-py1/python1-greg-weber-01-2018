# a function to print out all integers from 1 - 2000 with some identifying text as to weather the number is even or odd.abs

def odd_even():
    for number in range(1,2001):
        if number % 2 == 1:
            print 'The number is {}. This is an odd number.'.format(number)
        else:
            print 'The number is {}. This is an even number.'.format(number)

odd_even()



#function that itirates through a list of numbers and returns a list where every value has been multiplied by a given input value

#test lists
x = [1,2,3,4,5]
y = [-2,-5,0,5,11]

def multiply(num_list, n):
    for i in range(0,len(num_list)):
       num_list[i] = num_list[i] * n
    return num_list


print multiply(x,5)
print multiply(y,-2.5)


#Hacker Challenge: Function that takes multiply function as argument. Returning the multiplied list as a two diminsional
#  list. Each internal list should contain 1's times the number in the original list. So taking in ([1,2,3],3) should return
# [[1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1]]

def layered_multiples(arr):
    new_arr = []
    for i in range (0, len(arr)):
        #create new sublist
        new_arr.append([])  
        #variable to hold current number in arr
        num = arr[i]
        #append 1's to sublist (num/num will always equal to 1)
        while num > 0:
            new_arr[i].append(num/num)
            num -= 1
    return new_arr

x = layered_multiples(multiply([2,4,5],3))
print x