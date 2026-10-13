words=input().split()
size=len(words)
cnt=0
key=["ai", "data", "model", "learn", "train", "neural"]
for i in range(size):
    word=words[i]
    if(word in key):
        cnt+=1

if(cnt>=2):
    print("AI Detected")
else:
    print("Not AI Related")

