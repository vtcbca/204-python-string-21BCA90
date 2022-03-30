'''write a script to create a list with 5 string and count total number of string with even number of length with string using UDF
Name : Laxman Sirvi
Date : 30-03-22'''
x=[]
a=0
for i in range (5):
    s=input('Enter any string : ')
    x.append(s)
print(x)
for i in x:
    if len(i)%2==0:
        a=a+1
print('\nTotal sring of even number of character is ',a,'\n')
for i in x:
    if len(i)%2==0:
        print(i)
