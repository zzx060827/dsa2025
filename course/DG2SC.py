from DFSGraph import DFSGraph
from xGraph import XGraph
from bfs import bfs
import sys, getopt

class SCCGraph(DFSGraph):
    def SCC(self):
        gt = DFSGraph(self.T())
        gt.dfs()
        self.__dfs(gt)
        scc = {}
        for v in self:
            u = v
            while u.getPred():
                u = u.getPred()
            scc.setdefault(u, []).append(v)
        return scc.values()

    def __dfs(self, gt):
        for aVertex in self:
            aVertex.setColor('white')   # 颜色初始化
            aVertex.setPred(None)
        gtsfin=lambda x:gt.getVertex(x.getId()).fin
        #for aVertex in self:           # 从每一个顶点开始遍历
        for aVertex in sorted([i for i in self], key=gtsfin, 
                reverse=True):
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex) # 第一次运行后还有未包括的顶点
                                       # 则建立森林

    def DAG(self):
        scc = self.SCC()
        def group(v, scc):
            for vv in scc:
                if v in vv:
                    return vv
            return None
        dag = XGraph()
        for v in self:
            vv = '-'.join([n.getId() for n 
                in group(v, scc)])
            for u in v.getConnections():
                uu = '-'.join([n.getId() for n
                    in group(u, scc)])
                if vv != uu:
                    dag.addEdge(vv, uu)
        return dag

def printGraph(g):
    """
       print a digraph in adjacency list.
    """
    for v in g:
        nbrs = ' '.join([u.getId() for u in v.getConnections()])
        if nbrs:
            print("{} : {}".format(v.getId(), nbrs))

def printCypher(g, entity, relation):
    """
       print cypher script for neo4j
    """
    print("//创建实体")
    for v in g:
        print("CREATE (s{}:{}{{name:'{}'}})".format(v.getId().replace('-','_')
            , entity, v.getId()))
    adj = [(v, v.getConnections()) for v in g if v.getConnections()]
    Adj = {}
    for i in range(5):
        Adj[i] = selectWeight(adj, i)
    for i in range(5):
        if Adj[i]:
            rel = relation+str(i) if i>0 else relation
            printCypherRel(entity, rel, Adj[i])
    print("//返回图")
    print("MATCH (n:{})".format(entity))
    print("RETURN n")

def selectWeight(adj, weight):
    adj = [(u, [v for v in vv if u.getWeight(v)==weight]) for (u, vv) in adj]
    adj = [(u, vv) for (u, vv) in adj if vv]
    return adj

def printCypherRel(entity, relation, adj):
    print("//创建实体之间的关系")
    print("MATCH (a:{}),(b:{})\n WHERE ".format(entity, entity), end="")
    print('\nOR '.join(['a.name="{}" AND b.name in {}'.format(u.getId(), [v.getId() for v in vv]) for (u, vv) in adj]))
    print("CREATE (a)-[r:{}]->(b)".format(relation))
    print("RETURN type(r)")

def readGraph(f):
    g = SCCGraph()
    for ln in f:
        ln = ln[:-1]
        if not ln:
            break
        ln = ln.split(":")
        u = ln[0].split()
        vv = ln[1].split()
        for v in vv:
            g.addEdge(u[0], v)
    return g

def help():
    print('Usage: DG2SC.py [-g <graphfile>]')
    return

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hg:",["graphfile="])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    gf = ''
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-g", "--graphfile"):
            gf = arg

    if gf:
        with open(gf) as f:
            g = readGraph(f)
    else:
        g = readGraph(sys.stdin)
    print("**********Graph**************")
    #printGraph(g)
    printCypher(g, "Class", "know")
    print("**********SCC**************")
    for c in g.SCC():
        print([v.getId() for v in c])
    print("**********DAG**************")
    dag = g.DAG()
    #printGraph(dag)
    printCypher(dag, "scc", "know")

    D = XGraph(dag)
    P = [v for v in D if v.inDegree==0]
    Q = [v for v in D if v.outDegree==0]
    p, q = len(P), len(Q)
    print("P({})={}".format(p, [v.getId() for v in P]))
    print("Q({})={}".format(q, [v.getId() for v in Q]))
    if p < q:           #add edge: Q[0]<== Q[1],...,[q-p]
        for i in range(1, q-p+1):
            D.addEdge(Q[i].getId(), Q[0].getId(), cost=1)
            g.addEdge(Q[i].getId().split('-')[0], Q[0].getId().split('-')[0], cost=1)
    elif p > q:
        for i in range(1, p-q+1):
            D.addEdge(P[0].getId(), P[i].getId(), cost=2)
            g.addEdge(P[0].getId().split('-')[0], P[i].getId().split('-')[0], cost=1)
    print("**********D**************")
    printCypher(D, "D", "know")
    P = [v for v in D if v.inDegree==0]
    Q = [v for v in D if v.outDegree==0]
    p, q = len(P), len(Q)
    print("P({})={}".format(p, [v.getId() for v in P]))
    print("Q({})={}".format(q, [v.getId() for v in Q]))

    Bn = XGraph()
    for v in P:
        d = XGraph(D)
        bfs(d, d.getVertex(v.getId()))
        for u in Q:
            if d.getVertex(u.getId()).getColor() == 'black':
                Bn.addEdge(v.getId(), u.getId())
    printCypher(Bn, "B{}".format(len(P)), "know")
    P = [v for v in Bn if v.inDegree==0]
    Q = [v for v in Bn if v.outDegree==0]
    l = [(s, t) for s in P for t in Q if t not in s.getConnections()]
    while l:
        s, t = l[0]
        T=Bn.T()
        for ss in T.getVertex(t.getId()).getConnections():
            for tt in Bn.getVertex(s.getId()).getConnections():
                Bn.addEdge(ss.getId(), tt.getId())
        Bn.delVertex(t.getId())
        Bn.delVertex(s.getId())
        g.addEdge(t.getId().split('-')[0], s.getId().split('-')[0], cost=3)
        P = [v for v in Bn if v.inDegree==0]
        Q = [v for v in Bn if v.outDegree==0]
        l = [(s, t) for s in P for t in Q if t not in s.getConnections()]
    else:
        printCypher(Bn, "B{}".format(len(P)), "know")
        for i in range(len(P)):
            g.addEdge(Q[i].getId().split('-')[0], P[i].getId().split('-')[0], cost=4)
    printCypher(g, "SCG", "know")
    print("**********SCC**************")
    for c in g.SCC():
        print([v.getId() for v in c])

if __name__ == "__main__":
    main(sys.argv[1:])
