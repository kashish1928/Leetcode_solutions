class Solution:
    def letterCombinations(self, digits: str) -> List[str]: 
        if not digits:
            return []

        mapping = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }

        if(len(digits) == 1):
            return mapping[digits]
        
        res = []

        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            
            for letter in mapping[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
        
        backtrack("", digits)

        return res

        