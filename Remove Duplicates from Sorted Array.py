"""#my solution ^_^ idk what to type for return type soooo I'll leave it empty here 
def removeduplicates(l:list[int]):
    if not l :
        return None
    p1 = 0
    p2  = 1 
    while p2 <= len(l)-1:
        if l[p1] ==l[p2]:
            l.pop(p2)
        else:
            p1+=1
            p2+=1
    return len(l),l 
#Time complexity O(n**2)
"""
#Neet Code Solution (improved a bit by me)
def removeDuplicates(l:list[int]):
    if not l :
        return None
    left = 1 
    for r in range (1,len(l)):
        if l[r] != l[r-1]:
            l[left] = l[r]
            left+=1 
    return left,l         
#Time Complexity O(n)
print(removeDuplicates([0,1,1,2,3,3]))        