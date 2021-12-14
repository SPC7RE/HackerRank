#!/usr/bin/env python3

'''
Finds a substring with bigest count of vowels, 
with custom length k, from a string.
'''

# from file
# with open('test.txt', 'r') as f:
# 	s = f.read()

def subString(s, k):
	# Write your code here
	vowels = {'a', 'e', 'i', 'o','u'}
	gen = (s[i:i+k] for i in range(0, len(s)))

	longest = ''
	current = 0
	for i in gen:
		counter = sum([i.count(x) for x in vowels])
		if current < counter:
			 current = counter
			 longest = i

	if len(longest) <= 1:
		return 'Not found!'
	else:
		return longest

if __name__ == '__main__':
  s = 'ssssssdkkkkkkksssssaaammmmmmmmeeooouuunnnnnnnniiiaaaooouuueee'
  k = 16
  print(subString(s, k))
