# #print all odd numbers from 1 to 1000 using a for loop

for num in range(1001): #for loop to run through the intigers from 1 to 1000
    if num % 2 == 1:  #conditional using the modulus opperator to check if the remainder is 1 == true
        print num



# #print all multipules of 5 from 5 to 1,000,000

for int in range (5, 1000001): #use range upto 1,000,001 to include 1,000,000 in the output
    if int % 5 == 0: #checks to see if current intiger is a multiple of 5
        print int



# #print the sum of all values in the list 

a = [1,2,5,10,255,3]
sum = 0
for i in range(0, len(a)):  #for loop to run through the indexs of the list
    sum += a[i]   #adds up the values in the list
    print 'incrementally the sum is:', sum
print 'the sum of the values in list a is:', sum


#print the average values in the list

b = [1,2,5,10,255,3]
sum = 0
for num in b: #this is a more shorthand way of writing the loop -- for num in range(0, len(b))
    sum += num
avg = sum / (len(b))  #computes the average by divinding the sum by the number of items in the list

print 'the sum of the values in list b is:', sum
print 'the length of list b is:', len(b)
print 'therefore the average of the values in list b (rounded since there are no float values) is:', avg
