import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        primes=[True]*n
        for i in range(2,int(math.sqrt(n))+1):
            if primes[i]==False:
                continue
            for j in range(i*i,n,i):
                primes[j]=False
        for i in range(2,n):
            if primes[i]:
                count+=1
        return count
        