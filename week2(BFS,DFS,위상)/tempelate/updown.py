dx = [-1, 1, 0, 0]
dy = [-1, 1, 0, 0]

for i in range(4):

    next_x = cur_x + dx[i]
    next_y = cur_y + dy[i]
    visited[next_x][next_y] = True
    queue.append((next_x, next_y))