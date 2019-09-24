#function double takes a list as an argument and returns the list with odd numbers only
def double(numbers):
    #for the length of the list passed in iterate
    for i in range (len(numbers)):
        #if even number add one to make it odd
        if (numbers[i] % 2 == 0):
            numbers[i] += 1
    #return updated list to function call
    return numbers


print "This program will never finish with an even number in a list!"
#case 1 - straight into function
print "Original list = [1, 2, 3, 4, 5]"
print "End list = " + str(double([1,2,3,4,5]))
#case 2 - into function from varible
evenList = [2,4,6,8,10]
print "Original list = " + str(evenList)
print "End list = " + str(double(evenList))
#case 3 - stored in variable from function
finalCase = double([24,16,8,7,10])
print "Original list = [24, 16, 8, 7, 10]"
print "End list = " + str(finalCase)

