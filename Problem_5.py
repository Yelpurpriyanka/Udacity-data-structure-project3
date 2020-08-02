# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False
        
    def insert(self, char):
    
        if char not in self.children:
            self.children[char] = TrieNode()
            
    def suffixes(self, suffix = ''):
    
        res = []
        for key in self.children:
            if self.children[key].word_end:
                res.append(suffix+key)
            res += self.children[key].suffixes(suffix+key)
        return res
        
class Trie:
    def __init__(self):
    
        self.root = TrieNode()

    def insert(self, word):
    
        current_node = self.root
        for c in word:
            current_node.insert(c)
            current_node = current_node.children[c]
        current_node.word_end = True
                

    def find(self, prefix):
        
        current_node = self.root
        for c in prefix:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return None
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



prefixNode = MyTrie.find("")
print(prefixNode.suffixes())
print('----------------------')

prefixNode = MyTrie.find("an")
print(prefixNode.suffixes())
print('----------------------')


prefixNode = MyTrie.find("ant")
print(prefixNode.suffixes())
print('----------------------')


prefixNode = MyTrie.find("f")
print(prefixNode.suffixes())
print('----------------------')

prefixNode = MyTrie.find("tripod")
print(prefixNode.suffixes())
