import pytest


class WordDictNode():
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.wdNode = WordDictNode()
        
    def addWord(self, word: str) -> None:
        curr_node = self.wdNode
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = WordDictNode(c)
            curr_node = curr_node.children[c]
        curr_node.is_end = True
        
    def search(self, word: str, curr_node=None) -> bool:
        if curr_node is None:
            curr_node = self.wdNode

        if not word:
            return curr_node.is_end
        
        c = word[0]
        if c == ".":
            for child in curr_node.children.values():
                if self.search(word[1:], child):
                    return True
            return False
        else:
            if c in curr_node.children:
                return self.search(word[1:], curr_node.children[c])
            else:
                return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

def test_case_1():
    wd = WordDictionary()
    commands = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    values = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

    response = []
    for command, value in zip(commands, values):
        if command == "WordDictionary":
            wd = WordDictionary()
            response.append(None)
        elif command == "addWord":
            wd.addWord(value[0])
            response.append(None)
        elif command == "search":
            response.append(wd.search(value[0], wd.wdNode))

    expected = [None, None, None, None, False, True, True, True]
    assert response == expected


if __name__ == '__main__':
    pytest.main()