##m=[[1,2],[3,4],[5,6],[7,8]]
ans=[[m[col][row] for col in range(len(m)) ]for row in range(len(m[0]))]
print(*ans)
