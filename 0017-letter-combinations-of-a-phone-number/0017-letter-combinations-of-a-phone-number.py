from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: empty input returns an empty list (not [""])
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = [""]
        for digit in digits :
            result_new = []
            letter = mapping[digit]
            for combo in letter :
                for i in result :
                    result_new.append(i+combo)
            result = result_new      
        return result          