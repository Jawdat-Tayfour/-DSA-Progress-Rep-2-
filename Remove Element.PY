"""# My solution ^_^
def removeallocc(l:list[int],n:int):
    for i in range(len(l)):
        if n in l:
            l.remove(n)
    return len(l)

# Time Complexity O(n**2), Oh, I'm so stupid it looks like I've learnt nothing from the remove duplicates problem, anyways, down is Neet code solution.Have fun."""


#Neet Code Solution
def removeallocc(l:list[int],n:int):
    k = 0 
    for i in range(len(l)):
        if l[i] != n :
            l[k] = l[i]
            k+=1
    return k         
# it's clearly O(n) because all he does within the n iterations is constant time operations. Good luck fella programmer.^_^


print(removeallocc([0,1,2,2,3,0,4,2],2))