#my solution ^___^ 
"""def uglynumberdetector(n:int)-> bool:
    while n >= 1 :
        if n%2==0:
            n = n//2
            continue
        elif n%3==0:
            n = n//3
            continue
        elif n%5==0:
            n = n//5
            continue
        elif n == 1 :
            return True
        else:
            return False
    return True                 
    
    #Time compelxity O(log(n))
    """
#Neet Code Solution
def uglynumberdetector(n:int) -> bool:
    for i in [2,3,5]:
        while n%i ==0:
            n=n//i
    return n==1        
#Time complexity O(log(n)) , both are the same with different approaches. yay ^_^

un = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15,14]     
for i in  un :  
    print(uglynumberdetector(i))    