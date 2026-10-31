inp=input().split()
sum=0
for i in range(len(inp)):
      sum+=int(inp[i])

avg=(sum/len(inp))

if(avg<85):
      print("Dark Image")
elif(avg<=170):
      print("Normal Image")
else:
      print("Bright Image")