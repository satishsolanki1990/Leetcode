'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Another logic: insert app -> {'a':{'p':{'p':{},flag=T},flage:F},flag:F}
'''


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.end_flag = False
        self.children = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ch = word[0]  # a
        if ch not in self.start:
            self.start[ch] = Node(ch)  # {'a':node(a,F,{})}
        next_level = self.start  ## {'a':node(a,F,{})}
        i = 0
        while i < len(word) - 1:
            next_level = next_level[ch].children  # {}
            ch = word[i + 1]  # e
            if ch not in next_level:
                next_level[ch] = Node(ch)  # {'e':{}}
            i += 1
        next_level[ch].end_flag = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ch = word[0]  # a
        if ch not in self.start:
            return False
        next_level = self.start
        i = 0
        while i < len(word) - 1:
            next_level = next_level[ch].children  # {'a':node(a,F,{})}
            ch = word[i + 1]  # p
            if ch not in next_level:
                return False  # 'a':{'p':node(p,F,{})}
            i += 1
        return next_level[ch].end_flag

    # apple startWith ap -> True
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ch = prefix[0]  # a
        if ch not in self.start:
            return False
        next_level = self.start
        i = 0
        while i < len(prefix) - 1:
            next_level = next_level[ch].children  # {'a':node(a,F,{})}
            ch = prefix[i + 1]  # p
            if ch not in next_level:
                return False  # 'a':{'p':node(p,F,{})}
            i += 1
        return i == len(prefix) - 1


