import string

class Trie:

    def __init__(self):
        self.count = 0
        self.root = TrieNode()

    def insert(self, key):
        key = key.lower()
        self.count += 1
        pCrawl = self.root
        for char in key:
            ind = string.lowercase.index(char)
            if (pCrawl.children[ind] is None):
                pCrawl.children[ind] = TrieNode()
            pCrawl = pCrawl.children[ind]
        pCrawl.value = self.count
    

    def search(self, key):
        key = key.lower()
        pCrawl = self.root
        for char in key:
            ind = string.lowercase.index(char)
            if (pCrawl.children[ind] is None):
                return None
            pCrawl = pCrawl.children[ind]
        return pCrawl

    def __contains__(self, key):
        if (self.search(key)):
            return True
        else:
            return False

    


class TrieNode:

    def __init__(self):
        self.value = 0
        self.children = [None]*len(string.lowercase)


t = Trie()
t.insert("karl")
t.insert("butts")
print "kar" in t
print "but" in t
