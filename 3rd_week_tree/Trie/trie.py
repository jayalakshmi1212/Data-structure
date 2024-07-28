class TrieNode:
    def __init__(self):
        self.children={}
        self.endword=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word:str):
        current=self.root

        for c in word:
            if c not in current.children:
                current.children[c]=TrieNode()
            current=current.children[c]
        current.endword=True

    def search(self,word:str):
        current=self.root

        for c in word:
            if c not in current.children:
                return False
            current=current.children[c]
        return current.endword
    
    def start_with(self,prefix:str):
        current=self.root

        for c in prefix:
            if c not in current.children:
                return False
            current=current.children[c]
        return True
  
trie=Trie()
trie.insert("kanyakumari")
trie.insert("karnataka")
trie.insert("indonesia")
trie.insert("india")
words_to_check = ["karnataka", "india", "indonesian", "kanya", "kanyakumari"]
results = {word: trie.search(word) for word in words_to_check}
print(results)
print(trie.start_with("ka"))