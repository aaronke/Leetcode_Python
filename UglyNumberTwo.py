class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        index=[0]*3
        primes=[2,3,5]
        ugly=[0]*n
        ugly[0]=1
        for i in xrange(1,n):
            ugly[i]=2**31-1
            for j in xrange(0,3):
                ugly[i]=min(ugly[i],primes[j]*ugly[index[j]])
            for j in xrange(0,3):
                if primes[j]*ugly[index[j]]==ugly[i]:
                    index[j]+=1
        return ugly[n-1]