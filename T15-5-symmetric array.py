

print('enter an array as x,y,z,...')
a=input()
t=0
ar=a.split(',')
l=len(ar)
for i in range(l//2):
    if i==0 or i==l-1:
        if ar[0]==ar[l-1]:
           t=1
        else:
            t=2 
    elif i!=0 and i!=l-1 :
        if ar[i]==ar[l-i]:
            t=1

if t==0 or t==2:
    print('array is not symmetric!')

elif t==1:
    print('array is symmetric.')