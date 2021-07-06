class Definitions:
    CONST_N_LETTERS_TILDE = 5
    CONST_N_LETTERS_ENYE = 1
    CONST_N_LETTERS_SPECIAL = 3
    CONST_N_LETTERS_CAST = 26 + CONST_N_LETTERS_TILDE + \
        CONST_N_LETTERS_ENYE + CONST_N_LETTERS_SPECIAL
    SPECIAL_LETTER = {'ñ': 26, 'á': 27, 'é': 28, 'í': 29,
                      'ó': 30, 'ú': 31, ' ': 32, '-': 33, 'ü': 34}


class TreeNode:

    def __init__(self, parent, letter=None):
        self.parent = parent
        self.letter = letter
        self.children = [None] * Definitions.CONST_N_LETTERS_CAST
        self.leaf = False

    def indexLetter(self, letter):
        index = -1
        if(letter not in tuple(Definitions.SPECIAL_LETTER)):
            index = ord(letter) - 97
        else:
            index = Definitions.SPECIAL_LETTER[letter]
        return index

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
            self.leaf = True

    def searchChildNode(self, word):
        returnvalue = self
        lengthW = len(word)
        if(lengthW > 0):
            letter = word[0]
            word = word[1:]
            index = self.indexLetter(letter)
            node = self.children[index]
            if(node != None):
                returnvalue =  node.searchChildNode(word)
            elif (lengthW > 1):
                raise Exception("Cadena de entrada no existente")
        return returnvalue

    def getAllLeafs(self, inArray, word):
        if(self.isLeaf()):
            inArray.append(word)
        else:
            if(self.leaf):
                inArray.append(word)
            for i in range(Definitions.CONST_N_LETTERS_CAST):
                if(self.children[i] != None):
                    self.children[i].getAllLeafs(inArray, word + self.children[i].letter)
        
    def isLeaf(self):
        isLeaf = True
        for i in range(Definitions.CONST_N_LETTERS_CAST):
            if(self.children[i] != None):
                isLeaf = False
                break
        return isLeaf