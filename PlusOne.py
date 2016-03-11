class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length=len(digits)
        for i in range(length-1,-1,-1):
            if digits[i]+1>9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        digits.insert(0,1)
        return digits
        
        