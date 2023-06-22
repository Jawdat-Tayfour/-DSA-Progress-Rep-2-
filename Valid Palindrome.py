# My solution ^_^
def validPal(n:str):
    My_Pal = ''
    for i in n :
        if i.isalnum():
            My_Pal+=i
    r = len(My_Pal)-1      
    l=0
    My_Gal = My_Pal.lower()
    while l!=r:
        if My_Gal[l] != My_Gal[r]:
            return False
        l+=1
        r-=1
        
    return True 

# Time Complexity is O(N + M), where N is the length of the input string n and M is the length of the resulting My_Pal string.^_^
#My Solution 2 : 

def validPal2(n:str):
    My_pal = ''
    My_gal = ''
    for i in n :
        if i.isalnum():
            My_gal+=i
    My_gal = My_gal.lower()
    for i in range(len(My_gal)-1,-1,-1):
        My_pal+=My_gal[i]
    if My_gal == My_pal:
        return True     

# Time Complexity is O(N + M), where N is the length of the input string n and M is the length of the resulting My_Pal string.^_^
# but validPal 2 is less effecient because it uses an unneccessary for creating My_Pal.

#Neet Code Solution
def validPal3(n:str):
    newstr = ''
    for c in n :
        if c.isalnum():
            newstr+=c.lower()
    return newstr == newstr[::-1]   
#Voila he made it in 5 lines, like wtf lmao. it's also O(N + M) but more efficient due to the way he compared strings.
# 
# Neet Code Solution 2 :
def validPal4(n:str):
    l, r = 0, len(n) - 1
    while l < r:
        while l < r and not alphanum(n[l]):
            l += 1
        while r > l and not alphanum(n[r]):
            r -= 1    
        if n[l].lower() != n[r].lower():
            return False 
        l, r = l + 1, r - 1
    return True     

def alphanum(c):
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
#This one is O(n). ^_^ good luck fella programmer ! . 


print(validPal4("A man a plan a canal : panama"))

