#1
# print("---Q1----")
# while True:
#     try:
#         num=input("enter number ")
#         num=int(num)
#         print(num)
#         break
#     except ValueError  as e: 
#         print("Not valid integer : ")

#2
# print("---Q2----")    
# while True:
#     try:
#         f=open("C:\\Users\\dell\\Desktop\\testt.txt",'r')
#         f.read()
#         print(f)
#         break
#     except FileNotFoundError  as e: 
#         print("file does not exist : ")
#         break

#3
# print("---Q3----") 
# f=open("E:\\ITI\\Python\\lab03.txt",'r') 
# list=f.readlines()
# print(list)
# print(len(list))

#4
# print("---Q4----") 
# while True:
#     l=input("Enter Number")
#     try:
#         ll=int(l)
#         if l==l[::-1]:
#             print("plaindrome")
#             break
#         else:
#             print("not")    
#     except Exception as e:    
#         print("Try again")

#5
# print("---Q5----") 
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10,11,12]
# l3=[]
# for i in range(len(l1)):
#     if l1[i]%2 !=0 :
#         l3.append(l1[i])
# for i in range(len(l2)):
#     if l2[i]%2 ==0 :
#         l3.append(l2[i])
# print(l3)  

#6
print("---Q6----")
def exponent(base,exp):
    r=base**exp
    return r
print(exponent(5,3))