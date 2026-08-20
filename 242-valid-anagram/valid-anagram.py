class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {} #dictionary

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1 #if the ch come once freq = 1, in case it repeats, it will be freq += 1
        
        for ch in t:
            if ch not in freq:
                return False
            else:
                if freq[ch] == 0: #in case the char is there in t, and the frequency of that char in s is zero: not anagram
                    return False
                else:
                    freq[ch] -= 1 #if the chat in t also exist in dict i.e. "s" , freq of that char will be freq - 1.
        return True