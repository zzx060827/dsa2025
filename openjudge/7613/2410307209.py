n=int(input())
cell=[]
ave=0
for i in range(n):
    t=float(input())
    cell.append(t)
    ave+=t
cell.sort()
ave=(ave-cell[-1]-cell[0])/(n-2)
E=0
for i in range(1,n-1):
    if abs(cell[i]-ave)>E:
        E=abs(cell[i]-ave)

print('{0:.2f} {1:.2f}'.format(ave,E))
