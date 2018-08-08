#Milestone_Project_1
class Milestone_1:
	def __init__(self,w,h,n,str,sent_1,sent_2):
		self.w=w
		self.h=h
		self.n=n
		self.str=str
		self.sent_1=sent_1
		self.sent_2=sent_2		         
        # Reverse string
	def reverse(self):
		rev=self.str[::-1]
		print("the reverse of the string is:",rev)
        #Palindrome or not
	def palindrome(self):
		rev=self.str[::-1]
		if self.str==rev:
			print("the string is palindrome")
		else:
			print("the string is not palindrome") 
	#BMI Calculator
	def bmi_calculator(self):
		h=self.h
		w=self.w
		print(self.w/self.h**2)
	#Factorial
	def factorial(self):
		factorial=1
		if self.n<0:
			print("factorial number doesnot exists")
		elif self.n==0:
			print("the factorial of 0 is 1")
		else:
			for i in range(factorial,self.n+1):
				factorial=factorial*i
		print("factorial number of",self.n,"is:",factorial)
	#Vowels
	def vowel(self):
		vowel=['a','e','i','o','u','A','E','I','O','U']
		count=0
		for i in self.str:
			if i in vowel:
				count+=1
		print("no.of vowels:",count)
	#Punctuations
	def punctuations(self):
		punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		no_punctuations=""
		for i in self.sent_1:
			if i not in punctuations:
				no_punctuations=no_punctuations+i
		print(no_punctuations)
	# Print * Triangle
	def pattern(self):
		for i in range(0,self.n):
			for j in range(0,i+1):
				print("*",end="")
			print("\n")
	#Sorting ann Splitting
	def sort(self):
		word=self.sent_2
		sent_2=word.split()
		print(sent_2)
		sent_2.sort()
		print(sent_2)
		
obj_milestone1=Milestone_1(45,5.3,7,'madam',"hel@#$%lo w<>~!orld","welcome to world of python")
obj_milestone1.reverse()
obj_milestone1.palindrome()
obj_milestone1.bmi_calculator()
obj_milestone1.factorial()
obj_milestone1.vowel()
obj_milestone1.punctuations()
obj_milestone1.pattern()
obj_milestone1.sort()
		