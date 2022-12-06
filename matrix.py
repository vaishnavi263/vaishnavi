rows=int(input("Enter the value of rows : "))
cols=int(input("Enter the value of colums : "))
last=rows*cols
test = list(range(1,last+1))
for i in range(1,len(test)):
    if i%3==0:
        if i==last:
            pass
        else:
            test[i-1],test[i]=test[i],test[i-1]
row1=[]
row2=[]
row3=[]
for i in range(0,len(test)):
    if i%3==0:
        row1.append(test[i])
    elif i%3==1:
        row2.append(test[i])
    else:
        row3.append(test[i])
print(row1)
print(row2)
print(row3)