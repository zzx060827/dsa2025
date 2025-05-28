def delete(canter,time):
    length=len(canter)
    l=length//3
    r=l*2
    mid=['-']*l
    if time>1:
        ans=delete(canter[:l],time-1)+mid+delete(canter[r:],time-1)
    else:
        ans=canter[:l]+mid+canter[r:]
    return ans

def main():
    n=int(input())
    if n==1:
        print('*-*')
        exit(0)
    length=3**n
    canter=['*'] * length
    ans=delete(canter,n)
    print(''.join(ans))

if __name__=='__main__':
    main()