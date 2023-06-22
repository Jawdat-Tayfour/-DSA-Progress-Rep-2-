import heapq
"""# my solution ^_^
def LastStoneWeight(l:list[int]) -> int: #Heeeeeeeeeeeeeey I rememberd to add a return type Yay.
    while len(l)>1 :
        maxEl = max(l)
        l.remove(maxEl)
        maxEl2 = max(l)
        l.remove(maxEl2)
        if maxEl == maxEl2 : 
            continue 
        elif maxEl>maxEl2:
            l.append(maxEl - maxEl2)
        else:
            l.append(maxEl - maxEl2)
    if len(l)>=1:
        return l[0]
    else :
        return 0 
# time complexity of O(n**2)
"""

# Neet Code Solution 
def LastStoneWeight(l:list[int]) ->int :
    l = [-i for i in l]
    heapq.heapify(l)
    while len(l)>1:
        first = heapq.heappop(l)
        second = heapq.heappop(l)
        if second>first:
            heapq.heappush(l,(first - second))
    l.append(0)        
    return abs(l[0])
# Time Complexity O(n*log(n)) Still faster than mine though


print(LastStoneWeight([1,2,5,4,8,9,6,7,3]))
