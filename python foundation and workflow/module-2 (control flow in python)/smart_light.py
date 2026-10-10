inp=input()
numbers=inp.split()
brightness=int(numbers[0])
threshold=int(numbers[1])
if(brightness>=threshold):
    print("ON")
else:
    print("OFF")