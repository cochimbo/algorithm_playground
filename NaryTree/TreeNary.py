from TreeNode import TreeNode


class TreeNary:
    def __init__(self):
        self.firstNode = TreeNode(None)

    def insertWord(self, word):
        self.firstNode.insertNode(word)

    def deleteWord(self, word):
        print("delete " + word)

    def searchNode(self, word):
        return self.firstNode.searchChildNode(word)

    def depth(self):
        return 0
