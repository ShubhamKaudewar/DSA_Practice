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

    def remove(self, word: str) -> bool:
        def _remove(node, word, depth):
            if depth == len(word):
                if not node.is_end:
                    return False  # Word not found
                node.is_end = False
                # If node has no children, it can be deleted
                return len(node.children) == 0
            c = word[depth]
            if c not in node.children:
                return False  # Word not found
            can_delete = _remove(node.children[c], word, depth + 1)
            if can_delete:
                del node.children[c]
                return not node.is_end and len(node.children) == 0
            return False

        return _remove(self.trieNode, word, 0)