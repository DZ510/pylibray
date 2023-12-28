class KMPMatch():
    def __init__(self,matchstr:str):
        self.matchstr = matchstr
        self.next = list()
    
    def setmatchstr(self,matchstr:str):
        self.matchstr = matchstr

    
    def get_public_prestufix(prefixset,stufixset):
        pass


    def buildnextarray(self):
        for index in range(1,len(self.matchstr)):
            if self.matchstr[index] == "?":
                self.next.append(-1)
            temp_str = self.matchstr[:index]
            prefixsset = self.__getall_prefix_strs(temp_str)
            suffixsset = self.__getall_suffix_strs(temp_str)
            equal_fixstr = prefixsset & suffixsset
            max_equal_presuffix = sorted(equal_fixstr,key=lambda x:len(x),reverse= False)
            if len(max_equal_presuffix) == 0:
                #print("not find public presuffix",end="\r")
                self.next.append(0)
            else:
                #print(max_equal_presuffix[0])
                self.next.append(len(max_equal_presuffix[0]))
            
        pass

    def match(self,orgstr:str):
        #kmp match algorithm
        match_index = 0
        for index in range(0,len(orgstr),1):
            while True:
                if match_index > len(self.matchstr):
                    match_index = 0
                if match_index == len(self.matchstr):
                    return True,index-match_index

                if orgstr[index] == self.matchstr[match_index]:
                    match_index+=1
                    break
                else:
                    if match_index == 0:
                        break
                    match_index=match_index-(match_index-self.next[match_index-1])
            pass
        return False,-1

    def __getall_prefix_strs(self,deststr):
        temp_prefix = set()
        for index in range(0,len(deststr)-1,1):
            tmpstr = deststr[:index+1]
            temp_prefix.add(tmpstr)
        return temp_prefix
    
    def __getall_suffix_strs(self,deststr):
        temp_suffix = set()
        for index in range(len(deststr)-1,0,-1):
            tmpstr = deststr[index:]
            temp_suffix.add(tmpstr)
        return temp_suffix
