def Counter(ls=[]):
    dic={}
    for x in ls:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    return dic