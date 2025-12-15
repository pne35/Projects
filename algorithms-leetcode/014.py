class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        current_word = ""
        found = False
        letter = ""
        res = min(len(ele) for ele in strs)
        for count in range(res):
            found = False
            letter = ""
            for x in range(len(strs)):
                if found != True:
                    found = True
                    letter += strs[x][count]
                elif(strs[x][count] != letter):
                    letter = ""
                    break  
            if letter != "":
                current_word += letter
            else:
                break
        return current_word
        
