from graph import Graph, Vertex

def knightGraph(bdSize):
    ktGraph = Graph(Vert=Vertex)
    for row in range(bdSize):                         #遍历每一行
        for col in range(bdSize):                     #遍历行上的每一个格子
            #按照“马走日”，返回下一步可能的位置
            for e in legalMoves(row, col, bdSize):
                ktGraph.addEdge((row, col), e)  #在骑士周游图中为两个格子加一条边
    return ktGraph

def legalMoves(x, y, bdSize):
    offsets = [(-1, -2), (-1,2),(-2,-1),(-2,1),
                   (1, -2), (1,2), (2,-1), (2,1)]    #马走日的8种走法
    for ix, iy in offsets:
        #检查一下不能走出棋盘
        if 0 <= x+ix < bdSize and 0 <= y+iy < bdSize:
            yield(x+ix, y+iy)

def knightTour(n, path, u, limit):
    """
    n:层次；path:路径；u:当前顶点；limit:搜索总深度
    """
    u.setColor('grey')
    path.append(u)                                   #当前顶点涂色并加入路径
    if n < limit:
        nbrList = list(u.getConnections())           #对所有的合法移动依次深入
        for nbr in nbrList:
            #选择“白色”未经深入的点, 层次加一，递归深入
            if nbr.getColor() == 'white' and knightTour(n+1, path, nbr, limit):
                return True
        else:                                        #所有的“下一步”都试了走不通
            path.pop()                               #回退途径
            u.setColor('white')                      #改回颜色
            return False                             #回到上一层，尝试下一个顶点
    else:       # n==limit，基本结束条件
        return True

if __name__ == "__main__":
    bd_size = int(input("Please input board size:"))
    g = knightGraph(bd_size)
    path=[]
    start = g.getVertex((1, 1))
    if knightTour(0, path, start, bd_size**2 - 1):
        for i, v in enumerate(path):
            print(i, v.id)
    else:
        print("knight tour failed!")
