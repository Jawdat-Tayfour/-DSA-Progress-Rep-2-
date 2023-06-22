#my solution ^_^ it didn't work 
"""def MCCS(l:list[int])-> int : 
    right = len(l)-1
    left = len(l)-2
    while left>=0:
        l[right]= l[right]
        l[left] = l[left] if left +2 == len(l) else l[left]+l[right]
        min_cost = min(l[left],l[right])
        left-=1
        right-=1
        print(l)
    return min_cost 
    # didn't work I'll leave it here just so you can laugh at it.^_^
    """
#Neet Code Solution:

def MCCS (l:list[int])-> int:
    l.append(0)
    for i in range(len(l)-3,-1,-1):
        l[i] += min(l[i+1],l[i+2])
        print(l[0],l[1])
    return min(l[0],l[1])    
# O(n) Time Complexity we are only iterating over the length of the list and adding(constant time operation).
print(MCCS([10,15,20]))    