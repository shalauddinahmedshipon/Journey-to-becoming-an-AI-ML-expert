# Take a string as input. Count how many vowels it has (a, e, i, o, u in both lowercase and uppercase) using a loop. Print only the count. Sample Input: Education Sample Output: 5

word=input()
new_word=word.lower()
size=len(word)
cnt=0
for i in range(size):
    ch=new_word[i]
    if(ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        cnt+=1

print(cnt)