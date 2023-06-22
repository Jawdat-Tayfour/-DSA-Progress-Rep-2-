#my solution don't read it it's not the right answer but I just put it still to prove to y'all that I tried my best. ^_^
"""def unemailchecker(emails:list[str]):
    emailsdic = {}
    local_name = ""
    local_name2 = ""
    local_name3 = ""
    for i in range(len(emails)):
        
        email_list = list(emails[i].split("@"))
        if "." in email_list[0] and "+" in email_list[0] :
            local_namez =list(email_list[0].split("."))
            for j in local_namez:
                local_name += j
            local_namez2 = list(email_list[0].split("+"))
            local_name += local_namez2[0]
            emailsdic[i] = local_name +"@"+ email_list[1]  
            continue              
        elif "." in email_list[0]:
            local_namez3 =list(email_list[0].split("."))
            for k in local_namez3:
                local_name2 += k
            emailsdic[i] = local_name2 +"@"+ email_list[1]        
            continue
        elif "+" in email_list[0]:
            local_namez2 = list(email_list[0].split("+"))
            local_name3 = local_namez2[0]
            emailsdic[i] = local_name3 +"@"+ email_list[1]    
            continue
        
    return emailsdic    """
#Neet Code Solution 1 
"""def unemailchecker(emails:list[str]) -> int:
    unique =set()
    for e in emails:
        local,domain = e.split("@")
        local = local.split("+")[0]
        local = local.replace(".","")
        unique.add((local,domain))
    return len(unique)       """

#Time Complexity O(n) that's a lesson to me to always work in a clear mindset and a relaxed brain and body. you can't solve problems while you're tired champ 
#I'll head to sleep GN. Y'all See you tomorrow! ^_^. I complicated the simple , like, for real. Haha.


#Neet code solution 2:
def unemailchecker(emails:list[int]) -> int:
    i=0
    local = ''
    unique = set()
    for e in emails : 
        while e[i] not in ["@","+"]:
            if e[i] != '.':
                local+=e[i]
        while e[i] != '@':
            i+=1
        domain = e[i+1:]
        unique.add((local,domain))
    return len(unique)    
print(unemailchecker(['18j.wdat@gmail.com','ta.jwdat@gmail.com']))        
