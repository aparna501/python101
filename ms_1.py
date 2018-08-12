# sorting and spliting

'''
input:welcome to the world of python
output:of
       python
       the
       to
       welcome
       world'''

def sort(string):  
    print("this is a sorting function") 
    word.sort()
    for i in word:
        print(i)
string=("welcome to the world of python")
word=string.split() 
sort(string)

# BMI CALCULATOR

'''
input:enter your weight 45
      enter your height 5.3
output:45.0'''


weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
print(weight/height*height)

# REVERSE A STRING

'''
input: enter a string aparna
output: the reverse of the string is:anrapa'''

str=input("enter a string:")
rev=str[::-1]
print("the reverse of the string is:",rev)

# Print # in Triangle

'''
input:5
output:*
       ** 
       ***
       ****
       *****'''

def pattern(num):
    for i in range(0,num):
        for j in range(0,i+1):
            print(" *",end="")
        print("\n")

num=5
pattern(num)

# Factorial of a number

'''
output:
the factorial of 7 is:5040'''

def factorial(n):
    factorial = 1
    if n<0:
       print("factorial number doesnot exits")
    elif n==0:
       print("the factorial of 0 is 1")
    else:
       for i in range(factorial,n+1):
           factorial = factorial * i
    print("the factorial number of",n,"is:",factorial)
n = 7
factorial(n)

# Palindrome or not

'''
input:enter a string:madam
output:the string is palindrome'''

str=input("enter a string:")
rev=str[::-1]
if str==rev:
	   print("the string is palindrome")
else :
	print("the string is not palindrome")

# Vowels

'''
output:No.of vowels:4'''
def vowel(str):
    str="I LovE My moM"

    vowel=['a','e','i','o','u' or 'A','E','I','O','U']
    count=0
    for i in str:
        if i in vowel:
           count+=1
    print("No. of vowels:",count)
vowel(str)


#Puncuations

'''
output:WELCOME tO WORLD OF PYtHON'''
def punct(str):
    punct= '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
    no_punct=""
    for i in str:
        if i not in punct:
           no_punct=no_punct+i
    print(no_punct)
str=("WEL$%^COME t@O WOR*!LD OF PYt^HON")
punct(str)

