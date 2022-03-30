from multiprocessing.pool import ThreadPool
from TreeNode import TreeNode

################################################################################
# @brief : Base class to build a tree with N Nodes per leaf 
# and reference all the nodes functions
################################################################################


class TreeNary:
    ############################################################################
    # @brief : Constructor of the class
    # @param : None
    # @return : None
    ############################################################################
    def __init__(self):
        self.firstNode = TreeNode(None)
    ############################################################################
    # @brief : Insert a new word into the tree
    # @param : word : word to insert
    # @return : None
    ############################################################################

    def insertWord(self, word):
        self.firstNode.insertNode(word)
    ############################################################################
    # @brief : Deletes a word from the tree
    # @param : word : word to delete
    # @return : None
    ############################################################################
    
    def deleteWord(self, word):
        # TODO : implement function
        raise Exception("Not implemented yet")
    
    ################################################################################
    # @brief : Returns all the leafs hanging from a heading string
    # @param : word : heading string
    # @return : None
    ################################################################################
    def searchNode(self, word):
        return self.firstNode.searchChildNode(word)
    
    ################################################################################
    # @brief : TODO
    # @param : None
    # @return : None
    ################################################################################
    def depth(self):
        #TODO : implement function
        raise Exception("Not implemented yet")
