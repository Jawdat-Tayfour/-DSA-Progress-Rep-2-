# My Solution ^_^ so easy tbh.
"""def LOLW(n:str)->int:
    counter = 0
    for i in reversed(range(len(n)-1)):
        if n[i] == " ":
            continue
        else:
            counter+=1
            if n[i-1] == " ":
                return counter
                
    return 0 
# Time Complexity o(n) we may iterate through the whole list                 
                """
#Neet Code Solution 
def LOLW(n:str):
    i , length = len(n)-1 , 0
    while n[i] ==" ":
        i-=1
    while i>=0 and n[i] != " ":
        length+=1
        i-=1
    return length        
# Same Time Complexity O(n) but chatGPT says the his code is better treating the edge case where the string has leading spaces. Anyways have a good day Ya'll ^_^.
print(LOLW("My name is Banana    "))