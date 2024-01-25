import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().rstrip())) for _ in range(N)]
ch_board = [[-1]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# ✨ BFS
def BFS(x,y):
    dq = deque([])
    dq.append((x,y))
    ch_board[x][y] = 0
    while dq:
        xx,yy = dq.popleft()
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if 0<=nx<N and 0<=ny<N and ch_board[nx][ny] == -1 :
                if board[nx][ny] == 1:
                    ch_board[nx][ny] = ch_board[xx][yy]
                    dq.appendleft((nx,ny))
                else:
                    ch_board[nx][ny] = ch_board[xx][yy]+1
                    dq.append((nx,ny))
    print(ch_board[N-1][N-1])

                    
BFS(0,0)