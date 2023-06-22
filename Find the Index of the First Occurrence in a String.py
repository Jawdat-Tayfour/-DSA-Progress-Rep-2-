# My solution ^_^
def FTIOTFOIAS(s:str,n:str)-> int:
    if not n :
        return 0 
    if len(n)>len(s):
        return -1
     
    spointer,npointer  = 0,0
    ind = []
    while spointer<len(s) and npointer<len(n):
        if s[spointer] == n[npointer]:
            spointer+=1
            npointer+=1

        else:
            spointer+=1    
            npointer=0
    if npointer == len(n):
        return spointer-npointer
    else:
        return -1 
#O(n) Time Complexity Babyyyyyyyyyyyyyyyyyyyyyyyyyyy, without actually seening the explaination as well. ^__^


#Neet Code Solution

def FTIOTFOIAS2(haystack:str,needle:str):
    if needle == "":
        return 0 
    for i in range (len(haystack)+1-len(needle)):
        for j in range (len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j==len(needle)-1:
                return i  
    return -1 
# O(n*m) Time complexity. due to the nested for loops. anyways he says that there's another solution so let's dive into it. 

#Neet Code Solution 2
def FTIOTFOIAS3(haystack:str,needle:str):
    if needle == "":
        return 0
    for i in range(len(haystack)+1-len(needle))    
        if haystack[i:i+len(needle)] == needle:
            return i     
        return -1 
   
# O(n) Time Complexity 




print(FTIOTFOIAS("jwdat","at"))           
