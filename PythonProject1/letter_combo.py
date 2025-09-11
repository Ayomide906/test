class Solution:
    def __init__(self, digits):
        self.digits = digits
        self.num_dict = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
    def letter_combinations(self):
        if not self.digits:
            return []
        result = []
        def backtrack(index, path):
            if index == len(self.digits):
                result.append(path)
                return
            for char in self.num_dict[self.digits[index]]:
                backtrack(index + 1, path + char)
        backtrack(0, "")
        return result

# Example use
tf = Solution("23")
print(tf.letter_combinations())
