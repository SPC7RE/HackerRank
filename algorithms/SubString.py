#!/usr/bin/env python3

'''
Finds a substring with bigest count of vowels, 
with custom length k, from a string.
Currently max lenght size that can handle is k = 175 
'''

# from file
# with open('test.txt', 'r') as f:
# 	s = f.read()

def subString(s, k):
	# Write your code here
	vowels = {'a', 'e', 'i', 'o','u'}
	gen = (s[i:i+k] for i in range(0, len(s)))

	chunks = []
	for i in gen:
		chunks.append(i) 

	# print(chunks)	

	countVowels = []
	for i in range(len(chunks)):
			countVowels.append(sum([chunks[i].count(x) for x in vowels]))

	index = countVowels.index(max(countVowels))

	if max(countVowels) <= 1:
			return 'Not found!'
	else:
			return chunks[index]

if __name__ == '__main__':
  s = 'ssssssdkkkkkkksssssaaammmmmmmmeeooouuunnnnnnnniiiaaaooouuueee'
  k = 16
  print(subString(s, k))
