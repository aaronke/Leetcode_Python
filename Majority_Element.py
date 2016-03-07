def majorityElement(self,nums):
	dict = {}
    for n in nums:
        dict[n] = dict.get(n,0) +1
        if dict[n] > len(nums)/2:
            return n