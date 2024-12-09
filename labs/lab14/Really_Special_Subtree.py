class edge(object):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.w=c
class Unionfind(object):
   
    def __init__(self):
        self.leader = {}  # maps member to group leader
        self.group = {}   # maps group leader to set of members
 
    def makeSet(self, e):
        group = set(e)
        self.group[e[0]] = group
        for i in group:
            self.leader[i] = e[0]

    def getNumGroups(self):
        """Return the number of groups"""
        return len(self.group)

    def find(self,e):
        return self.leader[e]

    def union(self,a,b):
        l1=self.leader[a]
        l2=self.leader[b]
        if(l1!=l2):
            g1=self.group[l1]
            g2=self.group[l2]
            g1|=g2
            del self.group[l2]
            for i in g2:
                self.leader[i]=l1

n,m=map(int,input().split())
listed=[]
u=Unionfind()
for i in range(m):
    a,b,c=map(int,input().split())
    e=edge(a,b,c)
    listed.append(e)
s=0
for i in range(n): u.makeSet([i+1])
listed.sort(key=lambda x: (x.w,x.a+x.b+x.w))
for i in listed:
    if u.find(i.a)!=u.find(i.b):
        u.union(i.a,i.b)
        s+=i.w
print (s)