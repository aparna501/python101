#Largest number using nested-if-else
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if (a>b) and (a >c):
	print("The largest number is",a)
	if (b >c) and (c> a):
   		 print("The largest number is",b)
else:
    print("The largest number is c",c)
'''
input:Enter the value of a:10
      Enter the value of b:100
      Enter the value of c:1000
output:The largest number is 1000'''