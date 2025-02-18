st=input()
s=[char for char in st]

s.sort()

def pmt(s,t):
    if len(s)==1:
        t.append(s[0])
        print(''.join(t))
    else:
        for i in range(len(s)):
            t1=t+[s[i]]
            s1=s[:i]+s[i+1:]
            pmt(s1,t1)

pmt(s,[])            