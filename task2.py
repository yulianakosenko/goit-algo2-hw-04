from trie import Trie


class Homework(Trie):
    """
    Розширення базового класу Trie.
    """

    def count_words_with_suffix(self, pattern) -> int:
        """
        Повертає кількість слів,
        що закінчуються заданим суфіксом.
        """

        if not isinstance(pattern, str):
            raise TypeError(
                f"Illegal argument: pattern = {pattern} must be a string"
            )

        count = 0

        for word in self.keys():
            if word.endswith(pattern):
                count += 1

        return count

    def has_prefix(self, prefix) -> bool:
        """
        Перевіряє,
        чи існує хоча б одне слово
        із заданим префіксом.
        """

        if not isinstance(prefix, str):
            raise TypeError(
                f"Illegal argument: prefix = {prefix} must be a string"
            )

        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True


if __name__ == "__main__":

    trie = Homework()

    words = [
        "apple",
        "application",
        "banana",
        "cat"
    ]

    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів,
    # що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1
    assert trie.count_words_with_suffix("ion") == 1
    assert trie.count_words_with_suffix("a") == 1
    assert trie.count_words_with_suffix("at") == 1

    # Перевірка наявності префікса
    assert trie.has_prefix("app") is True
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True
    assert trie.has_prefix("ca") is True

    print("=" * 50)
    print("Усі тести успішно пройдено!")
    print("=" * 50)