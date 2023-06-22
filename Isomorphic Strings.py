# My Solution ^_^
def Isomorphic(n:str,m:str)->bool:
    if len(n) != len(m):
        return False 
    str = {}
    str2 = {}
    for i in range(len(n)):
        str[n[i]] = m[i]
        str2[m[i]]= n[i]
    loc = ''
    loc2=''
    for k in range(len(n)):
        loc+=str[n[k]]
        loc2+=str2[m[k]]
    if loc == m and loc2 == n :
        return True 
    return False     
#Time complexity is O(2N) where N is the length of the words. yay ^_^


def Isomorphic2(n:str,m:str)->bool:
    mapSt,mapTs={},{}
    for i in range(len(n)):
        c1,c2 = n[i],m[i]
        if (c1 in mapSt and mapSt[c1]!=c2)or (c2 in mapTs and mapTs[c2]!=c1):
            return False 
        mapSt[c1] = c2
        mapTs[c2] = c1
    return True 
# Time complexity is O(2N) where N is the length of the words.

"""On the other hand, the Isomorphic2 function uses a more efficient approach. 
It iterates through the strings once, performing constant-time operations for each character. 
The time complexity of the Isomorphic2 function is O(N), where N is the length of the input strings n and m.
 Therefore, Isomorphic2 is better than Isomorphic in terms of time complexity."""
# - ChatGPT , 2023 

print(Isomorphic("add","bar"))