import pytest
from typing import List
from helper.Trie import TrieNode, Trie

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()

        # Insert each folder broken into parts
        for f in folder:
            # Remove initial "/" and split, e.g. "/a/b" -> ["a", "b"]
            parts = f.strip("/").split("/")
            trie.insert(parts)

        output = []

        # DFS and collect only top-level folders
        def dfs(node, path):
            if node.is_end:
                output.append(path)
                return  # Do not go deeper

            for child in node.children.values():
                new_path = path + "/" + child.val if path else "/" + child.val
                dfs(child, new_path)

        dfs(trie.trieNode, "")
        return output


def test_case_1():
    sol = Solution()
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    expected = ["/a","/c/d","/c/f"]
    actual = sol.removeSubfolders(folder)
    assert actual == expected

def test_case_2():
    sol = Solution()
    folder = ["/a","/a/b/c","/a/b/d"]
    expected = ["/a"]
    actual = sol.removeSubfolders(folder)
    assert actual == expected

def test_case_3():
    sol = Solution()
    folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    expected = ["/a/b/c","/a/b/ca","/a/b/d"]
    actual = sol.removeSubfolders(folder)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()