from pprint import pformat


class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return f"({self.data})"


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        if self.root.data is None:
            return str(self.root.data)
        return pformat({"%s" % self.root.data}, indent=1)

    def insert(self, word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word

    def startWith(self, prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if not node:
                return False
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert("cook")
    t.insert("cake")
    print(t)
