class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []

        def get_all_partitions(no_partitions, word) -> list[list[str]]:
            res = []
            if len(word) <= no_partitions:
                []
            if no_partitions == 0:
                return [[word]]

            for index in range(1, len(word)):
                prefix = word[0:index]
                postfixes = get_all_partitions(no_partitions-1, word[index:])
                if len(postfixes):
                    for p in postfixes:
                        res.append([prefix] + p)
            return res

        def is_palindrome(word):
            return word == word[::-1]

        for i in range(len(s)):
            parts = get_all_partitions(i, s)
            for part in parts:
                for item in part:
                    if not is_palindrome(item):
                        break
                else:
                    result.append(part)

        return result


print(Solution().partition('b'))
