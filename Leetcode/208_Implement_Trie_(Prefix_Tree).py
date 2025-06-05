import pytest

class TrieNode():
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

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

def test_case_1():
    trie = Trie()
    commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    values = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    
    response = []
    for command, value in zip(commands, values):
        if command == "Trie":
            trie = Trie()
            response.append(None)
        elif command == "insert":
            trie.insert(value[0])
            response.append(None)
        elif command == "search":
            response.append(trie.search(value[0]))
        elif command == "startsWith":
            response.append(trie.startsWith(value[0]))
            
    expected = [None, None, True, False, True, None, True]
    assert response == expected
    
if __name__ == '__main__':
    pytest.main()