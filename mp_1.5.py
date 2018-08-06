import sys
word=input("enter a vowel")
def vowels(word):
	vowel=['a','e','i','o','u','A','E','I','O','U']
	count=0
	for letter in word:
		if letter in word:
			count=count+1
			print(count)
			return