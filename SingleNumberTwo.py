class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counters=[0]*32
        result=0
        neg=0
        for i in range(0,32):
            for x in nums:
                if x<0:
                    neg+=1
                    x=~(x-1)
                if (x>>i)&1==1:
                    counters[i]+=1
            result|=(counters[i]%3)<<i
        if neg%3>0:
            result=-result
        return result
        