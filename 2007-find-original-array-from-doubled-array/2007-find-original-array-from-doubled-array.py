class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        if len(changed)%2!=0:
            return []
        
        changed.sort()
        
        count_dict = {}
        for i in changed:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        
        for i in count_dict:
            if count_dict[i]==0 or i==0:
                continue
            
            if i*2 in count_dict and count_dict[i*2]>=count_dict[i]:
                ans += [i]*count_dict[i]
                count_dict[2*i] -= count_dict[i]
                count_dict[i] = 0
                
            
            else:
                return []
        
        if 0 in count_dict:
            if count_dict[0]%2==0:
                ans += [0]*(count_dict[0]//2)

            else:
                return  []
        
        return ans