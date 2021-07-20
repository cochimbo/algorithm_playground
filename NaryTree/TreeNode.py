"""
Class for static definitions
"""
class Definitions:
    CONST_N_LETTERS_TILDE = 5
    CONST_N_LETTERS_ENYE = 1
    CONST_N_LETTERS_SPECIAL = 3
    CONST_N_LETTERS_CAST = 26 + CONST_N_LETTERS_TILDE + \
        CONST_N_LETTERS_ENYE + CONST_N_LETTERS_SPECIAL
    SPECIAL_LETTER = {'ñ': 26, 'á': 27, 'é': 28, 'í': 29,
                      'ó': 30, 'ú': 31, ' ': 32, '-': 33, 'ü': 34}
    SPECIAL_LETTER_TUPLE = tuple(SPECIAL_LETTER)
    ASCII_LOWCASE_OFFSET = 97
    ZERO = 0
"""
Class defining all the nary tree for spanish words Node attributes and methods
"""
class TreeNode:

    def __init__(self, parent, letter=None):
        self.parent = parent
        self.letter = letter
        self.children = [None] * Definitions.CONST_N_LETTERS_CAST
        self.children = [None for _ in range(Definitions.CONST_N_LETTERS_CAST)]
        self.wordleaf = False
    
    def indexLetter(self, letter):
        index = -1
        if(letter not in Definitions.SPECIAL_LETTER_TUPLE):
            index = ord(letter) - Definitions.ASCII_LOWCASE_OFFSET
        else:
            index = Definitions.SPECIAL_LETTER[letter]
        return index
    """
    Insert a node in the tree if it does not exist, if it exist position the pointer to the existing
    """
    def insertNode(self, word):
        if(len(word) > 0):
            letter = word[0]
            word = word[1:]
            index = self.indexLetter(letter)
            nextNode = self.children[index]
            if (nextNode == None):
                self.children[index] = TreeNode(self, letter)
                self.children[index].insertNode(word)
            else:
                nextNode.insertNode(word)
        else:
            self.wordleaf = True
    """
    Returns the terminal node corresponding to a certain word, exception if not found
    """
    def searchChildNode(self, word):
        returnvalue = self
        lengthW = len(word)
        if(lengthW > Definitions.ZERO):
            letter = word[0]
            word = word[1:]
            index = self.indexLetter(letter)
            node = self.children[index]
            if(node != None):
                returnvalue =  node.searchChildNode(word)
            elif (lengthW > 1):
                raise Exception("Cadena de entrada no existente")
        return returnvalue
    """
    Returns all the leafs hanging from a heading string
    """
    def getAllLeafs(self, inArray, word):
        if(self.isTerminalLeaf()):
            inArray.append(word)
        else:
            if(self.wordleaf):
                inArray.append(word)
            for i in range(Definitions.CONST_N_LETTERS_CAST):
                if(self.children[i] != None):
                    self.children[i].getAllLeafs(inArray, word + self.children[i].letter)
    """
    Returns if a node is a leaf (considering leaf a Node with no children)
    """
    def isTerminalLeaf(self):
        isLeaf = True
        for i in range(Definitions.CONST_N_LETTERS_CAST):
            if(self.children[i] != None):
                isLeaf = False
                break
        return isLeaf