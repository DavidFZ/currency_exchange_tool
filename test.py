class Edge():
    def __init__(self,u,v,cost):
        self.u = u
        self.v = v
        self.cost = cost
nodenum = 5

edgeList = []
dis = [float("inf")]*nodenum
pre = [-1]*nodenum

edgeList.append(Edge(0,1,-1))
edgeList.append(Edge(1,2,3))
edgeList.append(Edge(3,1,1))
edgeList.append(Edge(1,3,2))
edgeList.append(Edge(1,4,2))
edgeList.append(Edge(0,2,4))
edgeList.append(Edge(3,2,5))
edgeList.append(Edge(4,3,-3))

edgenum = len(edgeList)

original = 0
def Bellman_Ford(original):
    #令起点到自身的距离为0
    for i in range(nodenum):
        if(i == original):
            dis[i] = 0
    print(dis,'\n')
    for i in range(nodenum-1):
        for j in range(edgenum):
            if(dis[edgeList[j].v] > dis[edgeList[j].u] + edgeList[j].cost):
                dis[edgeList[j].v] = dis[edgeList[j].u] + edgeList[j].cost
                pre[edgeList[j].v] = edgeList[j].u
        print('dis',dis)
        print('pre',pre,'\n')
    flag = True
    for i in range(edgenum):
        if(dis[edgeList[i].v] > dis[edgeList[i].u] + edgeList[i].cost):
            flag = False
            break
    return flag
print(Bellman_Ford(original))