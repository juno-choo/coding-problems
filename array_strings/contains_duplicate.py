def findDuplicate(nums: list[int]) -> int:
	slow, fast = 0, 0
	while True:
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast:
			break   
	slow2 = 0
	while True:
		slow = nums[slow]
		slow2 = nums[slow2]
		if slow == slow2:
			return slow
		
nums = [2,3,1,3]
nums2 = [1,1]
nums3 = [1,2,3,4,2]
print(findDuplicate(nums))
print(findDuplicate(nums2))
print(findDuplicate(nums3))
