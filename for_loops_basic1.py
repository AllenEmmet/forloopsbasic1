#print integers 0-50
for integers in range(51):
    print(integers)
#print multiples of five 5-1000
for num in range(5,1001,5):
    print(num)
#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for integer in range(1,101):
    if(integer%10==0):
        print('Coding Dojo')
    elif(integer%5==0):
        print('Coding')
    else:
        print(integer)
#Add odd integers from 0 to 500,000, and print the final sum.
oddnum = []
for integer in range(0,500000):
    if(integer%2!=0):
        oddnum.append(integer)
totalsum = 0
for num in range(0,len(oddnum)):
    totalsum += oddnum[num]
print(totalsum)
#Print positive numbers starting at 2018, counting down by fours.
for num in range(2018, 0, -4):
    print(num)

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lownum = 10
highnum=50
mult = 3 
for num in range(lownum, highnum+1):
    if num%mult == 0:
        print(num)