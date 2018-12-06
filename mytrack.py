with open('mytrack.txt')as f:
    fread=f.readlines()
fsplite=fread[0].strip().split(":")
[x,y]=[[],[]]
for i in range(len(fsplite)):
    if i % 2==0:
        x.append(fsplite[i])
    else:
        y.append(fsplite[i])
movex=[]
movey=[]
for i in range(len(x)-1):
    movex.append(int(x[i+1])-int(x[i]))
    movey.append(int(y[i+1])-int(y[i]))
print(movex,'\n',movey)