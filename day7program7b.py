m=[[1,2],[3,4],[5,6],[7,8]]
ans=[]
for row in range(len(m[0])):
    ans.append([m[col][row] for col in range(len(m)) ])
print(*ans)
