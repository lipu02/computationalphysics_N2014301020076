blank=[[' ' for j in range (40)]for i in range (30)]
blank[25][13:26]='A',' ','m','o','v','i','n','g',' ','h','e','a','r','t'
A=[[' ' for j in range (9)]for i in range (8)]
for j in [1,2,6,7]:
    A[0][j]='#'
for j in [0,3,5,8]:
    A[1][j]='#'
for j in [0,4,8]:
    A[2][j]='#'
for i in range(5):
    A[3+i][i]='#'
    A[7-i][i+4]='#'
f=open("moving_heart.txt",'wb')
for k in range(30):
    for i in range(8):
        for j in range(9):
            blank[i+10][j+k]=heart[i][j]
#output
    for i in range(30):
        print 
        for j in range(40):
            print blank[i][j],
#output to text file
    for i in range(30):
        f.write('\n')
        for j in range(40):
            f.write(blank[i][j])
for a = "A"
l = list(a)
for a = "".join(l)            
#clear
    for i in range(8):
        for j in range(9):
            blank[i+10][j+k]=' '
f.close()
