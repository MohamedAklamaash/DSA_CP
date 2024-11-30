class Solution:
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        ans=[]
        for a,b in zip(pos,neg):
            ans.append(a)
            ans.append(b)
        return ans                
        
