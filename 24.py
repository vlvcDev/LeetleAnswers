# Minimum Rotated Sorted Array
# Write a function solve that finds the minimum element in a rotated sorted array. 

# Time: 1:42

def solve(nums):
  smallest = nums[0]
  for num in nums:
    if num < smallest:
      smallest = num
  return smallest

# This is an O[n] answer that just iterates throughout the whole list and finds the smallest number by comparing it to the smallest number found so far.
# I presume that a quicker answer would involve a binary search, where you can find the smallest number in O[log n] time.

def solve(nums):
  left = 0
  right = len(nums) - 1
  mid = 0
  while left < right:
    mid = left + (right - left) // 2
    if nums[mid] > nums[right]:
      left = mid + 1
    else:
      right = mid
  return nums[left]