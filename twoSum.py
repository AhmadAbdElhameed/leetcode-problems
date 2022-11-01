class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## previous values
        dict = {}
        for i,number in enumerate (nums):
            if (target - number) in dict:
                return ([dict[target - number],i])
            else:
                dict[number] = i 