from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = dict(Counter(words))
        ans = 0
        
        word_dict = {k: v for k, v in reversed(sorted(word_dict.items(), key=lambda item: item[1]))}
        print(word_dict)
        
        repeat = 0
        for word in word_dict:
            if word[0]==word[1]:
                if repeat == 0:
                    ans += word_dict[word]*2
                    if word_dict[word]%2!=0:
                        repeat = 1
                else:
                    ans += (word_dict[word]//2)*4
                    word_dict[word] = 0
            else:
                if word[::-1] in word_dict:
                    min_val = min(word_dict[word],word_dict[word[::-1]])
                    
                    word_dict[word]-=min_val
                    word_dict[word[::-1]] -= min_val
                    ans += min_val*4
        
        return ans