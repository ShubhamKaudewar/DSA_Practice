class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.trieNode = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.trieNode

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode(c)
            curr_node = curr_node.children[c]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        curr_node = self.trieNode
        for c in word:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        return curr_node.is_end

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.trieNode
        for c in prefix:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        return True