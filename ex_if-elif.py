#sysmodule using if-else:
import sys
pgm_name=sys.argv[0]
print(pgm_name)
num=int(sys.argv[1])
if num>0:
	print("the number is  positive")
elif num<0:
	print("the number is negative")
else:
	print(" equal to 0")

'''
input:python ex_if-elif.py 4
output:
ex_if-elif.py
the number is  positive'''