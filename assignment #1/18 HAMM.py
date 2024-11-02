with open (r"assignment #1/hamm.txt", "r") as file: 
    s = file.readline()
    t = file.readline()

counter = 0

if len(s) == len(t):
    for i in range(len(s)):
        if s[i] != t[i]:
            counter +=1
print(counter)