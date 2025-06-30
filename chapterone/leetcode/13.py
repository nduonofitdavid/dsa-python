class Solution:
    def romanToInt(self, s: str) -> int:
        table: dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        used: dict = {}
            
        specials = {('I', 'V'), ('I', 'X'), ('X', 'L'), ('X', 'C'), ('C', 'D'), ('C', 'M')}

        total: int = 0
        for i in range(len(s)):
            if ((len(s) - 1) - i) != 0:
                chr_i = s[i]
                n_chr = s[i + 1]
                if i in used:
                    continue
                if (chr_i, n_chr) in specials:
                    total += table[n_chr] - table[chr_i]
                    used[i + 1] = i + 1
                else:
                    total += table[chr_i]
            else:
                total += table[s[i]] if i not in used else 0
        return total



