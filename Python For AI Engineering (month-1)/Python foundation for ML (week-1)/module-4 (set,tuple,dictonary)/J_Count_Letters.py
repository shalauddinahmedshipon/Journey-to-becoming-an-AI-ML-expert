str=input()
dic={}
size=len(str)
for i in range(size):
    if(dic.get(str[i],0)==0):
        dic[str[i]]=1
    else:
        dic[str[i]]+=1

for key,value in sorted(dic.items()):
    print(key,":",value)
    