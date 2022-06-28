import string 
alphabet_list = list(string.ascii_uppercase)

f = open("Problem-22.txt", "r")
x=(f.read().replace('"',"").split(","))
x.sort(key=lambda x: x.upper())
score=0
for i in x:
    for k in i:
        for j in alphabet_list:
            if k==j:
                score+=(alphabet_list.index(j)+1)*(x.index(i)+1)
print(score)
