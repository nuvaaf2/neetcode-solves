class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def backtrack(i, path):

            if i == len(digits):
                res.append(path)
                return

            current_digit = digits[i]
            for letter in phone[current_digit]:
                backtrack(i + 1, path + letter)

        backtrack(0, "")
        return res
        