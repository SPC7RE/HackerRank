
#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/apple-and-orange/problem


def countApplesAndOranges(s, t, a, b, apples, oranges):
	# Write your code here
	
	sam_left_fence = s 
	sam_right_fence = t
	
	apple_tree = a
	orange_tree = b
	
	all_ground_apples = [i + apple_tree for i in apples] 
	all_ground_oranges = [i + orange_tree for i in oranges] 
	
	apples_inbound = 0
	for i in all_ground_apples:
		if sam_left_fence <= i and sam_right_fence >= i:
			apples_inbound += 1
	
	oranges_inbound = 0
	for j in all_ground_oranges:
		if sam_left_fence <= j and j <= sam_right_fence:
			oranges_inbound += 1
	
	print(apples_inbound)
	print(oranges_inbound)

  
if __name__ == '__main__':
  
  countApplesAndOranges(7,11, 5, 15, [-2, 2, 1], [5, -6])
