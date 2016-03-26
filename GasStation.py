class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if gas==None or len(gas)==0:
            return 0
        for i in xrange(0,len(gas)):
            gas[i]=gas[i]-cost[i];
        sum=0
        left,index=0,0
        for i in xrange(0,len(gas)):
            sum+=gas[i]
            left+=gas[i]
            if sum<0:
                sum=0
                index=i+1
        return index if left>=0 else -1