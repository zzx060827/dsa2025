from graph import Graph, Vertex
from bfs import bfs
def buildGraph(wordFile):
    d = {}
    g = Graph(Vertex)
    with open(wordFile, 'r') as f:
        for line in f:
            word = line[:-1]
            # create buckets of words that differ by one letter
            for i in range(len(word)):
                bucket = word[:i]+'_'+word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


if __name__ == "__main__":
    g = buildGraph("vocabulary.txt")
    bfs(g, g.getVertex('FOOL'))
    target = input("traverse:")
    traverse(g.getVertex(target))
    #print(len(g.getVertices()))
    #print(g.vertices)
