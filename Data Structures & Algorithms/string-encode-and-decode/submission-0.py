class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for w in strs:
            result += str(len(w)) + "#" + w
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#",i)
            length = int(s[i:j])
            i = j + 1
            word = s[i: i + length]
            result.append(word)
            i = i + length
        return result

        


   

