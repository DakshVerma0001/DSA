class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        left = 0
        right = 0
        n = len(nums)

        while right < n-1: #we have to stop when right reaches the last element, so to continue till the second last we used this
            farthest = 0
            for i in range (left, right+1): #we used right + 1 to also consider the last element of the array
                farthest = max(farthest, i + nums[i])
            left = right + 1 #new left will be the immediate next index of right so right + 1
            right = farthest #farthest will become the new right
            jump += 1 #jump = jump + 1
            
        return jump
        