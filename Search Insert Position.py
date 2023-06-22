"""#my solution
def SIP(l: list[int],n:int):
    for i in range(len(l)):
        if l[i] == n :
            return i 
    for i in range(len(l)-1):
        if l[i] < n and l[i+1]>n:
            return i+1
    if l[-1]<n:
        return len(l)
    return None 
"""
#time complexity O(n)
#my solution 2 
"""def SIP(l:list[int],n:int):
    first = 0 
    last = len(l)-1
    
    while first<=last:
        mid = (first + last )//2
        if l[mid] == n :
            return mid 
        elif l[mid]>n:
            last = mid -1 
        elif l[mid]<n :
            first = mid+1
    first = 0 
    last = len(l)-1
    while first<=last:
        mid = (first + last )//2
        if l[mid] < n and (mid == len(l) - 1 or l[mid + 1] > n):
            return mid+1 
        if l[mid]>n:
            last = mid -1 
        elif l[mid]<n:
            first = mid+1

    return len(l)
    
    # Time complexity O(log(n))
    """

#Neet code solution
def SIP(l:list[int],n:int):
    first = 0 
    last = len(l)-1
    while first<=last:
        mid = (first + last )//2
        if l[mid] == n :
            return mid
        elif l[mid]>n:
            last = mid -1 
        else : 
            first = mid +1 
    return first            
# Time Complexity O(log(n)) same as my last one but with less code. lol. man how could I miss that. the more you see the more you learn yk.  

print(SIP([1,3,5,6],0))


