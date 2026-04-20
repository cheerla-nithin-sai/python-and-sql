# Last updated: 4/20/2026, 1:27:46 PM
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        word_map = dict()

        for ch in words[0]:
            word_map[ch] = 1 if ch not in word_map else word_map[ch] + 1
            
        for idx in range(1, n):
            temp_map = dict()

            for ch in words[idx]:
               temp_map[ch] = 1 if ch not in temp_map else temp_map[ch] + 1
            
            for key, val in word_map.items():
                if key in temp_map:
                    word_map[key] = min(temp_map[key], val)
                else:
                    word_map[key] = 0

        
        ans = []

        for key, val in word_map.items():
            for idx in range(val):
                ans.append(key)
        
        return ans