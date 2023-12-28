from queue import Queue

class TrieNode:
    def __init__(self):
        self.faild = None
        self.parent = None
        self.isend = False
        self.val = None
        self.childs = dict()
        pass




class AhoMulitMatch:
    def __init__(self,mulit_matchstrs:list):
        self.mulit_match = mulit_matchstrs.copy()
        self.trie_tree = TrieNode()
        pass

    def build_acmod(self):
        #构建trie树 以及构建失配指针
        for string in self.mulit_match:
            curnode = self.trie_tree
            for ch in string:
                if ch not in curnode.childs.keys():
                    tempnode = TrieNode()
                    tempnode.val = ch
                    tempnode.parent = curnode
                    curnode.childs[ch]=tempnode
                    curnode = tempnode
                else:
                    curnode = curnode.childs[ch]
            curnode.isend = True
        #构建失配指针      
        temp = Queue()
        temp.put(self.trie_tree)
        while not temp.empty():
            curnode = temp.get()
            if curnode.parent is None:
                curnode.faild = curnode
                for key,node in curnode.childs.items():
                    temp.put(node)
            elif curnode.parent == self.trie_tree:
                for key,node in curnode.childs.items():
                    temp.put(node)
                curnode.faild = self.trie_tree
            else:
                for key,node in curnode.childs.items():
                    temp.put(node)
                parent_faild_node = curnode.parent.faild
                while True:
                    if parent_faild_node == self.trie_tree:
                        curnode.faild = self.trie_tree
                        break
                    elif curnode.val in parent_faild_node.childs.keys():
                        curnode.faild = parent_faild_node[curnode.val]
                        break
                    else:
                        parent_faild_node = parent_faild_node.faild

        pass

    def getcurnode_to_rootnode_str(self,node:TrieNode):
        string_str = ""
        curnode = node
        while True:
            if curnode == self.trie_tree:
                break
            string_str += curnode.val
            curnode = curnode.parent
        return string_str[::-1]


    def search_orgstring(self,orgstrings):
        #传入待匹配全文  返回匹配到的位置index
        #{
        #   "AABBCCDD":[20081,28952],
        #   "AABBCEEF":[2032,2048]
        #}
        resulttab = dict()
        curnode = self.trie_tree
        stringleng = len(orgstrings)
        index = 0
        while True:
            if index >= stringleng:
                break
            ch = orgstrings[index]
            if ch not in curnode.childs.keys():
                if curnode.isend:
                    matchstr = self.getcurnode_to_rootnode_str(curnode)
                    offset = index - len(matchstr) - 1
                    if matchstr not in resulttab.keys():
                        resulttab[matchstr] = set()
                    resulttab[matchstr].add(offset) 
                    #实际上已经失配了 所以当前节点需要指向faild节点
                    curnode = curnode.faild
                    pass
                elif curnode.faild.isend:
                    matchstr = self.getcurnode_to_rootnode_str(curnode)
                    offset = index - len(matchstr) - 1
                    if matchstr not in resulttab.keys():
                        resulttab[matchstr] = set()
                    resulttab[matchstr].add(offset) 
                    #实际上已经失配了 所以当前节点需要指向faild节点
                    curnode = curnode.faild
                    pass
                else:
                    if curnode == self.trie_tree:
                        index+=1
                    else:
                        curnode = curnode.faild
            else:
                curnode = curnode.childs[ch]
                index+=1

        return resulttab

    def showtree():
        pass


    def insert_str():
        pass

    def delete_str():
        pass

    
if __name__ == "__main__":
    ACobj = AhoMulitMatch(["ABCDEF","ABCDFE"])
    ACobj.build_acmod()
    print(ACobj.search_orgstring("SWDAFDAABCDEFCSAWABCDFEDSDWAWAWAWS"))