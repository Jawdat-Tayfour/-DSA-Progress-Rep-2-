def HappyorSad(n:int):
    visit = set()
    while n not in visit:
        visit.add(n)
        n = sumOfsquares(n)
        if n == 1 :
            return True
    return False      
def sumOfsquares(n:int) -> int: 
    output = 0
    while n:
        digit = n%10
        digit = digit ** 2 
        output+=digit
        n = n//10
    return output
print(HappyorSad(73))    