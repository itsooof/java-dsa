# 34. Find First and Last Position of Element in Sorted Array

'''Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity. '''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=bisect_left(nums,target)
        if l==len(nums) or nums[l]!=target:
            return -1, -1
        r= bisect_right(nums,target)-1
        return l, r