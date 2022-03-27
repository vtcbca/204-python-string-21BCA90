'''Write a script to enter any sentence and print those word which is palindrom. Also print total number of palindrom word.
 Name : Laxman Sirvi.
 Date : 12-03-22'''
a=input("Enter any string : ")
l=list(a.split ())
c=0
l1=[]
for i in l:
    b=i[::-1]
    if i==b:
        l1.append(i)
        print (i)
        c=c+1
print("Total {} palindrom word in string : {}".format(c,l1))
