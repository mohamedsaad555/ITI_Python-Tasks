#1
print("---Q1----")
result1=input("please enter a number ")
x=open("C:\\Users\\dell\\Desktop\\test.txt",'w')
x.write('{}'.format(result1))
x=result1
result=input("please enter a number ")
y=open("C:\\Users\\dell\\Desktop\\test-.txt",'w')
y.write('{}'.format(result))
y=result
def q1(length,start):
    z=[]
    for i in range(length):
          z.append(start)
          start+=1
    return z
print(q1(int(x),int(y)))

#2
print("---Q2----")
name=input("please enter a name ")
n=open("C:\\Users\\dell\\Desktop\\test2.txt",'w')
n.write('{}'.format(name))
#Email=input("Enter email and hit enter ")
print("type of text ", type(name))
#print("type of text ", type(Email))
import re
 
# Define a function for
# for validating an Email
def check(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat,s):
        print("valid")
    else:
        print("Invalid Email")
 
# Driver Code
if __name__ == '__main__':
 
    # Enter the email
    email = "ankitrai326@gmail.com"
 
    # calling run function
    check(email)

    email=input("please enter an email ")
    n1=open("C:\\Users\\dell\\Desktop\\test2_mail.txt",'w')
    n1.write('{}'.format(name))
 
 #   email =input(" enter email ") 
    check(email)
 


#3
print("---Q3----")
f3=open("C:\\Users\\dell\\Desktop\\test3.txt","r")
count=0
total=0
avg=0
f3.seek(0)

for line in f3:
    line=line.strip()
    if line=="done" :
        print("total",total)
        print("count",count)
        print("avg",avg)
        break

    elif line.isnumeric():
        num=int(line)
        total=total+num
        count=count+1
        if count !=0:
            avg=total/count
               

