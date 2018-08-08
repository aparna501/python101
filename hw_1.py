#Square root

num=4
num_sqrt=num**(1.0/2)
print(num_sqrt)
'''
input:num=4
out:the square root of 4 is 2.0'''

#Area of triangle

a = float(input('Enter the first side: '))
b = float(input('Enter the second side: '))
c = float(input('Enter the third side: '))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(1.0/2)
print(f'The area of the triangle is {area}')

'''
input:Enter the first side:7
      Enter the second side:8
      Enter the third side:9
output:The area of the triangle is 26.832815729997478'''

#Quadratic Equation
import cmath
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
d=(b**2)-(4*a*c)
sqrt_d=d**(.5)
s1=(-b-sqrt_d)/(2*a)
s2=(-b+sqrt_d)/(2*a)
print('The solution of :',s1,s2)

'''
output:The solution are (-0.5-0.3872983346207417j) and (-0.5+0.3872983346207417j)
'''

# print

print("." * 10)
'''output:..........'''
