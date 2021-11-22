import sys
n=int(input())

node=list(map(int,input().split()))
visited=[False]*n

tar=int(input())

visited[tar]=True

graph=[[] for _ in range(n)]
start=0

for i in range(n):
    if node[i]!=-1:
        graph[i].append(node[i])
        graph[node[i]].append(i)
    else:
        start=i
        visited[start]=True

if start==tar:
    print(0)
    sys.exit(0)

q=[start]
ans=0

while q:
    s=q.pop(0)
    flag=True
    for j in graph[s]:
        if visited[j]==False:
            visited[j]=True
            flag=False
            q.append(j)
    if flag:
        ans+=1
print(ans)
