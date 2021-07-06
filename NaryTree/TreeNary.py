from TreeNode import TreeNode

"""
Base class to start building and reference all the nodes functions
"""
class TreeNary:
    def __init__(self):
        self.firstNode = TreeNode(None)

    def insertWord(self, word):
        self.firstNode.insertNode(word)
    """
    TODO
    """
    def deleteWord(self, word):
        print("delete " + word)

    def searchNode(self, word):
        return self.firstNode.searchChildNode(word)

    def depth(self):
        return 0
