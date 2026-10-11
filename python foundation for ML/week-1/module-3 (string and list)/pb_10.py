# You are given a list of marks: [90, 40, 75, 88, 35]. For each mark, print the mark and Pass if it is at least 40, otherwise Fail. Then print how many students passed and the average of all marks. Sample Input: No input Sample Output: 90 Pass 40 Pass 75 Pass 88 Pass 35 Fail Passed: 4 Average: 65.6

marks=input().split()
pas=0
total=0
for i in range(len(marks)):
    mark=int(marks[i])
    total+=mark
    if(mark>=40):
        pas+=1
        print(mark,"Pass",end=" ")

    else:
        print(mark,"Fail",end=" ")
avg=(total/len(marks))
print("Passed:",pas,end=" ")
print("Average:",avg)


