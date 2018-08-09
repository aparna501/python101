#list
animal=['cat','dog','rabbit']
animal.append('pig')
print('updated animal list:',animal)
'''
input $ output:Updated animal list:  ['cat', 'dog', 'rabbit', 'pig']'''

#Vowel list
vowel=['a','e','i','u']
vowel.insert(3,'o')
print('updated list:',vowel)
'''
input $ output:Updated List:  ['a', 'e', 'i', 'o', 'u']'''

# empty range

print(list(range(0)))

print(list(range(10)))

 
print(list(range(1, 10)))
'''
output:
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]'''

#Enumerate
grocery = ['bread', 'milk', 'butter']


for item in enumerate(grocery):
 
	print(item)

print('\n')

for count, item in enumerate(grocery):
 
	print(count, item)

print('\n')

for count, item in enumerate(grocery, 100):
 
	print(count, item)

'''
output:(0, 'bread')
(1, 'milk')
(2, 'butter')

0 bread
1 milk
2 butter

100 bread
101 milk
102 butter'''

#range()
x = range(6)
for n in x:
  print(n)
'''output:
0
1
2
3
4
5'''

#ex:2
x = range(3, 6)
for n in x:
  print(n)
'''output:
3
4
5'''

#ex:3
x = range(3, 20, 2)
for n in x:
  print(n)
'''output:
3
5
7
9
11
13
15
17
19'''

#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
'''output:
apple'''

#ex:2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
'''output:
apple
banana'''

#ex:3
for x in range(2, 6):
  print(x)
'''output:
2
3
4
5'''

#ex:4
for x in range(2, 30, 3):
  print(x)
'''output:
2
5
8
11
14
17
20
23
26
29'''
