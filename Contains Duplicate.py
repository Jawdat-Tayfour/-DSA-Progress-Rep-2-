# My solution
def CD(n:list[int]):
    noDops = set()
    for i in n:
        noDops.add(i)
    if len(noDops) != len(n):
        return True 
    return False 
# O(n) Time Complexity , O(n) Space Complexity, Yay ^_^

# Neet Code Solution 
def CD2(n:list[int]):
    hashset = set()
    for i in n: 
        if n in hashset:
            return False 
        hashset.add(n)
    return True     
# O(n) Time Complexity , O(n) Space Complexity. Finally we wrote something equivelent. :D 

print(CD([1,2,3,4,5,5,5])) 