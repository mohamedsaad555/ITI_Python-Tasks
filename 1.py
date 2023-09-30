#1
x=['a','e','i','o','u']
print("---Q1----")
print(x.count,x)
###
String = input('Enter the string :')
count = 0
#to check for less conditions
#keep string in lowercase
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        #if True
        count+=1
#check if any vowel found
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))
#2
print("---Q2----")
y=[1,3,5,4,2]
y.sort()
print(y)
y.reverse()
print(y)
#######
print("Input five integers:")
nums = list(map(int, input().split()))
nums.sort()
print(nums)
nums.reverse()
print("After sorting the said integers:")
print(*nums)

#3
print("---Q3----")
name=["iti","iti","iti"]
print(name.count("iti"))
#4
print("---Q4----")
string="hello"
def rem_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)
    string = "hello"
rem_vowel(string)
# string = "hello"
# rem_vowel(string)
#z="hello"
#z1=z.replace("e","")
#z2=z.replace("o","")
#print(z1+z2)
#5
print("---Q5----")
loc="internet"
letter='i'
print(loc.rfind(letter))
#6
print("---Q6----")
Num1 = int(input("Enter the number you want to generate a multiplication table for, then hit the `enter` key: "))
ourRange = range(1,4)
for x in ourRange:
    result = Num1 * x
    print(Num1," * ",x," = ",result)
Num2 = int(input("Enter the number you want to generate a multiplication table for, then hit the `enter` key: "))
ourRange = range(1,4)
for x in ourRange:
    result = Num2 * x
    print(Num2," * ",x," = ",result)  
    l1=[3]
    l2=[[1],[2,4],[3,6,9]]
    l1.append(l2)
    print(l1) 
#another solution    
    x=int((input("enter number")))
    res=[]
    for i in range(1,x+1):
        f=[i*j for j in range(1,i+1)]
        res.append(f)
        print(f)

    #7
print("---Q7----")
# take input
row = int(input("Enter the number of rows: "))
# display the pattern
for i in range(1, row + 1):
    # print space
    for j in range(1, row - i + 1):
        print(" ", end = "")
    # print *
    for j in range(1, i + 1):
        print("*", end = "")
        
    # new line
    print("")









