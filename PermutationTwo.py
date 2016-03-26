class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        visited=[False]*len(nums)
        nums.sort()
        self.dfs(nums,res,[],visited)
        return res
        
    def dfs(self,nums,res,temp,visited):
        if len(temp)==len(nums):
            res.append(temp)
        for i in xrange(0,len(nums)):
            if visited[i]==False:
                if i>0 and nums[i]==nums[i-1] and visited[i-1]==False:
                    continue
                visited[i]=True
                self.dfs(nums,res,temp+[nums[i]],visited)
                visited[i]=False
        