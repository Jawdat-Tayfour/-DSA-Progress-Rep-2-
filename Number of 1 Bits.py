# My Solution ^_^
def NO1B(n:int):
    m = str(n)
    count=0
    for i in m :
        if i =="1":
            count+=1
    return count        
#Time complexity O(log(n)) n is the number of digits since we are sure that the input is going to be 32int then it's also in constant time 
# but my solution doesn't work if the input started with zero,it also uses more space for str convert.
#  so let's learn some more Neat code from Neet code. ^_^ 

#Neet code solution
def NO1B2(n:int):
    res = 0 
    while n:
        res+=n%2
        n=n>>1
    return res

#O(32)->O(1) Complexity, but works for 0 starting input. and runs in constant space as well. 

#Neet code Solution 2 
def NP1B3(n:int):
    res = 0 
    while n :
        n = n & (n-1)
        res+=1
#that's the qucickest solution, it only runs through the ones of the input runs in constant space and constant time
# I think I should learn more about bit manipulation, anyways, have a good day. ^_^         

print(NO1B2(0b010101010101010101010))