class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        visited = set()
        adj_matrix = {}

        def find_words_with_char_difference(word):
            possible_words = []
            for w in wordList:
                dif = 0
                for i in range(len(w)):
                    if dif > 1:
                        break
                    if w[i] != word[i]:
                        dif += 1
                if dif == 1:
                    possible_words.append(w)
            return possible_words

        # create adj_matrix
        for word in wordList:
            adj_matrix[word] = find_words_with_char_difference(word)

        adj_matrix[beginWord] = find_words_with_char_difference(beginWord)

        def dfs(word, path: set):
            if word == endWord:
                return 1

            shortest_path_length = 6000
            path.add(word)

            for child in adj_matrix[word]:
                if child in path:
                    continue
                shortest_path_length = min(
                    shortest_path_length, dfs(child, path))
            path.remove(word)
            return shortest_path_length + 1

        res = dfs(beginWord, set())
        if res >= 6000:
            return 0
        return res


beginWord = "hit"
endWord = "cog"
wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb",
            "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]

print(Solution().ladderLength(beginWord, endWord, wordList))
