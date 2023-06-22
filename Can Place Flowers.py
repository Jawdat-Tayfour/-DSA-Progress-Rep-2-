def CPF(l:list[int],n:int):
    # when the length of the list is odd we can add (len(l)//2)+1 flowers
    # when the length of the list is even we can add len(l) //2 flowers  
    # let's start with that. 
    if len(l)%2 == 0 :
        NOPF = len(l)//2
    if len(l)%2 != 0:
        NOPF = (len(l)//2)+1
    counter = 0
    for i in l:
        if i == 1 :
            counter+=1
    NOPF = NOPF - counter
    return NOPF == n 
# My solution O(n) Time Complexity I feel like it's right and wrong at the same time I tried a couple of inputs and they worked out. 
#Anyways.
#Neet Code Solution 
def CPF2(l:list[int],n:int)-> bool :
    f = [0] + l  + [0]
    for i in range (1,len(f)-1):
        if f[i-1] == 0 and f[i] == 0 and f[i+1]:
            f[i] = 1
            n-=1
    return n<=0
# O(n) Time Complexity this one def works 
#Neet Code Solution 2 :
def CPF3(l:list[int],n:int):
    empty = 0 if l[0] else 1
    for f  in l :
        if f : 
            n-= int((empty-1)/2)
            empty = 0 
        else:
            empty+=1
    n-= (empty)//2
    return n <= 0        
print(CPF([1,0,0,0,1],1))
#O(n) Time Complexity this one also works 