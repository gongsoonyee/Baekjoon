from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 사탕 초기 위치
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'


# 한 방향으로 사탕 이동
def move(x, y, dx, dy):
    count = 0

    while board[x + dx][y + dy] != '#':
        x += dx
        y += dy
        count += 1

        if board[x][y] == 'O':
            break

    return x, y, count


def bfs(rx, ry, bx, by):
    q = deque([(rx, ry, bx, by, 0)])
    visited = {(rx, ry, bx, by)}

    while q:
        crx, cry, cbx, cby, depth = q.popleft()

        if depth >= 10:
            continue

        for d in range(4):
            nrx, nry, rc = move(crx, cry, dx[d], dy[d])
            nbx, nby, bc = move(cbx, cby, dx[d], dy[d])

            # 파란 사탕이 빠지면 실패
            if board[nbx][nby] == 'O':
                continue

            # 빨간 사탕만 빠지면 성공
            if board[nrx][nry] == 'O':
                return depth + 1

            # 두 사탕이 겹치면 충돌 처리
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]

            state = (nrx, nry, nbx, nby)

            if state not in visited:
                visited.add(state)
                q.append((*state, depth + 1))

    return -1


print(bfs(rx, ry, bx, by))