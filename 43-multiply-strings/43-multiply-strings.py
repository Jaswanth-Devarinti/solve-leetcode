class Solution:
    
    def convert_to_int(self,s):
        return ord(s)-ord('0')
    
    def add_two_strings(self,s1,s2):
        min_length = min(len(s1),len(s2))
        ans_str = ''
        carry = 0
        for i,j in zip(s1[::-1][:min_length],s2[::-1][:min_length]):
            val = self.convert_to_int(i)+self.convert_to_int(j)+carry
            carry = val//10
            ans_str = str(val%10)+ans_str
        
        long_str = s1 if len(s2)==min_length else s2
        
        for i in long_str[:-min_length][::-1]:
            val = self.convert_to_int(i)+carry
            carry = val//10
            ans_str = str(val%10)+ans_str
        
        if carry!=0:
            ans_str = str(carry)+ans_str
            
        print(s1,s2,ans_str)
        
        return ans_str
    
    def multiply_with_single_digit(self,s1,num):
        ans_str = ''
        carry = 0
        for i in s1[::-1]:
            val = self.convert_to_int(i)*self.convert_to_int(num)+carry
            carry = val//10
            ans_str = str(val%10)+ans_str
            
        if carry!=0:
            ans_str = str(carry)+ans_str
        
        return ans_str
    
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1=='0' or num2=='0':
            return '0'
        
        total_sum = self.multiply_with_single_digit(num1,num2[-1])

        
        for ind,i in enumerate(num2[:-1][::-1]):
            initial_sum = self.multiply_with_single_digit(num1,i)
            total_sum = self.add_two_strings(total_sum,initial_sum+'0'*(ind+1))
        
        return total_sum
            
            
            